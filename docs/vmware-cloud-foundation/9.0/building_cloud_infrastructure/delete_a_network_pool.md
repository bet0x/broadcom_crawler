---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools/delete-a-network-pool.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Delete a Network Pool
---

# Delete a Network Pool

You can delete a network pool if none of the ESX hosts with an IP address from the pool belong to a workload domain. The default pool created during deployment cannot be deleted.

Ensure that the ESX hosts in the network pool are not assigned to a workload domain. To verify this, view the network pool details and confirm that the Used IPs for the network pool is 0.

To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

1. In the vSphere Client, click Global Inventory ListsHostsNetwork Pools.
2. Click the vertical ellipsis (three dots) in the network pool row you want to edit and then click Delete.
3. Click Delete.