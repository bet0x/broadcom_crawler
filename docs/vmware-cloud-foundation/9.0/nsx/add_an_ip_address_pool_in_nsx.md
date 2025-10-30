---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ip-address-management-ipam/add-an-ip-address-pool-in-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an IP Address Pool in NSX
---

# Add an IP Address Pool in NSX

You can configure
IP address pools for use by components such as DHCP.

1. With admin privileges, log in
   to NSX Manager.
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
8. Click
   Save.

   After you add an IP address pool and IP addresses have been allocated from
   the pool, you will not be able to delete the pool. If you want to expand the
   pool, you must add new IP ranges. For example, if the existing range is
   192.168.1.11 - 192.168.1.20 and you want to expand it to 192.168.1.10 -
   192.168.1.30, add the following two ranges:
   - 192.168.1.10 -
     192.168.1.10
   - 192.168.1.21 -
     192.168.1.30