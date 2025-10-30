---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/deregister-an-antrea-kubernetes-cluster-from-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Deregister an Antrea Kubernetes Cluster from NSX
---

# Deregister an Antrea Kubernetes Cluster from NSX

Use the deregisterjob.yaml file that is included with the antrea-interworking-version.zip file to deregister an Antrea Kubernetes cluster from NSX.

- In addition to the [VMware Cloud Foundation license](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered), which entitles your NSX environment to networking features, you must have a security license that enables full access to the distributed firewall feature.
- Open the deregisterjob.yaml file in a text editor and replace the image URLs with any one these container images that are hosted on VMware Harbor Registry.
  - projects.registry.vmware.com/antreainterworking/interworking-debian:version
  - projects.registry.vmware.com/antreainterworking/interworking-ubuntu:version
  - projects.registry.vmware.com/antreainterworking/interworking-photon:version

  For
  version information, see the VMware Container Networking with
  Antrea release notes at <https://docs.vmware.com/en/VMware-Container-Networking-with-Antrea/index.html>.

  If your Kubernetes cluster does not have Internet access, you can find the container images in the antrea-interworking-version.zip file, which you downloaded before registering the Kubernetes cluster. If the interworking deployment is running in the Kubernetes cluster, the container images are already loaded on the cluster nodes. The deregister job and the interworking deployment use the same container images.

1. Run the following kubectl command to submit the deregisterjob.yaml file to the Kubernetes API server.

   $ kubectl apply -f deregisterjob.yaml

   This job takes some time to complete. The following actions happen in the background:
   - Deletes the interworking deployment.
   - Deletes the resources of the Antrea Kubernetes cluster from the NSX inventory. The resources include pods, services, ingress rules, nodes, and network policies.
   - Removes references to the Antrea Kubernetes cluster in the distributed firewall policies and groups (if any).
   - Deletes the Antrea custom resources, which were managed by NSX from the Kubernetes cluster. These custom resources include: Traceflow, ClusterNetworkPolicy, ClusterGroup, and Tier.
2. Check the status of the deregister job by running the following kubectl command:

   kubectl get job -o wide deregister -n vmware-system-antrea

   Wait for the job to complete. You might have to run this command a few times to check the status of the job.
3. After the deregister job is completed, run the following kubectl command to delete the vmware-system-antrea namespace and the role-based access control (RBAC) resources.

   kubectl delete -f interworking.yaml --ignore-not-found

   The ignore-not-found flag is used in this command to avoid the Resource Not Found error in the command output if some resources are not found for deletion.

   RBAC resources, such as ServiceAccount, ClusterRole, and ClusterRoleBinding are deleted.

Verify that the Antrea Kubernetes cluster is not shown in the NSX inventory.

1. In the NSX Manager UI, navigate to InventoryContainersClusters.
2. Observe that the Antrea Kubernetes cluster is not shown in the inventory.

Optional: After deregistering the Antrea Kubernetes cluster, delete the principal identity (PI) user and the self-signed certificate.

- To delete the PI user account, navigate to SystemUser ManagementUser Role Assignment. Next to the PI user name, click

  ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)

  , and then click Delete.
- To delete the self-signed certificate, navigate to SystemCertificates. Next to the certificate name, click

  ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)

  , and then click Delete.

If required, you can re-register the same Antrea Kubernetes cluster. However, before re-registering the cluster, ensure that you have run the following kubectl command:

```
kubectl delete -f interworking.yaml --ignore-not-found
```

To re-register the same Antrea Kubernetes cluster, do any one of the following:

- If you want to reuse the same PI user account and self-signed certificate for re-registering the Antrea Kubernetes cluster, do not delete PI user account and the self-signed certificate from NSX. In this case, no changes are required in the bootstrap-config.yaml.
- If you want to use a new PI user account and self-signed certificate for re-registering the Antrea Kubernetes cluster, delete the old PI user account and the self-signed certificate. Begin the process by creating a self-signed certificate and use this new certificate to create a PI user account. Edit the tls.crt and tsl.key arguments in the bootstrap-config.yaml with the information of this new PI user.