---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-datapath.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enhanced Data Path
---

# Enhanced Data Path

Enhanced Datapath Path (EDP) is a packet forwarding stack, designed to provide superior performance in terms of throughput, packet rate, latency and cpu utilization.

EDP is suitable for general compute workloads, network workloads and niche workloads like NSX Edge, and telco NFV solutions. It is enabled automatically in new VCF 9 Workload Domains. Environments that were Converted, Imported or Upgraded to VCF9 (and not running the EDP virtual switch mode) can be configured by setting the Transport Nodes to operate in one of the following modes.

## EDP Standard

EDP Standard is a mode that provides increased network performance and very high packet processing efficiency out of the box, exceeding the performance possible with the Standard stack. EDP Standard is the recommended mode for maximizing host switch network performance in general compute environments and NSX Edge clusters. This mode is enabled by default.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cf9738d0-341a-45e1-bec0-04d1c05dd031.original.png)

## EDP Dedicated

EDP Dedicated is a prescriptive mode typically employed in specialized telco deployments. In this mode, knowledge of workload traffic patterns and specific network requirements are examined to determine the physical resources, like processing cores, that should be reserved for packet processing.

## Who should enable EDP?

Enhanced Data Path Standard is strongly recommended for environments with heavy packet processing functions like NSX Edge clusters or Network Extension, and is implemented as the default in VCF clusters to maximize or future-proof the network performance capabilities of those clusters.

To enable EDP Standard in environments that were Converted, Imported or Upgraded to VCF 9 and are still running Standard operational, read the following sections in this guide.