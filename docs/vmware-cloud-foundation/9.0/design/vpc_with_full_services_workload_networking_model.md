---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vcfa-all-apps-org-compatible.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VPC with Full Services Workload Networking Model
---

# VPC with Full Services Workload Networking Model

The model uses a primary (Tier-0) Gateway configured in Active/Standby mode. It provides a VPC-compatible workload domain with network connectivity established via a Centralized Transit Gateway. Individual tenants connect to the Tier-0 Gateway through their own Active/Standby Transit Gateways (TGWs). This workload networking model is the base building block to support all the VCF Automation tenancy models described in VCF Automation Provider Tenant Models and [Multi Tenancy Consumption Patterns](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/multi-tenancy-design-patterns.html). It can also be used in single tenant deployments without the integration with VCF Automation.

## VPC with Full Services Workload Networking Model Attributes

A VPC with Full Services Workload Networking Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Transit Gateway Type | Centralized |
| NSX Edge nodes required | Yes |
| Tier-0 Gateway HA Mode | Active/Standby |
| Network consumption model | VPC |
| NSX Tenancy Constructs | NSX Projects, VPCs |
| Consumption options | - vCenter UI/API - VCF Automation All Apps Orgs - vSphere Supervisor (i.e. VM Service, VKS, and more) - NSX UI/API |
| Provider gateway Type | - Tenant Dedicated Tier-0 Gateway - Tenant Shared Tier-0 Gateway - Tenant Dedicated VRF Gateway |

## Gateway Deployment Options

VPC with Full Services Workload Networking Model Options



| Design Area | Options |
| --- | --- |
| Gateway Deployment Options | - Single Tenant - Shared across multiple tenants - Dedicated, one Gateway for each tenant |
| VRF Adoption (Only applies if the Gateway is shared) | Yes or No |

Shared Gateway Option

- Multiple tenants can share a single Tier-0 Gateway and its NSX Edge node resources
- All tenant IP ranges must undergo Network Address Translation (NAT) before reaching the Tier-0 Gateway.

  - This NAT process happens automatically when VPC subnets are set to "Private TGW" or "Private VPC" access mode

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9bcd97bf-50ac-4500-9732-0d4b364f6c3d.original.png)



Dedicated Gateway Option

- Each tenant can have its own dedicated Tier-0 Gateway
- Supports direct routing of tenant-specific IP ranges to the Tier-0 Gateway

  - Achieved by setting VPC subnets to "Public" access mode, which bypasses NAT between TGW and Tier-0 Gateway
- Enables connection to dedicated external networks (like a VRF in physical fabric, a tenant-specific VPN, or a dedicated private circuit to remote locations)

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c474d030-5dc2-49f6-869d-aa04012e5d4b.original.png)

## Performance Considerations

The Active/Standby configuration of both gateways (Tier-0 and TGW) limits north-south throughput to a single edge node's capacity. However, this setup provides the necessary stateful services for VCF Automation and VKS, including source NAT on TGW and VPC Auto-SNAT. For improved throughput, it's recommended to:

- Use a dedicated Tier-0 Gateways per tenant
- Limit tenant size to match single-edge node capacity

## VRF Integration

When tenants need dedicated external network access or VPN connections but dedicated edge nodes are impractical, NSX VRFs (Virtual Routing and Forwarding) offer a solution:

- VRFs provide similar capabilities to dedicated Tier-0 Gateways
- Multiple VRFs can share a single edge node with their parent Tier-0 Gateway
- VRF limitations in this topology:

  - NAT is the only network service available on the inter-VRF connection to the parent Tier-0 Gateway
  - Gateway firewall and VPN services are restricted to uplink interfaces

VRF Gateways can be shared by multiple tenants. This variation may be desirable when multiple tenants, but not all, need access to the same set of upstream resources, such as VPNs, private WAN circuits, or VRFs in the physical network. When all tenants need access to the same upstream resources, a shared Tier-0 gateway is the most appropriate choice.

Dedicated VRF Gateway Option

 

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/3ee88bba-c5aa-4475-acd9-2a67d9eb19cb.original.png)

