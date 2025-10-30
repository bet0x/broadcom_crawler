---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/edge-vm-system-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge VM System Requirements
---

# NSX Edge VM System Requirements

Before you install NSX Edge, make sure that your environment meets the supported requirements.

The following conditions apply to the hosts for the NSX Edge nodes:

- NSX Edge nodes are supported only on ESX-based hosts with Intel-based and AMD-based chipsets.

  Otherwise, vSphere EVC mode may prevent NSX Edge nodes from starting, showing an error message in the console.
- If vSphere EVC mode is enabled for the host for the NSX Edge VM, the CPU must be Haswell or later generation.
- Only VMXNET3 vNIC is supported for the NSX Edge VM.

## NSX Edge VM Resource Requirements

| Appliance Size | Memory | vCPU | Disk Space | VM Hardware Version | Notes |
| --- | --- | --- | --- | --- | --- |
| NSX Edge Small | 4 GB | 2 | 200 GB | 11 or later (vSphere 7.0 or later) | Proof-of-concept deployments only.  L7 rules for firewall, load balancing and so on are not realized on a Tier-1 gateway if you deploy a small sized NSX Edge VM. |
| NSX Edge Medium | 8 GB | 4 | 200 GB | 11 or later (vSphere 7.0 or later) | Suggested for L2 through L4 features and when the total throughput requirement is less than 2 Gbps:  - NAT - Routing - L4 firewall - L4 load balancer |
| NSX Edge Large | 32 GB | 8 | 200 GB | 11 or later (vSphere 7.0 or later) | Suggested for L2 through L4 features and when the total throughput requirement is between 2 ~ 10 Gbps.  - NAT - Routing - L4 Firewall - L4 Load Balancer - L7 Load Balancer (for example, when SSL offload is required) - TLS Inspection  See [Scaling Load Balancer Resources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/key-load-balancer-concepts/scaling-load-balancer-resources.html).  For more information about what the different load balance sizes and NSX Edge form factors can support, see [VMware Configuration Maximums](https://configmax.broadcom.com/home). |
| NSX Edge Extra Large | 64 GB | 16 | 200 GB | 11 or later (vSphere 7.0 or later) | Suggested for features that have a higher total throughput requirement than the NSX Edge Large form factor:  - L7 load balancer - VPN - TLS Inspection - L7 Access Profile (URL filtering) - IDS/IPS - Malware prevention (Advanced Threat Protection)  See [Scaling Load Balancer Resources](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/key-load-balancer-concepts/scaling-load-balancer-resources.html).  For more information about what the different load balance sizes and NSX Edge form factors can support, see [VMware Configuration Maximums](https://configmax.broadcom.com/home). |

## NSX Edge VM CPU Requirements

For the DPDK support, the underlaying platform needs to meet the following requirements:

- CPU must have AESNI capability.
- CPU must have 1 GB Huge Page support.

| Hardware | Type |
| --- | --- |
| CPU | - Intel Xeon Platinum 9xxx, 8xxx - Intel Xeon Gold 6xxx, 5xxx - Intel Xeon Silver 4xxx - Intel Xeon Bronze 3xxx - Intel Xeon E56xx, L56xx, X56xx (Westmere-EP) - Intel Xeon E7-xxxx (Westmere-EX and later CPU generation) - Intel Xeon E5-xxxx (Sandy Bridge and later CPU generation) |
| - AMD EPYC Series processors |