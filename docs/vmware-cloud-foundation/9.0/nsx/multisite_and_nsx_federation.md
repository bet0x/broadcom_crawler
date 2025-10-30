---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Multisite and NSX Federation
---

# Multisite and NSX Federation

There are two options for managing NSX across multiple locations.

Comparison of Multisite and NSX Federation



|  | Multisite | NSX Federation |
| --- | --- | --- |
| Availability | NSX 2.3 | NSX 3.0 |
| Environments | Two locations in metropolitan regions (<10 ms across locations) with stretched VLAN | Other use cases |
| Number of NSX Manager clusters | 1 | 1 per location |
| Network Services | All features supported:   - Switching (Overlay and VLAN) - IPAM (DHCP and DNS) - Routing (VRF, EVPN, NAT and route redistribution) - Layer4+ services (Load Balancing, VPN) | All features supported from GM:   - Switching (Overlay and VLAN) - IPAM (DHCP Relay and static binding, and DNS) - L2-Bridge - Routing (NAT and route redistribution) - Routing protocols (BGP, Static)   Exceptions:   - T0-VRF - DHCP dynamic binding - Routing protocols (OSPF) - Routing VPN and EVPN - Load Balancing |
| Security Services | All features supported:   - Distributed Firewall - Gateway Firewall - FQDN Filtering - L7 App ID context support - Identity Firewall - Distributed IDS - Malware Prevention - Network Introspection - Endpoint Protection - Time-Based Firewall | All features supported from GM:   - Distributed Firewall - Gateway Firewall - FQDN Filtering - L7 App ID context support - Time-Based Firewall   Exceptions:   - Identity Firewall - Distributed IDS - Malware Prevention - Network Introspection and Endpoint Protection |
| High-Availability for Management Plane | NSX Manager VMs recovery   - With SRM from NSX. See [Working with VMware Live Site Recovery and Multisite Environments](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-multisite/working-with-vmware-site-recovery-manager-and-multisite-environments.html#GUID-7e521789-7acc-48d5-8996-61b3a9c47a83-en). - With vSphere HA. | NSX GM and LM VMs recovery with SRM. |
| High-Availability for Compute VMs | Compute VMs recovery   - With SRM from NSX. See [Working with VMware Live Site Recovery and Multisite Environments](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-multisite/working-with-vmware-site-recovery-manager-and-multisite-environments.html#GUID-7e521789-7acc-48d5-8996-61b3a9c47a83-en) . - With vSphere HA. | Compute VMs recovery   - With SRM from NSX with one limitation: Distributed Firewall on Workload VMs cannot be based on NSX tags. - With SRM from NSX without any limitations. |

Also see the [NSX Multi-location Design Guide](https://community.broadcom.com/blogs/dimitri-desmidt/2024/05/20/nsx-t-multi-location-design-guide) and [VMware Site Recovery Manager](https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery.html).