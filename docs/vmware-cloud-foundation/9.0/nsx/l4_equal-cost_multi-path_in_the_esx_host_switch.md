---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/equal-cost-multi-path-in-nsx.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > L4 Equal-Cost Multi-Path in the ESX Host Switch
---

# L4 Equal-Cost Multi-Path in the ESX Host Switch

You can apply Equal-Cost Multi-Path (ECMP) routing on ESX hosts operating in Enhanced Datapath (EDP) and Standard switch modes.

This capability is different from northbound ECMP routing. See Understanding ECMP Routing for scaling ECMP paths on edge nodes.

The ECMP has two modes: L3 ECMP and L4 ECMP.

With L4 ECMP, packet distribution is based on 5-tuple hash (IP address source, IP address destination, IP protocol, layer-4 port source, layer-4 port destination). This feature allows better distribution of traffic across all available Service Routers (SR).

- L4 ECMP requires Enhanced Datapath to be. enabled (EDP Standard and EDP Dedicated are both supported).
- Enabling L4 ECMP will significantly increase total flows

With L3 ECMP, you can apply the ECMP mode either directly to a Transport node or through the Transport Node Profile. Note that the ECMP mode configuration is not supported in the sub-TNP level. The TNP level ECMP mode configuration is inherited in the Sub-TNP profile.

To apply the ECMP mode to a Transport node, run the following API.

PUT https://<nsx-mgr>/policy/api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/

To apply the ECMP mode through a Transport Node Profile, run the following API.

PUT https://<nsx-mgr>/policy/api/v1/infra/host-transport-node-profiles/<transport-node-profile-id>

For more details about the APIs, see the NSX API Guide.

The ECMP 5-tuple feature (hashing on protocol number, source and destination address, and source and destination port) is disabled by default in ESX. You can enable it by setting the parameter lb\_ecmp to true with the following API call.

```
PUT https://<nsx-manager>/policy/api/v1/infra/connectivity-global-config
{
  "lb_ecmp": true,
  ...
}
```

You can see the current lb\_ecmp value with the API GET https://<nsx-manager>/policy/api/v1/infra/connectivity-global-config.

Notes about 5-tuple ECMP:

- When 5-tuple ECMP for ESX is enabled, it will be applied to all ESX hosts. Hosts that do not have ENS enabled might show unexpected behavior.
- Do not enable this feature if you have non-ENS hosts, or a mix of ENS and non-ENS hosts.
- There are appropriate validations to prevent you from enabling L4 ECMP for non-ENS switches.
- When 5-tuple ECMP is enabled, ENS-enabled hosts will consume significantly more flows. When the flow limit is reached, the performance of the host might be impacted.
- Certain topologies, such as a load balancer, where layer 3 does not provide enough path diversity, might benefit more with 5-tuple ECMP enabled.