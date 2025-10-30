---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vsphere-supervisor-deployment-types.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSphere Supervisor Models
---

# vSphere Supervisor Models

vSphere Supervisor is a workload domain capability that, when activated, enables a self-service consumption experience that uses a single declarative API to create resources such as Virtual Machines, Kubernetes Guest Clusters, Storage Volumes and other advanced services.

## vSphere Zones

A vSphere Zone is the boundary that maps to a single vSphere cluster. vSphere Zones can be tagged as vSphere Supervisor Management zones and/or assigned to one or more vSphere Namespaces as Workload Zones. A vSphere Zone can only be associated to one vSphere Supervisor instance.

| Supervisor Zone Type | Attributes |
| --- | --- |
| Management | - One vSphere Zone in a Single Management Zone configuration - Three vSphere Zones in a Three Management Zone configuration - Where Supervisor Control Plane nodes and Foundational Load Balancer (FLB) appliances are deployed. - Must be selected at vSphere Supervisor activation. |
| Workload | - Can be added or marked for removal from vSphere Namespaces post vSphere Supervisor activation. - Can be added to one or more vSphere Namespaces. |

ESX hosts that make up a vSphere Zone within each zone type should have similar performance characteristics to maintain consistent and predictable performance.

## Simplified Supervisor Model

VMware Cloud Foundation 9.0 allows you to create a simplified Supervisor deployment requiring fewer resources and configuration steps than a typical deployment. This simplified deployment allows access to a limited subset of Supervisor capabilities. You can then expand the deployment over time to build out to full Supervisor functionality.

For information on how to deploy or scale a Simplified Supervisor deployment, refer to the [Deploying with a Simplified Deployment Flow](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration/deploying-easy-supervisor.html).

Simplified Supervisor Model Diagram

This diagram illustrates an example of a Simplified Supervisor Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d046ec9a-e7b9-485c-bc71-19534623b630.original.svg)

Simplified Supervisor Model in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| Simplified Supervisor | - Single control plane VM. - Single vNIC control plane VM. - No load balancer. | - Minimal resources required. - Supports running VM Service. | - Does not support running vSphere Pods and other Superviser services. |

## vSphere Supervisor Zone Models

vSphere Supervisor can be deployed with a combination of Single or Three Management Zones and Combined or Isolated Workload Zones. A hybrid approach to these models is possible but not recommended.

The vSphere Supervisor Management Zone of a single or three zone choice must be made at activation and cannot be modified after.

Single Management Zone with Combined Workload Zones Model Diagram

This diagram illustrates an example of a Single Management Zone with Combined Workload Zones Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2a666aae-dc08-4c32-97fc-39152205b6a8.original.svg)



Single Management Zone with Isolated Workload Zones Model Diagram

This diagram illustrates an example of a Single Management Zone with Isolated Workload Zones Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/094fee0e-aa08-4ea3-9a97-252cc21af9d2.original.svg)

vSphere Supervisor Single Management Zone Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Single Management Zone with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/single-zone.html) | - A single vSphere Zone used for vSphere Supervisor management and application workloads. - Simple or high-availability control plane option. | - Simplest deployment model. - No additional vSphere clusters required for application workloads zones. | vSphere cluster availability impacts both Supervisor management and application workloads zones. |
| [Single Management Zone with Isolated Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-zone.html) | - One vSphere Zone used for vSphere Supervisor management workloads. - vSphere Zone used for management workloads are separate to application workloads. - Simple or high-availability control plane option. | Supervisor management and application workload availability impacts are independent of each other. | Additional vSphere clusters required for application workloads zones. |

Three Management Zones with Combined Workload Zones Model Diagram

This diagram illustrates an example of a Three Management Zones with Combined Workload Zones Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ec332fe0-48fb-4df8-98d9-39532459a54b.original.svg)



Three Management Zones with Isolated Workload Zones Model Diagram

This diagram illustrates an example of a Three Management Zones with Isolated Workload Zones Model deployment.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c4acf25c-6f36-45e0-b698-7d874e8fffe9.original.svg)

vSphere Supervisor Three Management Zones Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Three Management Zones with Combined Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-management-zones-with-combined-workload-zones-model.html) | Three vSphere Zones used for vSphere Supervisor management and application workloads. | - vSphere Supervisor management workload is protected from single vSphere cluster outages. - No additional vSphere clusters required for application workloads zones. | - High-availability control plane option only. - Activation by API only. |
| [Three Management Zones with Isolated Workload Zones Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/self-service-iaas-deployment-models/vsphere-supervisor-zone-models/three-management-zones-with-isolated-workload-zones-model.html) | - Three vSphere Zones used for vSphere Supervisor management workloads. - vSphere Zones used for management workloads are separate to application workloads. | Supervisor management and application workload availability impacts are independent of each other. | - High-availability control plane option only. - Additional vSphere clusters required for application workloads zones. - Activation by API only. |

## vSphere Supervisor Control Plane Availability Models

