---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/network-backing-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Networking Models
---

# Networking Models

VMware Cloud Foundation supports a number of Networking Models for connecting customer workloads to a customer network and for managing network configurations across workload domains.

## Network Consumption Models

Network consumption is the method by which cloud users consume VMware Cloud Foundation networking capabilities. Different capabilities are supported depending on the selected Network Consumption Model.

This table provides a comparison between the supported Network Consumption Models.



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [VCF Automation All Apps Orgs Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-consumption-models(1).html#GUID-46b01052-07d0-4738-af99-747fb3fac24e-en_id-204539d2-12d3-468c-a652-fa5d0b060d58) | - Consumption via VCF Automation or Supervisor UI/API - Prescriptive workload network design based on the VPC model. | - Supports VCF Automation All Apps Orgs - Supports Supervisor services (e.g., VKS) - Consistent cloud-like experience across compute, storage and networking. - Standardized deployment. | - Administrator should not interact directly with NSX UI/API except for troubleshooting. - Less flexibility in network design. - Best suited for new workloads. |
| [Virtual Private Cloud (VPC) Network Virtualization Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-consumption-models(1).html#GUID-46b01052-07d0-4738-af99-747fb3fac24e-en_id-0217e618-c8b2-48ad-989f-40d04448c859) | - Administrator utilizes vCenter or NSX UI/API to create and use NSX VPC - Cloud networking constructs - Partitioned virtual networks - Supports the NSX multi-tenancy framework. | - Simple consumption for non network specialists. - For single tenant, unified UI/API for managing compute, network, and storage (vCenter). - Self-service network and security services. - Embedded IPAM simplifies the creation of new networks and NAT. - Supports Supervisor services (e.g., VKS). | - VPC model cannot be consumed via NSX Global Manager. - Without VCF Automation All Apps Orgs, IaaS tenancy is provided at the networking and security level only. |
| [NSX Segment Network Virtualization Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-consumption-models(1).html#GUID-46b01052-07d0-4738-af99-747fb3fac24e-en_id-9a4605d4-cebb-4547-90fe-47920d4243e1) | - Administrator utilizes NSX UI/API to create logical network topologies - Uses policy NSX objects (Tier-0/Tier-1 gateways and segments). - Provides advanced NSX network and visibility capabilities. - Full support for NSX Federation. - Supports NSX Projects as part of the NSX multi-tenancy framework (Not in conjunction with NSX Federation) | - Allows extension of network topologies across NSX domains. - Full access to advanced NSX features. - Greater flexibility in network design. - Supports Supervisor services (e.g., VKS). | - Requires networking and NSX-specific knowledge. - Does not support VCF Automation All Apps Orgs. - No embedded IPAM for networks (DHCP is available) |
| [VLAN Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-consumption-models(1).html#GUID-46b01052-07d0-4738-af99-747fb3fac24e-en_id-430dff98-a073-462d-a239-9c5117489ec9) | - Administrator utilizes vCenter or NSX UI/API to create and VLANs - VMs connect to distributed port-groups or NSX VLAN segments. - Physical fabric handles network routing and delivery. | - Familiar traditional networking model for vSphere admins. - Supports Supervisor services (e.g., VKS). | - Lacks network virtualization benefits. - Tight coupling between physical network and application topologies. - Requires physical fabric changes to adapt to application changes. |

## Workload Networking Models

The Workload Networking Models define methods of providing layer 2/3 connectivity to workload virtual machines and network services. Each Workload Networking Model presents different capabilities regarding simplicity, performance, service availability, and scale-ability.

Each Workload Networking Model may be deployed and consumed via one or more Network Consumption Models.

| Workload Networking Model | Supported Network Consumption Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- | --- |
| [VPC with Full Services Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vcfa-all-apps-org-compatible.html) | - VCF Automation All Apps Orgs - Virtual Private Cloud (VPC) Network Virtualization | - Active/Standby Tier-0 Gateway. - Full support for VPC centralized network and security services (i.e., NAT, Gateway Firewall, VPC Default Auto SNAT, VPNs). | - Simplified VPC Consumption Model - VCF Automation All Apps Orgs and VKS Support - Support for vCenter UI consumption | For each tenant, North-South throughput is limited to a single NSX edge node. The solution can be scaled via dedicated NSX Edge nodes per tenant as described in the Large Scale Topology workload networking model. |
| [VPC Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vpc-scalable-topology.html) | Virtual Private Cloud (VPC) Network Virtualization | - Active/Active Stateless Tier-0 Gateway. - Partial support for centralized network services (i.e., no VPC Default Auto SNAT, VPNs). | - Simplified VPC Consumption Model. - Support for vCenter UI consumption. - Scalable North-South throughput. | - Some centralized VPC network services are not available (i.e., no VPC Default Auto SNAT, VPNs). - No support for VCF Automation All Apps Orgs and VKS. |
| [VPC Getting Started Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vpc-getting-started.html) | Virtual Private Cloud (VPC) Network Virtualization | - Distributed Transit Gateway. - NAT Support via VM External IPs (1:1 NAT) | - Does not require NSX Edge Nodes. - Simplified VPC Consumption Model - Support for vCenter UI consumption. | No support for centralized network services. |
| [NSX Segment Network Virtualization Scalable Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/workload-networking-classic-nsx-network-virtualization.html) | NSX Segment Network Virtualization | - Active/Active Stateless Tier-0 Gateway. - Partial support for centralized network services (i.e., no redundant VPNs). - Full NSX Federation support. | - Scalable North-South throughput. - VM Mobility across different VCF Instances or VCF WLDs via L2 extension. | - No support for VCF Automation Modern Experience. - No simplified VPC consumption. - No support for vCenter UI consumption. NSX Segments are presented as distributed virtual port-groups in vCenter. The VI Admin can attach VMs to them, but no CRUD operation is available for NSX networking object. |
| [Large Scale Topology Workload Networking Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-large-scale-topologies(1).html) | - Virtual Private Cloud (VPC) Network Virtualization - NSX Segment Network Virtualization | - A mix of Active/Active and Active/Standby Tier-0 Gateways connected back-to-back. - Full support for centralized services depending on the gateway type. - Support both VPC and NSX Segment network consumption models. | - Higher scalability. - Tailoring of tenant services and resources. - Tenant onboarding decoupled from the physical network. | - Higher complexity. - Higher resource requirements. - A higher number of NSX Edges Nodes. |

## Cross Workload Domain Networking Models

Cross Workload Domain Networking models allow networking and security services to be extended across workload domains via a single management interface. The Cross Workload domain networking model choice will depend upon the Network consumption model, workload networking model, and workload domain design chosen.

Cross Workload Domain Networking Models



| Cross Workload Domain Networking Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| NSX Federation | - Cross workload domain traffic goes trough the NSX Edge nodes. - Active and Standby global manager clusters can be deployed in the same or different VCF Instances. - Supports local egress - Multiple local NSX management plane clusters plus NSX global managers - Supports workload domains across VCF Instances | - Enables shared security services across workload domains. - Enables Layer 2 and Layer 3 network topology extension across NSX domains. - No layer2 connectivity is required between Active and Standby Global Manager cluster. - Independent control plane availability per workload domain. - Cross workload domain traffic supports any MTU via TCP mss adjustment and fragmentation. - Coexists with local consumption of VPC. | - Layer 3 connectivity is required between global managers. - Some NSX features are not available from the Global Manager. Consult NSX Documentation for details. |
| Shared NSX Instance | - Cross workload domain traffic leverages fully distributed forwarding on the ESX host. - Local Egress not supported. - Single NSX management plane. - Shared NSX control plane across workload domains. - Does not support workload domains across VCF Instances. | - Enables shared security services across workload domains in the same VCF Instance. - Full support of VPC consumption models. | - Appropriate MTU must be available end-to-end (workload MTU + 200 bytes). - Management plane recovery must be provided by the underlying infrastructure. |