---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/changing-the-distributed-router-interfaces--mac-address.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Changing the Distributed Router Interfaces' MAC Address
---

# Changing the Distributed Router Interfaces' MAC Address

All logical router interfaces in NSX and NSX-V setups have the same MAC address (02:50:56:56:44:52). Starting
with NSX 3.0.2, you can change this address in
NSX to avoid issues when migrating VMs
from an NSX-V setup to an
NSX setup.

Changing the MAC address involves making two
API calls.

If you have not created any transport node, make the following GET API call. For
example:

```
GET https://10.40.79.126/api/v1/global-configs/RoutingGlobalConfig

Response:
{
  "l3_forwarding_mode" : "IPV4_ONLY",
  "logical_uplink_mtu" : 1500,
  "vdr_mac" : "02:50:56:56:44:77",
  "vdr_mac_nested" : "02:50:56:56:44:52",
  "allow_changing_vdr_mac_in_use" : true,
  "resource_type" : "RoutingGlobalConfig",
  "id" : "49b261fe-f4e4-46ad-958c-da9cb4271e32",
  "display_name" : "49b261fe-f4e4-46ad-958c-da9cb4271e32",
  "_create_user" : "system",
  "_create_time" : 1595313890595,
  "_last_modified_user" : "admin",
  "_last_modified_time" : 1595465694142,
  "_system_owned" : false,
  "_protection" : "NOT_PROTECTED",
  "_revision" : 14
}
```

Take the response of the call, change the
vdr\_mac value, and use it to make the following PUT API call.
For
example:

```
PUT  https://10.40.79.126/api/v1/global-configs/RoutingGlobalConfig
{
  "l3_forwarding_mode" : "IPV4_ONLY",
  "logical_uplink_mtu" : 1500,
  "vdr_mac" : "02:50:56:56:44:99",
  "vdr_mac_nested" : "02:50:56:56:44:53",
  "allow_changing_vdr_mac_in_use" : true,
  "resource_type" : "RoutingGlobalConfig",
  "id" : "49b261fe-f4e4-46ad-958c-da9cb4271e32",
  "display_name" : "49b261fe-f4e4-46ad-958c-da9cb4271e32",
  "_create_user" : "system",
  "_create_time" : 1595313890595,
  "_last_modified_user" : "admin",
  "_last_modified_time" : 1595465694142,
  "_system_owned" : false,
  "_protection" : "NOT_PROTECTED",
  "_revision" : 14
}

Response:
{
  "l3_forwarding_mode" : "IPV4_ONLY",
  "logical_uplink_mtu" : 1500,
  "vdr_mac" : "02:50:56:56:44:99",
  "vdr_mac_nested" : "02:50:56:56:44:53",
  "allow_changing_vdr_mac_in_use" : true,
  "resource_type" : "RoutingGlobalConfig",
  "id" : "49b261fe-f4e4-46ad-958c-da9cb4271e32",
  "display_name" : "49b261fe-f4e4-46ad-958c-da9cb4271e32",
  "_create_user" : "system",
  "_create_time" : 1595313890595,
  "_last_modified_user" : "admin",
  "_last_modified_time" : 1595466163148,
  "_system_owned" : false,
  "_protection" : "NOT_PROTECTED",
  "_revision" : 15
}
```

If you have already created transport nodes,
make the same GET and PUT API calls, except that for the PUT call, set the parameter
allow\_changing\_vdr\_mac\_in\_use to true.