---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Adding Profiles
---

# Adding Profiles

NSX provides the system-generated IPSec tunnel profile and an
IKE profile that are assigned by default when you configure either an IPSec VPN
or L2 VPN service. A system-generated DPD profile is created for an IPSec VPN
configuration.

The IKE and IPSec profiles provide information about
the algorithms that are used to authenticate, encrypt, and establish a shared secret
between network sites. The DPD profile provides information about the number of seconds
to wait in between probes to detect if an IPSec peer site is alive or not.

If you decide not to use the default profiles provided
by NSX, you can configure your own profile using the
information in the topics that follow in this section.