## VPC with Full Services Workload Networking Model Design Requirements for Single Tenant or Shared Gateway

VPC Full Services Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCFSVC-REQD-CFG-001 | Two (2) NSX Edge nodes must be available. | - This model requires the centralized security services provided by the NSX Edge nodes. - Exactly two (2) nodes are required to support an Active/Standby Tier-0 gateway. | Additional resources must be available to support the NSX edge nodes. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-002 | Use large or X-Large nodes if using NSX Edge appliance form factor, or use bare-metal NSX Edge. | Supervisor cluster requires load balancing services to be instantiated on the NSX Edge nodes. | Additional resources must be available to support the NSX Edge nodes. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-003 | Use Centralized Connectivity for the connectivity of the Transit Gateway in the Default Project. | This model requires the centralized services provided by the NSX Edge nodes. | Additional resources must be available to support the NSX edge node, following one of the models described in the edge design section. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-004 | Tier-0 gateway must be deployed in Active/Standby HA mode. | - VCF Automation All Apps Orgs require VPC Auto SNAT. - VPC Auto SNAT requires an Active/Standby Tier-0 gateway. | - A single edge processes the entirety of the North-South traffic. - Scaling North-South traffic requires distributing Tenants across multiple Tier-0 gateways. |

## VPC with Full Services Workload Networking Model Design Recommendations for Single Tenant or Shared Gateway

