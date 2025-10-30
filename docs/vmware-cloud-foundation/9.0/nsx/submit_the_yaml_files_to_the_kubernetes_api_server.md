---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx/submit-the-yaml-files-to-the-kubernetes-api-server.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Submit the YAML Files to the Kubernetes API Server
---

# Submit the YAML Files to the Kubernetes API Server

To register an Antrea Kubernetes cluster
to NSX, you must submit the
bootstrap-config.yaml file and the
interworking.yaml Deployment manifest file to the Kubernetes API
server.

Ensure that:

- The prerequisite tasks for
  registering an Antrea Kubernetes
  cluster to NSX are
  completed. See [Prerequisites for Registering an Antrea Kubernetes Cluster to NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx/prerequisites-for-registering-an-antrea-kubernetes-cluster-to-nsx.html#GUID-bc2b148b-bf39-47e1-8589-a8fc8e5d61dc-en).
- Values of mandatory arguments
  are specified in the bootstrap-config.yaml file. See
  [Edit the Bootstrap Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/registering-an-antrea-kubernetes-cluster-to-nsx/edit-the-bootstrap-configuration-file.html#GUID-be35ec24-4d60-429d-9436-46420e59f489-en).

1. Run the following kubectl command to submit the
   .yaml files to the Kubernetes API server:

   $ kubectl apply -f bootstrap-config.yaml -f
   interworking.yaml

   Ensure that bootstrap-config.yaml file comes first in
   the command.

   This command registers the Antrea Kubernetes cluster to NSX. The register-xxx and
   interworking-yyy pods are deployed in the vmware-system-antrea
   namespace.

   Where:
   xxx and yyy are arbitrary numbers
   that represent instance IDs of the pods in your cluster.
2. Run the following kubectl command to view the list all pods in
   the vmware-system-antrea namespace:

   $ kubectl get pods -o
   wide -n vmware-system-antrea

   Verify that status of the
   register pod is Completed and the status of the
   interworking pod is Running.

   The containers of the Management Plane Adapter and the Central Control Plane Adapter in the
   interworking pod now start running in the Antrea Kubernetes cluster. The resources in the Antrea Kubernetes cluster are synced with the
   NSX inventory.

   After the Antrea Kubernetes cluster is registered to
   NSX, the Management Plane Adapter connects with
   the NSX Management Plane and performs a full synchronization of the Antrea Kubernetes cluster resources in the
   NSX inventory. The time
   required to do a full sync operation is directly proportional to the scale of the
   cluster. Thereafter, only a delta synchronization operation happens at regular
   predefined intervals. If the Management Plane Adapter fails due to any reason, the resources are not
   synced with the NSX inventory.
   Only after the adapter is up again, the resources in the Antrea Kubernetes cluster are compared with the
   existing objects in the NSX
   inventory and the difference (delta) is synchronized.
3. Perform this step only when your Antrea Kubernetes cluster uses Kubernetes version =
   1.20.
   1. Run the following
      kubectl command to
      register the Antrea Controller webhook on namespace creating events.

      $ kubectl
      apply -f ns-label-webhook.yaml

      You can find this Webhook
      definition file in the
      antrea-interworking-version.zip
      file, which you downloaded from the Download VMware
      Antrea page.
   2. Restart the Antrea Controller pod.

      kubectl rollout restart deployment antrea-controller -n
      kube-system

      This command deletes the existing
      Antrea Controller pod and creates a new Antrea Controller
      pod.
   3. Verify whether the new
      Antrea Controller
      pod is running.

      $ kubectl get pod -l component=antrea-controller -n
      kube-system

View the inventory of Antrea Kubernetes
cluster resources, such as pods, namespaces, Antrea Network Policies, Antrea Cluster Network Policies, and other resources in the
NSX Manager UI.

For more information, see:

- [View Details of Namespaces in an Antrea Kubernetes Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/viewing-inventory-of-an-antrea-kubernetes-cluster-in-nsx-manager/view-details-of-namespaces-in-an-antrea-kubernetes-cluster.html#GUID-9b4dc3c2-4fa1-4574-afeb-bff45eaeb03d-en)
- [View Details of an Antrea Kubernetes Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/viewing-inventory-of-an-antrea-kubernetes-cluster-in-nsx-manager/view-details-of-an-antrea-kubernetes-cluster.html#GUID-10bc1f9a-bfc6-4f24-b8a1-12df6cd02cf1-en)