For each vSphere Supervisor instance, one or three control plane nodes will be deployed to the selected Management Zones. The vSphere Supervisor control plane appliance can be deployed with one control plane node (Simple) and scale to three control plane (High-availability) nodes post activation for Single Management Zone model deployments.

vSphere Supervisor is deployed with simple control plane availability option when activating Supervisor as part of VCF workload domain creation. This can be scaled to the high-availability configuration after activation.

vSphere Supervisor Control Plane Availability Models in VMware Cloud Foundation



| Control Plane Availability | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| Simple Control Plane | - Single control plane node. - Default option when activating Supervisor as part of VCF workload domain creation. | - Simplified Supervisor activation. - Minimal resources required. | - Single point of failure. - Downtime during upgrade. - Not an option for Three Zone Management deployments. |
| High Availability Control Plane | - Three control plane nodes deployed for each Supervisor instance. - In a Three Management Zone model, one control plane node is deployed per zone. - Only option for Three Management Zone model | Protects against single control plane node failure. | Additional resources required. |

## vSphere Supervisor Load Balancer Models

vSphere Supervisor Load Balancer Models in VMware Cloud Foundation



| Load Balancer | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| NSX | - Default for NSX VPC and NSX Segment network virtualization models. - Not available for VLAN Networking model. | - No additional configuration required. - No additional entitlement required. | - Does not support Layer 7 application rules. - Cannot be used for non-Supervisor workloads |
| Avi | - Add-on component. - Available for all networking models. | - Highly scalable and performing. - Advanced monitoring features. - Can be shared with other workloads. | - Additional entitlement required. - Additional deployment and configuration required. |
| Foundation Load Balancer (FLB) | - Available for VLAN networking model only. - Deploys and shares the same resource and storage policy as the Supervisor management zone. - Single node or two node active/standby topology. - One-arm or two-armed configuration option | - No additional configuration required. - No additional entitlement required. | - Limited up to Layer 4 rules. - Limited scalability. - Not supported on zonal high availability deployment model. |

## vSphere Zones and Storage

Supervisor uses storage policies to integrate with storage available to vSphere. The policies represent datastores and manage storage placement of Supervisor objects. Storage policies support VCF cluster principal and supplemental datastores configured.

When assigning storage for Supervisor, availability and performance considerations should be made in relation to the underlying storage that supports the vSphere Zones used by Supervisor.

For detailed information, refer to the [Supervisor Storage](../../../../../../../../../../../output/sites/docworks-preview/vsphere-supervisor-installation-and-configuration-ditamap/vsphere-supervisor-concepts/supervisor-architecture-and-components/supervisor-storage.html#GUID-ff5ed184-5d87-4b7a-bac3-047b8692597b-en) in the vSphere Supervisor Platform documentation.

|  | Considerations | Examples |
| --- | --- | --- |
| Availability | Storage availability constructs should align with vSphere Zones. There is no replication of data between zones on the infrastructure layer. Each zone should be treated as an independent failure domain. | - If a datastore is a failure domain, each zone should utilize an independent datastore. - If a zone has physical failure domain boundaries such as ESX hosts and physical networking, physical storage placement should be co-located. |
| Performance | Storage consumed by the zone type and vSphere Namespace should have the same performance characteristics to maintain consistent and predictable performance. | - Storage for management zones should have the same performance characteristics. - Storage for all workload zones within the same vSphere Namespace should have the same performance characteristics. |

## Supervisor with vSAN

Supervisor can benefit from various vSAN storage topologies.

Supervisor vSAN Compute and Storage Model Support

The following table describes the supportability of various [vSphere Supervisor Models](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vsphere-supervisor-deployment-types.html) in combination of various vSAN Compute Cluster Models and vSAN Storage Cluster Models.



| vSphere Zones | Compute Cluster Storage Model | vSAN Storage Model | Support |
| --- | --- | --- | --- |
| Single | vSAN Compute Cluster | Single vSAN Storage Cluster | Yes |
| Multiple | vSAN Compute Cluster | Single vSAN Storage Cluster per Zone | Yes |
| Multiple | vSAN Compute Cluster | Shared vSAN Storage Cluster between Zones | Not recommended |
| Single | vSAN Stretched Compute | Single vSAN Stretched Cluster | Yes |
| Multiple | vSAN Stretched Compute | Shared vSAN Stretched Cluster between Zones | Not applicable |
| Multiple | vSAN Stretched Compute | Single vSAN Stretched Cluster per Zone | No |
| Single | vSAN Compute Cluster | Single vSAN Stretched Storage Cluster | Yes |
| Multiple | vSAN Compute Cluster | Single vSAN Stretched Storage Cluster per Zone | Yes |
| Multiple | vSAN Compute Cluster | Shared Single vSAN Stretched Storage Cluster between Zones | Not recommended |
| Multiple | vSAN Compute Cluster | Shared Single vSAN Stretched or Stretched Storage Cluster with each vSAN availability zone aligned to one vSphere zone. | Yes |