---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools/add-or-remove-a-network-pool-ip-address-range.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Add a Network Pool IP Address Range 
---

# Add a Network Pool IP Address Range

You can edit a network pool to add a new IP address range.

To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

1. In the vSphere Client, click Global Inventory ListsHostsNetwork Pools.
2. Click the vertical ellipsis (three dots) in the network pool row you want to edit and then click Add additional Network Pool IP Range.
3. Enter the start and end IP addresses and click Add.