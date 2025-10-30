---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Design Blueprints for VMware Cloud Foundation
---

# Design Blueprints for VMware Cloud Foundation

To assist with choosing an architecture for your specific business and technology requirements, the Design Blueprints section provides a set of pre-defined architecture topologies, based on specific design profiles. To deliver a ready-to-consume solution, providing the full set of capabilities (end-to-end design) offered by the VMware Cloud Foundation platform, each Design Blueprint provides a prescriptive selection of the deployment models available for each VMware Cloud Foundation component.

## Understanding Design Blueprints

A VMware Cloud FoundationDesign Blueprint:

- Is a prescriptive end-to-end design for a VCF fleet in a commonly requested architecture topology, created to help accelerate time to value when building a new VMware Cloud Foundation platform.
- Has a prescriptive selection of deployment models chosen from the design library to conform to the design profile of the Design Blueprint.
- Can be deployed as is, with no alterations, or can be used as template where any of the deployment models can be substituted for alternatives from the same category within the design library. See [Design Library for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library.html).
- Reflects the initial deployment of a VCF fleet and supports expansion in a variety of ways to support the needs of your organization.
- Provides a set of planning, implementation and design elements (requirements and recommendations) based on the chosen deployment models.

## Choosing and Using a Design Blueprint

Before assessing any of the provided Design Blueprints, you should familiarize yourself with the options available within the VCF architecture, by reading the [Architectural Options in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts.html) section of this document. This will help you understand the ways in which you can substitute selections within the Design Blueprint for other deployment models that better suit your organizations needs.

This design guide covers the following pre-defined Design Blueprints:

- [VCF Fleet in a Single Site with Minimal Footprint](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design.html)
- [VCF Fleet in a Single Site](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-management-design-with-multiple-availability-zones.html)
- [VCF Fleet with Multiple Sites in a Single Region](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vsphere-only-to-vcf-fleet-upgrade-blueprint.html)
- [VCF Fleet with Multiple Sites across Multiple Regions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-4.html)
- [VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-5.html)

Each Design Blueprint has a Design Profile section to help you quickly establish if the Design Blueprint is a good fit for your organizational needs, and is structured using the following categories:

- Consumption
- Physical Site Configuration
- Availability
- Isolation
- Recoverability
- Expansion

Review each of the Design Blueprints provided until you find the one that most closely matches your requirements. If it is a perfect fit, then use it as is to deploy your VCF fleet. If it is not a perfect fit, then using the knowledge you gained in the [Architectural Options in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts.html) section of this document, review the Design Selections sections of the Design Blueprint and substitute any of the selected models for alternatives from the same category in the design library to create your own custom Design Blueprint. Each substituted model will have a list of its specific design elements in its section within the design library.

Once your pre-defined or custom Design Blueprint it deployed, your VCF fleet may evolve according to your emerging needs of your organization. While you may choose to evolve your VCF fleet to align with different blueprints over time, there is no requirement to expand in any given manner, or to remap your organization to a different blueprint should that evolution take your configuration in a different direction than the initial deployment.

## Understanding Physical Site Configurations

The following terminology definitions help you better understand the provided Design Blueprint in the context of the physical site configuration.

