---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-large-scale-topologies(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Large Scale Topology Workload Networking Model
---

# Large Scale Topology Workload Networking Model

This model is mainly designed for service providers managing multiple tenants via VCF Automation, each using the "VPC with full services" topology". It can also be leveraged in architectures based on the NSX Segment consumption model where VCF Automation All Apps Orgs are not in use. Its key purpose is to provide centralized access to shared services, including Internet connectivity, while enabling dedicated VPN services for each tenant. The solution features a stateless Active/Active Tier-0 Gateway at the aggregation layer, providing shared services and internet access across all tenants.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/85f13379-6a67-4cf5-9e7d-ddf6c68c3826.original.png)

## Large Scale Topology Workload Networking Model Attributes

A Large Scale Topology Workload Networking Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Transit Gateway Type | Centralized |
| NSX Edge nodes required | Yes |
| Tier-0 Gateway HA Mode | Mix of Active/Standby and Active/Active |
| Network consumption model | VPC and NSX Segment Network Virtualization |
| NSX Tenancy Constructs | NSX Projects, VPCs |
| Consumption options | - vCenter UI/API - VCF Automation All Apps Orgs - VMware Kubernetes Engine (VKS) - NSX UI/API |

## Common challenged addressed

Tenant Onboarding Complexity:

- Reduces physical fabric configuration requirements for new tenant connections
- Streamlines tenant integration process

Shared Resource Access:

- Centralizes shared network access (e.g., Internet VLAN)
- Addresses VRF connection limitations:

  - VRFs under the same parent Tier-0 Gateway cannot connect to the same VLAN
  - VRFs on different edge nodes (different parent Tier-0 gateways) can connect
- Optimizes IP space utilization:

  - Reduces public IP consumption (traditionally 1-3 IPs per Tier-0/VRF on shared Internet VLAN)

## Key Components

- Aggregation Layer: Active/Active stateless Tier-0 Gateway
- Tenant Layer: Individual dedicated Tier-0 Gateways or VRFs
- Interconnection: Shared overlay segment between tenant and aggregation gateways
- Routing: eBGP peering between aggregation Tier-0 and tenant gateways

## Tenant Deployment Options

High-Throughput Tenants:

- Dedicated Tier-0 Gateway
- Dedicated pair of edge nodes
- Full North-South services capacity (limited to single Edge Node due to Active/Standby mode)

Lower-Throughput Tenants:

- Dedicated VRF
- Shared edge node pairs
- Provider-determined tenant-to-edge node ratio
- Configurable VPN services

## Large Scale Topology Workload Networking Model Design Requirements

| Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-LSCA-REQD-CFG-01 | Each aggregation Tier-0 Gateway edge node must peer with all tenant VRF/Tier-0 Gateway edge nodes | Full mesh peering between tenant and aggregation Gateways will prevent black holing of traffic in some failure scenario in which traffic is received by the tenant edge node running the standby gateway. | Additional BGP peering must be configured |
| VCF-WLDNET-LSCA-REQD-CFG-02 | Use EBGP between tenant and provider gateways | Avoid the IBGP requirement of peering between tenant gateways | Additional BGP ASNs must be available |

## Large Scale Topology Workload Networking Model Design Recommendations

| Recommendation ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-LSCA-REQD-RCMD-01 | Do not configure BGP peering between tenant VRFs or tenant Tier-0 Gateways | Simpler and more scalable BGP peering design | None. |
| VCF-WLDNET-LSCA-REQD-RCMD-02 | Shared overlay segment for interconnection | More robust transport layer, especially when TEP Groups are enabled | - Peering over a VLAN is suported but it less reliable. - Peering over VLAN is the only option when the Gateways are managed by different NSX Managers. Peering over VLAN should only be used in such cases. |