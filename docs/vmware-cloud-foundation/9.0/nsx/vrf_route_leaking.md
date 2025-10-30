---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/vrf-route-leaking.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > VRF Route Leaking
---

# VRF Route Leaking

By default, the data plane traffic between VRF instances is isolated in NSX. By configuring VRF route leaking, traffic can be exchanged between VRF instances. Static routes must be configured on the tier-0 VRF instances to allow traffic to be exchanged.

Two topology options are supported in NSX:

- Local VRF-to-VRF route leaking
- Northbound VRF leaking

Multi-tier routing architecture is required for traffic to be exchanged in a VRF leaking topology since static routes pointing to tier-1 distributed router (DR) uplinks are required.

## Local VRF-to-VRF Route Leaking

Tier-1 DR IP addresses can be checked by using both the Edge node CLI or Network Topology in NSX Manager.

The diagram depicts a sample topology for the local VRF-to-VRF route leaking option.

![Tier-0 VRF A and Tier-0 VRF B are configured with static routes which allows traffic to be exchanged between them.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/14deaff8-59fe-4d2c-a63d-5f87a9d40b87.original.png)

The configuration workflow for the sample topology is as follows:

| Tier-0 VRF A Configuration Workflow |
| --- |
| 1. Select NetworkingTier-0 Gateway. 2. For tier-0 VRF A, click the menu icon (three dots) and select Edit. 3. Click Routing. 4. In the Static Routes field, click SetAdd Static Route and configure the static route:    1. Enter a name for the static route.    2. In the Network field, enter a prefix. For example, 172.16.20.0/24 5. In the Next Hops column, click SetSet Next Hops and define the next hops for the static route:    1. Enter the IP address of the tier-1 DR uplink in VRF B. For example, 100.64.90.1  Tier-1 DR IP addresses can be checked by using both the Edge node CLI or Network Topology in NSX Manager.    2. Enter the Admin Distance of 1.    3. Enter the scope. For example, VRF-B |

| Tier-0 VRF B Configuration Workflow |
| --- |
| 1. Select NetworkingTier-0 Gateway. 2. For tier-0 VRF B, click the menu icon (three dots) and select Edit. 3. Click Routing. 4. In the Static Routes field, click SetAdd Static Route and configure the static route:    1. Enter a name for the static route.    2. In the Network field, enter a prefix. For example, 172.16.10.0/24 5. In the Next Hops column, click SetSet Next Hops and define the next hops for the static route:    1. Enter the IP address of the tier-1 DR uplink in VRF A. For example, 100.64.80.1  Tier-1 DR IP addresses can be checked by using both the Edge node CLI or Network Topology in NSX Manager.    2. Enter the Admin Distance of 1.    3. Enter the scope. For example, VRF-A |

## Northbound VRF Route Leaking

For this topology option, the northbound static route should have a next hop as an external IP address reachable in the destination VRF routing table. It is not recommended to point static routes directly to connected IP address uplinks as the static route would fail if an outage occurs on that link or neighbor. A loopback or virtual IP address host route (/32) can be advertised in the network in the destination VRF. Since the host route is advertised by both top of rack switches, two ECMP routes are installed in the tier-0 VRF. A return static route should be created in the destination VRF pointing to the tier-1 DR uplink IP address as the next hop.

The following diagram depicts a sample topology for the northbound VRF route leaking option.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7fa2bfba-3699-46c9-9274-33ff10acd880.original.png)

The configuration workflow for the sample topology is as follows:

| Tier-0 VRF A Configuration Workflow |
| --- |
| 1. Select NetworkingTier-0 Gateway. 2. For tier-0 VRF A, click the menu icon (three dots) and select Edit. 3. Click Routing. 4. In the Static Routes field, click SetAdd Static Route and configure the static route:    1. Enter a name for the static route.    2. In the Network field, enter a prefix. For example, 10.10.10.0/24 5. In the Next Hops column, click SetSet Next Hops and define the next hops for the static route:    1. Enter the IP address of the tier-1 DR uplink in VRF B. For example, 192.168.1.1    2. Enter the Admin Distance of 1.    3. Enter the scope. For example, VRF-B |

| Tier-0 VRF B Configuration Workflow |
| --- |
| 1. Select NetworkingTier-0 Gateway. 2. For tier-0 VRF B, click the menu icon (three dots) and select Edit. 3. Click Routing. 4. In the Static Routes field, click SetAdd Static Route and configure the static route:    1. Enter a name for the static route.    2. In the Network field, enter a prefix. For example, 172.16.10.0/24 5. In the Next Hops column, click SetSet Next Hops and define the next hops for the static route:    1. Enter the IP address of the tier-1 DR uplink in VRF A. For example, 100.64.80.1    2. Enter the Admin Distance of 1.    3. Enter the scope. For example, VRF-A |