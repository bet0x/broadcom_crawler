---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/network-i-o-control.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Network I/O Control
---

# Network I/O Control

Use vSphere Network I/O Control to set Quality of Service (QoS) levels on network traffic.

vSphere Network I/O Control is a feature available with vSphere Distributed Switches. Use it to implement Quality of Service (QoS) on network traffic. This can be useful for vSAN when vSAN traffic must share the physical NIC with other traffic types, such as vMotion, management, and VMs.

## Reservations, Shares, and Limits

You can set a reservation so that Network I/O Control guarantees minimum bandwidth is available on the physical adapter for vSAN.

Reservations can be useful when bursty traffic, such as vMotion or full host evacuation, might impact vSAN traffic. Reservations are only invoked if there is contention for network bandwidth. One disadvantage with reservations in Network I/O Control is that unused reservation bandwidth cannot be allocated to virtual machine traffic. The total bandwidth reserved among all system traffic types cannot exceed 75 percent of the bandwidth provided by the physical network adapter with the lowest capacity.

vSAN best practices for reservations. Traffic reserved for vSAN cannot be allocated to virtual machine traffic, so avoid using NIOC reservations in vSAN environments.

Setting shares makes a certain bandwidth available to vSAN when the physical adapter assigned for vSAN becomes saturated. This prevents vSAN from consuming the entire capacity of the physical adapter during rebuild and synchronization operations. For example, the physical adapter might become saturated when another physical adapter in the team fails and all traffic in the port group is transferred to the remaining adapters in the team. The shares option ensures that no other traffic impacts the vSAN network.

vSAN recommendation on shares. This is the fairest bandwidth allocation technique in NIOC, and is preferred for use in vSAN environments.

Setting limits defines the maximum bandwidth that a certain traffic type can consume on an adapter. If no one else is using the additional bandwidth, the traffic type with the limit also cannot consume it.

vSAN recommendation on limits. As traffic types with limits cannot consume additional bandwidth, avoid using NIOC limits in vSAN environments.

## Network Resource Pools

You can view all system traffic types that can be controlled with Network I/O Control. If you have multiple virtual machine networks, you can assign certain bandwidth to virtual machine traffic. Use network resource pools to consume parts of that bandwidth based on the virtual machine port group.

## Enabling Network I/O Control

You can enable Network I/O Control in the configuration properties of the vDS. Right-click the vDS in the vSphere Client, and choose menu Settings > Edit Settings.

Network I/O Control is only available on vSphere distributed switches, not on standard vSwitches.

You can use Network I/O Control to reserve bandwidth for network traffic based on the capacity of the physical adapters on a host. For example, if vSAN traffic uses 10 GbE physical network adapters, and those adapters are shared with other system traffic types, you can use vSphere Network I/O Control to guarantee a certain amount of bandwidth for vSAN. This can be useful when traffic such as vSphere vMotion, vSphere HA, and virtual machine traffic share the same physical NIC as the vSAN network.