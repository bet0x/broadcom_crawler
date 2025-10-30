---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/create-a-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Create a vSAN Cluster
---

# Create a vSAN Cluster

You can create a cluster, and then configure the cluster for vSAN.

1. Right-click a data center and select New Cluster.
2. Type a name for the cluster in the Name text box.
3. Turn on DRS, vSphere HA, and vSAN for the cluster. 

   Check Enable vSAN ESA to use vSAN ESA. vSAN ESA is optimized for high-performance flash storage devices that provide greater performance and efficiency.
4. Select any option to Choose how to set up the cluster's image. For more information on setting up cluster image, see [Create a Cluster That Uses an Image by Composing a New Image](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/cluster-operations-and-vsphere-lifecycle-manager.html#GUID-1CC78B7E-2AD4-4442-ADFD-37E841B969AE-en) in the Managing Host and Cluster Lifecycle guide.
5. (Optional) Select Manage configuration at a cluster level check box to ensure that all the ESX hosts in the cluster have the same settings.
6. Click Next.
7. Select an image from the Image Library of Lifecycle Manager.
8. Click Next and review the cluster details.
9. Click Finish.

   The cluster appears in the inventory.
10. Add hosts to the vSAN cluster. 

    vSAN clusters can include hosts with or without capacity devices. For best results, add hosts with capacity.

Configure services for the vSAN cluster. See [Configure a vSAN Cluster Using the vSphere Client](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/configure-a-cluster-for-vsan-using-the-vsphere-client.html#GUID-e6128a7b-81bf-4aaa-9065-6ab90e24bdfc-en).