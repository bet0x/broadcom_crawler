---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking/design-library-workload-networking-vpc-getting-started.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VPC Getting Started Workload Networking Model
---

# VPC Getting Started Workload Networking Model

This model enables rapid adoption of VPC network virtualization without requiring NSX Edge VM deployment. It uses a Distributed Transit Gateway (DTGW), which differs from previous models by utilizing distributed rather than centralized connectivity. This topology offers a simplified starting point for organizations looking to implement VPC network virtualization with minimal infrastructure requirements. No centralized network service is available in this topology.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/11971c7c-f4a7-4f86-b2f2-4d4e204fb590.original.png)

## VPC Getting Started Workload Networking Model Attributes

A VPC Getting Started Workload Networking Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Transit Gateway Type | Distributed |
| NSX Edge nodes required | No |
| Tier-0 Gateway HA Mode | Does Not Apply |
| Network consumption model | VPC |
| NSX Tenancy Constructs | NSX Projects, VPCs |
| Consumption options | - vCenter UI/API - NSX UI/API |

## Key Components

- Distributed Transit Gateway (DTGW)
- External VLAN connection to the physical network
- Direct interconnection between DTGW and physical fabric via the external VLAN

## External VLAN Requirements

- The external VLAN must be accessible to all ESX hosts running VPC workloads.
- For multi-pNIC ESX hosts, the external VLAN must be available on NSX TEP-enabled pNICs

## Network Traffic considerations

- All external traffic must route through the external VLAN gateway IP
- Servers on the external VLAN cannot directly access VPC workloads
- VPC workloads on "private VPC" or "private TGW" subnets can only be exposed to external clients using External IPs

## Network Services Considerations

- NAT rule configuration is not available
- VPC and TGW centralized firewall and NAT are not available
- VPC Auto-SNAT is not available
- DHCP is only supported via Distributed DHCP
- No option to integrate VPN services

## VPC Getting Started Workload Networking Model Design Requirements

| Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-01 | In the physical fabric, extend one external VLAN across the entire NSX Domain (one or more WLDs) | It provides connectivity for external IPs or public subnets for VMs in VPCs connected to the Distributed TGW. | Physical fabric must meet this requirement. If meeting this requirement is impossible, an alternative solution incorporating NSX Edges and C-TGW should be implemented. |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-02 | Make the external VLAN available on the VDS and pNICs where the NSX TEPs are connected | Public subnets and External IPs of VMs in VPCs connected to the Distributed TGW are presented to the external VLAN via the uplinks where TEPs are enabled. | Physical fabric must be configured to allow the external VLANs on the correct ESX interfaces. |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-03 | Do not connect any device on the external VLAN except for the physical switches | Devices on the external network will not have connectivity to VPC external IP because the D-TGW responds to ARP requests sourced from the external VLAN gateway only. | External VLAN must be dedicated to external IP and VPC public subnets and cannot be shared with any other workloads. |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-04 | In the Default VPC Connectivity Profile of the Default project, assign a range of enterprise-wide routable IPs part of the external VLAN CIDR as the external IP Block | This range will be used for any VPC inbound and outbound traffic. Any External IP or Public subnet will be assigned from this range. | If the range is exhausted additional CIDRs can be added up to a total of 5. Ranges can be added in a CIDR format only. |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-05 | Exclude any IP assigned to physical network devices on the external network from assignment to VPCs if the external block includes them | IP Address conflicts may arise if the exclusion is not configured | The external VLAN Gateway IP is excluded by default. Additional Exclusion can be configured via the NSX API, by allocating those IPs to the default project. |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-06 | In the default VPC Connectivity Profile of the Default project disable N-S Services | N-S services are not available when using D-TGW | If N-S services are required, an alternative solution incorporating NSX Edges and C-TGW should be implemented. |
| VCF-WLDNET-VPCGSTRT-REQD-CFG-07 | In the default VPC Connectivity Profile of the Default project disable Default Outbound NAT | Default Outbound NAT requires N-S services | If N-S services are required, an alternative solution incorporating NSX Edges and C-TGW should be implemented. |

## VPC Getting Started Workload Networking Model Design Recommendations

| Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-WLDNET-VPCGSTRT-RCMD-CFG-01 | In the Default VPC Connectivity Profile of the Default project, assign a non-routable CIDR to the Private-TGW IP block | The range will be used to carve out Private TGW subnets in the default project. Those subnets allow No-NAT communication between VPCs but prevent connectivity upstream of the D-TGW without the use of an External IP | If Private TGW subnets are not required, this step can be omitted. |