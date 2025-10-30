---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/managing-transport-nodes/nsx-maintenance-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Maintenance Mode
---

# NSX Maintenance Mode

If you want to avoid vMotion of VMs to a transport node that is not functional, place that transport node in NSX Maintenance Mode.

To put a transport node in NSX Maintenance Mode, select the node, click ActionsNSX Maintenance Mode.

When you put a host in NSX Maintenance Mode, the transport node cannot participate in networking. Therefore, you must vMotion all VMs to another host before initiating NSX Maintenance Mode. Also, VMs running on other transport nodes that have VDS as the host switch cannot be vMotioned to this transport node. In addition, logical network cannot be configured on ESX hosts as the status of host switch on the ESX host would be shown as Down.

Scenarios to put the transport node in NSX Maintenance Mode:

- A transport node is not functional.
- If a host has hardware or software issues that are unrelated to NSX, but you want to retain the node and its configurations in NSX, place the host in NSX Maintenance Mode.
- A transport node is automatically put in NSX Maintenance Mode when an upgrade on that transport node fails.

Any transport node put in the NSX Maintenance Mode is not upgraded.