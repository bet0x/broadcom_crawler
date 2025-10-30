---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-the-nsx-t-edge-nodes-in-the-vi-workload-domain-vcf-4-5.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the NSX Edge Nodes
---

# Start the NSX Edge Nodes

You continue powering on the NSX infrastructure in the workload domain by starting the NSX Edge nodes by using the vSphere Client.

1. Identify the vCenter instance that runs NSX Edge nodes.
2. Log in to vCenter for the workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. In the VMs and templates inventory, expand the tree of workload domain vCenter Server and expand data center for the workload domain.
4. Right-click an NSX Edge node from the edge cluster and select PowerPower on.

   This operations takes several minutes to complete.
5. Repeat these steps to power on the remaining NSX Edge nodes.