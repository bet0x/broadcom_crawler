---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-nsx-t-edge-nodes-in-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the NSX Edge Nodes
---

# Start the NSX Edge Nodes

You continue powering on the NSX infrastructure in the management domain by starting the NSX Edge nodes by using the vSphere Client.

1. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
2. In the VMs and templates inventory, expand the management domain vCenter Server tree and expand the management domain data center.
3. Right-click an NSX Edge node from the edge cluster and select PowerPower on.

   This operations takes several minutes to complete.
4. Repeat these steps to power on the remaining NSX Edge nodes.