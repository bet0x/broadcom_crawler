---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/advanced-nic-teaming/understanding-network-air-gaps.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Understanding Network Air Gaps
---

# Understanding Network Air Gaps

You can use advanced NIC teaming methods to create an air-gap storage fabric. Two storage networks are used to create a redundant storage network topology, with each storage network physically and logically isolated from the other by an air gap.

You can configure a network air gap for vSAN in a vSphere environment. Configure multiple VMkernel ports per vSAN host. Associate each VMkernel port to dedicated physical uplinks, using either a single vSwitch or multiple virtual switches, such as vSphere Standard Switch or vSphere Distributed Switch.

![Multiple VMkernel ports per host](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/38e9de7a-8c9e-4a54-8265-d5a897ad228f.original.png)

Typically, each uplink must be connected to fully redundant physical infrastructure.

This topology is not ideal. The failure of components such as NICs on different hosts that reside on the same network can lead to interruption of storage I/O. To avoid this problem, implement physical NIC redundancy on all hosts and all network segments. Configuration example 2 addresses this topology in detail.

These configurations are applicable to both L2 and L3 topologies, with unicast configuration.