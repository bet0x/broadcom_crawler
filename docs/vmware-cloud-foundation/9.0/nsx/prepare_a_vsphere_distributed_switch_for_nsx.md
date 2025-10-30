---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Prepare a vSphere Distributed Switch for NSX
---

# Prepare a vSphere Distributed Switch for NSX

Before you configure an NSX transport node using vSphere Distributed Switch (VDS) as a host switch, ensure that the VDS created on a vCenter 7.0 or a later version is configured to manage NSX traffic.

- Verify that ESX hosts have the required number of physical NICs to meet networking requirements. For example, if you plan to configure teaming policies and remote span port mirroring, ensure that a free physical NIC is available to avoid uplink conflicts.
- Ensure that the MTU value of the physical switch port or LACP port is set to 1700 bytes.

High-level tasks to configure a cluster or a standalone managed host using a VDS switch.

To create a VDS switch supporting NSX networking, the following conditions must be met:

- vCenter 7.0 or a later version
- ESX 7.0 or a later version

1. In a vCenter, create a VDS. For more information about creating a VDS, see [Prepare a vSphere Distributed Switch for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html).

   - Set the MTU value for the VDS to at least 1600. A minimum MTU of 1700 is recommended.

     [Prepare a vSphere Distributed Switch for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/prepare-a-vsphere-distributed-virtual-switch-for-nsx-t.html) On VDS 7.0 or later, the default MTU size is 1500. To prepare a VDS for NSX overlay networking, the MTU size of the VDS must be at least 1600 (minimum of 1700 is recommended). If the MTU size of the VDS is below 1600, NSX Manager notifies you that the MTU size will be automatically increased to 1600.
   - Add hosts, that you want to prepare for NSX networking, to VDS created in vCenter.
   - Assign Physical NICS of each of the host as uplinks on the VDS.
2. In NSX, add an uplink profile that defines a teaming policy mapping NSX uplinks with VDS uplinks.
3. In NSX, prepare an ESX host using VDS as the host switch.

   At the end of the configuration, the host is prepared as NSX transport node with VDS as the host switch.

Configure the host as a transport node. See [Prepare ESX Cluster Hosts as Transport Nodes by Using TNP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/prepare-esxi-cluster-hosts-as-transport-nodes.html#GUID-9849f4e0-0bf1-470e-ab72-2a6afbe6c2ae).