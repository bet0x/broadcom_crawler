---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-nsx-t-edge-nodes-in-the-vi-workload-domain-vcf-4-5.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down the NSX Edge Nodes in the Workload Domain
---

# Shut Down the NSX Edge Nodes in the Workload Domain

You begin shutting down the NSX infrastructure in a workload domain in VCF by shutting down the NSX Edge nodes that provide north-south traffic connectivity between the physical data center networks and the NSX SDN networks

1. Identify the vCenter instance that runs NSX Edge nodes.
2. Log in to vCenter for the workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. In the VMs and Templates inventory, locate the NSX Edge appliance.
4. Right-click the an NSX Edge appliance and select PowerShut down Guest OS.
5. Repeat the steps for the remaining NSX Edge appliances in the VCF domain.