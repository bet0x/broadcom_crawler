---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/deregister-an-antrea-kubernetes-cluster-from-nsx/clean-up-antrea-data-from-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Clean up Antrea Data from NSX
---

# Clean up Antrea Data from NSX

If you destroy the Antrea Kubernetes cluster or delete the Antrea- NSX Interworking Adapter before running the deregisterjob.yaml file, some Antrea data is retained in the NSX inventory.

- You must have the user name and password of the NSX Enterprise Admin user.
- You must be able to connect to NSX Manager UI and API.

You can use the instructions in this documentation to clean up the Antrea data from NSX.

Starting with VMware Container Networking™ with Antrea™ version 1.7.0, the antreansxctl command-line utility provides the cluster-cleanup command to clean up leftover Antrea data in the NSX inventory.The antreansxctl utility is a Linux-only executable. So, you require a Linux machine to run this utility.

To learn about the usage of this cluster-cleanup command, see the antreansxctl Command-Line  documentation in the VMware Container Networking with Antrea Installation Guide.

In VMware Container Networking™ with Antrea™ versions prior to 1.7.0, the antreansxctl command-line utility is unavailable. In that case, you can run a curl command, as explained in the following procedure. The curl command calls an NSX API to delete the leftover Antrea data from the NSX inventory.

1. Find the path of the Antrea Kubernetes cluster in the NSX Manager UI. 
   1. From your browser, log in to an NSX Manager at https://nsx-manager-ip-address.
   2. Navigate to InventoryContainersClusters.
   3. Expand the cluster to be deleted and copy the text that you see next to the Path field.

      For example:

      ![Highlights the path of a container cluster in NSX Manager UI.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/97dfebb1-d564-48f6-9799-ffdcb0dda4ff.original.png)
2. Run the following curl command to delete the Antrea data from NSX:

   ```
   curl -k -u '{AdminUserName}:{AdminPassword}' \
   -X DELETE -H "X-Allow-Overwrite: true" \
   https://{NSX-Mgr-IP}/policy/api/v1{Path}?cascade=true
   ```

   In this command:
   - Replace {AdminUserName}, {AdminPassword}, and {NSX-Mgr-IP} with their actual values as applicable to your NSX environment.
   - Replace {Path} with the text that you copied in step 1.

   For example:

   ```
   curl -k -u 'Admin:Password123' \
   -X DELETE -H "X-Allow-Overwrite: true" \
   https://192.168.1.1/policy/api/v1/infra/sites/default/enforcement-points/default/cluster-control-planes/cluster-sales?cascade=true
   ```