---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/tier-1-in-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Tier-1 Gateway Configurations in NSX Federation
---

# Tier-1 Gateway Configurations in NSX Federation

With NSX Federation, you can deploy a
tier-1 gateway to provide distributed routing only, or you can configure services on
it.

## Tier-1 Gateway for Distributed Routing Only

You can create a tier-1 gateway in NSX Federation for distributed routing only. This gateway has the same
span as the tier-0 gateway it is linked to. The tier-1 does not use Edge nodes for
routing. All traffic is routed from host transport nodes to the tier-0 gateway.
However, to enable cross-location forwarding, the tier-1 allocates two Edge nodes
from the Edge cluster configured on the linked tier-0 to use for that traffic.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a92e2087-ee3c-4898-b7a2-3847c223d446.original.png)

## Tier-1 Gateway with Services or Custom Span

You configure the tier-1 gateway with
Edge clusters if you need one of the following configurations:

- You want to run services on the
  tier-1 gateway.
- You want to deploy a tier-1
  gateway that has a different span than the linked tier-0 gateway.

  You can remove locations,
  but you cannot add locations that are not already included the span of
  the tier-0 gateway.

You select one of the locations to be the primary location. All other locations are
secondary. The HA mode for the tier-1 gateway is Active Standby. All traffic passing
through this tier-1 gateway passes through the active edge node in the primary
location.

If both the tier-1 gateway and the linked
tier-0 gateway have primary and secondary locations, configure the same location to
be primary for both gateways to reduce cross-location traffic.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/eb84f9ac-45f2-4827-a1d8-624d02472a8b.original.png)