VPC Full Services Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-01 | Use External BGP (EBGP) as the routing protocol between the Tier-0 gateway and the physical network. | - BGP is a scalable solution to interconnect the virtual network environment to the physical fabric. - New dynamically created networks in the VMware Cloud Foundation platform are automatically advertised to the physical network. BGP is a standard protocol supported by the majority of the datacenter switches. - EBGP simplifies the interconnection compared to internal BGP (IBGP) by eliminating the need for full-mesh peering and creating a clear boundary between the administrative domains of VMware Cloud Foundation and the physical network. | Physical switches must support EBGP. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-02 | Use a unique private BGP AS number for the Tier-0 gateway. | It prevents advertisements from being dropped by the BGP loop detection check. If the peering devices only advertise the default route, having a unique BGP AS may not be necessary. It is assumed that the Tier-0 is peering to internal devices and it's not an Internet-facing router, in which case a public AS number is required. | A unique BGP AS must be available for the Tier-0. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-03 | Each of the two (2) NSX Edge nodes where the Active/Standby Tier-0 Gateway runs will peer with two separate physical network devices. | It provides redundancy at the physical network layer, without requiring an edge failover. | - If the NSX Edge is deployed in a virtual machine form factor, the ESX host where it runs must be connected to two (2) physical switches running BGP. - If the NSX Edge is a bare-metal NSX Edge, the server where the bare-metal NSX Edge software is installed must be connected to two (2) physical switches running BGP. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-04 | The physical network devices peering to the Tier-0 Gateway are physically connected to the ESX host where the NSX Edges run, or to the bare-metal NSX Edge. | - The Layer 3 peering is not dependent on any Layer 2 technology, making it easier to map a physical failure to a routing convergence. - Peering over a VLAN transported over multiple physical switches and over potentially multiple redundant paths increases the operational complexity of the design. | The physical switches connected to the ESX host where the NSX Edge Node is running or those connected to a bare-metal NSX Edge must be BGP capable. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-05 | If using edge VMs, use two (2) interfaces for data path fastpath traffic. | Two (2) data plane fastpath interfaces provide redundancy for both VLAN and Overlay traffic. Using the additional two (2) data plane fastpath interfaces does not increase the performance of the NSX edge VM in the majority of situations, in particular when the additional vNics leverage the same set of pNICs. When the ESX hosts have four (4) pNICs available to the NSX Edge appliances, we recommend the use of multiple NSX Edge nodes connected to different sets of pNICs. | Two (2) physical NICs must be available on the ESX hosts where the NSX Edge Node in VM form factor is running. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-06 | If using bare-metal NSX Edge, use four (4) pNIC interfaces for data path traffic | Bare-metal NSX Edge nodes are generally limited by the speed of their interfaces. In most cases, increasing the number of interfaces in use will linearly improve the throughput that can be achieved. | - Four (4) data plane fastpath pNIC must be available on the bare-metal NSX Edge server. - Using two (2) 100G pNICs is a good option for bare-metal NSX Edges when four (4) pNICs are not available. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-07 | Each edge data path interface transports both VLAN and TEP traffic. | Two (2) data path interfaces are sufficient to provide redundancy for both types of traffic. | Inbound and outbound traffic from the virtual network are mixed on the same vNICs, making monitoring less intuitive. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-08 | Every NSX Edge shares the same VLAN to peer to a specific physical device. With two (2) physical devices, it means two (2) peering VLANs are needed. | Adding or replacing additional edge nodes to the NSX Edge node cluster doesn't require creating new VLANs on the physical fabric. | Peering subnet ranges should accommodate NSX Edge cluster growth. |
| VCF-WLDNET-VPC-RCMD-CFG-09 | Use /28 or larger uplink peering subnets are recommended. | Allow to scale the Tier-0 gateway to eight (8) NSX Edge nodes when in an Active/Active configuration. | For an Active/Standby Tier-0, the peering subnets can be smaller as the Tier-0 is limited to two (2) NSX Edge nodes. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-10 | Peering VLANs are transported on trunk port groups connected to the edge fp-eth0 and fp-eth1 interfaces. | - Trunk port groups allow to transport both peering VLAN and TEP VLAN traffic on the same edge vNIC. - Trunk port groups allow seamless integration of VRFs and service interfaces for VLANs. | - Peering VLANs and TEP VLAN are transported on the same peering port-groups but they have different NIC teaming requirements. - Peering VLANs do not need to failover between uplinks, the TEP VLAN does. - The teaming policy for port group must be active/standby to satisfy the TEP VLAN requirement. - Physical switches should prune the peering VLAN from their interfaces where they are not required and should avoid transporting them on the inter-switch link, or via a physical overlay extension (e.g., VXLAN in an EVPN fabric) |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-11 | Set the MTU of the Tier-0 external interfaces to the MTU of the peering interface on the physical network switches (e.g., 9000). | Some network devices set the df bit to "Do not Fragment" on the BGP peering session, a mismatch in the MTU may cause peering issues. | Manual configuration is required. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-12 | Set the global gateway MTU to the value of the external interfaces of the Tier-0 gateway minus 200 (i.e., 8800 = 9000 -200). | Avoid fragmentation at the NSX layer when packets larger than the default 1500 bytes are exchanged between workloads in the virtual network and workloads on the physical network. | Must be set post deployment in NSX as a global setting. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-13 | Enable BFD between the Tier-0 gateway and the physical devices. | Provide fast failure detection and failover with minimal CPU overhead. It permits leaving the BGP timers to their default. | Physical switches need to support BFD. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-14 | Use the default BGP timers, 60/180. | When BFD is enabled, there is no need to lower the default BGP timer settings increasing edge CPU overhead. | - BFD is required for fast failure detection and failover. - If BFD is not available on the physical switches, BGP timers can be lowered to allow a faster failover. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-15 | On the Tier-0 Gateway, enable redistribution of the following network types into BGP:   - Transit Gateway Static | In this model, all workloads are connected to transit gateways. This setting allows for VPC public subnets, NAT IPs, and load balancer VIPs to be advertised to the physical network. | All VPC public subnets, NAT IPs, and load balancer VIPs will be advertised to all BGP peers. If filtering is required, route filters should be configured. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-16 | Create a route filter allowing the advertisement of the default route only from the physical network to the Tier-0 Gateway. A corresponding summarization from the physical network is recommended. | In most cases, the virtual network is a stub network with a single exit point. The filtering reduces the Tier-0 routing table, simplifying troubleshooting and potentially reducing converge time. It also prevents RFP checks from being triggered by asymmetric routing advertisements from the physical switches. | If the virtual network has multiple exit points, for example, one to shared services and one as a private interconnection to the tenant's remote data center, this recommendation cannot be implemented. In such cases reducing the routing table size via summarization is still recommended. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-17 | Leave the RPF check enabled (set to strict) on all four external interfaces of the Tier-0 Gateway. | RPF check mitigates IP Address spoofing attacks. | Asymmetric routing advertisements (Not asymmetric routing, which is normal in any ECMP configuration a supported by the RFP check) from the physical switches will trigger the RPF check and drop nonmalicious traffic. RPF check should be enabled only if consistent routing advertisement from all BGP peers can be guaranteed via route summarization and filtering. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-18 | Set BGP Graceful restart to Helper-only. | Graceful restart may slow down the BGP convergence by waiting for the peer device control plane to recover. Helper-only ensures that routing convergence is delayed only when a peer device negotiates graceful restart. The helper-only setting will allow the Tier-0 gateway to adapt to the peer device behavior. | If the peer device doesn't support graceful restart or if graceful restart is not desirable it may be better to disable graceful restart altogether. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-19 | Set the Forwarding Up timer to 5 seconds (Default). | This will delay traffic from being forwarded to the edge from the virtual network before the routing table is fully populated. | - |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-20 | If leveraging this topology for VCF Automation All Apps Orgs, use the Default Project for system namespace's VPCs. | When VCFA All Apps Orgs are in use, in each Organization will have its dedicated NSX Project. The Default space will not be used and it will be available to be consumed by system VPCs to support the IaaS control plane. The WLD creation workflow follows this model when the new WLD has a new dedicated NSX Manager. | This approach is not recommended if the NSX default project is also consumed via other means, for example via the vCenter UI, which allows the configuration of VPCs in the default project. In general, when VCF Automation is in use, it's not recommended to mix another network consumption vehicle in the same workload domain. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-21 | In the Default VPC Connectivity Profile of the Default project set the NSX Edge cluster as the same where the Tier-0 Gateway is deployed. | This choice will lead to the VPC centralized services running on the same pair of edge nodes as the Tier-0 Gateway and TGW. Because all traffic for the tenant will traverse the single edge node where the TGW and Tier-0 Gateways are active. Scaling the VPC services on a dedicated edge cluster is generally not beneficial in this model because of the Active/Standby nature of the Tier-0 gateway. A better scaling strategy is to create parallel topologies with A/S Tier-0 Gateways sharing the edge cluster with VPC centralized services, one topology per tenant, following the dedicated gateway model. | Edge Nodes will leverage additional CPU cycles to serve Tier-0 Gateway, TGW, and VPC centralized services. Monitor the CPU utilization via one of the following methods:   - NSX Edge CLI - NSX API/UI - VCF Ops   Do not use the vCenter UI graphs to monitor the NSX Edge CPU utilization as it will provide unreliable results. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-22 | In the default VPC Connectivity Profile of the Default project enable N-S Services. | N-S services are required for VPC's Auto-SNAT, SNAT, and DNAT services, which are necessary for VCFA All Apps Orgs and VKS. | Any traffic between different VPCs will traverse the NSX edge node. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-23 | In the default VPC Connectivity Profile of the Default project enable Default Outbound NAT. | Auto-SNAT is necessary for VCFA All Apps Orgs and VKS. | Any traffic between different VPCs will traverse the NSX edge node. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-24 | In the Default VPC Connectivity Profile of the Default project, assign an IP range of enterprise-wide routable IPs to the external IP block ( a /24 CIDR or larger is preferred). | This IP range will be used for any tenant outbound and inbound traffic. It means that any NAT IP, Public subnet range, or Load Balancer VIP will be assigned from this range. | If the IP range is exhausted, additional CIDRs can be added up to a total of 5. Ranges can be added in a CIDR format only. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-25 | In the Default VPC Connectivity Profile of the Default project, assign an IP range of non-routable IPs to the Private-TGW IP block ( a /23 CIDR or larger is preferred). | This IP range will be used for inter-VPC connectivity within the tenant boundary. It will be used to assign CIDRs for Private TGW VPC Subnets. | Workloads on Private-TGW subnets will be reachable from any other tenant workloads without requiring NAT, but no connectivity from workloads outside of the tenant boundary will be available without exposing the workloads via a NAT Rule, or a Load Balancer VIP, or an external IP. |

