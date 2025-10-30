---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/virtual-private-clouds-overview.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Virtual Private Clouds Overview
---

# Virtual Private Clouds Overview

Virtual Private Clouds (VPCs) are logically isolated networking subnets routed together by a VPC Gateway. VPCs are defined under their NSX Project by either an Enterprise Admin or a Project Admin.

A VPC connects to a Transit Gateway (recommended) and can have the following types of subnets:

- **Private - VPC**: A subnet scoped to the VPC and routed with other subnets inside the same VPC, but not to the outside network. NAT is needed if outside communication is required.
- **Private - Transit Gateway**: Subnets allowing inter-VPC connectivity below the Transit Gateway without NAT. It requires IP translation if workloads need to be reachable to an outside network.
- **Public**: A subnet that is accessible from outside the environment, from other VPCs but also from customers and workload above the Transit Gateway.

In case you have to grant access to specific workloads on private networks from the outside environment, you can use External IPs.

**External IPs** – IPs that allow outside connectivity for a VM on a private network by performing IP translation. It is implemented with 1:1 NAT on the workload picking an IP from External IP block and assigning it to the VM.

Regardless of External Connection type (Centralized or Distributed), it is possible to configure Static Routes, Groups and DHCP Server in a VPC.

VPC in NSX

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e086f369-a58b-477a-9404-2b09eca81b78.cq5dam.web.1280.1280.jpeg)

## Services in VPC leveraging Edge Nodes

In the case of environments with Centralized Connection and an Edge Node made available through the VPC Connectivity Profile, the VPC can have the following Services as part of the VCF entitlement:

- NAT: full NAT configuration
- Stateless North-South Firewall (Centralized)
- Load Balancer (only for Supervisor Cluster)

Additionally, a VPC can benefit from the following additional features (with proper licenses):

- Integration with AVI Load Balancer
- Stateful North-South Firewall (Centralized)