---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/workload-domains-in-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview >   VCF Taxonomy
---

# VCF Taxonomy

The VCF fleet, VCF Instance, and VCF domains logical constructs provide a modular approach to building and managing your private cloud. Each construct has clear scope and components.

For information on designing a VCF platform according to industry recommendations and best practices, see the [VCF Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html) documentation.

VCF Fleet, VCF Instances, and VCF Domains

![VCF Operations can manage both VCF Instances, made of a management domain and several workload domains, and vCenter instances connected to clusters. VCF Automation can work with VCF Instances.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8e4db722-a16d-4a51-ab59-442828d317a4.original.svg)

Constructs of a VCF Private Cloud



| Construct | Description | Components |
| --- | --- | --- |
| VCF Instance | Compute, storage, networking virtual infrastructure that runs business workloads. A VCF Instance consists of VCF domains - a management domain and, optionally, additional workload domains. The first vSphere cluster of a management domain runs the management components for the VCF Instance. | - SDDC Manager - NSX - vCenter - ESX |
| VCF fleet | An environment that is managed by a single set of fleet-level management components - VCF Operations and VCF Automation. A VCF fleet contains one or more VCF Instances and might contain one or more standalone vCenter instances, managed by the VCF Operations instance for the fleet.  The management domain of the first VCF Instance in the VCF fleet hosts the fleet-level management components. | - One or more VCF Instances - One or more standalone vCenter instances - VCF Operations - VCF Automation |
| VCF private cloud | The highest level of management and consumption for the underlying software-defined data center resources. A VCF private cloud can contain one or more VCF fleets. | - One or more VCF fleets |

## VCF Domains

A VCF domain in a VCF Instance consists of the following components:

- One vCenter instance.
- One or more vSphere clusters with vSphere HA and vSphere DRS enabled.
- At least one vSphere Distributed Switches per cluster for system traffic and NSX segments for workloads.
- Dedicated NSX Manager instance, either specifically for the VCF domain or shared between VCF domains, for configuring and implementing software-defined networking.
- Optional. One or more NSX Edge clusters, added after you create the workload domain, that connects the workloads in the workload domain for logical switching, logical dynamic routing, and load balancing.
- One or more shared storage allocations as principal or supplemental storage.

Types of VCF Domains



| VCF Domain Type | Description |
| --- | --- |
| Management domain | The management domain is created during the deployment or convergence process by the VCF Installer . It contains the management components of the VCF Instance and, for the first VCF Instance, VCF Operations and VCF Automation.  In addition to the components that are common for each VCF domain, the management domain includes the SDDC Manager appliance and the fleet management appliance, that adds workflows for infrastructure management automation to the VCF Operations instance for the VCF fleet. |
| Workload domain | You create workload domains in VCF Operations to run consumer workloads.  For the first workload domain in your environment, VCF Operations deploys a vCenter instance and an NSX Manager instance in the management domain. For each additional workload domain, VCF Operations deploys an additional vCenter instance. New workload domains can share the same NSX Manager cluster with an existing workload domain or you can deploy a new NSX Manager cluster. Workload domains cannot use the NSX Manager cluster for the management domain. |