---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/teaming-policy.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Teaming Policy
---

# Teaming Policy

A teaming policy defines how VDS uses its uplink for redundancy and traffic load balancing.

In the Teaming section, you can either enter a default teaming policy or you can choose to enter a named teaming policy that is only applicable to VLAN networks. Click Add to add a naming teaming policy. A teaming policy defines how VDS uses its uplink for redundancy and traffic load balancing. You can configure a teaming policy in the following modes:

- Failover Order: Specify an active uplink along with an optional list of standby uplinks. If the active uplink fails, the next uplink in the standby list replaces the active uplink. No actual load balancing is performed with this option. Standby uplinks and multiple active uplinks are not supported for NSX Edge transport nodes. Also, for an NSX Edge transport node, active uplink used in one profile should must not be used in another profile.
- Load Balance Source: Maps a virtual interface of a VM to an uplink. Traffic sent by this virtual interface will leave the host through this uplink only, and traffic destined to this virtual interface will necessarily enter the virtual switch through this uplink. Select a list of active uplinks. When you configure a transport node, you can pin each interface of the transport node to one active uplink. This configuration allows use of several active uplinks at the same time. No standby uplink is configured in this case.

  To manage VLAN traffic, if you configure a default teaming policy in Load Balance Source mode, then on failure of the first uplink, traffic will not fail over to the second uplink interface.
- Load Balance Source MAC Address: Select an uplink based on a hash of the source Ethernet. NSX Edge transport nodes do not support this teaming policy.

- On ESX hosts: For default teaming policy - Load Balance Source MAC, Load Balance Source, and Failover Order teaming policies are supported.
- On NSX Edge: For default teaming policy, Load Balance Source and Failover Order teaming policies are supported. For named teaming policy, only Failover Order policy is supported.

(ESX hosts and NSX Edge) You can define the following policies for a transport zone:

- A Named teaming policy for every VLAN-based logical switch or segment.
- A Default teaming policy for the entire VDS.

Named teaming policy: A named teaming policy means that for every VLAN-based logical switch or segment, you can define a specific teaming policy mode and uplinks names. This policy type gives you the flexibility to select specific uplinks depending on the traffic steering policy, for example, based on bandwidth requirement.

- If you define a named teaming policy, VDS uses that named teaming policy if it is attached to the VLAN-based transport zone and finally selected for specific VLAN-based logical switch or segment in the host.
- If you do not define any named teaming policies, VDS uses the default teaming policy.

For more details, see [Configure Named Teaming Policy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/configure-named-teaming-policy.html).