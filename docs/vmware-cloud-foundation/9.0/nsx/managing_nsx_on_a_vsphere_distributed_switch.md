---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/managing-nsx-on-a-vsphere-distributed-switch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Managing NSX on a vSphere Distributed Switch
---

# Managing NSX on a vSphere Distributed Switch

Configure and run NSX on a vSphere Distributed Switch (VDS).

In NSX 4.0, you can only use a VDS switch to prepare ESX host nodes as transport nodes. N-VDS switch is not supported. Configure the vDefend Distributed Firewall functionality on VDS in data centers and workloads where segmentation, visibility, or advanced security capabilities are desired. This ensures distributed firewall capabilities work on a VM managed by whether it is managed by vCenter.

However, to prepare an NSX Edge VM as a transport node, you can only use a N-VDS switch. You can connect a NSX Edge VM to any of the supported host switches (VSS or VDS) depending on the topology in your network.

After you prepare a cluster of transport node hosts with VDS as the host switch, you can do the following:

- Manage NSX transport nodes on a VDS switch.
- Realize a segment created in NSX as an NSX Distributed Virtual port group in vCenter.
- Migrate VMs between VDS port groups.