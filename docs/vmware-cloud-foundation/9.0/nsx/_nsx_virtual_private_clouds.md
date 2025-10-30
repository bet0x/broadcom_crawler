---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Virtual Private Clouds
---

# NSX Virtual Private Clouds

NSX Virtual Private Clouds (VPCs) is an abstraction layer that simplifies
setting up self-contained virtual private cloud networks within an NSX project to consume networking and security services
in a self-service consumption model.

NSX VPCs represent an additional layer of multi-tenancy within a
project. It provides a simplified consumption model of networking and security
services, which is aligned to the experience that you would have in a public cloud
environment.

An NSX VPC hides the complexity of the underlying NSX infrastructure, network topology, networking
objects, and IP address management from the application owners and offers them a
self-service consumption model to run applications in their own private space.

Application owners or DevOps engineers do not
need to know about the underlying NSX
infrastructure for running applications within their isolated space. They can add
subnets (networks) inside the NSX VPC that
is assigned to them, and configure security policies to meet their application
requirements without having any dependency on the Enterprise Admin.

NSX VPCs are optional under a project. The following diagram shows
two projects in the org. Project 1 contains NSX VPCs whereas Project 2 contains no NSX VPCs.

![This diagram is explained in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9401fafb-aaf4-40d3-8aca-360caad98ffe.original.png)

The following diagram shows a sample logical
view of an NSX VPC inside project 1. Both
projects 1 and 2 are connected to the same tier-0 or tier-0 VRF gateway.

![This diagram is explained in the surrounding text.](/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/nsx/images/vpc-concept-2.png)

The NSX VPC inside project 1 contains three subnets:

- App subnet (private)
- Web subnet (public)
- Test subnet (isolated)

Each NSX VPC within a project represents an independent routing domain. Subnets
within an NSX VPC represent independent
layer 2 broadcast domains. Subnets are realized as overlay segments in the default
transport zone of the project. Users that are assigned the VPC Admin role or the Network
Admin role in the NSX VPC can add subnets in
the NSX VPC. In addition to these two roles,
an NSX VPC can also have the following user
roles, but with their scope confined to the NSX VPC:

- Security Admin
- Network Operator
- Security Operator

When an NSX VPC is created, the Project Admin specifies the external IP blocks and
the private IP blocks to use for creating the subnets in the VPC. The supported subnet
access modes are Private, Public, and Isolated. To learn more about subnet access modes,
see the Access Modes for
NSX VPC Subnets section later
in this documentation.

When an NSX VPC is created successfully, the system implicitly creates a
gateway. However, this implicit gateway is exposed to the Project Admin in a
read-only mode and is not visible to the NSX VPC users.

The lifecycle of this implicit gateway is
managed by the system. When an NSX VPC
is deleted, the implicit gateway is deleted automatically.

In the NSX Policy data model, NSX VPC objects are created under projects at the following path:

```
/orgs/default/projects/<project_id>/vpcs/<vpc-id>
```

The realized implicit gateway is at the
following path:

```
/orgs/default/projects/<project_id>/infra/tier-1s/
```

## Example of an NSX VPC

Let us assume that your organization has
created a project named "Sales" in its NSX environment. The objective of the Project Admin is to provide
an isolated networking and security environment for the application developers of
the "Order management" and "Analytics" applications in the Sales business unit.

The application developers require an
ability to provision networks and configure security policies for these two
applications in a self-service consumption model and without any dependency on the
Enterprise Admin or the Project Admin.

To achieve this objective, the Project
Admin can create two NSX VPCs inside
the "Sales" project and assign these NSX VPCs to the application developers.

For example:

| VPC Name | VPC Users | IP Address Blocks |
| --- | --- | --- |
| Order Management | Jim: VPC Admin  Bob: Network Operator  Carol: Security Operator | Private IPv4 block: 172.16.0.0/24  External IPv4 block: 192.168.1.0/24 |
| Analytics | Mike: VPC Admin  Steve: Network Operator  Maria: Security Operator | Private IPv4 block: 172.18.0.0/24  External IPv4 block: 192.168.1.0/24 |

