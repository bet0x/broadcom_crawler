---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools/create-a-network-pool.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a Network Pool
---

# Create a Network Pool

A network pool must include the vMotion network information. Depending on the type of storage you are using, you must provide network information for vSAN, NFS, and iSCSI.

The subnet in a network pool cannot overlap the subnet of another pool.

To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

Starting with VMware Cloud Foundation 9.0 and vSphere Foundation 9.0, the vSphere Virtual Volumes capability, also known as vVols, is deprecated and will be removed in a future release of VMware Cloud Foundation and vSphere Foundation. Support for vSphere Virtual Volumes will continue for critical bug fixes only for versions of vSphere 8.x, VMware Cloud Foundation and vSphere Foundation 5.x, and other supported versions until end-of-support for the respective release.

1. In the vSphere Client, click Global Inventory ListsHostsNetwork Pools.
2. Click Create Network Pool.
3. Enter a name for the network pool.
4. Select the network type(s). 

   - For vSAN ESA/OSA and NFS, you can include both vSAN and NFS network information in the same network pool or create separate network pools for vSAN and NFS.
   - For vSAN storage, select vSAN, vSAN Storage Client, and vMotion.`
   - For vSAN compute, select vSAN and vMotion.
   - For VMFS on FC, select vMotion only or vMotion and NFS.
   - For vVols on FC, select vMotion only or vMotion and NFS.
   - For vVols on iSCSI, select vMotion and iSCSI.
   - For vVols on NFS, select vMotion and NFS.
5. Provide the following network information for the selected network type(s). 

   | Option | Description |
   | --- | --- |
   | VLAN ID | Enter a VLAN ID between 1 and 4094. |
   | MTU | Enter an MTU between 1500 and 9000. |
   | Network | Enter a subnet IP address. |
   | Subnet Mask | Enter the subnet mask.  You cannot change the subnet after the network pool is created. |
   | Default Gateway | Enter the default gateway. |
   | Included IP Ranges | Enter an IP address range from which an IP address can be assigned to hosts that are associated with this network pool. The IP address range must be from within the specified subnet. You cannot include the IP address of the default gateway in the IP address range. You can enter multiple IP address ranges. Ensure that you have entered the correct IP address range. IP ranges cannot be edited after the network pool is created. |
6. Click Save.