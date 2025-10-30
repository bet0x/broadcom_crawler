---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/continuous-availability-vcf-operations-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Continuous Availability VCF Operations Model
---

# Continuous Availability VCF Operations Model

The Continuous Availability VCF Operations Model separates the VCF Operations cluster into two fault domains, stretching across two vSphere instances in two separate availability zones, and protects the analytics cluster against the loss of an entire fault domain.

VCF Operations uses a robust architecture to ensure data availability and fault tolerance across analytics nodes. Data is stored in pairs of analytics nodes, distributed across two fault domains, ensuring continuous availability and synchronization. Each object is stored in two nodes (primary and replica) across fault domains, providing redundancy and resilience in case of failures.

A fault domain consists of one or more analytics nodes, grouped according to their physical location in the data center. The two fault domains enables VCF Operations to tolerate failure of an entire physical location and failures from resources dedicated to a single fault domain. This design requires a VCF Operations witness in a third site.

To deploy the VCF Operations with continuous availability, you first deploy the initial VCF Operations instance by using the Simple VCF Operations Model or the High Availability VCF Operations Model. You then create a second VCF Instance in a separate site/availability zone where you deploy the VCF Operations witness.

## Continuous Availability VCF Operations Model Attributes

A Continuous Availability VCF Operations Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Availability | Implements design with two VCF instances, across two availability zones to protect data from an availability zone failure.  Inside the availability zone, relies on vSphere HA to restart the nodes in the event of an ESX host failure. |
| Scalability | Supports scale-up and scale-out.  Scale-out is supported for the VCF Operations data nodes and VCF Operations collector nodes. |
| Recovery | Redeploy of a components in one of the availability zones in case of availability zone failure.  Restore through a backup for the whole deployment, in case of both availability zones failure. |
| Load balancing | Optional external load balancer for the VCF Operations cluster UI. |

## Continuous Availability VCF Operations Model Options

A Continuous Availability VCF Operations Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Networking | - Default VM management distributed port group - Dedicated distributed port group - NSX segment (overlay or VLAN backed) |
| Licensing | - Connected Mode - Disconnected Mode |

## Continuous Availability VCF Operations Model Design Requirements

Common VCF Operations Design Requirements for All Models



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-COM-001 | Deploy a single VCF Operations fleet management appliance in the default management vSphere cluster. | Provides life cycle management operations for VCF Operations fleet management components. | None. |
| VCF-OPS-REQD-COM-002 | Protect VCF Operations fleet management appliance by using vSphere HA. | Ensures availability of VCF Operations fleet management appliance without requiring manual intervention during an ESX host failure event. | None. |
| VCF-OPS-REQD-COM-003 | Deploy a single VCF Operations collector appliance in the default management vSphere cluster. | - Removes the load from the VCF Operations analytic node(s) from collecting metrics from local-instance applications. - Reuse VCF Operations collectors to gather both logs and metrics across the VCF environment. - Centralized management of logs and metrics, reducing administrative overhead. | You may need to scale-up the VCF Operations collector nodes to a greater size based on the known or forecast virtual machine and object count across each connected VCF Instance to adhere to the scale limits. |
| VCF-OPS-REQD-COM-004 | Protect VCF Operations collector appliance by using vSphere HA. | Ensures availability of VCF Operations collector appliance without requiring manual intervention during an ESX host failure event. | None. |

