---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/congestion-control-and-flow-control.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using Congestion Control and Flow Control
---

# Using Congestion Control and Flow Control

Flow control is used to manage the rate of data transfer between senders and receivers on the network. Congestion control handles congestion in the network. Flow control is enabled by default on the ESX hosts.

## Flow Control

You can use flow control to manage the rate of data transfer between two devices.

Flow control is configured when two physically connected devices perform auto-negotiation. An overwhelmed network node might send a pause frame to halt the transmission of the sender for a specified period.

One reason to use pause frames is to support network interface controllers (NICs) that do not have enough buffering to handle full-speed reception. This problem is uncommon with advances in bus speeds and memory sizes.

## Congestion Control

Congestion control helps you control the traffic on the network.

Congestion control applies mainly to packet switching networks. Network congestion within a switch might be caused by overloaded inter-switch links. If inter-switch links overload the capability on the physical layer, the switch introduces pause frames to protect itself.

## Priority Flow Control

Priority-based flow control (PFC) helps you eliminate frame loss due to congestion.

Priority-based flow control ([IEEE 802.1Qbb](http://www.ieee802.org/1/pages/802.1bb.html)) is achieved by a mechanism similar to pause frames, but operates on individual priorities. PFC is also called Class-Based Flow Control (CBFC) or Per Priority Pause (PPP).

## Flow Control Design Considerations

By default, flow control is enabled on all network interfaces in ESX hosts.

Flow control configuration on a NIC is done by the driver. When a NIC is overwhelmed by network traffic, the NIC sends pause frames.

Flow control mechanisms such as pause frames can trigger overall latency in the VM guest I/O due to increased latency at the vSAN network layer. Some network drivers provide module options that configure flow control functionality within the driver. For information about configuring flow control on ESX hosts, see Broadcom knowledge base article [1013413](https://knowledge.broadcom.com/external/article?legacyId=1013413).

In deployments with 1 GbEs, leave flow control enabled on ESX network interfaces (default). If pause frames are a problem, carefully plan disabling flow control in conjunction with Hardware Vendor Support or Broadcom Global Support Services.

To learn how you can recognize the presence of pause frames being sent from a receiver to an ESX host, see [Troubleshooting the vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/troubleshooting-the-vsan-network.html#GUID-fb8dd038-9b78-42c3-b558-adf19db6364b-en). A large number of pause frames in an environment usually indicates an underlying network or transport issue to investigate.