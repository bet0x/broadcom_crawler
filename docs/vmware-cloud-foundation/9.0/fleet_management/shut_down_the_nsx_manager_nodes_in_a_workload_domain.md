---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-nsx-t-managers-in-the-vi-workload-domain-vcf-4-5.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down the NSX Manager Nodes in a Workload Domain
---

# Shut Down the NSX Manager Nodes in a Workload Domain

You continue shutting down the NSX infrastructure for the workload domain by shutting down the NSX Manager VM or cluster by using the vSphere Client.

1. Identify the vCenter instance that runs NSX Manager.
2. Log in to vCenter for the management or workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. In the VMs and Templates inventory, locate an NSX Manager appliance.
4. Right-click the NSX Manager appliance and select PowerShut down Guest OS.
5. In the confirmation dialog box, click Yes.

   This operation takes several minutes to complete.
6. Repeat the steps for the remaining NSX Manager appliances.