After roles are assigned to the
NSX VPC users, these users can add
subnets inside the NSX VPC and configure
security policies for these workloads. The security policies impact only the
workloads within the NSX VPC and not
outside the NSX VPC.

For example, the following diagram shows
three subnets named as Dev, Test, and Production inside the Order Management
NSX VPC, and three subnets named as
App, Web, and DB in the Analytics NSX VPC. Workload VMs are attached to all the subnets. The
NSX VPCs are attached to the same
tier-0 or tier-0 VRF gateway of the Sales project.

![This diagram is explained in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/71d08b73-dbb7-45aa-b51b-d976389f3fce.original.png)

## High-Level NSX VPC Workflow

At a high level, the NSX VPC workflow is as follows:

1. Project Admin: Adds
   NSX VPC inside a project and
   defines basic NSX VPC settings,
   such as IP assignment, DHCP configuration, edge cluster, and so on.
2. Project Admin: Assigns roles to
   users in the NSX VPC.
3. Project Admin: Defines quota or
   limits for the number of objects that users can create within the
   NSX VPC.
4. VPC Admin or Network Admin:
   Adds subnets in the NSX VPC.
   Connects workloads to these subnets based on business requirements.
5. VPC Admin or Security Admin:
   Adds security policies in the NSX VPC to meet the security requirements of the workloads
   that are connected to the subnets in the VPC.

## Access Modes for NSX VPC Subnets

The supported access modes for subnets in
an NSX VPC are:

Private
:   A private subnet is
    accessible only within the NSX VPC. Workloads that are attached to a private
    subnet can communicate with workloads on other private or public
    subnets within the same NSX VPC.

    If the IP assignment for
    the private subnet is set to "automatic", the subnet IP blocks
    (subnet CIDRs) are automatically assigned from the private IPv4
    blocks that are assigned to the NSX VPC. If the IP assignment for the private subnet
    is set to "manual", the VPC admin can manually assign the subnet
    CIDR.

    The CIDR of a VPC subnet
    cannot overlap with the CIDR of another VPC subnet in the same
    NSX VPC. However,
    the subnet IPs can overlap with the subnet in another NSX VPC. It is possible to
    accomplish this configuration by allocating different private IP
    blocks with the same IP ranges to different NSX
    VPCs.

    Multiple NSX VPCs in a project can share
    the same private IPv4 block. In this case, the private subnets will
    be unique across the different VPCs that share the same private IP
    block.

    If the Default
    Outbound NAT option is turned on for the
    NSX VPC, a default
    SNAT rule is created for the NSX VPC to allow traffic from the workloads on the
    private subnets to be routed outside the NSX VPC. On similar lines, if
    this option is turned off, the traffic from the private subnet
    cannot be routed outside the NSX VPC.

Public
:   A public subnet is
    accessible from outside the NSX VPC. This subnet is auto-advertised up to the
    tier-0 gateway of the project, and it enjoys direct external
    connectivity, by default. In other words, the IPv4 addresses in the
    public subnets are reachable both from the project and outside the
    project.

    If the IP assignment for
    the public subnet is set to "automatic", the subnet IP blocks
    (subnet CIDRs) are automatically assigned from the external IPv4
    blocks that are specified for the project. If the IP assignment for
    the public subnet is set to "manual", the VPC admin can manually
    assign the subnet CIDR.

Isolated
:   An isolated subnet is not
    internally connected to the realized implicit gateway. Workloads on
    an isolated subnet can communicate with each other but cannot
    communicate with workloads on private or public subnets within the
    same NSX VPC. In
    addition, packets from isolated subnets cannot go outside the
    NSX VPC.

    A VPC Admin must manually
    specify the CIDR address of an isolated subnet.