---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-the-nsx-t-manager-virtual-machines-in-the-vi-workload-domain-vcf-4-5.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the NSX Manager Nodes
---

# Start the NSX Manager Nodes

You begin powering on the NSX infrastructure in the workload domain by starting the NSX Manager appliance or cluster by using the vSphere Client.

1. Identify the vCenter instance that runs NSX Manager.
2. Log in to vCenter for the management or workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. In the VMs and templates inventory, expand the management domain vCenter Server tree and expand the management domain data center.
4. Power on the NSX Manager nodes for the workload domain.
   1. Right-click NSX Manager node and select PowerPower on.
   2. Repeat the steps to power on the remaining NSX Manager nodes.

   This operation takes several minutes to complete until the NSX Manager cluster becomes fully operational again and its user interface - accessible.
5. Log in to NSX Manager for the workload domain at https://<nsx\_manager\_cluster\_fqdn> as admin.
6. Verify the system status of the NSX Manager cluster.
   1. On the main navigation bar, click System.
   2. In the left pane, navigate to ConfigurationAppliances.
   3. On the Appliances page, verify that the NSX Manager cluster has a Stable status and all the listed NSX Manager nodes are available.