---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/upgrade-antrea-nsx-interworking-deployment-in-an-antrea-kubernetes-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Upgrade Antrea- NSX Interworking Deployment in an Antrea Kubernetes Cluster
---

# Upgrade Antrea- NSX Interworking Deployment in an Antrea Kubernetes Cluster

If
you have upgraded the VMware Container Networking version to a new release, the Antrea- NSX interworking
deployment in your registered Antrea Kubernetes
cluster must be upgraded together.

1. The VMware Container Networking version in your Antrea Kubernetes cluster, which is registered to
   NSX, must be upgraded
   successfully.
2. Complete only the following
   prerequisite steps that are mentioned in [Prerequisites for Registering an Antrea Kubernetes Cluster to NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx/prerequisites-for-registering-an-antrea-kubernetes-cluster-to-nsx.html). Skip the
   other prerequisite steps at this link.
   - Determine the
     Antrea version from
     the Kubernetes cluster.
   - Download the
     Antrea- NSX interworking zip file.
   - Import the container
     images to container registry.

     Make sure to edit
     the interworking.yaml and
     deregisterjob.yaml files, and update
     the image URLs to the imported image, or to the online image
     URL.

1. Run the following kubectl
   commands to delete the register job and the
   antrea-interworking deployment.

   ```
   kubectl delete job register -n vmware-system-antrea --ignore-not-found
   kubectl delete deployment antrea-interworking -n vmware-system-antrea --ignore-not-found
   ```

   Do not delete the
   vmware-system-antrea namespace, configmaps, and secrets
   in this namespace.
2. Run the following kubectl command to submit the
   interworking.yaml file to the Kubernetes API server,
   and trigger the upgrade.

   ```
   kubectl apply -f interworking.yaml
   ```

   Only the
   interworking.yaml must be submitted. The
   bootstrap-config.yaml file is not required for the
   upgrade process.
3. Run the following kubectl
   command to list all the pods in the vmware-system-antrea
   namespace.

   ```
   kubectl get pods -o wide -n vmware-system-antrea
   ```

   Observe that the status of the register-xxx pod is
   Running. Because the Antrea Kubernetes cluster is already
   registered to NSX, the
   register-xxx pod skips the registration process and the status soon changes to
   Completed. The old interworking-yyy pod status
   changes to Terminating, and the new
   interworking-zzz pod status changes to Running.

   When the new interworking-zzz
   pod status is Running, and the ready containers
   are 4/4, there is no need to restart the
   containers, and the upgrade is
   successful.

   ```
   #Example output:

   NAME                            READY   STATUS   RESTARTS   AGE   IP          NODE            NOMINATED NODE   READINESS GATES
   interworking-7764988ddd-wnvcg   4/4     Running  0          29s   192.168.x.y example-node-10 <none>           <none>
   ```
4. Run the following kubectl
   command to verify that the new interworking-zzz pod is using the new image and
   the image URLs are the same as expected.

   Make sure to replace the "interworking-7764988ddd-wnvcg" pod name with the
   actual pod name that you see in the output of the kubectl get
   pods command of the previous step.

   ```
   kubectl get pods -o yaml interworking-7764988ddd-wnvcg -n vmware-system-antrea | grep image:

   # Example output:
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
       image: vmware.io/antrea/interworking:0.11.0
   ```