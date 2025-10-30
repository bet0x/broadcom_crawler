---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/network-requirements-for-vsan/bandwidth-and-latency-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Bandwidth and Latency Requirements
---

# Bandwidth and Latency Requirements

To ensure high performance and availability, vSAN clusters must meet certain bandwidth and network latency requirements.

The bandwidth requirements between the primary and secondary sites of a vSAN stretched cluster depend on the vSAN workload, amount of data, and the way you want to handle failures. For more information, see [vSAN Stretched Cluster Bandwidth Sizing](https://www.vmware.com/docs/vmw-vsan-stretched-cluster-bandwidth-sizing).

Bandwidth and Latency Requirements



| Site Communication | Bandwidth | Latency |
| --- | --- | --- |
| Single Site |  | 1ms latency RTT. |
| Site to Site | vSAN OSA: minimum of 10 GbEs  vSAN ESA: minimum of 10 GbEs  The bandwidth requirement is based on the number of VMs being replicated between sites. | Less than 5 ms latency RTT. |
| Site to Witness | 2 Mbps per 1000 vSAN components | - Less than 500 ms latency RTT for 1 host per site. - Less than 200 ms latency RTT for up to 10 hosts per site. - Less than 100 ms latency RTT for 11-15 hosts per site. |
| vSAN Compute-Only Cluster to a vSAN Storage Cluster |  | Minimum 5 ms latency RTT. |