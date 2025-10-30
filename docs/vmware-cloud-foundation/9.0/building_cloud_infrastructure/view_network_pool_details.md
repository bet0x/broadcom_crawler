---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools/view-network-pool-details.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > View Network Pool Details
---

# View Network Pool Details

You can view the network details for a network pool as well as the total number of used and available IP addresses.

To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

1. In the vSphere Client, click Global Inventory ListsHostsNetwork Pools.
2. Click the arrow to the left of the pool name.

   ![Network pool details, including the number of free and used IP addresses and other information.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cfe5c526-5b73-4a4f-9203-896e8930d3f1.original.png)

   A summary view of the network pools details is displayed.
3. Click the name of a network pool. 

   A detailed view of the network pool details is displayed, including network types and included IP ranges.