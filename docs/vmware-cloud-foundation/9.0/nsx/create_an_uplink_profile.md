---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an Uplink Profile
---

# Create an Uplink Profile

An uplink is a link from the NSX Edge nodes or hypervisor nodes to the top-of-rack switches or NSX logical switches. A link is from a physical network interface on an NSX Edge node or hypervisor nodes to a switch.

- See NSX Edge network requirements in [NSX Edge Installation Requirements](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/nsx-edge-installation-requirements.html).
- Each uplink in the uplink profile must correspond to an up and available physical link on your hypervisor host or on the NSX Edge node.

  For example, your hypervisor host has two physical links that are up: vmnic0 and vmnic1. Suppose vmnic0 is used for management and storage networks, while vmnic1 is unused. This might mean that vmnic1 can be used as an NSX uplink, but vmnic0 cannot. To do link teaming, you must have two unused physical links available, such as vmnic1 and vmnic2.

  For an NSX Edge, tunnel endpoint and VLAN uplinks can use the same physical link. For example, vmnic0/eth0/em0 might be used for your management network and vmnic1/eth1/em1 might be used for your fp-ethX links.

An uplink profile defines policies for the uplinks. The settings defined by uplink profiles can include teaming policies, active and standby links, transport VLAN ID, and MTU setting.

Consider the following points when configuring Failover Teaming Policy for VM appliance-based NSX Edge nodes and Bare Metal NSX Edge:

- For uplinks used by a teaming policy, you cannot use the same uplinks in a different uplink profile for a given NSX Edge transport node. Standby uplinks are not supported and must not be configured in the failover teaming policy. If the teaming policy uses more than one uplink (active/standby list), you cannot use the same uplinks in the same or a different uplink profile for a given NSX Edge transport node.
- Supported scenarios:
  - Bare Metal NSX Edge supports a single active uplink and a standby uplink. They do not support multiple standby uplinks.
  - NSX Edge VMs do not support any standby uplinks - single or multiple standby uplinks.

Consider the following points when configuring Load Balance Source for VM appliance-based NSX Edge nodes:

- Supports multiple active uplinks.
- You cannot use LAG to configue the teaming policy.
- In the Active Uplinks field, enter uplink labels that will be associated to physical NICs when you prepare transport nodes. For example, uplink1, uplink2. When you prepare transport nodes, you will associate uplink1 to pnic1 and uplink2 to pnic2.
- You must use the Load Balanced Source teaming policy for traffic load balancing.

Consider the following points when configuring Load Balance Source for Bare Metal NSX Edge:

- Supports multiple active uplinks.
- In the Active Uplinks field, you can use LAGs or enter individual uplink lables. For example, LAG1 or uplink1, uplink2.
- A LAG must have two physical NICs on the same N-VDS.
- The number of LAGs that you can actually use depends on the capabilities of the underlying physical environment and the topology of the virtual network. For example, if the physical switch supports up to four ports in an LACP port channel, you can connect up to four physical NICs per host to a LAG.
- In the LACP section, Bare Metal NSX Edge only supports Source and destination MAC address, IP address and TCP/UDP port.
- If multiple LAG uplinks are configured on a Bare Metal NSX Edge, enter a unique LAG name for each LAG uplink profile.
- If multi-vtep uplink profile is used for Bare Metal NSX Edge or edge VMs, NSX only supports Load Balance Source teaming policy.
- You must use the Load Balanced Source teaming policy for traffic load balancing.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricProfilesUplink ProfilesAdd Profile.
3. Enter an uplink profile name. Add an optional uplink profile description.
4. Teamings: Click Set. Create a default teaming policy and optionally a named teaming policy. In the Set Teamings window, complete the fields.
   1. Click Add Teaming.
   2. In the Teaming Policy drop-down field, select from Failover Order, Load Balance Source or Load Balance Source MAC address.
   3. In the Active Uplinks field, enter the active uplink name. For example, uplink1, uplink2 and so on.
   4. In the Standby uplinks field, enter the standby uplink name.
   5. To enable preemptive failover from a standby uplink to an active uplink after the active comes back up, enable Failback. If you do not want the active uplink to carry traffic once it is back up again after a failure (non-preemptive), disable Failback.
   6. Click Add.
   7. Click Apply.

      For more details on teamings, see [Teaming Policy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/teaming-policy.html) and [Configure Named Teaming Policy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/configure-named-teaming-policy.html).
5. LAGs: Click Set to configure Link aggregation groups (LAGs) using Link Aggregation Control Protocol (LACP) for the transport network.
   1. On The Set LAGs window, click Add LAG.
   2. Enter a name for the LAG.
   3. Select the LACP mode - Active or Passive.
   4. Select the LACP Load Balancing mode.
   5. Enter the number of uplinks.
   6. Select the LACP time out type - Slow or Fast.
   7. Click Add.
   8. Click Apply.

      For more details on LAG, see [Link Aggregation Groups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/link-aggregation-groups.html).
6. Enter a Transport VLAN ID value. The transport VLAN set in the uplink profile tags overlay traffic only and the VLAN ID is used by the Tunnel Endpoint Pools (TEP IP Pools).

   While you can choose any of the available pre-created default uplink profiles, note that you can only edit and configure the transport VLAN ID field to a value of your choice. You cannot edit any other field of a pre-created default uplink profile.
7. Enter the MTU value. 

   For hosts that use vSphere VDS, configure MTU on the VDS from vCenter. The uplink profile MTU default value is 1700 bytes and is applicable to transport-nodes that use N-VDS.

   The MTU field is optional. If you do not configure it, NSX takes the value set in the Tunnel Endpoint MTU field. If both MTU fields are set, uplink profile MTU value ovrerrides the tunnel endpoint MTU value.

   ![Global Fabric Settings](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/12e3888e-26cd-4b04-b38c-b4f3c6043573.original.png)

   For more information on MTU guidance, see [Guidance to Set Maximum Transmission Unit](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/mtu-guidance.html).
8. Configure global tunnel endpoint MTU.

In addition to the UI, you can also view the uplink profiles with the API call GET /policy/api/v1/infra/host-switch-profiles.