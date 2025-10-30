---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vcf-automation-overview/vsphere-supervisor.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview >   vSphere Supervisor  
---

# vSphere Supervisor

VMware vSphere Supervisor ® is the foundation of VCF consumption and can be enabled during workload domain creation or directly in vCenter.

It transforms vSphere clusters into modern application platforms by embedding a platform-level Kubernetes control plane directly into ESX hosts, exposing a unified declarative API surface. This integration allows end users to provision and manage workloads, including VMs, containers via vSphere Pods, full Kubernetes clusters through VKS, OCI image registries, and data services through a consistent API interface.

vSphere Supervisor maintains enterprise-grade governance, security, and operational consistency through vCenter, VCF Operations, and VCF Automation. Its vSphere Namespaces provide the foundation for multi-tenancy, enabling GitOps-based workflows, and delivering cloud-like self-service in private data centers.

For an overview of vSphere Supervisor concepts and how they apply in VCF Automation, see the [vSphere Supervisor Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration.html) and [Building Cloud Applications](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-cloud-applications.html) documentation.

## Considerations

- Use NSX Virtual Private Clouds (VPC) workload networks

  This configuration is a requirement for using VCF Automation.

  While other workload network types, such as vSphere Distributed Switch and NSX Tier-0/Tier-1 segments, are supported if you plan to directly use vSphere Supervisor for application provisioning, the use of VPC workload networks gives you the ability to provide application provisioning in VCF Automation, keeping the data and infrastructure of organizations isolated.
- Determine if a Single-Zone Supervisor or Multi-Zone Supervisor deployment is required

  In VCF 9.0, a Supervisor deployed in a single-zone configuration cannot be converted to a multi-zone deployment after enablement. You must determine the target deployment model before initiating the Supervisor enablement process.

## Getting Started

- Single-Zone Deployment

  A Single-Zone Supervisor deployment uses a single vSphere cluster to host both workloads and Supervisor management components. It can be enabled either during the [workload domain creation process](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/deploy-a-vi-workload-domain-using-the-sddc-manager-ui.html) or via the [Supervisor Enablement workflow in vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration.html). Additional vSphere Zones can be added after initial enablement. However, these zones are used exclusively for workload placement and do not host Supervisor control plane components.
- Multi-Zone Deployment

  A Multi-Zone Supervisor deployment uses three vSphere clusters, placing each cluster into a vSphere Zone. vSphere Zones are used by workloads and Supervisor management components to deliver high availability and expose each cluster as an independent, consumable availability zone. This configuration provides a resilient, HA-capable platform.

  Additional vSphere Zones can be added after initial enablement. However, these additional zones are available for workload consumption only, not for Supervisor control plane components.
- Single Host

  Also a Single-Zone Supervisor with a single Control Plane VM deployed to a single ESX host, with vSphere HA disabled. While it shares the same characteristics as other single-zone deployments, in this configuration, any host failure results in downtime for the Supervisor Control Plane and potentially for associated workloads.
- Easy Supervisor

  This is a Single-Zone simplified deployment that uses workload networking on top of vSphere Distributed Switch, designed as a fast and simple starting point for proof-of-concept environments and production deployments leveraging vSphere Distributed Switch. For more information, see [Deploying Supervisor with a Simplified Deployment Flow](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration/deploying-easy-supervisor.html).

  An Easy Supervisor deployment consists of:

  - One Supervisor Control Plane VM
  - A shared network for both workload and management traffic
  - No load balancer

  You can deploy only VMs. Additional services, such as VKS, can be enabled by configuring a load balancer after the initial deployment.

  You cannot use this deployment option with VCF Automation.