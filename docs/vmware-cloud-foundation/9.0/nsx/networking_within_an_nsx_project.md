---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/networking-within-an-nsx-project.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Networking Within an NSX Project
---

# Networking Within an NSX Project

A subset of NSX networking features are currently supported in
projects.

The following screen capture shows the features that are available on the
Networking page in a project.

![Networking page in a project.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8ef347b9-4718-42bb-a37f-845dd6eb1f2a.original.png)

Tier-0 gateways and edge clusters in the
system are allocated to projects. These objects are owned by the Enterprise Admin in the
default space.

## Managing Tier-1 Gateways in a Project

- Tier-1 gateways and segments inside
  a project can connect to tier-0 gateways that are assigned to the project.
- Tier-1 gateways and DHCP are
  provisioned on edge clusters that are assigned to the project.
- Tier-1 gateways that are
  provisioned on the edge clusters will benefit from the configuration that an
  Enterprise Admin has done on the edge cluster, for example, configuration of the
  failure domain.
- Tier-1 service interfaces can connect to networks that are created within the
  projects and to networks that are shared with the projects.
- Features such as NAT, Gateway
  Firewall, and VPN can be configured on the tier-1 gateways that are created
  inside a project. Tier-1 gateways that are configured in the default space
  cannot be allocated to projects.

## Managing Networks in a Project

- Currently, overlay segments are supported in projects.
- Segments inside a project are realized in the project default transport zone.
  The project default transport zone is automatically assigned when a project is
  created and it is the same as the default transport zone of the
  system.
- DHCP profiles can be created on edge clusters that are allocated to the
  project.
- Segments can use the DHCP profiles that are shared with the project.
- To provide distributed security to VMs inside a project, these VMs must be
  connected to the segments inside a project.
- Private IPv4 blocks that are
  created in a project can be used for adding private subnets in the NSX VPCs within the project.