---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/features-available-for-consumption-under-nsx-projects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Features Available for Consumption Under NSX Projects
---

# Features Available for Consumption Under NSX Projects

In a multi-tenant NSX environment, you can configure a subset of NSX features under projects.

This provides flexibility to the tenants while allowing Enterprise Admin and other administrators of the default space to control the overall system life cycle and connectivity.

Features Available Under Projects



| NSX Feature | Available Under Projects | Notes |
| --- | --- | --- |
| System | | |
| Edge Clusters | Assigned during project creation | During project creation, the Enterprise Admin assigns an edge cluster from the default space to a project. |
| System Life cycle | Managed by the Enterprise Admin | Platform-wide operations such as install, upgrade, and backup are managed by the Enterprise Admin. |
| Certificates | Yes | Certificate management tasks are available under projects only for service certificates. |
| Networking | | |
| Tier-0 or Tier-0 VRF Gateway | Assigned during project creation | During project creation, the Enterprise Admin assigns a tier-0 gateway or a tier-0 VRF gateway from the default space to a project.  The services on the tier-0 gateway are managed by the Enterprise Admin from the default space. |
| Dynamic Routing (BGP/OSPF) | Managed by the Enterprise Admin | Dynamic routing is configured on the tier-0 gateway or tier-0 VRF gateway by the Enterprise Admin. |
| EVPN | Managed by the Enterprise Admin | EVPN is configured on the tier-0 gateway or tier-0 VRF gateway by the Enterprise Admin. |
| Tier-1 Gateway | Yes |  |
| Static Routing | Yes | Static routing on the tier-1 gateway is configured by the Project Admin. |
| Overlay Segments | Yes |  |
| VLAN Segments | No |  |
| Segment Profiles   - SpoofGuard - IP Discovery - MAC Discovery - Segment Security - QoS | Yes |  |
| L2 Bridge | No |  |
| L2 VPN | Yes | On each tier-1 gateway of the project, you can configure only one L2 VPN service. |
| IPSec VPN (L3 VPN) | Yes | On each tier-1 gateway of the project, you can configure only one IPSec service.  For configuring route-based IPSec VPN, static-routes are supported. Dynamic routing with virtual tunnel interface (VTI) using BGP is not supported on the tier-1 gateway of the project. |
| NAT | Yes |  |
| Load Balancer | No |  |
| DNS Forwarder   - DNS Services - DNS Zones | Yes |  |
| IP Address Pools/IP Address Blocks | Yes |  |
| IPv6 Profiles (DAD/ND) | Yes |  |
| Gateway QoS Profiles | Yes |  |
| DHCP and DHCP Relay | Yes |  |
| Security | | |
| Distributed Firewall | Yes | Only for VMs that are connected to segments in a project. Firewall rules that are managed by the Enterprise Admin in the default space have the highest precedence followed by the project policies.  DFW policies with Antrea groups in the Sources, or Destinations, or Applied To of the firewall rules are not supported under projects. |
| Exclusion List | Managed by the Enterprise Admin | Exclusion list excludes a VM from all the firewall application rules. |
| Gateway Firewall | Yes | The Enterprise Admin and Project Admin can manage the gateway firewall rules on the tier-1 gateways of the project only within the context of a project. The Project Admin can delete or modify the gateway firewall rules in the project that are created by the Enterprise Admin. |
| Identity Firewall | No | Identity firewall is not available under projects. Identity firewall rules can be configured only in the default space and these rules can be applied to VMs inside projects. |
| Distributed IDS/IPS | Yes |  |
| Gateway IDS/IPS  Malware Prevention  TLS Decryption | No |  |
| TLS Inspection  FQDN Filtering  URL Filtering | No  Yes  Yes | FQDN Analysis dashboard is not exposed to the Project Admin. It is available only to the Enterprise Admin. |
| Firewall Profiles   - Session Timer - Flood Protection - DNS Security | Yes |  |
| Inventory | | |
| Services | Yes |  |
| Groups (static and dynamic memberships) | Yes | Kubernetes member types are not available under a project for creating dynamic membership criteria. |
| Antrea Groups | No |  |
| Context Profiles/L7 Access Profiles | Yes |  |
| Tags | Yes |  |
| Virtual Machines (visibility/tagging) | Yes | Only for VMs that are connected to segments in a project. |
| Container Clusters | No | Kubernetes resources in Antrea Kubernetes clusters that are registered to NSX are not exposed to the project inventory. |
| Plan and Troubleshoot | | |
| Traceflow | Yes | Traceflow can only use VMs and ports that are a part of the project. If the destination is an IP that routes to another project, these details are hidden in the Traceflow output. |
| Antrea Traceflow | No |  |
| Live Traffic Analysis | No |  |
| IPFIX | Managed by the Enterprise Admin | IPFIX is managed centrally by the Enterprise Admin in the default space. |
| Port Mirroring | Managed by the Enterprise Admin | Port mirroring is configured centrally by the Enterprise Admin in the default space. |
| Security Intelligence | No | Security Intelligence features are not exposed to the Project Admin. Only the NSX Enterprise Admin has full access to all the Security Intelligence features.  The Security Intelligence features (network flow visualization, micro-segmentation recommendations, and suspicious traffic analysis) are not project-aware. These features work with all the network traffic flow data within your entire on-premises NSX environment. If multi-tenancy is used, that is, if projects are defined in your NSX environment, Security Intelligence displays all the NSX objects that are in the default space and all the NSX objects from all the projects, whether you are using the Default view or the All Projects view. |