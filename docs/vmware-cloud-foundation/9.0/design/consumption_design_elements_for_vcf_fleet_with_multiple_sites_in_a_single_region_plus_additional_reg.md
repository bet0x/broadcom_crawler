---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-5/design-elements-for-vcf-fleet-with-multiple-sites-in-a-single-region-plus-additional-regions/consumption-design-elements-for-vcf-fleet-with-multiple-sites-in-a-single-region-plus-additional-region.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Consumption Design Elements for VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s)
---

# Consumption Design Elements for VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s)

This section provides the consumption requirements and recommendations for the VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s) blueprint

## Management Domain

High Availability VCF Automation Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-HA-001 | Deploy VCF Automation as a three node cluster in the default management vSphere cluster. | Supports high availability objectives. | - Analysis will be required to determine which node size is appropriate for your deployment. - Node can be resized after deployment as necessary. |
| VCF-AUTO-REQD-HA-002 | [Deploy VCF Automation in separate DVPG or NSX Overlay](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking/deploy-vcf-management-components-on-an-nsx-overlay-segment.html) as a three node cluster through VCF VCF Operations fleet management. | Supports different network other than default management network for security requirements. | If deployed via VCF Operations fleet management, all the VCF Operations components (to include fleet manager) will need to be fully up and functional prior to starting the VCF Automation deployment. |
| VCF-AUTO-REQD-HA-003 | If VCF Automation is deployed as high availability deployment will default to the medium node size. Review the configuration maximums for the medium node size to determine if it will be sufficient for your use cases | Ensures that the VCF Automation node sizing is appropriate for your use cases. | If your use cases require the large size nodes you will need to perform a scale up action through VCF Operations fleet management post deployment. |
| VCF-AUTO-REQD-HA-004 | Protect all VCF Automation nodes by using vSphere HA. | Supports the high availability objective without requiring manual intervention during an ESX host failure. | None |

Fleet Level Components on Shared Management Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-SM-REQD-001 | Use the management domain vCenter VM management port group for the Fleet level components | No additional network required | - No logical network isolation - NSX load balancer not supported |
| VCF-FLT-SM-REQD-002 | Use the same VLAN for Fleet level components and the VCF Instance managment VMs | No additional VLAN required | Separate physical firewall rules may not be possible with single VLAN |

Fleet Level Components on Shared Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-FLT-SM-RCMD--001 | Deploy the fleet level components during initial deployment using VCF Installer. | Simplified deployment using UI. | None. |

VCF Automation Provider Authentication Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-PROV-001 | Configure an identity provider for the VCF Automation Provider. | - Allows provider to leverage an enterprise directory. - Enables named access control to Infrastructure level constructs. - Required to provision administrative access to the Provider Administrator Portal for any account other than the default local admin account. | If not configured, the only access to the Provider Administrator Portal will be through the default local admin account created during installation. |
| VCF-AUTO-REQD-PROV-002 | Leverage the VCF Identity Broker identity provider. | - Provides Single Sign-On with the rest of the VMware Cloud Foundation components. - Leverages the authentication direction for VMware allowing support for future enhancements. | None. |

VCF Automation Tenant Authentication Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-TEN-001 | Configure an identity provider for VCF Automation Tenants. | - Allows tenant to leverage enterprise directory. - Enables named access control to tenant level constructs. - Required to provision administrative or user access to the Organization portal for any account other than the first user account established during Organization creation. | If not configured, the only access to the Organization Portal will be through the first user account established during Organization creation. |

## Workload Domain

vSphere Supervisor Design Requirements for all Zone Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-AMZ-REQD-CFG-001 | vSphere clusters must have vSphere HA enabled. | Required feature to automatically recover from host failure. | Sufficient spare ESX host resources required for vSphere HA functionality. |
| VCF-SUP-AMZ-REQD-CFG-002 | vSphere clusters must have vSphere DRS enabled in Fully Automated or Partially Automated mode. | Required feature to automatically balance resource utilization within the cluster. | Sufficient host resources required for vSphere DRS functionality. |
| VCF-SUP-AMZ-REQD-CFG-003 | vSphere Zones must be configured. | vSphere clusters needs to be configured with vSphere Zone names before it can be utilized by vSphere Supervisor. | A vSphere Zone name will be generated for a Single Management Zone Model if not configured and cannot be changed. |

vSphere Supervisor Single Management Zone Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-SMZ-REQD-CFG-001 | One available vSphere Zone of a supported vSphere Cluster model that is not in use by another Supervisor instance at activation. | vSphere Zone for Supervisor management workload use. | vSphere Zone will not be available for another vSphere Supervisor instance within the same vCenter. |

vSphere Supervisor Networking Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-NET-REQD-CFG-001 | NSX centralized gateway must be deployed in Active/Active configuration when deploying with NSX Segment Networking Model. | Required topology. | NSX centralized gateway must be manually configured |
| VCF-SUP-NET-REQD-CFG-002 | NSX centralized gateway must be deployed in Active/Standby configuration when deploying on NSX VPC Networking Model. | Required topology. | Sufficient throughput is required from the active edge node. |
| VCF-SUP-NET-REQD-CFG-003 | Opt-out of Supervisor activation when deploying a workload domain when activating Supervisor for any networking model other than NSX VPC with NSX Load Balancer. | Activating Supervisor as part of the workload domain deployment is only possible on NSX VPC with NSX Load balancer topology. | Supervisor activation needs to be performed from vCenter. |

vSphere Supervisor Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-RCMD-CFG-001 | Activate vSphere Supervisor with NSX VPC Networking Model. | - Benefits of NSX VPC and VCF Automation All Apps. - Out of the box configuration during workload domain creation. | NSX VPC Centralized Gateway connectivity must be manually configured. |
| VCF-SUP-RCMD-CFG-002 | Deploy control plane in high-availability mode. | High availability for vSphere Supervisor control plane. | Additional hosting resources are required. |

vSphere Supervisor Control Plane Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-CP-REQD-CFG-001 | Five consecutive management IP addresses routable to vCenter, NSX and Avi management networks. | Required for integration and management communications. | Requires precise IP address management. |
| VCF-SUP-CP-REQD-CFG-002 | Three vSphere Zones required for High-Availabiliy Model in a Three Management Zone Model. | Control Panel nodes are evenly placed with one per zone to protect against a single vSphere cluster failure. | Additional vSphere clusters are required. |

vSphere Supervisor Control Plane Design Recommendations



| Design Requirement ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-CP-RCMD-CFG-001 | Deploy high availability (three) control plane VMs.  \*Applicable to Non-Simplified Supervisor models only. | Three control plane VMs allow for continuous availability of the Supervisor control plane during rolling upgrades and single node outages. | Additional resources are required to support the extra control plane VMs. |

vSphere Supervisor NSX Load Balancer Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SUP-NLB-REQD-CFG-001 | Workload networking model must be NSX Segment or NSX VPC. | Compatibility with NSX Virtual Networking models only. | Incompatible with VLAN Networking model. |
| VCF-SUP-NLB-REQD-CFG-002 | NSX Edge cluster must be deployed. | NSX Load Balancers run on NSX Edges. | NSX Edge design, deployment and configuration required. |
| VCF-SUP-NLB-REQD-CFG-003 | NSX Edge nodes must be deployed with a minimum of large form factor. | NSX Load Balancers have fixed resource allocations on NSX Edge nodes. Large form factor is required to accommodate basic system and workload needs. | Large form factor resources required. If additional load balancers are required, NSX Edges can be scaled up or out. |