---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configuring-appliances.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring Appliances
---

# Configuring Appliances

Some system
configuration tasks must be done using the command line or API.

For complete command line
interface information, see the
NSX Command-Line Interface Reference. For complete API
information, see the
NSX API Guide.

System configuration
commands and API requests.



| Task | Command Line  (NSX Manager and NSX Edge) | API Request  (NSX Manager only) |
| --- | --- | --- |
| Set system timezone | set timezone <timezone> | PUT https://<nsx-mgr>/api/v1/node |
| Set NTP Server | set ntp-server <ntp-server> | PUT https://<nsx-mgr>/api/v1/node/services/ntp |
| Set a DNS server | set name-servers <dns-server> | PUT https://<nsx-mgr>/api/v1/node/network/name-servers |
| Set DNS Search Domain | set search-domains <domain> | PUT https://<nsx-mgr>/api/v1/node/network/search-domains |

The recommended method to configure
an NTP server for all appliances is to configure a node profile. See [Configure a Node Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configure-a-node-profile.html#GUID-039fa17d-48f8-4fa6-9949-30ad93be4e9c-en). If
you configure an NTP server individually on an appliance, be sure to configure the
same NTP server on all the appliances.