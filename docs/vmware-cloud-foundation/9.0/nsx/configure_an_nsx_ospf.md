---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-ospf.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX OSPF
---

# Configure an NSX OSPF

OSPF (Open Shortest Path First) is an interior gateway protocol (IGP) that
operates within a single autonomous system (AS). Starting with NSX 3.1.1, you can configure OSPF on
a tier-0 gateway.

The OSPF feature has the following capabilities and restrictions:

- Only OSPFv2 is supported.
- The tier-0 gateway can be active-active or active-standby (preemptive and
  non-preemptive).
- Only the default VRF is supported.
- You can configure a single area on a tier-0 gateway with a maximum of two
  tier-0 uplinks per Edge node.
- Backbone, normal area, and NSSA (not-so-stubby area) are supported.
- No redistribution is supported between BGP and OSPF.
- OSPF and BGP can be used together in the case of BGP multi-hop where the
  peer IP is learned through OSPF.
- The same redistribution features supported for BGP are supported for OSPF
  (tier-0 uplinks, downlinks, loopbacks, tier-1 downlinks, etc.). Depending on
  the area type, redistribution for all these networks will result in the Edge
  node generating type 5 external LSA (link-state advertisement) or type 7
  external LSA with type 2 metric only (e2 or n2 routes). The Edge node itself
  can learn any type of LSA.
- MD5 and plain password authentication are supported on the area
  configuration.
- Federation is not supported.
- Route summarization for e2 and n2 routes is supported.
- The interface running OSPF can be broadcast or numbered point-to-point
  (/31).
- OSPF sessions can be backed with BFD.
- For graceful restart, only the helper mode is supported.
- Redistribution route maps are supported. Only the matching of prefix lists
  is applicable. No set actions.
- OSPF ECMP is supported up to maximum of 8 paths.
- Default Originate is supported.
- NAT with OSPF is not
  supported.
- Tier-0 VIP with OSPF is not
  supported.

How the OSPF router ID (RID) is
determined:

- If there is no loopback
  interface, OSPF takes the highest interface IP address as RID.
- If OSPF has already chosen the
  highest interface IP as RID, adding a loopback interface will not affect
  OSPF neighborship and RID is not changed.
- If RID is the highest interface
  IP and loopback is present, disabling and enabling OSPF will change the RID
  to the loopback IP.
- If RID is the highest interface
  IP and loopback is present, rebooting the edge node, enabling maintenance
  mode on the edge node, or restarting the routing process will not change the
  RID.
- If RID is the highest interface
  IP and loopback is present, redeploying or replacing the edge transport node
  will change the RID to the loopback interface IP.
- If RID is the highest interface
  IP and loopback is present, modifying or deleting the highest interface IP
  address will change the RID to the loopback interface IP.
- If RID is the loopback
  interface IP, modifying or deleting the highest interface IP will not change
  the RID.
- Clearing OSPF neighbors will
  change the RID. It retains only the old RID.
- A soft restart or hard restart
  of OSPF adjacency from a remote site does not affect the OSPF RID.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingTier-0
   Gateways.
3. Click the OSPF toggle to
   enable OSPF.
4. In the Area
   Definition field, click Set to add an
   area definition.

   You can add only one area definition.

   1. Click Add
      Area Definition.
   2. Enter an area ID.

      The value must be a number or 4 numbers in IPv4 format (for example,
      1.2.3.4).
   3. In the
      Type column, select
      Normal or NSSA.

      An OSPF NSSA (not-so-stubby area) allows external routes to be flooded
      within the area.
   4. In the
      Authentication column, select
      None, Password, or
      MD5.
   5. In the Key
      ID column, enter a key ID if
      Authentication is set to
      MD5.
   6. In the
      Password column, enter a password if
      Authentication is set to
      Password or MD5.

      In NSX
      3.1.3.2 and earlier, the plain-text and MD5 passwords can have a maximum
      of 8 characters. Starting with NSX 3.1.3.3, the MD5 password can have a
      maximum of 16 characters, and the maximum length of the plain-text
      password remains to be 8 characters.
   7. Click
      Save.
5. In the Graceful
   Restart field, select either Disable or
   Helper Only.
6. Click the
   ECMP toggle to enable or disable ECMP.

   ECMP (equal-cost multi-path) routing allows packet forwarding to occur over
   multiple best paths. It can provide fault tolerance for failed paths.
7. In the Route
   Summarization field, click Set to add a
   summary address.

   Route summarization can reduce the number of LSAs that are flooded into an
   area. You can summarize one or more ranges of IP addresses and send routing
   information about these addresses in a single LSA.

   1. Click Add
      Prefix.
   2. Enter an IP address
      prefix in CIDR format.
   3. In the
      Advertise column, select
      Yes or No to indicate
      whether to advertise the summary route.

      The default is Yes.
   4. Repeat the steps above
      to add more prefixes.
8. Click the Default
   Route Originate toggle to enable or disable default route
   originate.

   Enable this to redistribute the default route in OSFP.
9. In the OSPF
   Configured Interfaces field, click Set to
   configure OSPF on existing external interfaces.
   1. Click
      Configure Interface.
   2. In the
      Interface column, select an interface from
      the dropdown list.
   3. In the Area
      ID column, select an area ID from the dropdown
      list.
   4. In the
      Network Type column, select
      Broadcast or
      P2P.
   5. In the
      OSPF column, set the toggle to
      Enabled.
   6. Click the
      BFD toggle to enable or disable BFD.
   7. If BFD is enabled,
      select a BFD profile.
   8. To change the
      OSPF Hello Interval, enter a new value.

      The default is 10 seconds. This parameter specifies the time between
      Hello messages.
   9. To change the
      OSPF Dead Interval, enter a new value.

      The default is 40 seconds. If a Hello message is not received within
      this time interval, the neighbor is considered unavailable..
   10. Click
       Save.
   11. Repeat the steps above
       to configure more interfaces.
10. Click
    Save.
11. Click Route
    Re-distribution to expand the section.
12. Click the OSPF Route
    Redistribution Status toggle to enable OSPF.
13. If you have route
    re-distribution rules configured, click the number to see the current rules or
    to add additional ones. If you do not have any configured, click
    Set to add re-distribution rules. Add
    OSPF to the Destination
    Protocol of any rule that will redistribute routes into OSPF.
    Remember to do this step if you plan to add re-distribution rules later.

After you configure OSPF, in the
OSPF Neighbors field, you can click
View to see information about OSPF neighbors. The information
displayed includes Neighbor IP Address,
Interface, Source, Edge
Node, Priority, and
State.

Note: If
a neighbor is not reachable, an alarm about the neighbor will be raised. If the
neighbor is no longer in the network, simply acknowledge the alarm but do not
resolve it. If you resolve the alarm, it will be raised again.