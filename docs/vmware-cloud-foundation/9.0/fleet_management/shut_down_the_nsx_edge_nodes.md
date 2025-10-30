---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-nsx-t-edge-nodes-in-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down the NSX Edge Nodes
---

# Shut Down the NSX Edge Nodes

You begin shutting down the NSX infrastructure in the management domain VMware Cloud Foundation by shutting down the NSX Edge nodes that provide north-south traffic connectivity between the physical data center networks and the NSX SDN networks

1. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
2. In the VMs and Templates inventory, locate the NSX Edge appliance.
3. Right-click the an NSX Edge appliance and select PowerShut down Guest OS.
4. In the confirmation dialog box, click Yes.

   This operation takes several minutes to complete.
5. Repeat the steps for the remaining NSX Edge nodes for the domain.