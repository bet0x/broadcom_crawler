---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-an-ip-pool-for-tunnel-endpoint-ip-addresses.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an IP Pool for Tunnel Endpoint IP Addresses
---

# Create an IP Pool for Tunnel Endpoint IP Addresses

NSX Transport Nodes are configured with tunnel endpoint (TEP pool) IP addresses. Tunnel endpoints are the source and destination IP addresses used in the external IP header to identify the hypervisor hosts originating and end the NSX encapsulation of overlay frames. You can use either DHCP or manually configured IP pools for tunnel endpoint IP addresses.

You can also create IP pools for TEP IP addresses during the VCF cluster creation workflow. The VCF workflow or API will create the IP pools if required.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Navigate to NetworkingIP Address Pools.
3. Click Add IP Address Pool.
4. Enter a name and optionally a description.
5. From the Subnets column, click
   Set to add the subnets.
6. Click the Add Subnet drop-down menu and choose either
   IP Block or IP Ranges:

   - Choose IP
     Block to use an IP block of the allowable IP
     addresses:

     | Setting | Description |
     | --- | --- |
     | Select IP Blocks | Choose an IP address block. |
     | Size | Specify the size or the number of IP addresses in the IP address block. |
     | Allocation Range | Specify the allocation range for the IP address block. For an IPv6 address block, you must specify an allocation range. The allocation range value cannot be more than 1048576. |
     | Auto Assign Gateway | Click the toggle to enable or disable automatic gateway IP assignment. |
   - Choose IP
     Ranges to specify the range of IP addresses that can be
     used:

     | Setting | Description |
     | --- | --- |
     | Enter IPv4 or IPv6 Ranges | Enter the range of IPv4 or IPv6 addresses. Transport nodes and tunnel endpoints (TEPs) do not allow a mixed IP address pool to be used (an IP pool with both IPv4 and IPv6 ranges). Ensure that the IP range consists of only IPv4 or only IPv6 addresses. |
     | CIDR | Enter the IP address range in CIDR format. |
     | Gateway IP | Enter the gateway address. |
     | DNS Server | Enter the list of the DNS (domain name system) server IP addresses separated by commas. |
     | DNS Suffix | Enter the DNS suffix. For example, corp.local. |
7. Click Add and then Apply.
8. Click Save.

   IP Pools are configured for only those hosts that participate in overlay traffic (hosts that are members of an overlay transport zone). So, TEP tunnels are not required for host clusters that are member of VLAN transport zones only and/or management host clusters (hosting NSX Appliances / NSX Edge VMs) if management appliances are connected to VLAN backed VDS portgroups.

The IPv4 or IPv6 address pool is listed on the IP pool page.

If you are using API to view the list of IP addresses allocated from an IP pool, run the NSX Manager API. Do not run the Policy API to view IP pool allocations.

For example, the Policy API call does not retrieve IP addresses allocated from an IP pool.

GET https://<nsxmanager-IP>/policy/api/v1/infra/ip-pools/TEP-IP-Pool/ip-allocations

```
{
"results": [],
"result_count": 0,
"sort_by": "display_name",
"sort_ascending": true
}
```

The NSX Manager API retrieves IP addresses allocated from an IP pool.

GET https://<nsxmanager-IP>/api/v1/pools/ip-pools/<ip-pool-UUID>/allocations

```
{
"results": [
{
   "allocation_id": "192.85.85.12",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.13",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.14",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.15",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.16",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.17",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.18",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.19",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.20",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.21",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.11",
   "_protection": "NOT_PROTECTED"
},
{
   "allocation_id": "192.85.85.22",
   "_protection": "NOT_PROTECTED"
}
],
"result_count": 12
}
```

Create an uplink profile. See [Create an Uplink Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html).