## Next steps

Once the workload networking for single tenant or shared gateway multi-tenant setup is ready the following options are available:

- Provision tenant-specific networking via tenant manager in VCF Automation
- Start VPC consumption via vCenter
- Expand the design to the dedicated gateway option
- Expand the design with VRF integration

## VPC with Full Services Workload Networking Model Design Requirements for Dedicated Gateway

The following design requirements and recommendations assume that the design for "VPC with Full Services model" for single tenant or shared gateway model has been provisioned already

Dedicated Gateway Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCFSVC-REQD-CFG-05 | The "VPC Full Services Model for single tenant or shared gateway options" must be in place. | The "VPC Full Services Model for single tenant or shared gateway options" will support the system VPCs and optionally any tenant deployed following the shared gateway model. | Two additional edge nodes are required solely to support the System VPCs. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-06 | Two (2) NSX Edge nodes (Large, X-Large, or bare metal) must be available for each tenant adhering to the dedicated gateway deployment model. | - Each tenant will have exclusive access to the resources provided by a pair of edge nodes. This will limit resource contention and will allow the multi-tenant design to scale. - Also, the provider will be able to configure tenant services on a tenant-dedicated Tier-0 gateway, for example VPNs, leveraging tenant-specific IP addresses for local and remote networks. | Additional ESX hosts or pNICs must be available to support the additional edge nodes. In most cases, connecting multiple edge nodes to the same pair of pNICs will not achieve the desired scalability objective. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-07 | A tier-0 in Active/Standby mode must be deployed for each tenant adhering to the dedicated gateway deployment model. | VPC Auto SNAT requires an Active/Standby Tier-0 gateway. VCFA All Apps Orgs require VPC Auto SNAT. | A single edge processes the entirety of the North-South traffic for the tenant. |

