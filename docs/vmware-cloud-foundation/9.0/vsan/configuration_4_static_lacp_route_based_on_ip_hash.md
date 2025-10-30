---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/nic-teaming-configuration-examples/configuration-4-static-lacp---route-based-on-ip-hash.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configuration 4: Static LACP – Route Based on IP Hash
---

# Configuration 4: Static LACP – Route Based on IP Hash

You can use a two-port LACP static port-channel on a switch, and two active uplinks on a vSphere Standard Switch.

In this configuration, use 10 GbE networking with two physical uplinks per server. A single VMkernel interface (vmknic) for vSAN exists on each host.

For more information about host requirements and configuration examples, see the following Broadcom knowledge base articles:

- [Host requirements for link aggregation for ESX (1001938)](https://knowledge.broadcom.com/external/article?legacyId=1001938)
- [Sample configuration of EtherChannel / Link Aggregation Control Protocol (LACP) with ESX and Cisco/HP switches (KB 1004048)](https://knowledge.broadcom.com/external/article?legacyId=1004048)

vSAN over RDMA does not support this configuration.

## Configure the Physical Switch

Configure a two-uplink static port-channel as follows:

- Switch ports 43 and 44
- VLAN trunking, so port-channel is in VLAN trunk mode, with the appropriate VLANs trunked.
- Do not specify the load-balancing policy on the port-channel group.

These steps can be used to configure an individual port-channel on the switch:

Step 1: Create a port-channel.

#interface port-channel 13

Step 2: Set port-channel to VLAN trunk mode.

#switchport mode trunk

Step 3: Allow appropriate VLANs.

#switchport trunk allowed vlan 3266

Step 4: Assign the correct ports to the port-channel and set mode to active.

#interface range Te1/0/43, Te1/0/44

#channel-group 1 mode on

Step 5: Verify that the port-channel is configured as a static port-channel.

#show interfaces port-channel 13

Channel Ports Ch-Type Hash Type Min-links Local Prf

------- ----------------------------- -------- --------- --------- --

Po13 Active: Te1/0/43, Te1/0/44 
Static 
 7 1 Disabled

Hash Algorithm Type

1 - Source MAC, VLAN, EtherType, source module and port Id

2 - Destination MAC, VLAN, EtherType, source module and port Id

3 - Source IP and source TCP/UDP port

4 - Destination IP and destination TCP/UDP port

5 - Source/Destination MAC, VLAN, EtherType, source MODID/port

6 - Source/Destination IP and source/destination TCP/UDP port

7 - Enhanced hashing mode

## Configure vSphere Standard Switch

This example assumes you understand the configuration and creation of vSphere Standard Switches.

This example uses the following configuration:

- Uplinks named vmnic0 and vmnic1
- VLAN 3266 trunked to the switch ports and port-channel
- Jumbo frames

On each host, create a vSwitch1 with MTU set to 9000, and vmnic0 and vmnic1 added to the vSwitch. On the Teaming and Failover Policy, set both adapters to the Active position. Set the Load Balancing Policy to Route Based on IP Hash.

Configure teaming and failover for the distributed port group for vSAN traffic as follows:

- Load balancing policy set to Route Based on IP hash.
- Network failure detection set to Link status only.
- Notify Switches set to Yes.
- Failback set to Yes.
- Ensure both uplinks are in the Active uplinks position.

Use defaults for network detection, Notify Switches and Failback. All port groups inherit the Teaming and Failover Policy that was set at the vSwitch level. You can override individual port group teaming and failover polices to differ from the parent vSwitch, but make sure you use the same set of uplinks for IP hash load balancing for all port groups.

## Configure Load Balancing

Although both physical uplinks are utilized, there is not a consistent balance of traffic across all physical vmnics. The figure shows that only active traffic is vSAN traffic, which was essentially four vmknics or IP addresses. The behavior might be caused by the low number of IP addresses and possible hashes. However, in some situations, the virtual switch might consistently pass the traffic through one uplink in the team. For further details on the IP Hash algorithm, see the [vSphere Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking.html) guide.

## Network Redundancy

In this example, vmnic1 is connected to a port that has been disabled from the switch, to focus on failure and redundancy behavior. Note that a network uplink redundancy alarm has triggered.

No vSAN health alarms were triggered. Cluster and VM components are not affected and Guest Storage I/O is not interrupted by this failure.

## Recovery and Failback

Once vmnic1 recovers, traffic is automatically balanced across both active uplinks.