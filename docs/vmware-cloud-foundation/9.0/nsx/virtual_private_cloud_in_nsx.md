---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Virtual Private Cloud in NSX
---

# Virtual Private Cloud in NSX

VCF 9.0 provides a consistent networking consumption model that is based on Virtual Private Clouds (VPCs) and Transit Gateways (TGW). This model is natively multi-tenant and can be used not only from NSX, but also from VCF (from vCenter, VCF Automation, and monitored from VCF Operations). It aims to provide a standardised, simple, and powerful Cloud networking experience not only to the network administrators but to all cloud users from VCF.

This cloud networking consumption is built using the following objects:

- **External Connections**: Defines outside connectivity for a Transit Gateway to the datacenter. An external connection can be centralized or distributed.
- **Transit Gateway (TGW)**: Gateway interconnecting VPCs and connecting to outside datacenter through external connections.
- **Virtual Private Cloud (VPC)**: On demand logical networks connected together that can be either advertised (public subnets) or exposed through networking services like External IPs or NAT. For simplicity, VPCs in VCF leverage three profiles:

  - VPC Connectivity Profile: Defines outside connectivity configuration for VPCs such as the Transit Gateway they are connected to, the IP Blocks available for consumption, and if a default outbound NAT is configured
  - VPC Service Profile: Defines the common configurations for services available in the VPC such as DHCP, DHCP Relay, or different subnet profiles.
  - VPC Security Profile: VPC Security profiles, which is the default only, activates on a Gateway Firewall for all VPCs in the project. (Stateless Gateway Firewall is part of VCF entitlement. For Stateful Gateway Firewall, you require a vDefend license.)

The following image provides an overview of the new simplified model.

Simplified VPC model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/fc45ccbe-04e4-4bb8-bad7-7b29730ee2dc.cq5dam.web.1280.1280.jpeg)

**Note:** In addition to the recommended method to create VPCs leveraging the VPC Connectivity Profile, VPC Service Profile and the connection through the Transit Gateways it is supported to have VPCs directly connected to the Tier-0 in user-defined Projects. Those VPCs won’t benefit from multiple enhancements brought up in VCF 9.0 like for instance the ability to create Private - Transit Gateway networks for cross- VPC connections and cannot be configured from vCenter or from VCF Automation.

## Overview of VPCs in the Default Project

VPCs are available by default in NSX within the Default project without the need to create tenants (NSX Project). This provision allows administrators to benefit from VPC independently with VPCs in the default context being configurable from vCenter as well.

VPCs in the Default project

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b72afc21-bd08-46b2-a6a3-e93dfdb1e301.cq5dam.web.1280.1280.jpeg)

Use a multi-tenant platform with the ability to partition networking and security configurations of a single NSX deployment in multiple tenants (NSX Project). Those tenants allow multiple users to configure networking and security and configure Virtual Private Clouds (VPCs). For more information about multi-tenancy, see [NSX Projects](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/nsx-multi-tenancy/nsx-projects.html).

To offer simple on-boarding, a system is created with a Transit Gateway, a default Connectivity Profile, and a default Service Profile in the Default Project. These objects can be configured as part of the workload domain setup deployment and allow consumption of VPCs from NSX or vCenter.

- VPCs created in the Default Project will use the system default overlay transport zone.
- VPCs created in the Default Project will connect to the default Transit Gateway. It is not possible to have VPCs directly connected to Tier-0 in the Default Project.
- VPCs created from vCenter will leverage the default Connectivity and Service profiles but other profiles can be created and used from NSX.

The Default project is the default context for the administrator and as such is not made for multi-tenancy like a user-defined project. You cannot assign a user to the Default project (it is possible to assign a user to a specific set of VPCs only). Additionally, the Default project can access resources such as external connections, external IP blocks, and Edge nodes without having the need to define them as shared resources, which is unlike a user-defined project where you have to define resources that can be shared.

## VPC Consumption from vCenter

As mentioned earlier, in VCF 9.0, VPC offers a VCF-wide consumption framework for networking that is simple and also standardized. VPCs are now available in vCenter for consumption so that a vCenter administrator can have a control over compute, networking, and storage from one interface and at the same time also have the visibility so that the objects are consistent between users and interfaces.

In VCF 9.0, VPCs are visible in the vCenter network inventory and the vCenter administrator can also consume the VPCs, subnets, and external IPs for VPCs of the Default project from there. You can also allow or restrict VPC management in vCenter by configuring the required setting in NSX by navigating to System > Fabric > Compute Manager. For more information about VPC access, see [Add a Compute Manager.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html)

VPC Access Setting

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8aef0b7e-eb30-4537-80fb-01143d4a52cd.cq5dam.web.1280.1280.jpeg)