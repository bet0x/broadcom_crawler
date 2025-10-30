---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure
---

# Building Cloud Infrastructure

Use **VCF Operations** and the **vSphere Client** as a VI administrator to add and configure infrastructure for consumer and management workloads in the VCF private cloud after you deploy or converge to a VCF fleet and a VCF Instance with its management domain.

- You can start adding workload domains to a VCF Instance and individual clusters and hosts to these workload domains.

  VCF Operations deploys the vCenter and NSX Manager instances for the added workload domains. You can also enable vSphere Supervisor on the default cluster of the workload domain.
- You can import vCenter instances with their managed ESX hosts as workload domains so that they are included in identity and access management, certificate management, and lifecycle management operations performed centrally in VCF Operations .
- You can also add NSX network services to the management domain and the workload domains of a VCF Instance by deploying NSX Edge clusters, transit gateways, and virtual private clouds (VPCs). Then you can configure workloads to use these network services.

  You can place VCF Operations and VCF Automation on NSX overlay or VLAN segments so that they can use the NSX load balancer, or to support planned migration and disaster recovery, or IP mobility.

  You can configure consumer workloads to use the network services either in VCF Automation or directly in the vSphere Client.
- If you want to implement vSAN stretched clusters in a workload domain, you can use the SDDC Manager API for automated stretched cluster configuration.

## In This Chapter

- [Managing ESX Hosts in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management.html)
- [Managing VCF Domains in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains.html)
- [Stretching vSAN Clusters in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters.html)
- [Managing Network Connectivity in vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter.html)
- [Managing Virtual Private Clouds in vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter.html)

## Getting to Know VCF

To apply this documentation, you must be acquainted with the [VCF Product Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9.html), [VCF Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html), and [VCF Release Notes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes.html).

## Deploying or Converging to VCF

For information about deploying or converging to a VCF fleet or VCF Instance, see [Deployment, Convergence, and Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment.html).

## SDKs, APIs, and CLI for VCF Administration

You can build, operate, and manage your VCF private cloud by using the VCF SDK and APIs, and VCF PowerCLI. See [Administration SDKs, APIs, and CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/administration-sdks-cli-and-tools.html).