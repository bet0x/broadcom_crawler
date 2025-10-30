---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/simple.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Simple VCF Operations Model
---

# Simple VCF Operations Model

The Simple VCF Operations Model deploys a single node of all the VCF Operations components and uses vSphere HA as an availability mechanism.

The Simple VCF Operations Model includes three single-node components.

**Simple VCF Operations Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cfcd79fb-e61d-40b9-aece-cd786b25d140.original.svg)

## Simple VCF Operations Model Attributes

A Simple VCF Operations Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Availability | Relies on vSphere HA to restart the nodes in the event of an ESX host failure. |
| Scalability | Supports scale-up and scale-out.  Scale-out is supported for the VCF Operations data nodes and VCF Operations collector nodes. |
| Recoverability | Restore through a backup. |

## Simple VCF Operations Model Options

A Simple VCF Operations Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Networking | - Default VM management distributed port group - Dedicated distributed port group - NSX segment (overlay or VLAN backed) |
| Licensing | - Connected Mode - Disconnected Mode |

## Simple VCF Operations Model Design Requirements

Simple VCF Operations Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-SIM-001 | Deploy VCF Operations as a single node in the default management vSphere cluster. | - Supports the simple deployment objective. - Provides the capacity required for monitoring virtual machines or objects within the monitoring scale limits. - Supports scale-out to a high availability model. | - You must select a size for the VCF Operations cluster nodes based on the known or forecasted virtual machine and object count across each connected VCF Instance to adhere to the scale limits. - No application level high availability. |

Common VCF Operations Design Requirements for All Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-COM-001 | Deploy a single VCF Operations fleet management appliance in the default management vSphere cluster. | Provides life cycle management operations for VCF Operations fleet management components. | None. |
| VCF-OPS-REQD-COM-002 | Protect VCF Operations fleet management appliance by using vSphere HA. | Ensures availability of VCF Operations fleet management appliance without requiring manual intervention during an ESX host failure event. | None. |
| VCF-OPS-REQD-COM-003 | Deploy a single VCF Operations collector appliance in the default management vSphere cluster. | - Removes the load from the VCF Operations analytic node(s) from collecting metrics from local-instance applications. - Reuse VCF Operations collectors to gather both logs and metrics across the VCF environment. - Centralized management of logs and metrics, reducing administrative overhead. | You may need to scale-up the VCF Operations collector nodes to a greater size based on the known or forecast virtual machine and object count across each connected VCF Instance to adhere to the scale limits. |
| VCF-OPS-REQD-COM-004 | Protect VCF Operations collector appliance by using vSphere HA. | Ensures availability of VCF Operations collector appliance without requiring manual intervention during an ESX host failure event. | None. |

## Simple VCF Operations Model Design Recommendations

Common VCF Operations Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-RECD-COM-001 | Enable data persistence on each VCF Operations collector appliance. | Provides the ability to store data in case of connectivity issues. | Storage availability on each VCF Operations collector must be monitored. |
| VCF-OPS-RECD-COM-002 | Configure VCF Operations to use a notifications configuration to route notifications for system events. | Integrates VCF Operations system events notifications to platform engineers, providing an enhanced user experience. | You must configure and maintain the notification integration. |
| VCF-OPS-RECD-COM-003 | Add a physical data center object to the VCF Operations configuration for the geographic location of each VCF Instance. | Provides organization of the VCF Operations collector nodes in VCF Operations inventory. | VCF Operations must have connection to the Internet to view and set the precise geographic coordinates in the UI. |
| VCF-OPS-RECD-COM-004 | Activate the Ping integration in VCF Operations. | Provides metrics on the availability of endpoints. | You must activate the integration manually. |
| VCF-OPS-RECD-COM-005 | Configure the currency in the VCF Operations global options based on your organization requirements. | To receive benefits of the VCF Operations cost engine, you must select a currency. | None. |

## VCF Operations - Networking and Internet Access Design Choices

