---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster/network-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Networking Requirements for vSAN
---

# Networking Requirements for vSAN

Verify that the network infrastructure and the networking configuration on the ESX hosts meet the minimum networking requirements for vSAN.

Networking Requirements for vSAN



| Networking Component | Requirement |
| --- | --- |
| Host Bandwidth | Each host must have minimum bandwidth dedicated to vSAN.   - vSAN OSA: Dedicated 1 GbE for hybrid configurations, dedicated or shared 10 GbEs for all-flash configurations - vSAN ESA: Dedicated or shared 10 GbEs minimum, recommended 25GbE or higher. See [vSAN Compatibility guide](https://compatibilityguide.broadcom.com/pages/vsan-esa-readynode-hardware-guidance).   For information about networking considerations in vSAN, see [Designing the vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/designing-the-virtual-san-network.html#GUID-cbf63199-0e87-4e95-96da-6dc0f41afc69-en). |
| Connection between hosts | Each host in the vSAN cluster, regardless of whether it contributes capacity, must have a VMkernel network adapter for vSAN traffic. See [Set Up a VMkernel Network for vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san/set-up-networking-for-virtual-san.html#GUID-c79fd921-d9a9-4b37-b7e8-7a10e8292979-en). |
| Host network | All hosts in your vSAN cluster must be connected to a vSAN Layer 2 or Layer 3 network. |
| IPv4 and IPv6 support | The vSAN network supports both IPv4 and IPv6. |
| Network latency | - Maximum of 1 ms RTT for single site (non-stretched) vSAN clusters between all hosts in the cluster - Maximum of 5 ms RTT between the two main sites for vSAN stretched clusters - Maximum of 200 ms RTT from a main site to the vSAN witness host - Maximum of 5ms RTT between the vSAN client cluster and vSAN storage cluster |