| Term | Definition in a Design Blueprints Context |
| --- | --- |
| Region | - A region is comprised of one of more physical sites in a single metropolitan area i.e. within synchronous replication latencies. - Recovery of management/business workloads between regions is a disaster recovery process. |
| Single Site | - A site represents a logical and a physical boundary that is managed as a single, contained entity. It may offer levels of isolation at the physical layer (power, HVAC, connectivity, etc.) but represents a single fault domain for at least one level of infrastructure. - VCF fleet (management and business workloads) are deployed in a single site. - Protecting any given component or workload to another site is not within the scope of a Design Blueprint, as recovery generally depends upon a second (recovery) site. - A single site can support multiple clusters, workload domains and VCF Instances based on the scale and workload isolation required. |
| Multiple Independent Sites | - VCF fleet (management and business workloads) are distributed across multiple independent sites, but one site will operate the VCF fleet management components, creating a level of dependency on that one site. - Sufficient network connectivity exists between sites to facilitate centralized management. This generally means layer-3 connectivity with separate, non-overlapping IP address spaces at each site - Either the latency or bandwidth are not suited to protecting management components and business workloads across sites, or there is no desire to do. - Additional sites can be deployed as follows based on requirements:    - Clusters in existing VCF domains.   - Additional VCF domains.   - Additional VCF Instances with appropriate VCF fleet management components. - Each site can support multiple clusters, workload domains and VCF Instances based on the scale required |
| Multiple Sites in a Single Region | - VCF fleet is distributed across multiple sites that are connected to provide centralized management and site resilience for management and/or business workloads. - Latency and bandwidth are suitable for protecting management and/or business workloads across sites using stretched cluster technology or any other protection level (based on their individual requirements) by leveraging the appropriate vSphere Cluster Model. - With the use of stretched clusters, the VCF fleet management components, as well as other management and customer workloads can operate across a pair of sites to provide enhanced availability at the infrastructure layer, in addition to application-layer availability capabilities. - Additional sites can be deployed as follows based on requirements:    - Clusters in existing VCF domains.   - Additional VCF domains.   - Additional VCF Instances or to stretch clusters between sites. - Each site can support multiple clusters, workload domains and VCF Instances based on the scale required - Provides a suitable platform for a layered disaster recovery solution if required. |
| Multiple Sites across Multiple Regions | - VCF fleet is distributed across multiple sites that are connected for the purpose of providing site resilience for management and/or business workloads, as well as for centralized management. - Latency and bandwidth are not suitable for protecting management and/or business workloads across sites using stretched cluster technology, but may be used to provide all other protection levels (based on their individual requirements) by leveraging the appropriate vSphere Cluster Model. - One site will operate the VCF fleet management components, and additional sites can be deployed as follows based on requirements:    - Clusters in existing VCF domains.   - Additional VCF domains.   - Additional VCF Instances. - Each site can support multiple clusters, workload domains and VCF Instances based on the scale required - Provides a suitable platform for a layered disaster recovery solution if required. |

## VCF Fleet Architecture and Blueprints

Each of the Design Blueprint in this section has a scope of a single VCF fleet. VCF fleets are completely independent from a management and operational perspective, and have no shared components.

A VCF private cloud may contain multiple VCF fleets, related through layers outside of the VCF boundary - for example applications may have components in multiple VCF fleets, multiple VCF fleets may also share some underlying physical infrastructure such as datacenters (sites), racks, and network equipment, or be associated with a common external management platform.

To determine whether a deployment should be contained within an entire VCF fleet or spread across different VCF fleets a number of factors need to be reviewed:

**Physical Location**

- Since the VCF Operations, Fleet Management & VCF Automation components will reside in the initial cluster, all the resources within the VCF Fleet should be within suitable latency, and support sufficient network bandwidth for traffic to and from the initial cluster management components and the ESX hosts and workloads in other locations.

**Environment Role or Compliance Separation**

- To support validating end-to-end upgrades or physical isolation, if full separation is required between environments providing different roles (for example Development, Testing, Pre-Production, Production or environments that adhere to a specific compliance regime) , it may be necessary to have separate VCF Fleets for these different environments.

**Scale**

- If any aspect of the environment may exceed the scale limits for a VCF Fleet (see ConfigMax), it should be proactively divided into multiple VCF Fleets based on logical boundaries to avoid hitting a scale limit during a growth period.

**Business Organization**

- In some cases there may be a desire to fully isolate groups at all levels of infrastructure and applications. Although VCF provide a multi-tenant experience, in cases where a potential divestiture is planned, or for other business requirements, separate VCF Fleets may be desired for different business groups.

**Availability Requirements**

- If there are different environments that have different availability requirements for the VCF Fleet management components, you can either build to the highest requirement, or separate the workloads into different VCF Fleets that match the availability requirements of the workloads they will manage.

Once the VCF Fleet layout is determined for the organization, the most appropriate Blueprint for each environment can be selected for its VCF Fleet, and scaled out as needed.

