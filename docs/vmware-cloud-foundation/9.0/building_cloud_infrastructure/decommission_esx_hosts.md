---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/decommission-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Decommission ESX Hosts
---

# Decommission ESX Hosts

Removing ESX hosts from the global inventory is called decommissioning. If you want to re-use a host in a different VCF domain, you must decommission, re-image, and commission the host before adding it to the VCF domain.

The hosts that you want to decommission must not be assigned to a VCF domain. If a host is assigned to a VCF domain, you must remove it before you can decommission it.

To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

See [VMware Configuration Maximums](https://configmax.broadcom.com/home) for information about the maximum number of hosts you can decommission at one time and the maximum number of decommission hosts tasks that you can run in parallel.

1. In the vSphere Client, click Global Inventory ListsHostsUnassigned Hosts.
2. Select one or more hosts and click Decommission Selected Hosts.
3. Activate or deactivate Skip failed hosts during decommissioning.

   This setting is enabled by default. When enabled, hosts that fail are skipped and decommissioning continues on the remaining hosts.
4. Click Confirm.

If the decommissioned host was previously part of a VCF domain, you must re-image it before commissioning it again and adding it to a VCF domain. If the decommissioned host was not part of a VCF domain, you do not have to re-image it before commissioning it again.