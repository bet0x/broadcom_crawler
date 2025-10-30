---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/network-latency-statistics.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Network Latency Statistics
---

# Network Latency Statistics

In a network, latency can accumulate at multiple endpoints in the data path. As a network administrator, you need the ability to monitor the latency of a network to diagnose and troubleshoot performance bottlenecks in the network.

The following network latency statistics can be measured on host transport nodes:

- pNIC to vNIC
- vNIC to pNIC
- vNIC to vNIC
- VTEP to VTEP

In NSX, the following limitations apply to measuring latency statistics:

- Only ESX host transport nodes are supported for measuring network latency in the data plane.
- Edge transport nodes are not supported.
- On VLAN segments, network latency is measured only when the two vNICs belong to VMs on the same ESX host.
- When the VMs are attached to separate segments, network latency is measured only when the data traffic is routed through the distributed router (DR) instance on the ESX host transport nodes. If the data traffic is routed through the DR instance on the edge transport nodes, network latency is not measured.
- Enhanced networking stack (ENS) does not support vNIC-to-pNIC, pNIC-to-vNIC, or vNIC-to-vNIC latency.
- Latency measurement is not supported when an east-west network traffic protection is configured using partner service VMs. Latency monitoring is disabled on the ports of service virtual machine (SVMs) and guest VMs.
- Latency measurement is not supported on the Data Processing Unit (DPU).

You can export the latency data to external network performance monitoring tools and run analytics on the data. The external monitoring tools are also called collectors. By using a collector, you can achieve greater network visibility, optimize network performance, and identify the endpoints in the data path that cause a significant latency in the network.

After the hosts are configured to measure network latency statistics, the network operations agent (netopa) on the hosts periodically polls the data plane. When latency data is available, the agent exports the data at preconfigured intervals to the external collectors.

- The netopa agent can export the network latency statistics only to VCF Operations for networks. Other collector tools are not supported currently.
- For VTEP statistics, VCF Operations for networks 5.0 or later is required. For the pNIC and vNIC statistics, VCF Operations for networks 5.3 or later is required.
- You can configure ESX hosts to measure network latency statistics only by using the NSX REST APIs.

You can measure network latency statistics for both standalone ESX hosts and ESX hosts that are a part of the vCenter cluster. However, VCF Operations for networks supports collecting latency statistics only from vCenter-managed ESX hosts and not from standalone ESX hosts.

## pNIC-to-vNIC and vNIC-to-pNIC Latency

When pNIC latency measurement is enabled on a host transport node, vNIC-to-pNIC latency and pNIC-to-vNIC latency are computed for each vNIC on the host transport node.

![Diagram shows pNIC to vNIC and vNIC to pNIC latency on a single host.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/125dd03a-6c34-49e0-98fc-ca4f4ae4475b.original.png)

pNIC-to-vNIC and vNIC-to-pNIC latency statistics are exported to the external collector in the following format:

Endpoint1, Endpoint2, Max, Min, Avg

Where:

- Endpoint1, Endpoint2 can either be the virtual interface ID (VIF ID) or the name of the physical adapter on an ESX host (vmnic).
- Max, Min, and Avg represent the maximum, minimum, and average latency values between the two endpoints in microseconds.

## vNIC to vNIC Latency

This latency represents the time taken by the data packet to travel from the source vNIC to the destination vNIC either on the same ESX host or different ESX hosts. If the vNICs are on different ESX hosts, only GENEVE encapsulation protocol is supported in the overlay tunnel between the hosts.

![Diagram shows vNIC to vNIC latency between VMs on the same host and on different hosts.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6765c6d6-7488-4e8d-a83c-f17fc783e7d3.original.png)

vNIC to vNIC network latency is computed as follows:

- When the source VNIC1 on VM1 and the destination VNIC2 on VM2 are on the same host, a single-trip latency is calculated for each trip and exported to the collector. In other words, latency for each trip from VNIC1 to VNIC2 and from VNIC2 to VNIC1 is computed separately.
- When the source VNIC1 on VM1 and the destination VNIC2 on VM2 are on different hosts, total round-trip latency is calculated, and only a single latency value is exported to the collector. If there is no return traffic from VNIC2 to VNIC1, no network latency is exported to the collector.

NSX calculates the vNIC-to-vNIC latency between hosts directly by using the timestamps in the GENEVE encapsulated packets. You do not have to enable pNIC latency measurement on the host and the VTEP-to-VTEP latency. The pNIC-to-vNIC, vNIC-to-pNIC, and VTEP-to-VTEP statistics are independent of the vNIC-to-vNIC statistic.

vNIC-to-vNIC latency statistics are exported to the external collector in the following format:

VIF1, VIF2, Max, Min, Avg

Where:

- VIF1, VIF2 represent the virtual interfaces or the vNICs.
- Max, Min, and Avg represent the maximum, minimum, and average latency values between the two vNICs in microseconds.

## VTEP-to-VTEP Latency

This latency represents the total round-trip time taken by the data packet to travel from the source VTEP to the destination VTEP. To measure VTEP-to-VTEP latency, you must enable latency in the transport zone profile.

![Diagram shows VTEP to VTEP latency between hosts.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b2e0a8e3-8cf1-4288-afea-acda45f02e93.original.png)

To calculate the VTEP-to-VTEP latency between ESX hosts, Bidirectional Flow Detection (BFD) protocol is used. NSX extends the BFD protocol with timestamps in the payload to support latency computation between the VTEPs. BFD packets are transmitted at regular intervals in each tunnel between the hosts to compute the VTEP-to-VTEP latency.