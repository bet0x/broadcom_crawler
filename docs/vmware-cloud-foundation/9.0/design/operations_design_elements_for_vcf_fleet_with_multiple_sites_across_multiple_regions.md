---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-4/design-elements-for-vcf-fleet-with-multiple-sites-across-multiple-regions/operations-design-elements-for-vcf-fleet-with-multiple-sites-across-multiple-regions.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Operations Design Elements for VCF Fleet with Multiple Sites Across Multiple Regions
---

# Operations Design Elements for VCF Fleet with Multiple Sites Across Multiple Regions

This section provides the operations requirements and recommendations for the VCF Fleet with Multiple Sites Across Multiple Regions blueprint

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

High Availability VCF Operations Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-HA-001 | Deploy VCF Operations as a cluster of three nodes in the default management vSphere cluster. | - Supports the high availability objectives by deploying VCF Operations as a cluster. - Provides the capacity required for monitoring virtual machines or objects within the monitoring scale limits. - Supports scale-out with additional data nodes. | - You must select a size for the VCF Operations cluster nodes based on the known or forecasted virtual machine and object count across each connected VCF Instance to adhere to the scale limits. - Create an anti affinity rule (Separate Virtual Machines) for the VMs in the cluster after the deployment. |
| VCF-OPS-REQD-HA-002 | Deploy a single Unified VCF Operations collector node in the default management vSphere cluster. | Removes the load from the VCF Operations cluster from collecting metrics from local-instance applications. | You may need to scale-up the VCF Operations collector nodes to a greater size based on the known or forecasted virtual machine and object count across each connected VCF Instance to adhere to the scale limits. |
| VCF-OPS-REQD-HA-004 | Apply a vSphere Distributed Resource Scheduler (DRS) anti-affinity rule to the VCF Operations cluster nodes. | Using vSphere DRS prevents the VCF Operations cluster nodes from running on the same ESX host and risking the high availability of the cluster. | - You must perform additional configuration to set up an anti-affinity rule. - You must have a minimum of four ESX hosts in the default management vSphere cluster to ensure you can put an ESX host in maintenance mode. - If additional data nodes are added, you must update the anti-affinity rule and ensure there are enough ESX hosts in the default management vSphere cluster to ensure you can put an ESX host in maintenance mode. |
| VCF-OPS-REQD-HA-007 | The certificate for VCF Operations must include the FQDNs for all cluster nodes in the SAN (subject alternative name) attribute.  The SAN does not need to include the FQDN of VCF Operations collector nodes. | Ensures that the communication to the VCF Operations UI and API, and cross-component, is encrypted. | Prior to scale-out, the certificate for VCF Operations must be changed to also include the FQDN of the additional node in the SAN (subject alternative name) attribute. |
| VCF-OPS-REQD-HA-001 | If using an optional external load balancer in the high availability deployment model, the certificate for VCF Operations **must** also include the FQDN of the load balancer in the SAN (subject alternative name) attribute. | Ensures that the communication to the VCF Operations UI and API, and cross-component, is encrypted when using an external load balancer with the high availability model. | None. |

High Availability VCF Operations Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-RCMD-HA-001 | Deploy VCF Operations with an external load balancer to load balance the connections across the VCF Operations cluster nodes. | Required to deploy a VCF Operations cluster deployment with distributed user interface access across members. | You must configure the external load balancer configuration to support this VCF Operations configuration. |
| VCF-OPS-RCMD-HA-002 | Create a collector group in VCF Operations for each VCF Instance and assign the default VCF Operations collector appliance. | Provides increased availability to metric collection across the VCF Operations collector appliances asigned to the collector group. | Manual reconfiguration of the VMware Cloud Foundation adapter required to utilze multiple VCF Operations collector appliances with the group. |
| VCF-OPS-RCMD-HA-003 | Deploy an additional VCF Operations collector node in the default management vSphere cluster. | Extends the availability of the VCF Operations collectors by balancing the load across the collectors when added to a collector group. | - You must deploy the collector node after the deployment of the VCF Operations. - Additional collector node should be deployed for all VCF Instances that requires a collector group. |
| VCF-OPS-RCMD-HA-004 | Apply a vSphere Distributed Resource Scheduler (DRS) anti-affinity rule to the VCF Operations collector nodes. | Using vSphere DRS prevents the VCF Operations collectors from running on the same ESX host and risking the high availability of the collectors. | You must perform manual configuration to set up an anti-affinity rule. |
| VCF-OPS-RCMD-HA-005 | Reconfigure the default VMware Cloud Foundation Adapter in VCF Operations to use a local-instance collector group for a VCF Instance. | Increases the availability of metric collection. | This must be reconfigured post-deployment. |

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