---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/managing-nsx-on-a-vsphere-distributed-switch/managing-nsx-distributed-virtual-port-groups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Managing NSX Distributed Virtual Port Groups
---

# Managing NSX Distributed Virtual Port Groups

A transport node prepared with VDS as a host switch ensures that segments created in NSX is realized as an NSX Distributed Virtual port group on a VDS switch and Segment in NSX .

In earlier versions of NSX, a segment created in NSX are represented as an opaque network in vCenter. When running NSX on a VDS switch, a segment is represented as an NSX Distributed Virtual Port Groups.

Any changes to the segments on the NSX network are synchronized in vCenter.

In vCenter, an NSX Distributed Virtual Port Group is represented as ![Icon representing NSX Distributed Virtual Port Group.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/81dd0767-5a66-455c-8068-764dcaeea940.original.png).

![
            NSX segment is realized as a NSX object in vCenter.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d8f2b3d2-de13-4762-8785-4423784bf25f.original.png)

Any NSX segment created in NSX is realized in vCenter as an NSX object. A vCenter displays the following details related to NSX segments:

- NSX Manager
- Virtual network identifier of the segment
- Transport zone
- Attached virtual machines

The port binding for the segment is by default set to Ephemeral. Switching parameters for the switch that are set in NSX cannot be edited in vCenter and conversely.

In a vCenter, an NSX Distributed Virtual port group realized does not require a unique name to differentiate it with other port groups on a VDS switch. So, multiple NSX Distributed Virtual port groups can have the same name. Any vSphere automations that use port group names might result in errors.

In vCenter, you can perform these actions on an NSX Distributed Virtual Port Group:

- Add VMkernel Adapters.
- Migrate VMs to Another Network.

However, NSX objects related to an NSX Distributed Virtual port group can only be edited in NSX Manager. You can edit these segment properties:

- Replication Mode for the segment
- VLAN trunk ID used by the segment
- Switching Profiles (for example, Port Mirroring)
- Ports created on the segment

For details on configuring a vSphere Distributed Virtual port group, refer to the vSphere Networking Guide.