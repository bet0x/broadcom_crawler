---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/features-available-for-consumption-under-nsx-vpcs.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Features Available for Consumption Under NSX VPCs 
---

# Features Available for Consumption Under NSX VPCs

NSX VPC exposes a simplified set of
features to allow application owners or DevOps engineers to consume NSX networking and security objects in a self-service
consumption model.

The following objects are assigned by the
Project Admin during an NSX VPC creation and
are available for consumption in the VPC.

- Tier-0 or VRF gateway
- Edge cluster
- IP blocks (private, external)
- Various profiles (for example, QoS
  profile, IP discovery profile, and many more)
- IPAM strategy (DHCP, external,
  none)

A Project Admin can optionally enable an
NSX VPC for Avi Load Balancer.

NSX VPC users can create or modify the following objects in their private
VPC space:

Network connectivity
:   - Subnets (public,
      private, isolated)
    - Static routes

Network services
:   - NAT rules (SNAT, DNAT,
      reflexive)

Security services
:   - East-west firewall
      rules
      (L4/L7)
    - North-south firewall
      rules (L4 only)

Inventory objects
:   - Groups (static and
      dynamic memberships)

      To view the list of
      NSX objects
      that are supported for adding statically or dynamically to a
      group definition, see [Groups in an NSX VPC](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/groups-in-an-nsx-vpc.html).