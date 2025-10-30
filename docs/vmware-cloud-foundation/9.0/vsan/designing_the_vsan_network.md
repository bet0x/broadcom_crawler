---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-the-virtual-san-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Designing the vSAN Network
---

# Designing the vSAN Network

Consider networking features that can provide availability, security, and bandwidth guarantee in a vSAN cluster.

For details about the vSAN network configuration, see [Understanding vSAN Networking.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking.html)

## Networking Failover and Load Balancing

vSAN uses the teaming and failover policy that is configured on the backing virtual switch for network redundancy only. vSAN does not use NIC teaming for load balancing.

If you plan to configure a NIC team for availability, consider these failover configurations.

| Teaming Algorithm | Failover Configuration of the Adapters in the Team |
| --- | --- |
| Route based on originating virtual port | Active/Passive |
| Route based on IP hash | Active/Active with static EtherChannel for the standard switch and LACP port channel for the distributed switch |
| Route based on physical network adapter load | Active/Active |

vSAN supports IP-hash load balancing, but cannot guarantee improvement in performance for all configurations. You can benefit from IP hash when vSAN is among its many consumers. In this case, IP hash performs load balancing. If vSAN is the only consumer, you might observe no improvement. This behavior specifically applies to 1 GbE environments. For example, if you use four 1 GbE physical adapters with IP hash for vSAN, you might not be able to use more than 1 GbEs. This behavior also applies to all NIC teaming policies that VMware supports.

vSAN does not support multiple VMkernel adapters on the same subnet. You can use different VMkernel adapters on different subnets, such as another VLAN or separate physical fabric. Providing availability by using several VMkernel adapters has configuration costs that involve vSphere and the network infrastructure. You can increase network availability by teaming physical network adapters.

## Using Unicast in vSAN Network

You can design a simple unicast network for vSAN.

You can use DHCP with reservations, because the assigned IP addresses are bound to the MAC addresses of VMkernel ports.

## Using RDMA

vSAN can use Remote Direct Memory Access (RDMA). RDMA typically has lower CPU utilization and less I/O latency. If your hosts support the RoCE v2 protocol, you can enable RDMA through the vSAN network service in vSphere Client.

Consider the following guidelines when designing vSAN over RDMA:

- Each vSAN host must have a vSAN certified RDMA-capable NIC, as listed in the vSAN section of the Broadcom Compatibility Guide available at: <https://compatibilityguide.broadcom.com/>. Use only the same model network adapters from the same vendor on each end of the connection. Configure the DCBx mode to IEEE.
- All hosts must support RDMA. If any host loses RDMA support, the entire vSAN cluster switches to TCP.
- The network must be lossless. Configure network switches to use Data Center Bridging with Priority Flow Control. Configure a lossless traffic class for vSAN traffic marked at priority level 3.
- vSAN with RDMA does not support LACP, IP-hash-based NIC teaming, or route based on physical network adapter load. vSAN with RDMA does support NIC failover.
- All hosts must be on the same subnet. vSAN with RDMA supports up to 32 hosts.
- vSAN with RDMA does not support vSAN stretched clusters and vSAN storage clusters.

## Allocating Bandwidth for vSAN by Using Network I/O Control

vSAN traffic can share physical network adapters with other system traffic types, such as vSphere vMotion traffic, vSphere HA traffic, and virtual machine traffic. To guarantee the amount of bandwidth required for vSAN, use vSphere Network I/O Control in the vSphere Distributed Switch.

In vSphere Network I/O Control, you can configure reservation and shares for the vSAN outgoing traffic.

- Set a reservation so that Network I/O Control guarantees that minimum bandwidth is available on the physical adapter for vSAN.
- Set shares so that when the physical adapter assigned for vSAN becomes saturated, certain bandwidth is available to vSAN and to prevent vSAN from consuming the entire capacity of the physical adapter during rebuild and synchronization operations. For example, the physical adapter might become saturated when another physical adapter in the team fails and all traffic in the port group is transferred to the other adapters in the team.

For example, on a 10 GbE physical adapter that handles traffic for vSAN, vSphere vMotion, and virtual machines, you can configure certain bandwidth and shares.

Example Network I/O Control Configuration for a Physical Adapter That Handles vSAN



| Traffic Type | Shares |
| --- | --- |
| vSAN | 100 |
| vSphere vMotion | 70 |
| Virtual machine | 30 |

For information about using vSphere Network I/O Control to configure bandwidth allocation for vSAN traffic, see the [vSphere Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking.html) guide.

## Marking vSAN Traffic

Priority tagging is a mechanism to indicate to the connected network devices that vSAN traffic has high Quality of Service (QoS) demands. You can assign vSAN traffic to a certain class and mark the traffic accordingly with a Class of Service (CoS) value from 0 (low priority) to 7 (high priority). Use the traffic filtering and marking policy of vSphere Distributed Switch to configure priority levels.

For more information, see [What is Traffic Filtering and Marking Policy](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking/networking-policies/traffic-filtering-policy.html) in the vSphere Networking guide.

## Segmenting vSAN Traffic in a VLAN

Consider isolating vSAN traffic in a VLAN for enhanced security and performance, especially if you share the capacity of the backing physical adapter among several traffic types.

## Jumbo Frames

If you plan to use jumbo frames with vSAN to improve CPU performance, verify that jumbo frames are enabled on all network devices and hosts in the cluster.

By default, the TCP segmentation offload (TSO) and large receive offload (LRO) features are enabled on ESX. Consider whether using jumbo frames improves the performance enough to justify the cost of enabling them on all nodes on the network.