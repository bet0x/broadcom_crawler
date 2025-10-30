---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-the-arp-limit-of-a-tier-0-or-tier-1-gateway-or-logical-router.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure the ARP Limit of a Tier-0 or Tier-1 Gateway or Logical Router
---

# Configure the ARP Limit of a Tier-0 or Tier-1 Gateway or Logical Router

You can configure the ARP limit of a tier-0 or tier-1 gateway or logical router using
the API. The limit specifies the maximum number of ARP entries per transport node at each
gateway or logical router.

To read or set the global ARP limit, use the following API methods and parameter:

| Method | URI | Parameter |
| --- | --- | --- |
| GET, PUT, PATCH | /policy/api/v1/infra/global-config | arp\_limit\_per\_gateway (range: 5000 - 50000, default: 50000) |

To read or set the ARP limit for a specific
tier-0 or tier-1 gateway, use the following API methods and parameter. If the limit is
not set, the global ARP limit will apply.

| Method | URI | Parameter |
| --- | --- | --- |
| GET, PUT, PATCH | /policy/api/v1/infra/tier-0s/<tier-0-id> | arp\_limit (range: 5000 - 50000, no default) |
| GET, PUT, PATCH | /policy/api/v1/infra/tier-1s/<tier-1-id> | arp\_limit (range: 5000 - 50000, no default) |

Note that updating the ARP limit using
Manager GlobalConfig API is not allowed.