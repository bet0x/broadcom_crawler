---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/groups-created-for-server-pools-and-virtual-servers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Groups Created for Server Pools and Virtual Servers
---

# Groups Created for Server Pools and Virtual Servers

NSX Manager automatically creates groups
for load balancer server pools and VIP ports.

Load Balancer created groups are visible under Inventory Groups.

Server pool groups are created with the name NLB.PoolLB.Pool\_NameLB\_Name with group member IP addresses assigned:

- Pool configured with no LB-SNAT (transparent): 0.0.0.0/0
- Pool configured with LB-SNAT Automap: T1-Uplink IP 100.64.x.y and
  T1-ServiceInterface IP
- Pool configured with LB-SNAT IP-Pool: LB-SNAT IP-Pool

VIP Groups are created with the name NLB.VIP.virtual server name
and the VIP group member IP addresses are VIP IP@.

For server pool groups, you can create an allow traffic distributed firewall rule from
the load balancer ( NLB.PoolLB. Pool\_NameLB\_Name). For Tier-1 gateway firewall, you can create an allow
traffic from clients to LB VIP NLB.VIP.virtual server name.