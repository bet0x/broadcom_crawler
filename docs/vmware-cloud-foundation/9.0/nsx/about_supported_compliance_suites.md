---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/about-supported-compliance-suites.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > About Supported Compliance Suites
---

# About Supported Compliance Suites

You can specify a security compliance suite to use to configure the security profiles
used for an IPSec VPN session.

A security compliance suite has predefined
values that are used for different security parameters and that cannot be modified. When
you select a compliance suite, the predefined values are automatically used for the
security profile of the IPSec VPN session you are configuring.

The following table lists the compliance suites that are supported for IKE profiles in
NSX and the values that
are predefined for each.

| Compliance Suite Name | IKE Version | Encryption Algorithm | Digest Algorithm | Diffie Hellman Group |
| --- | --- | --- | --- | --- |
| CNSA | IKE V2 | AES 256 | SHA2 384 | Group 15, Group 20 |
| FIPS | IKE FLEX | AES 128 | SHA2 256 | Group 20 |
| Foundation | IKE V1 | AES 128 | SHA2 256 | Group 14 |
| PRIME | IKE V2 | AES GCM 128 | Not Set | Group 19 |
| Suite-B-GCM-128 | IKE V2 | AES 128 | SHA2 256 | Group 19 |
| Suite-B-GCM-256 | IKE V2 | AES 256 | SHA2 384 | Group 20 |
| The AES 128 and AES 256 algorithms use the CBC mode of operation. | | | | |

The following table lists the compliance
suites that are supported for IPSec profiles in NSX and the values that are predefined for each.

| Compliance Suite Name | Encryption Algorithm | Digest Algorithm | PFS Group | Diffie-Hellman Group |
| --- | --- | --- | --- | --- |
| CNSA | AES 256 | SHA2 384 | Enabled | Group 15, Group 20 |
| FIPS | AES GCM 128 | Not Set | Enabled | Group 20 |
| Foundation | AES 128 | SHA2 256 | Enabled | Group 14 |
| PRIME | AES GCM 128 | Not Set | Enabled | Group 19 |
| Suite-B-GCM-128 | AES GCM 128 | Not Set | Enabled | Group 19 |
| Suite-B-GCM-256 | AES GCM 256 | Not Set | Enabled | Group 20 |
| The AES 128 and AES 256 algorithms use the CBC mode of operation. | | | | |