## VPC with Full Services Workload Networking Model Design Recommendations for Dedicated Gateway

Dedicated Gateway Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-26 | Use EBGP as the routing protocol between the Tier-0 gateway and the physical network. | - BGP is a scalable solution to interconnect the virtual network environment to the physical fabric. - New dynamically created networks in the VCF environment are automatically advertised to the physical network. BGP is a standard protocol supported by the majority of the datacenter switches. - EBGP simplifies the interconnection compared to IBGP by eliminating the need for full-mesh peering and creating a clear boundary between the administrative domains of VCF and the physical network. | Physical switches must support EBGP. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-27 | Use a unique private BGP AS number for the Tier-0 gateway. | It prevents advertisements from being dropped by the BGP loop detection check. If the peering devices only advertise the default route, having a unique BGP AS may not be necessary. It is assumed that the Tier-0 is peering to internal devices and it's not an Internet-facing router, in which case a public AS number is required. | A unique BGP AS must be available for the Tier-0 |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-28 | Each of the two edge nodes where the Active/Standby Tier-0 Gateway runs will peer with two separate physical network devices. | It provides redundancy at the physical network layer, without requiring an edge failover. | If the NSX Edge is a virtual machine, the ESX host where it runs must be connected to two physical switches running BGP. If the NSX edge is a Bare Metal edge, the server where the BM edge software is installed must be connected to two physical switches running BGP. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-29 | The physical network devices peering to the Tier-0 Gateway are physically connected to the ESX host where the NSX Edges run, or to the bare-metal NSX Edge. | - The Layer 3 peering is not dependent on ant L2 technology, making it easier to map a physical failure to a routing convergence. - Peering over a VLAN transported over multiple physical switches and over potentially multiple redundant paths increases the operational complexity of the design. | The physical switches connected to the ESX host where the NSX Edge appliances are running or those connected to a bare-metal NSX Edge must be BGP capable. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-30 | If using NSX Edge appliances, use two (2) interfaces for data plane fastpath traffic. | Two data plane fastpath interfaces provide .redundancy for both VLAN and Overlay traffic. Using the additional two (2) data plane fastpath interfaces does not increase the performance of the NSX edge VM in the majority of situations, in particular when the additional vNics leverage the same set of pNICs. When the ESX hosts have four (4) pNICs available to the edge VMs, we recommend the use of multiple edge nodes connected to different sets of pNICs. | Two (2) pNIC must be available on the ESX hosts where the NSX Edge VM is running. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-31 | If using bare metal edge, use four (4) pNIC interfaces for data plane fastpath traffic. | Bare metal NSX edge nodes are generally limited by the speed of their interfaces. In most cases, increasing the number of interfaces in use will linearly improve the throughput that can be achieved. | - 4 data plane fastpath pNIC must be available on the bare metal edge server. - Using 2 100G pNICs is a good option for bare metal edges when 4 pNICs are not available. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-32 | Each edge data plane fastpath interface transports both VLAN and TEP traffic. | Two data plane fastpath interfaces are sufficient to provide redundancy for both types of traffic. | Inbound and outbound traffic from the virtual network are mixed on the same vNICs, making monitoring less intuitive. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-33 | Every edge shares the same VLAN to peer to a specific physical device. With two physical devices, it means two peering VLANs are needed. | Adding or replacing additional edge nodes to the NSX edge node cluster doesn't require creating new VLANs on the physical fabric. | Peering subnet ranges should accommodate NSX edge cluster growth. |
| VCF-WLDNET-VPC-RCMD-CFG-34 | Use /28 or larger uplink peering subnets are recommended. | Allow to scale the Tier-0 gateway to 8 edge nodes when in an Active/Active configuration. | For an Active/Standby Tier-0, the peering subnets can be smaller as the Tier-0 is limited to 2 edge nodes. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-35 | Peering VLANs are transported on trunk port groups connected to the edge fp-eth0 and fp-eth1 interfaces. | - Trunk port groups allow to transport both peering VLAN and TEP VLAN traffic on the same edge vNIC. - Trunk port groups allow seamless integration of VRFs and service interfaces for VLANs. | Peering VLANs and TEP VLAN are transported on the same peering port-groups but they have different NIC teaming requirements.Peering VLANs do not need to failover between uplinks, the TEP VLAN does. The teaming policy for port group must be active/standby to satisfy the TEP VLAN requirement. Physical switches should prune the peering VLAN from their interfaces where they are not required and should avoid transporting them on the inter-switch link, or via a physical overlay extension (e.g., VXLAN in an EVPN fabric) |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-36 | Set the MTU of the Tier-0 external interfaces to the MTU of the peering interface on the physical network switches (e.g., 9000). | Some network devices set the df bit to "Do not Fragment" on the BGP peering session, a mismatch in the MTU may cause peering issues. | Manual configuration is required. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-37 | Set the global gateway MTU to the value of the external interfaces of the Tier-0 gateway minus 200 (i.e., 8800 = 9000 -200). | Avoid fragmentation at the NSX layer when packets larger than the default 1500 bytes are exchanged between workloads in the virtual network and workloads on the physical network. | Must be set post deployment in NSX as a global setting. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-38 | Enable BFD between the Tier-0 gateway and the physical devices. | Provide fast failure detection and failover with minimal CPU overhead. It permits leaving the BGP timers to their default. | Physical switches need to support BFD. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-39 | Use the default BGP timers, 60/180. | When BFD is enabled, there is no need to lower the default BGP timer settings increasing edge CPU overhead. | - BFD is required for fast failure detection and failover. - If BFD is not available on the physical switches, BGP timers can be lowered to allow a faster failover. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-40 | On the Tier-0 Gateway, enable redistribution of the following network types into BGP:   - Transit Gateway Static | In this model, all workloads are connected to transit gateways. This setting allows for VPC public subnets, NAT IPs, and load balancer VIPs to be advertised to the physical network. | All VPC public subnets, NAT IPs, and load balancer VIPs will be advertised to all BGP peers. If filtering is required, route filters should be configured. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-41 | Create a route filter allowing the advertisement of the default route only from the physical network to the Tier-0 Gateway. A corresponding summarization from the physical network is recommended. | In most cases, the virtual network is a stub network with a single exit point. The filtering reduces the Tier-0 routing table, simplifying troubleshooting and potentially reducing converge time. It also prevents RFP checks from being triggered by asymmetric routing advertisements from the physical switches. | If the virtual network has multiple exit points, for example, one to shared services and one as a private interconnection to the tenant's remote data center, this recommendation cannot be implemented. In such cases reducing the routing table size via summarization is still recommended. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-42 | Leave the RPF check enabled (set to strict) on all four external interfaces of the Tier-0 Gateway. | RPF check mitigates IP address spoofing attacks. | Asymmetric routing advertisements (Not asymmetric routing, which is normal in any ECMP configuration a supported by the RFP check) from the physical switches will trigger the RPF check and drop nonmalicious traffic. RPF check should be enabled only if consistent routing advertisement from all BGP peers can be guaranteed via route summarization and filtering. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-43 | Set BGP Graceful restart to Helper-only. | Graceful restart may slow down the BGP convergence by waiting for the peer device control plane to recover. Helper-only ensures that routing convergence is delayed only when a peer device negotiates graceful restart. The helper-only setting will allow the Tier-0 gateway to adapt to the peer device behavior. | If the peer device doesn't support graceful restart or if graceful restart is not desirable it may be better to disable graceful restart altogether. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-44 | Set the Forwarding Up timer to 5 seconds (default). | This will delay traffic from being forwarded to the edge from the virtual network before the routing table is fully populated. | None. |

