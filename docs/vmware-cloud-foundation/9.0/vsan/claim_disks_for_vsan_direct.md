---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/managing-storage-devices-in-vsan-cluster/claim-disks-for-vsan-direct.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Claim Disks for vSAN Direct
---

# Claim Disks for vSAN Direct

You can claim local storage devices as vSAN Direct for use with the vSAN Data Persistence Platform.

Only the vSAN Data Persistence platform can consume vSAN Direct storage. The vSAN Data Persistence platform provides a framework for software technology partners to integrate with Broadcom infrastructure. Each partner must develop their own plug-in for Broadcom customers to receive the benefits of the vSAN Data Persistence platform. The platform is not operational until the partner solution running on top is operational. For more information, see the vSphere Supervisor Concepts guide.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Click Claim Unused Disks.
5. On the Claim Unused Disks dialog, select the vSAN Direct tab.
6. Select a device to claim by selecting the checkbox in the Claim for vSAN Direct column. 

   Devices claimed for your vSAN cluster do not appear in the vSAN Direct tab.
7. Click Create.

For each device you claim, vSAN creates a new vSAN Direct datastore.

You can click the Datastores tab to display the vSAN Direct datastores in your cluster.