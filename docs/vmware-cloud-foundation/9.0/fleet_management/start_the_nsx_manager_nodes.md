---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-nsx-t-manager-virtual-machines-in-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the NSX Manager Nodes
---

# Start the NSX Manager Nodes

You begin powering on the NSX infrastructure in the management domain by starting the NSX Manager appliance or cluster by using the vSphere Client.

1. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
2. In the VMs and templates inventory, expand the management domain vCenter Server tree and expand the management domain data center.
3. Power on the NSX Manager nodes for the management domain.
   1. Right-click NSX Manager node and select PowerPower on.
   2. Repeat the steps to power on the remaining NSX Manager nodes.

   This operation takes several minutes to complete until the NSX Manager cluster becomes fully operational again and its user interface - accessible.
4. Log in to NSX Manager for the management domain at https://<nsxt\_manager\_cluster\_fqdn> as admin.
5. Verify the system status of NSX Manager cluster.
   1. On the main navigation bar, click System.
   2. In the left pane, navigate to ConfigurationAppliances.
   3. On the Appliances page, verify that the NSX Manager cluster has a Stable status and all NSX Manager nodes are available.