## VPC with Full Services Workload Networking Model Design Requirements for VRF Integration

VRF Integration Design Requirements



| Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCFSVC-REQD-CFG-08 | The "VPC Full Services Model for single tenant or shared gateway options" must be in place | The "VPC Full Services Model for single tenant or shared gateway options" will support the system VPCs and optionally any tenant deployed following the shared gateway model. | None. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-09 | Each tenant requiring a VRF will have a dedicated VRF deployed in Active/Standby Mode | The provider will be able to configure tenant services on a tenant-dedicated VPN, for example, VPNs leveraging tenant-specific IP addresses for local and remote networks. | Additional ESX hosts or pNICs must be available to support the additional edge nodes. In most cases, connecting multiple edge nodes to the same pair of pNICs will not achieve the desired scalability objective. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-10 | The tenant VRFs must be associated with the Tier-0 (Parent Tier-0) provisioned as part of the "VPC Full Services Model for single tenant or shared gateway options" | VPC Auto SNAT requires an Active/Standby Tier-0 gateway or VRF. VCFA All Apps Orgs require VPC Auto SNAT. | A single NSX Edge processes the entirety of the North-South traffic for the tenant. |
| VCF-WLDNET-VPCFSVC-REQD-CFG-11 | Each VRF uses two dedicated peering VLANs | VRFs sharing the same NSX edge node cannot share the same VLAN ID for any of their external interfaces | New VLANs must be created any time a new VRF is provisioned. In highly dynamic environments incorporating inline EVPN in the design will remove this design requirement. |

