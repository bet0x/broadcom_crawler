---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/network-requirements-for-vsan/physical-nic-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Physical NIC Requirements
---

# Physical NIC Requirements

Network Interface Cards (NICs) used in vSAN hosts must meet certain requirements. vSAN works on 10 GbEs, 25 GbEs, 40 GbEs, 50 GbEs, and 100 GbEs networks.

Ensure your hosts meet the minimum NIC requirements:

Minimum NIC Requirements and Recommendations



| Deployment Type | Support for 1 GbE NIC | Support for NICs Greater than 10 GbE | Inter-Node Latency | Inter-Site Link Bandwidth or Latency | Latency Between Nodes and vSAN Witness Hosts | Bandwidth Between Nodes and vSAN Witness Hosts |
| --- | --- | --- | --- | --- | --- | --- |
| vSAN HCI Cluster (Hybrid) | Yes | Yes | Less than 1 ms RTT. | NA | NA | NA |
| vSAN HCI Cluster (All Flash) | No | Yes | Less than 1 ms RTT. | NA | NA | NA |
| vSAN Stretched Cluster | No | Yes | Less than 1 ms RTT within each site. | Recommended is 25 GbE or higher (workload dependent) and 5 ms RTT. | Less than 200 ms RTT. Up to 10 hosts per site. | 2 Mbps per 1000 components (Maximum of 100 Mbps with 45 k components). |
| Less than 100 ms RTT. 11–15 hosts per site. |
| Two-Node vSAN Cluster | No | Yes | Less than 1 ms RTT within the same site. | Recommended is 25 GbE or higher and 5 ms RTT or less. | Less than 500 ms RTT. | 2 Mbps per 1000 components (Maximum of 1.5 Mbps). |
| vSAN Stretched Compute Cluster | No | Yes | Less than 1 ms RTT within each site. | Minimum 10 GbE and 5 ms RTT. | NA | NA |
| vSAN storage cluster | No | Yes | Less than 1 ms RTT | Minimum 10 GbE and 1 ms RTT | Less than 1 ms RTT | 2 Mbps per 1000 components |
| vSAN Stretched storage cluster | No | Yes | Less than 1 ms RTT within each site. | Recommended is 25 GbE or higher (workload dependent) and 5 ms RTT. | Less than 200 ms RTT. Up to 10 hosts per site. | 2 Mbps per 1000 components (Maximum of 100 Mbps with 45 k components). |
| Less than 100 ms RTT. 11–15 hosts per site. |

vSAN recommends the use of 25 GbE or higher NICs in the vSAN hosts. NIC requirements assume that the packet loss is not more than 0.0001% in vSAN. There can be a drastic impact on the vSAN performance, if any of these requirements are exceeded.

For more information about the vSAN stretched cluster NIC requirements, see [vSAN Stretched Cluster Guide](https://www.vmware.com/docs/vsan-stretched-cluster-guide).