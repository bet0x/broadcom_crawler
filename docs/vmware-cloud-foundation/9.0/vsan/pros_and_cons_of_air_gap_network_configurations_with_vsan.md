---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/pros-and-cons-of-air-gap-network-configurations-with-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Pros and Cons of Air Gap Network Configurations with vSAN
---

# Pros and Cons of Air Gap Network Configurations with vSAN

Network air gaps can be useful to separate and isolate vSAN traffic. Use caution when configuring this topology.

Pros

- Physical and logical separation of vSAN traffic.

Cons

- vSAN does not support multiple VMkernel adapters (vmknics) on the same subnet. For more information, see Broadcom knowledge base article [2010877](https://knowledge.broadcom.com/external/article?legacyId=2010877).
- Setup is complex and error prone, so troubleshooting is more complex.
- Network availability is not guaranteed with multiple vmknics in some asymmetric failures, such as one NIC failure on one host and another NIC failure on another host.
- Load-balanced vSAN traffic across physical NICs is not guaranteed.
- Costs increase for vSAN hosts, as you might need multiple VMkernel adapters (vmknics) to protect multiple physical NICs (vmnics). For example, 2 x 2 vmnics might be required to provide redundancy for two vSAN vmknics.
- Required logical resources are doubled, such as VMkernel ports, IP addresses, and VLANs.
- vSAN does not implement port binding. This means that techniques such as multi-pathing are not available.
- Layer 3 topologies are not suitable for vSAN traffic with multiple vmknics. These topologies might not function as expected.

Dynamic LACP combines, or aggregates, multiple network connections in parallel to increase throughput and provide redundancy. When NIC teaming is configured with LACP, load balancing of the vSAN network across multiple uplinks occurs. This load balancing happens at the network layer, and is not done through vSAN.

Other terms sometimes used to describe link aggregation include port trunking, link bundling, Ethernet/network/NIC bonding, EtherChannel.

This section focuses on Link Aggregation Control Protocol (LACP). The IEEE standard is 802.3ad, but some vendors have proprietary LACP features, such as PAgP (Port Aggregation Protocol). Follow the best practices recommended by your vendor.

The LACP support introduced in vSphere Distributed Switch 5.1 only supports IP-hash load balancing. vSphere Distributed Switch 5.5 and later fully support LACP.

LACP is an industry standard that uses port-channels. Many hashing algorithms are available. The vSwitch port-group policy and the port-channel configuration must agree and match.