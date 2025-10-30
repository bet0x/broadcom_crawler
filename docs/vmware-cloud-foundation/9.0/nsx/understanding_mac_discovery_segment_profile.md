---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-mac-discovery-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding MAC Discovery Segment Profile
---

# Understanding MAC Discovery Segment Profile

The MAC discovery segment profile supports two functionalities: MAC learning and MAC address change.

The MAC address change feature allows a VM to change its MAC address. A VM connected to a port can run an administrative command to change the MAC address of its vNIC and still send and receive traffic on that vNIC. This feature is supported on ESX only. In the default MAC discovery segment profile, this property is enabled.

MAC learning provides network connectivity to deployments where multiple MAC addresses get configured behind one vNIC, for example, in a nested hypervisor deployment where an ESX VM runs on an ESX host and multiple VMs run inside the ESX VM. Without MAC learning, when the vNIC of the ESX VM connects to a segment port, its MAC address is static. VMs running inside the ESX VM do not have network connectivity because their packets have different source MAC addresses. With MAC learning, the vSwitch inspects the source MAC address of every packet coming from the vNIC, learns the MAC address and allows the packet to proceed. If a MAC address that is learned is not used for a certain period of time, it is removed. This time period is not configurable. The field MAC Learning Aging Time displays the pre-defined value, which is 600.

MAC Learning will not learn a MAC address if it is already a known static MAC address on the host on the same VLAN or VNI. For example, the MAC address belongs to another VM's vNIC, a vmknic, or a VDR (virtual distributed router) port.

Note: A VDR port is always configured to send and receive traffic on any possible VNI (similar to how a trunk VLAN port behaves when it is configured on 0-4094). So the usage of a VDR port MAC address on any overlay segment through MAC learning is not possible.

MAC learning also supports unknown unicast flooding. Normally, when a packet that is received by a port has an unknown destination MAC address, the packet is dropped. With unknown unicast flooding enabled, the port floods unknown unicast traffic to every port on the switch that has MAC learning and unknown unicast flooding enabled. This property is enabled by default, but only if MAC learning is enabled.

The number of MAC addresses that can be learned is configurable. The maximum value is 4096, which is the default. You can also set the policy for when the limit is reached. The options are:

- Drop - Packets from an unknown source MAC address are dropped. Packets inbound to this MAC address will be treated as unknown unicast. The port will receive the packets only if it has unknown unicast flooding enabled.
- Allow - Packets from an unknown source MAC address are forwarded although the address will not be learned. Packets inbound to this MAC address will be treated as unknown unicast. The port will receive the packets only if it has unknown unicast flooding enabled.

If you enable MAC learning or MAC address change, to improve security, configure SpoofGuard as well.