---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Virtual Private Network (VPN)
---

# Virtual Private Network (VPN)

NSX supports IPSec Virtual Private Network (IPSec VPN) and Layer 2 VPN (L2 VPN) on an NSX Edge node.

- IPSec VPN offers site-to-site connectivity between an NSX Edge node and remote sites.
- L2 VPN allows you to extend L2 networks across data centers securely by enabling virtual machines to keep their network connectivity across geographical boundaries while using the same IP address

You must have a working NSX Edge node with at least one configured Tier-0 or Tier-1 gateway before you can configure a VPN service.

You can configure VPN services through NSX Manager or the REST API.

To configure VPN services, you must use new objects, such as Tier-0 gateways, that were created using the NSX Manager UI or Policy APIs that are included with NSX.

System-default configuration profiles with predefined values and settings are made available for your use during a VPN service configuration. You can also define new profiles with different settings and select them during the VPN service configuration.