## VPC with Full Services Workload Networking Model Design Recommendations for VRF Integration

| Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-45 | Use external BGP (EBGP) as the routing protocol between the VRF gateway and the physical network | BGP is a scalable solution to interconnect the virtual network environment to the physical fabric.  New dynamically created networks in the VCF environment are automatically advertised to the physical network. BGP is a standard protocol supported by the majority of the datacenter switches.  EBGP simplifies the interconnection compared to internal BGP (IBGP) by eliminating the need for full-mesh peering and creating a clear boundary between the administrative domains of VCF and the physical network. | Physical switches must support EBGP |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-46 | Use a unique private BGP AS number for the VRF gateway | It prevents advertisements from being dropped by the BGP loop detection check. If the peering devices only advertise the default route, having a unique BGP AS may not be necessary. It is assumed that the Tier-0 is peering to internal devices and it's not an Internet-facing router, in which case a public AS number is required. | A unique BGP AS must be available for each VRF |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-47 | The VRF will peer to the same physical devices as the Parent Tier-0 Gateway | VRF HA status is dependent on the HA status of the parent Tier-0 gateway. For this reason, the VRF and the Parent Tier-0 gateway must share the same type of physical failures and react to them consistently. Specifically, the design should avoid the VRF having an NSX Edge node in the "All BGP peers down" state while the parent T0 does not. More details are in the NSX Design Guide version 4.2.1 Chapter 4. | Designs where each VRF peers with a different upstream device incorporate additional risk. The risk can be avoided via the dedicated gateway model, which is not affected by this behavior as each Tier-0 gateway maintains its own HA state.  If VRFs with different upstream gateways are in use, the risk can be mitigated by peering each VRF edge node to multiple upstream devices to limit the chance of a VRF having an edge node in the "All BGP peers down" state while the Parent Tier-0 does not. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-48 | Peering VLANs are transported on trunk port groups connected to the edge fp-eth0 and fp-eth1 interfaces. | Trunk port groups allow to transport both peering VLAN and TEP VLAN traffic on the same edge vNIC.  Trunk port groups allow seamless integration of VRFs and service interfaces for VLANs. | Peering VLANs and TEP VLAN are transported on the same peering port-groups but they have different NIC teaming requirements.Peering VLANs do not need to failover between uplinks, the TEP VLAN does. The teaming policy for port group must be active/standby to satisfy the TEP VLAN requirement. Physical switches should prune the peering VLAN from their interfaces where they are not required and should avoid transporting them on the inter-switch link, or via a physical overlay extension (e.g., VXLAN in an EVPN fabric) |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-49 | Set the MTU of the Tier-0 external interfaces to the MTU of the peering interface on the physical network switches (e.g., 9000) | Some network devices set the df bit to "Do not Fragment" on the BGP peering session, a mismatch in the MTU may cause peering issues | Manual configuration is required |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-50 | Enable BFD between the VRF gateway and the physical devices | Provide fast failure detection and failover with minimal CPU overhead. It permits leaving the BGP timers to their default. | Physical switches need to support BFD |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-51 | Use the default BGP timers, 60/180 | When BFD is enabled, there is no need to lower the default BGP timer settings increasing edge CPU overhead. | BFD is required for fast failure detection and failover  If BFD is not available on the physical switches, BGP timers can be lowered to allow a faster failure detection and failover |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-52 | On the VRF, enable redistribution of the following network types into BGP:   - Transit Gateway Static | In this model, all workloads are connected to transit gateways. This setting allows for VPC public subnets, NAT IPs, and load balancer VIPs to be advertised to the physical network. | All VPC public subnets, NAT IPs, and load balancer VIPs will be advertised to all BGP peers. If filtering is required, route filters should be configured. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-53 | Create a ingress route filter allowing the advertisement of the default route only from the physical network to the VRF Gateway. A corresponding summarization from the physical network is recommended. | In most cases, the virtual network is a stub network with a single exit point. The filtering reduces the Tier-0 routing table, simplifying troubleshooting and potentially reducing converge time. It also prevents RFP checks from being triggered by asymmetric routing advertisements from the physical switches. | If the virtual network has multiple exit points, for example, one to shared services and one as a private interconnection to the tenant's remote data center, this recommendation cannot be implemented. In such cases reducing the routing table size via summarization is still recommended. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-54 | Leave the RFP check enabled (set to strict) on all four external interfaces of the Tier-0 Gateway | RPF check mitigates IP Address Spoofing Attacks | Asymmetric routing advertisements from the physical switches will trigger the RPF check and drop nonmalicious traffic. RPF check should be enabled only if consistent routing advertisement from all BGP peers can be guaranteed via route summarization and filtering. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-55 | Set BGP Graceful restart to Helper-only | Graceful restart may slow down the BGP convergence by waiting for the peer device control plane to recover. Helper-only ensures that routing convergence is delayed only when a peer device negotiates graceful restart. The helper-only setting will allow the Tier-0 gateway to adapt to the peer device behavior. | If the peer device doesn't support graceful restart or if graceful restart is not desirable it may be better to disable graceful restart altogether. |
| VCF-WLDNET-VPCFSVC-RCMD-CFG-56 | Set the Forwarding Up timer to 5 seconds (Default) | This will delay traffic from being forwarded to the edge from the virtual network before the routing table is fully populated | None |