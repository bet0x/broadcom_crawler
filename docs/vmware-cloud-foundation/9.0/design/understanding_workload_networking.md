---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/understanding-workload-networking.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Understanding Workload Networking
---

# Understanding Workload Networking

## Understanding Workload Networking

Each VPC is a separate, standalone network with 3 different types of IP addresses that each have different levels of reachability:

- VPC Private CIDRs are only advertised within the confines of the VPC and require NAT to connect to any resources outside of the VPC. These CIDRs are managed by the VPC (Project) Administrator and do not need to be unique across multiple VPCs.
- TGW Private IP blocks are only advertised within the confines of the NSX Project or VCF Automation Organization (and its TGW, which also is scoped to the NSX Project). The available IP blocks are defined by the Tenant Administrator. Multiple tenants can re-use the same IP space, however, as the traffic will be SNATed to an external IP before leaving the VPC, but must remain distinct from other IP space on the Tenant's enterprise network to ensure routability. Project administrators can allocate subnets from within the defined IP Blocks for use in their VPCs. These IPs have direct reachability to other VPCs within the Tenant using the TGW Private IP space.
- External IP Blocks are unique across the Enterprise network and are generally advertised upstream to the network infrastructure. These IPs are managed by the Provider and subnets within them can be assigned by the Tenant Admin from allocations defined by the Provider. IPs in this space are used for outbound Source NAT to enable external reachability for workings using Private IPs. The are also assigned to Load Balancer Virtual IPs (VIPs) for inbound application reachability.

Routing within the NSX Project is performed by the Transit Gateway (TGW), which has an external connection to upstream networks defined by the Provider.

Workload VPC Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/70773b52-098d-436b-86dc-f1afdb5c2e66.original.png)

|  |  |
| --- | --- |
| Design Objectives | Design Decisions |
| Define a networking model providing the appropriate level of isolation, scale and connectivity for each organization's workloads. Every organization should have sufficient external IP address allocations and guidance on reachability for external services to self-manage connectivity for their workloads. | - VPC Mapping:  vSphere Namespaces are managed by tenants, which includes mapping a vSphere Namespace to a VPC. Tenants can create a new VPC for each vSphere Namespace, or re-use the same VPC for multiple vSphere Namespaces.  Different VPCs should be used for workloads that require some level of network segregation (when on private VPC subnets) but also support communication between other workloads (on private TGW subnets). When no network separation is required, the same VPC can be used across the region.  VPCs only span a single region, so Namespaces in different regions will always be mapped to different VPCs. - Network Selection:  Each tenant manages 2 pools of addresses: Private VPC and Private TGW. These can be allocated independently of other tenants but it’s a good idea for tenant managers to keep addressing consistent within an enterprise. Service Providers may only publish a list of reserved address ranges used for external and management to avoid conflicts.  In addition, the Provider manages the External IP address blocks which are assigned to tenants. One of the public IPs is automatically assigned as a default SNAT IP for the VPC. This IP is used as the source for any traffic from a TGW Private IP when communicating with a resource outside of the Project. NAT rules can also be defined for Inbound traffic when required, or for Inbound or Outbound communication from a VPC Private IP address. Since these IPs are more limited, they should only be used where necessary, and not assigned directly to VM workloads, but to Load balancer VIPs or NAT rules, leveraging the default SNAT rule when possible. |