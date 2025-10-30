---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/configuring-an-nsx-multicast/create-an-igmp-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an IGMP Profile
---

# Create an IGMP Profile

Internet Group Management Protocol (IGMP) is a multicast protocol used in IPv4
networks.

Note that the IGMP snooping timeout for reports is 2 times the general query timeout.
By default, the IGMP snooping timeout value is 120 seconds. On ESX, the default IGMP snooping timeout value
is 60 seconds.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingNetworking Profiles.
3. Click the
   Multicast tab.
4. Click Add IGMP
   Profile.
5. Enter a profile name and the following profile details.

   | Option | Description |
   | --- | --- |
   | Query Interval (seconds) | Interval between general query messages. A larger value causes IGMP queries to be sent less often. Default: 30. Range: 1 - 1800. |
   | Query Max Response Time (seconds) | Maximum allowed time before sending a response to a membership query message. Default: 10. Range: 1 - 25. |
   | Last Member Query Interval (seconds) | Maximum amount of time between group-specific query messages, including those sent in response to leave-group messages. Default: 10. Range: 1 - 25. |
   | Robustness Variable | Number of IGMP query messages sent. This helps alleviate the risk of loss of packets in a busy network. A larger number is recommended in a network with high traffic. Default: 2. Range: 1 - 7. |