Continuous Availability VCF Operations Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-REQD-CA-001 | Deploy VCF Operations in the default management vSphere cluster. | - Supports the high availability objectives by deploying VCF Operations as a cluster. - Provides the capacity required for monitoring virtual machines or objects within the monitoring scale limits. - Supports scale-out with additional data nodes. | - You must select a size for the VCF Operations cluster nodes based on the known or forecasted virtual machine and object count across each connected VCF Instance to adhere to the scale limits. - Create an anti affinity rule (Separate Virtual Machines) for the VMs in the cluster after the deployment. |
| VCF-OPS-REQD-CA-002 | Deploy a single Unified VCF Operations collector node in the default management vSphere cluster. | Removes the load from the VCF Operations cluster from collecting metrics from local-instance applications. | You may need to scale-up the VCF Operations collector nodes to a greater size based on the known or forecasted virtual machine and object count across each connected VCF Instance to adhere to the scale limits. |
| VCF-OPS-REQD-CA-003 | The certificate for VCF Operations must include the FQDNs for all cluster nodes in the SAN (subject alternative name) attribute.  The SAN does not need to include the FQDN of VCF Operations collector nodes. | Ensures that the communication to the VCF Operations UI and API, and cross-component, is encrypted. | Prior to scale-out, the certificate for VCF Operations must be changed to also include the FQDN of the additional node in the SAN (subject alternative name) attribute. |
| VCF-OPS-REQD-CA-004 | Deploy a second VCF instance in a separate availability zone. | A second instance is needed to provide a separate SDDC Manager and fully independent infrastructure. |  |
| VCF-OPS-REQD-CA-005 | Satisfy latency requirements for different components. | VCF Operations Continuous Availability requires:   - 10ms with peaks up to 20 ms during 20 sec intervals between the cluster nodes. - 30ms between the witness and the cluster nodes. | Availability zones should be in close proximity and connected with enterprise grade connection. |
| VCF-OPS-REQD-CA-006 | 3rd location (Separate Availability zone) for witness node deployment. | The witness node ensures cluster health and determines which fault domain remains online during communication failures. |  |
| VCF-OPS-REQD-CA-007 | Reconfigure primary replica cluster node to a data node if VCF Operations was deployed with High Availability. | During the configuration of VCF Operations Continuous Availability we will deploy replication partner of the primary node in the second availability zone. |  |
| VCF-OPS-REQD-CA-008 | Deploy through vSphere:   - Replication partners to the nodes in the primary AZ in the secondary AZ. - Witness node in the designated 3rd location. | Replica nodes for all components, should be deployed from a template and later configured in VCF Operations. | Manual workflow spanning across vSphere and VCF Operations. |
| VCF-OPS-REQD-CA-009 | If using an optional external load balancer, the certificate for VCF Operations **must** also include the FQDN of the load balancer in the SAN (subject alternative name) attribute. | Ensures that the communication to the VCF Operations UI and API, and cross-component, is encrypted when using an external load balancer with the high availability model. | None. |

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

## Continuous Availability VCF Operations Model Design Recommendations

Common VCF Operations Design Recommendations for All Models



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-RECD-COM-001 | Enable data persistence on each VCF Operations collector appliance. | Provides the ability to store data in case of connectivity issues. | Storage availability on each VCF Operations collector must be monitored. |
| VCF-OPS-RECD-COM-002 | Configure VCF Operations to use a notifications configuration to route notifications for system events. | Integrates VCF Operations system events notifications to platform engineers, providing an enhanced user experience. | You must configure and maintain the notification integration. |
| VCF-OPS-RECD-COM-003 | Add a physical data center object to the VCF Operations configuration for the geographic location of each VCF Instance. | Provides organization of the VCF Operations collector nodes in VCF Operations inventory. | VCF Operations must have connection to the Internet to view and set the precise geographic coordinates in the UI. |
| VCF-OPS-RECD-COM-004 | Activate the Ping integration in VCF Operations. | Provides metrics on the availability of endpoints. | You must activate the integration manually. |
| VCF-OPS-RECD-COM-005 | Configure the currency in the VCF Operations global options based on your organization requirements. | To receive benefits of the VCF Operations cost engine, you must select a currency. | None. |

Continuous Availability VCF Operations Model Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-OPS-RCMD-CA-001 | Deploy VCF Operations with an external load balancer to load balance the connections across the VCF Operations cluster nodes. | Required to deploy a VCF Operations cluster deployment with distributed user interface access across members. | You must configure the external load balancer configuration to support this VCF Operations configuration. |
| VCF-OPS-RCMD-CA-002 | Create a collector group in VCF Operations for each VCF Instance and assign the default VCF Operations collector appliance. | Provides increased availability to metric collection across the VCF Operations collector appliances asigned to the collector group. | Manual reconfiguration of the VMware Cloud Foundation adapter required to utilze multiple VCF Operations collector appliances with the group. |
| VCF-OPS-RCMD-CA-003 | Reconfigure the default VMware Cloud Foundation Adapter in VCF Operations to use a local-instance collector group for a VCF Instance. | Increases the availability of metric collection. | This must be reconfigured post-deployment. |
| VCF-OPS-RCMD-CA-004 | Deploy a second VCF Operations collector appliance in the default management vSphere cluster and assign it to the collector group. | Increases the availability of metric collection. | None. |
| VCF-OPS-RCMD-CA-005 | Apply a vSphere Distributed Resource Scheduler (DRS) anti-affinity rule to the VCF Operations collector nodes in the same group. | Using vSphere DRS prevents the VCF Operations collectors from running on the same ESX host and risking the high availability of the collectors. | You must perform manual configuration to set up an anti-affinity rule. |