There are several options regarding connectivity to the external resources and network placement for the VCF Operations components. You should choose one option from each of the tables below.

Network Placement for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-NET-001 | Deploy the VCF Operations nodes on the distributed port group created by VCF Installer and reserved for management components. | Ensures that the VCF Operations nodes are deployed adjacent to the other components on the same Layer-2 network. | None. |

Network Placement for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-NET-001 | Deploy the VCF Operations nodes on a dedicated distributed port group **other** than default port group reserved for management components by VCF Installer. | Ensures that the VCF Operations nodes are deployed in a dedicated Layer-2 network. | - You must skip the deployment of the VCF Operation (and VCF Operations fleet management) when using the VMware Cloud Foundation Installer. - You must perform configuration to support the networking configuration as a post-deployment task before manually deploying the VCF Operations and its prerequisites. - You must perform deployment using the SDDC Manager API with JSON file as input. - You must ensure that VLAN is provisioned in each availability zone if stretched clusters are used. |

Network Placement for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-NET-001 | Deploy the VCF Operations nodes on a VLAN-backed NSX segment. | Ensures that the VCF Operations nodes are deployed in a dedicated Layer-2 network. | - You must skip the deployment of the VCF Operations (and VCF Operations fleet management) when using the VCF Installer. - You must perform configuration to support the networking configuration as a post-deployment task before manually deploying the VCF Operations and its prerequisites. - You must perform deployment using the SDDC Manager API with JSON file as input. - You must ensure that VLAN is provisioned in each availability zone if stretched clusters are used. |

Network Placement for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-NET-001 | Deploy the VCF Operations nodes on an overlay NSX segment. | Allow portability of the VCF Operations nodes to another VCF Instance in the VCF fleet without the need for reconfiguration of the IP addressing. | - You must skip the deployment of the VCF Operations (aVCF Operations fleet management) when using the VCF Installer. - You must perform configuration to support the networking configuration as a post-deployment task before manually deploying the VCF Operations and its prerequisites. - You must perform deployment using the SDDC Manager API with JSON file as input. |

Licensing for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-LIC-001 | Use VCF Operations in "Connected licensing mode". | - Provides easy license management and up to date states in overall licensing portal. - No manual interaction required. | VCF Operations will require outbound connection to internet directly or through a proxy server. |

Licensing for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-LIC-001 | Use VCF Operations in "Disconnected licensing mode". | If your policy does not permit access to internet for management components. | - You need to upload usage statistics from VCF Operations to Broadcom's licensing portal and then download and apply entitlements to all VCF Operations. - Usage statistics has be uploaded to the licensing portal every 180 days. |

VCF Operations Diagnostics Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-DIAG-001 | Manually upload Skyline Health Diagnostics and Advisory signatures. | If your policy does not permit access to internet for management components. | Signatures should be downloaded manually and then uploaded into VCF Operations. |

VCF Operations Diagnostics Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-DIAG-001 | Download Skyline Health Diagnostics and Advisory signatures directly from Broadcom's repository. | Ensures always up to date information about potential issues and mitigation steps in your environment. | VCF Operations will require outbound connection to internet directly or through a proxy server. |

Binary Management for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-BIN-001 | Connect to the online depot. | Ensures always up to date information about bundles for Install, Update, Patch and compatibility information. | VCF Operations will require outbound connection to internet directly or through a proxy server. |

Binary Management for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-BIN-001 | Connect to an offline depot. | If your policy does not permit access to internet for management components you may configure an internal depot. | The bundles should be downloaded to a system with access to the Broadcom's depot and then uploaded to the internal depot by following your internal procedures. |

Binary Management for VCF Operations Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implications |
| --- | --- | --- | --- |
| VCF-OPS-RECD-BIN-001 | Upload files manually. | Removes the overhead of installing and managing an additional appliance for internal depot. | You should download and upload all the files to the respective directories and set the right permissions. A lot of manual labor and error prone process. |