## Disaster Recovery

Disaster recovery is the process of recovering management and/or business workloads between sites and has the following attributes:

- The fail-over is “crash consistent” - the running state of workloads is not maintained by the infrastructure.
- There is a Recovery Point Objective (RPO), which is a delay in time between when data is written to storage in one location and when it is replicated to the other location.
- There is a Recovery Time Objective (RTO), which is the amount of time it takes for the workloads to be operational in the second location once the manually-initiated fail-over process is started.
- Typically this type of process is carried out between sites with latency too great to support synchronous replication of data.
- It may also be used between sites that have a much shorter latency, but where there is a desire to guard against the scenario where logical corruption of data is instantly replicated to other sites via synchronous replication.

Recovery with Design Blueprints

- All Design Blueprints support the recovery of management components through a backup and restore process, where backups can be scheduled automatically.
- Some management components support additional distributed availability models that can serve as a recovery solution under certain failure scenarios (for example VCF Operations can run in a continuous availability model across multiple regions). Other management components that do not support native backups, can be used with standard vSphere supported backup and recovery products.
- To successfully recover workloads in the event of a failure, all described solutions require the development of a recovery plan, addressing the compute resources (including storage) and network connectivity required at each site and the orchestration of moving workloads between the two sites. This plan should be rigorously validated and tested regularly to ensure its accuracy and completeness. The development and validation of the recovery plan is not within the scope of this guide or the listed Design Blueprints.

In addition to the backup and recovery model, which can be leveraged for customer workloads (using a separately available backup and restore solution), there are availability constructs, covered by Design Blueprints, that can address some of your recoverability and Business Continuity / Disaster Recovery (BC/DR) requirements:

- Stretched Clusters: [VCF Fleet with Multiple Sites in a Single Region](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vsphere-only-to-vcf-fleet-upgrade-blueprint.html) and [VCF Fleet with Multiple Sites in a Single Region plus Additional Region(s)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-5.html)Design Blueprints include a stretched cluster model between 2 sites within the same region. This is technically an availability model rather than a recovery model (since any disk writes are instantly replicated to the remote site), however, it can still provide recovery options for certain types of failure scenarios.
- Remote site recovery: [VCF Fleet with Multiple Sites across Multiple Regions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/blueprint-4.html) and Blueprint 5 include designs with multiple locations in different regions. While the scope of the Design Blueprints does not include implementing a data replication and workload recovery solution, the design provides a suitable basis for replicating workload data and orchestrating fail-over of workloads to the recovery site using VMware Live Recovery or a third party product.

## Expansion after Design Blueprint Deployment

The included Design Blueprints are starting points for the initial deployment and cover either a management domain only, or a management domain and the first workload domain. All VCF deployments may be expanded in the following ways and are subject to the limits defined in [VMware Configuration Maximums](https://configmax.broadcom.com/home).

| Type of Expansion | Methods of Expansion |
| --- | --- |
| Resource Expansion | - Add additional hosts to an existing vSphere cluster.    - Provides additional compute capacity (and storage if using vSAN) with automated workload balancing and failover within the scope of the entire cluster. All hosts in a cluster must have the same configuration and access to resources (networking, storage) - Add additional vSphere clusters to an existing VCF domain.    - Provides additional compute capacity (and storage if using vSAN) in an isolated scope from workloads in other clusters. Can have different configuration, networking and/or storage from other clusters. Automated failover and workload balancing does not span across clusters. - Add additional workload domains to an existing VCF Instance.    - Provides separate management & control plane (vCenter) from other workload domains, allowing for different configurations or to support separate locations or access. - Add additional VCF Instances to an existing VCF fleet    - Provides separate management & networking from other instances, allowing for different configurations or to support separate locations, while maintaining a common consumption instance (VCF Operations, VCF Automation and Fleet Management. |
| Availability Expansion | - Add Interconnected Site (in the same region) \* - Add Interconnected Site (in another region) \* |

\* Once a new site has been added, additional steps are required to leverage additional availability by deploying additional or modifying the configuration of existing vSphere clusters to use that site.