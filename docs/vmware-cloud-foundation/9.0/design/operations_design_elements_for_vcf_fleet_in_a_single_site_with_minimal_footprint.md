---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design/design-decisions-for-vcf-fleet-in-a-single-site-with-minimal-footprint/operations-design-elements-for-vcf-fleet-in-a-single-site-with-minimal-footprint.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Operations Design Elements for VCF Fleet in a Single Site with Minimal Footprint
---

# Operations Design Elements for VCF Fleet in a Single Site with Minimal Footprint

This section provides the operations requirements and recommendations for the VCF Fleet in a Single Site with Minimal Footprint blueprint

Common VCF Operations Design Requirements for All Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-COM-001 | Deploy a single VCF Operations fleet management appliance in the default management vSphere cluster. | Provides life cycle management operations for VCF Operations fleet management components. | None. |
| VCF-OPS-REQD-COM-002 | Protect VCF Operations fleet management appliance by using vSphere HA. | Ensures availability of VCF Operations fleet management appliance without requiring manual intervention during an ESX host failure event. | None. |
| VCF-OPS-REQD-COM-003 | Deploy a single VCF Operations collector appliance in the default management vSphere cluster. | - Removes the load from the VCF Operations analytic node(s) from collecting metrics from local-instance applications. - Reuse VCF Operations collectors to gather both logs and metrics across the VCF environment. - Centralized management of logs and metrics, reducing administrative overhead. | You may need to scale-up the VCF Operations collector nodes to a greater size based on the known or forecast virtual machine and object count across each connected VCF Instance to adhere to the scale limits. |
| VCF-OPS-REQD-COM-004 | Protect VCF Operations collector appliance by using vSphere HA. | Ensures availability of VCF Operations collector appliance without requiring manual intervention during an ESX host failure event. | None. |

Common VCF Operations Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-RECD-COM-001 | Enable data persistence on each VCF Operations collector appliance. | Provides the ability to store data in case of connectivity issues. | Storage availability on each VCF Operations collector must be monitored. |
| VCF-OPS-RECD-COM-002 | Configure VCF Operations to use a notifications configuration to route notifications for system events. | Integrates VCF Operations system events notifications to platform engineers, providing an enhanced user experience. | You must configure and maintain the notification integration. |
| VCF-OPS-RECD-COM-003 | Add a physical data center object to the VCF Operations configuration for the geographic location of each VCF Instance. | Provides organization of the VCF Operations collector nodes in VCF Operations inventory. | VCF Operations must have connection to the Internet to view and set the precise geographic coordinates in the UI. |
| VCF-OPS-RECD-COM-004 | Activate the Ping integration in VCF Operations. | Provides metrics on the availability of endpoints. | You must activate the integration manually. |
| VCF-OPS-RECD-COM-005 | Configure the currency in the VCF Operations global options based on your organization requirements. | To receive benefits of the VCF Operations cost engine, you must select a currency. | None. |

Simple VCF Operations Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-SIM-001 | Deploy VCF Operations as a single node in the default management vSphere cluster. | - Supports the simple deployment objective. - Provides the capacity required for monitoring virtual machines or objects within the monitoring scale limits. - Supports scale-out to a high availability model. | - You must select a size for the VCF Operations cluster nodes based on the known or forecasted virtual machine and object count across each connected VCF Instance to adhere to the scale limits. - No application level high availability. |

Network Placement for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-NET-001 | Deploy the VCF Operations nodes on the distributed port group created by VCF Installer and reserved for management components. | Ensures that the VCF Operations nodes are deployed adjacent to the other components on the same Layer-2 network. | None. |

Licensing for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-LIC-001 | Use VCF Operations in "Connected licensing mode". | - Provides easy license management and up to date states in overall licensing portal. - No manual interaction required. | VCF Operations will require outbound connection to internet directly or through a proxy server. |

VCF Operations Diagnostics Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-DIAG-001 | Download Skyline Health Diagnostics and Advisory signatures directly from Broadcom's repository. | Ensures always up to date information about potential issues and mitigation steps in your environment. | VCF Operations will require outbound connection to internet directly or through a proxy server. |

Binary Management for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-BIN-001 | Connect to the online depot. | Ensures always up to date information about bundles for Install, Update, Patch and compatibility information. | VCF Operations will require outbound connection to internet directly or through a proxy server. |

Lifecycle Management Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-LCM-001 | Use VCF Operations to perform the life cycle management of the management components. | Because the deployment scope of VCF Operations covers the full VMware Cloud Foundation platform, VCF Operationsperforms patching, update, or upgrade of these components across all workload domains. | The operations team must understand and be aware of the impact of a patch, update, or upgrade operation by using VCF Operations. |
| VCF-OPS-REQD-LCM-002 | Use vSphere Lifecycle Manager images to manage the life cycle of vSphere clusters. | - With vSphere Lifecycle Manager images, firmware updates are carried out through firmware and driver add-ons, which you add to the image you use to manage a cluster. - You can check the hardware compatibility of the hosts in a cluster against the Broadcom Compatibility Guide. - You can validate a vSphere Lifecycle Manager image to check if it applies to all hosts in the cluster. You can also perform a remediation pre-check. | - Updating the firmware with images requires an OEM-provided hardware support manager plug-in, which integrates with vSphere Lifecycle Manager. - An updated vSAN Hardware Compatibility List (vSAN HCL) is required during bring-up. |