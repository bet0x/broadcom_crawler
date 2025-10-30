---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/nsx-overview.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview >   NSX Overview
---

# NSX Overview

VMware NSX® enables network connectivity, operations, and scale. It uses a software-defined approach to networking that spans data centers, clouds and application frameworks.

NSX brings networking services closer to the application, whether running on virtual machines (VMs), containers or physical servers. This allows for a cloud operating model where networks can be provisioned and managed independently of the underlying hardware.

NSX replicates the entire network model in software, enabling any network topology—from simple to complex multi-tier networks—to be created and provisioned in seconds. Users can create multiple virtual networks with diverse requirements, leveraging a combination of the services offered over NSX or from a broad ecosystem of third-party integrations to build inherently more agile and secure environments. These services can then be extended to various endpoints within and across clouds.

## Layer 2 - Layer 7 Network Stack and Overlay Services

NSX provides a complete set of logical networking capabilities and services, including logical switching, routing, distributed load balancing, virtual private network (VPN), quality of service (QoS), and monitoring. These services are provisioned in virtual networks. Virtual networks are deployed non-disruptively over the networking hardware and can extend across data centers, private clouds, and container platforms.

- Switching. Enable logical Layer 2 overlay extensions across a routed (Layer 3) fabric within and across data center boundaries.
- Routing. Dynamic routing between virtual networks that is performed in a distributed manner in the hypervisor kernel, and scale-out routing with active-active failover with physical routers. Static routing and dynamic routing protocols are supported, including support for IPv6.
- Virtual routing and forwarding (VRF). Complete data plane isolation among tenants with a separate routing table, network address translation (NAT), and edge firewall support in each VRF on the NSX Tier-0 gateway.
- NSX gateway. Support for bridging between VLANs configured on the physical network and NSX overlay networks, for seamless connectivity between virtual and physical workloads.
- VPN. Site-to-site and unmanaged VPN for cloud gateway services.

## Multi-Site Networking and Disaster Recovery

By using NSX, you can move workloads between racks and data centers by decoupling them from the underlying networks. You can use network overlays and a consistent policy framework across different infrastructures without the need for any changes to the network when moving workloads. This capability supports workload mobility for disaster recovery and workload balancing, ensuring continuous availability and optimal application performance.

- Federation. Centralized policy configuration and enforcement across multiple locations from a single pane of glass, enabling network-wide consistent policy, operational simplicity, and simplified disaster recovery architecture.
- Multi-cloud networking. Enable consistent networking and security across data center sites, and across private cloud boundaries, irrespective of underlying physical topology or cloud platform.

## Network Automation with Declarative APIs

NSX can manage the provisioning, deployment, operations and retirement of networking infrastructure and applications from a central control pane. You can automate infrastructure operations and offload manual tasks with workflows and agile templating using tools such as VCF Automation, Terraform and Ansible. NSX abstracts network services from the underlying hardware, enabling programmable infrastructure through APIs. You can implement policies and workflows to automate tasks like network provisioning, security enforcement, load balancing, streamlining operations, and improving efficiency.

## Self-Service Networking with VPCs and Multi-Tenancy

VPCs provide isolated network environments within a shared infrastructure. You can use Virtual Private Cloud (VPC) constructs to provision and manage network resources to business units or project teams independently, with granular control over networking policies and resource allocation.

By creating projects, you can isolate security and networking objects across tenants in a single NSX deployment. You enable multi-tenant deployment and consumption of NSX services for the provider administrator and the tenants or organizations. The provider administrator can create projects, assign users and groups, and allocate quotas to restrict the configurations available to the tenants.

## NSX Documentation

For more information about the built-in NSX capabilities, see the [NSX documentation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management.html).