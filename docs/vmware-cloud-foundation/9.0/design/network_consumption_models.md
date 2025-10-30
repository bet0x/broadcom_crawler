---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-consumption-models(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Network Consumption Models
---

# Network Consumption Models

VMware Cloud Foundation (VCF) offers various approaches to network consumption. Administrators can select the model the best suit their requirements regarding how network and security services are created and life-cycled.

## VCF Automation All Apps Orgs network consumption model

When the goal is to leverage the VCF infrastructure via VCF Automation via All Apps Orgs, where the management of compute , storage and and network is centralized via single UI/API, the cloud user should not interact directly with the NSX UI/API other than for troubleshooting purposes. The cloud user should create and administer NSX VPCs via the VCF Automation API/UI.

## Network Consumption models based on custom topologies

This category encompasses designs where the deployment of workloads and network topologies are decoupled or only loosely coupled. A common example is a scenario where the network administrator manually creates a topology for a specific use case or tenants in NSX, then the VI Admin deploys workloads on top of that manually or via some automation.

Leveraging automation implies that the automation solution can discover the NSX-created networks (e.g., VPC subnets) or the corresponding vSphere dvpgs so that workloads can be connected to them. The automation solution doesn't require any awareness of how those networks are wired into the larger network design, which can be independently controlled by the network administrator in NSX. The network administrators have full freedom to deploy the Network Workload Design that best meets the application requirements. Various Network Workload designs are available and presented in the relevant section. The NSX administrator can select one for the entire infrastructure or mix multiple designs of the same or different types for different tenants or use cases.

The network consumption models based on custom topologies we will cover are:

- Virtual Private Cloud (VPC) Network Virtualization model
- NSX Segment Network Virtualization model
- VLAN Networking model

## Virtual Private Cloud (VPC) Network Virtualization model

A VPC is a cloud networking construct, a secure, isolated virtual network within a cloud environment. NSX VPCs bring the same characteristics and consumption model of the public cloud to VCF.

The NSX VPC is a foundational and required component for designs requiring VCF Automation All Apps Orgs, but it is also the recommended network consumption model for any custom topology aimed at supporting the manual deployment of workloads, VCF Automation VM Only Orgs, or third-party automation tools.

Starting with VCF 9, VPCs can be managed from the vCenter inventory networking tab making the vSphere client the single interface for managing compute, network, and storage for simple single-tenant deployments. Multi-tenant deployments not requiring the strong separation provided by VCF Automation All Apps Orgs can leverage VPCs within the NSX multi-tenancy framework to provide self-service network and security services via the NSX UI and API.

## NSX Segment Network Virtualization model

This model leverages Policy NSX objects such as Tier-0/Tier-1 Gateways and segments to deploy network topologies. This model allows the Network Administrator to leverage all of the advanced NSX network capabilities but requires more extensive networking and NSX-specific knowledge.

This model does not support VCF Automation All Apps Orgs, and while it does support supervisor services, it is recommended that new deployments of supervisor embrace the VPC-based topology.

For custom topologies, the VPC model is still the preferred approach for its simplicity and seamless integration with other VCF components such as vCenter.

The NSX Segment Network Virtualization model should be considered when the capabilities it provides compared to the VPC model are critical to meeting the design requirements. Among those, the ability to extend network topologies across workload domains in different VCF instances via NSX Federation is a primary use case.

Comparison between NSX Segment and VPC models



| Exclusive capabilities of the NSX Segment Network Virtualization Model | Alternatives when using the VPC Network Virtualization model |
| --- | --- |
| NSX Federation:   - Stretched Layer 2 and Layer 3 topologies across NSX Domains - Single point of management for security policies across NSX Domains - VM Mobility across NSX Domains | - Use a shared NSX Domain across VI WLDs - With separate NSX Domains, the NSX Enterprise Admin can leverage NSX federation to provide a single point of management for security policies across VPCs in different NSX domains - Duplicating VPCs with the same networking layout across NSX Domains allows the recovery of VMs one VPC at a time (It requires filtering the VPC IP ranges at the secondary site on the upstream Tier-0 gateway or VRF until the recovery process is initiated) |
| VPNs on Tier-1 Gateways | Configure VPNs on upstream VRF or Tier-0 Gateway, where dynamic routing is supported and peer redundancy can be provided. |
| Advanced Security Features supported on Tier-1 Gateway (Firewall Add-On required):   - Identity Firewall - URL Filtering - FQDN Analysis - IDS/IPS - Malware Detection - TLS Inspection | - Enable those capabilities on the upstream VRF or Tier-0 Gateway when supported(i.e., IDS/IPS, Identity Firewall), Firewall Add-On is required - Enable the equivalent Distributed Service when available (i.e. Distributed IDS/IPS or Distributed Malware Protection), Firewall Add-On is required |

## VLAN Networking Model

In this model, the only VCF component participating in the networking functionalities is the VDS, responsible for switching the traffic between the VMs running in the hypervisor and the physical uplinks. Once the packets are delivered to the upstream physical switch, it is the responsibility of the physical fabric to deliver them to the appropriate destination.Virtual machines are connected to distributed port-groups or NSX VLAN segments.

This model lacks the benefits provided by the NSX network virtualization which decouples the physical network from the topology requirements of the applications and services that run on top of it. With network virtualization, the physical fabric can be designed and operated based on a simpler and more stable model that does not require following the application's lifecycle. The role of adapting to the ever-changing application requirements is offloaded to the NSX network virtualization layer while the physical fabric design can be centered around maximizing throughput and high availability, minimizing latency, and optimizing operational efficiency.

The VLAN networking model is supported in VCF and may be appropriate for specific use cases, but it is not recommended for the majority of scenarios as it lacks the benefits provided by network virtualization. The benefits of network virtualization are summarized in the table below.

## Comparison VLAN Networking vs Network Virtualization (VPC or NSX Segment)

| Attribute | VLAN Networking | Network Virtualization (VPC or Policy NSX) |
| --- | --- | --- |
| VM Mobility | VM mobility is limited to the span of a VLAN (usually one rack) | VM mobility across Layer 3 boundaries – any topology |
| Rack Availability | Achieving rack availability via vSphere HA is not possible without extending VLANs between racks | Easy to achieve rack availability via vSphere HA for compute workloads regardless of the network fabric topology |
| Resource Pooling | Resource pooling is limited by the VLAN span | Heterogenous islands of computing are easily integrated. vSphere clusters can be distributed across N racks regardless of the network fabric topology |
| Infrastructure Agility | Slow application deployment dependent on physical network reconfigurations | The physical network is abstracted. No changes are required to support the application lifecycle |
| Change Management | Network changes require the reconfiguration of multiple devices | Single point of management for the entire logical network. The network can embrace an Infrastructure as Code (IoC) approach, where network constructs follow the application lifecycle |
| Disaster Recovery | Disaster recovery requires re-IP or extending networks across sites via the physical network | Easy disaster recovery without re-IP via NSX Federation (NSX Segment only) or Multi-AZ design. |
| L2 Scale | Fundamentally tied to MAC learning and L2 discovery over different types of underlay technology (e.g., traditional L2, EVPN) | Programmed from vSphere, and thus no MAC learning and abstracted from the physical network, reducing the leaf switch scale requirements |
| L2 Security | Physical fabric is directly exposed to L2 frames generated by the VMs (e.g., STP BPDU) | NSX Overlay isolates the physical fabric from the Layer 2 frames generated by the endpoints |
| Support of Advanced Networking (i.e., NAT, Firewall) | Tied to physical ASIC and limited by switch vendor | Software-defined allows scaling of the networking and security stack |

When using VLAN networking two options are available:

- Create distributed port-groups (dvpgs) in vCenter
- Create VLAN Segments in NSX Manager

When enabling "NSX on dvgps" for a vSphere cluster in NSX, workloads connected to dvpgs can leverage the same NSX distributed services as those connected to NSX Segments or VPC subnets. Those services include the vDefend Distributed Firewall (available as an advanced service), spoofguard, and any other services that can be applied via NSX segment profiles.

To use VLAN segments, workloads must be placed on the NSX-managed distributed virtual port groups that are automatically created when a VLAN segment is defined in NSX.

From a scalability perspective, using VLAN segments is better suited for larger environments with a high number of VDSs, vCenters, and dvpgs. When creating a VLAN segment in NSX, a corresponding vCenter dpvg is automatically created on any VDS part of the corresponding VLAN TZ. This provides simpler lifecycle management of VLAN networks via NSX manager in environments with numerous VDSs, across single or multiple vCenters. This consideration is particularly relevant for VMware Cloud Foundation platforms where each vSphere cluster has a dedicated VDS, increasing the number of VDSs and dvpgs to be managed.

Comparison Distributed Switch Port-Groups vs VLAN Segments



| Feature | Option 1: vCenter Distributed Switch Port-Groups | Option 2: NSX VLAN Segments |
| --- | --- | --- |
| Creation Method | Created directly in vCenter | Created in NSX Manager |
| NSX Services Support | Supported via "NSX on dvpgs" feature | Natively supported |
| Compatible Services | Distributed firewall, spoofguard, segment profiles (They require applying NSX to distributed port-groups) | Distributed firewall, spoofguard, segment profiles |
| Workload Placement | VMs connected to vCenter-managed dvpgs | VMs connected to NSX-managed dvpgs (auto-created) |
| Scalability | Suitable for smaller environments | Better for larger environments with many VDSs and vCenters |
| Lifecycle Management | Individual management of dvpgs in vCenter | Simplified management through NSX Manager |
| Multi-VDS Deployment | Requires manual creation of dvpgs on each VDS | Auto-creates corresponding dvpgs on all VDSs in VLAN TZ |

## NSX Federation

NSX Federation provides a single point of management for workload networking and security across NSX domains, regardless if those NSX domains are associated to workload domains, within, or across VCF Instances.

NSX Federation is compatible with all the network consumption models listed in the previous section but the level of integration and the benefits it can provide vary across them. The table below summarize its capabilities in the context of each of the available network consumption models.

The capabilities considered are :

- NSX Enterprise Admin centrally manages security policy and groups across NSX Domains
- Layer 2 and Layer 3 network topology extension across NSX Domains

Tenant (NSX Project) admins, and VPC admins do not have the ability to configure global groups and security policies spanning multiple NSX Domains, nor managing local groups and security policies for multiple NSX Domains via the NSX Global Manager.

NSX Federation capabilities in the different Network Consumption Models



| Network Consumption Model | NSX Federation Capabilities | |
| --- | --- | --- |
| NSX Enterprise Admin centrally manages security policy and groups across NSX Domains | Layer 2 and Layer 3 network topology extension across NSX Domains |
| VCF Automation All Apps Orgs | Yes. Tenant or VPC scoped groups and security policies are local to a single NSX Domain. | No |
| Virtual Private Cloud (VPC) Network Virtualization | Yes. Tenant or VPC scoped groups and security policies are local to a single NSX Domain. | No |
| NSX Segment Network Virtualization | Yes | Yes |
| VLAN Networking | Yes | No |

When extending networking and security services across workload domains part of the same VCF Instance, the goal can be achieved via NSX Federation or by sharing the NSX domain across the workload domains. When extending networking and security services across workload domains as part of different VCF Instances, NSX Federation is the only option. For workload domains that are part of the same VCF Instance, the two methods are compared in the table below

Comparison of NSX Federation vs Shared NSX Domain Capabilities for cross Workload Domain Networking



| Attribute | NSX Federation | Shared NSX domain | Considerations |
| --- | --- | --- | --- |
| Cross workload domain traffic | Cross workload domain traffic goes trough the NSX Edge nodes. | Cross workload domain traffic leverages fully distributed forwarding on the ESX host. | Consider the amount of cross workload domain traffic. If NSX Federation is selected, size the NSX Edge node accordingly, and distribute workloads on separate segments and Tier-1 gateways to spread the load across multiple NSX Edge nodes. |
| MTU | Cross workload domain traffic supports any MTU via TCP mss adjustment and fragmentation. | Appropriate MTU must be available end-to-end (workload MTU + 200 bytes). | If MTU cannot be guaranteed end-to-end, NSX Federation provides a solution. |
| Local egress | Yes | No | Implementing Local egress causes asymmetric north-south routing across the workload domains unless each stretched segment has workloads in a single workload domain and inbound routing is configured appropriately. |
| Management plane availability | Active/Standby model for Global Managers. Active and Standby clusters can be deployed in the same or different VCF Instances. Layer 3 connectivity is required. No layer2 connectivity is required between Active and Standby Global Manager cluster. | Single NSX Manager cluster across workload domain. Recovery must be provided by the underlying infrastructure, for example via a stretched vSphere cluster. | NSX Federation is the preferred solution for disaster recovery use cases. |
| Control plane availability | Independent per workload domain. | Shared across workload domains. | In a design with a shared NSX domain accross workload domains model requiring the recovery of workloads across such workload domains, workloads cannot be recovered until the control plane (NSX Manager appliances) is recovered. This limitation does not affect designs based on NSX Federation as each workload domain has an independent local control plane. |
| Feature support | Some NSX features are not available.  Refer to the NSX documentation for an up to date comprehensive list. | Full NSX feature support. | When the design requires the adoption of specific capabilities, NSX Federation may not meet those requirements. |