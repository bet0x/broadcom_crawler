---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-network-topologies/corner-case-deployments.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Corner Case Deployments
---

# Corner Case Deployments

It is possible to deploy vSAN in unusual, or corner-case configurations.

These unusual topologies require special considerations.

## Three Locations and No vSAN Stretched Cluster

You can deploy vSAN across multiple rooms, buildings or sites, rather than deploy a stretched cluster configuration.

This configuration is supported. The one requirement is that the latency between the sites must be at the same level as the latency expected for a normal vSAN deployment in the same data center. The latency must be <1ms between all hosts. If latency is greater than this value, consider a vSAN stretched cluster which tolerates latency of 5ms RTT.

For best results, maintain a uniform configuration across all sites in such a topology. To maintain availability of VMs, configure fault domains, where the hosts in each room, building, or site are placed in the same fault domain. Avoid asymmetric partitioning of the cluster, where host A cannot communicate to host B, but host B can communicate to host A.

## Two-Node Deployed as 1+1+Witness Stretched Cluster

You can deploy a two-node configuration as a vSAN stretched cluster configuration, placing each host in different rooms, buildings, or sites.

Attempt to increase the number of hosts at each site fail with an error related to licensing. For any cluster that is larger than two hosts and that uses the dedicated witness appliance/host feature (N+N+Witness, where N > 1), the configuration is considered a vSAN stretched cluster.