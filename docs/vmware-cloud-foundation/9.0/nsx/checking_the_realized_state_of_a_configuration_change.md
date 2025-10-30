---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/checking-the-realized-state-of-a-configuration-change.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Checking the Realized State of a Configuration Change
---

# Checking the Realized State of a Configuration Change

When you make a
configuration change,
NSX Manager
typically sends a request to another component to implement the change. For
some layer 3 entities, if you make the configuration change using the API, you
can track the status of the request to see if the change is successfully
implemented.

The configuration change that
you initiate is called the desired state. The result of implementing the change
is called the realized state. If
NSX Manager
implements the change successfully, the realized state will be the same as the
desired state. If there is an error, the realized state will not be the same as
the desired state.

For some layer 3 entities, when
you call an API to make a configuration change, the response will include the
parameter
request\_id. You can
use the parameters
request\_id and the
entity\_id to make an
API call to find out the status of the request.

This feature supports the following entities and APIs:

```
EdgeCluster
    POST /edge-clusters
    PUT /edge-clusters/<edge-cluster-id>
    DELETE /edge-clusters/<edge-cluster-id>
    POST /edge-clusters/<edge-cluster-id>?action=replace_transport_node

LogicalRouter
    POST /logical-routers
    PUT /logical-routers/<logical-router-id>
    DELETE /logical-routers/<logical-router-id>
    POST /logical-routers/<logical-router-id>?action=reprocess
    POST /logical-routers/<logical-router-id>?action=reallocate

LogicalRouterPort
    POST /logical-router-ports
    PUT /logical-router-ports/<logical-router-port-id>
    DELETE /logical-router-ports/<logical-router-port-id>

StaticRoute
    POST /logical-routers/<logical-router-id>/routing/static-routes
    PUT /logical-routers/<logical-router-id>/routing/static-routes/<static-route-id>
    DELETE /logical-routers/<logical-router-id>/routing/static-routes/<static-route-id>

BGPConfig
    PUT /logical-routers/<logical-router-id>/routing/bgp

BgpNeighbor
    POST /logical-routers/<logical-router-id>/routing/bgp/neighbors
    PUT /logical-routers/<logical-router-id>/routing/bgp/neighbors/<bgp-neighbor-id>
    DELETE /logical-routers/<logical-router-id>/routing/bgp/neighbors/<bgp-neighbor-id>
    POST /logical-routers/<logical-router-id>/routing/bgp/neighbors/<bgp-neighbor-id>

BGPCommunityList
    POST /logical-routers/<logical-router-id>/routing/bgp/community-lists
    PUT /logical-routers/<logical-router-id>/routing/bgp/community-lists/<community-list-id>
    DELETE /logical-routers/<logical-router-id>/routing/bgp/community-lists/<community-list-id>

AdvertisementConfig
    PUT /logical-routers/<logical-router-id>/routing/advertisement

AdvertiseRouteList
    PUT /logical-routers/<logical-router-id>/routing/advertisement/rules

NatRule
    POST /logical-routers/<logical-router-id>/nat/rules
    PUT /logical-routers/<logical-router-id>/nat/rules/<rule-id>
    DELETE /logical-routers/<logical-router-id>/nat/rules/<rule-id>

DhcpRelayService
    POST /dhcp/relays
    PUT /dhcp/relays/<relay-id>
    DELETE /dhcp/relays/<relay-id>

DhcpRelayProfile
    POST /dhcp/relay-profiles
    PUT /dhcp/relay-profiles/<relay-profile-id>
    DELETE /dhcp/relay-profiles/<relay-profile-id>

StaticHopBfdPeer
    POST /logical-routers/<logical-router-id>/routing/static-routes/bfd-peers
    PUT /logical-routers/<logical-router-id>/routing/static-routes/bfd-peers/<bfd-peers-id>
    DELETE /logical-routers/<logical-router-id>/routing/static-routes/bfd-peers/<bfd-peers-id>

IPPrefixList
    POST /logical-routers/<logical-router-id>/routing/ip-prefix-lists
    PUT /logical-routers/<logical-router-id>/routing/ip-prefix-lists/<ip-prefix-list-id>
    DELETE /logical-routers/<logical-router-id>/routing/ip-prefix-lists/<ip-prefix-list-id>

RouteMap
    POST /logical-routers/<logical-router-id>/routing/route-maps
    PUT /logical-routers/<logical-router-id>/routing/route-maps/<route-map-id>
    DELETE /logical-routers/<logical-router-id>/routing/route-maps/<route-map-id>

RedistributionConfig
    PUT /logical-routers/<logical-router-id>/routing/redistribution
RedistributionRuleList
    PUT /logical-routers/<logical-router-id>/routing/redistribution/rules

BfdConfig
    PUT /logical-routers/<logical-router-id>/routing/bfd-config

MplsConfig
    PUT /logical-routers/<logical-router-id>/routing/mpls

RoutingGlobalConfig
    PUT /logical-routers/<logical-router-id>/routing

IPSecVPNIKEProfile
    POST /vpn/ipsec/ike-profiles
    PUT /vpn/ipsec/ike-profiles/<ike-profile-id>
    DELETE /vpn/ipsec/ike-profiles/<ike-profile-id>

IPSecVPNDPDProfile
    POST /vpn/ipsec/dpd-profiles
    PUT /vpn/ipsec/dpd-profiles/<dpd-profile-id>
    DELETE /vpn/ipsec/dpd-profiles/<dpd-profile-id>

IPSecVPNTunnelProfile
    POST /vpn/ipsec/tunnel-profiles
    PUT /vpn/ipsec/tunnel-profiles/<tunnel-profile-id>
    DELETE /vpn/ipsec/tunnel-profiles/<tunnel-profile-id>

IPSecVPNLocalEndpoint
    POST /vpn/ipsec/local-endpoints
    PUT /vpn/ipsec/local-endpoints/<local-endpoint-id>
    DELETE /vpn/ipsec/local-endpoints/<local-endpoint-id>

IPSecVPNPeerEndpoint
    POST /vpn/ipsec/peer-endpoints
    PUT /vpn/ipsec/peer-endpoints/<peer-endpoint-id>
    DELETE /vpn/ipsec/peer-endpoints/<peer-endpoint-id>

IPSecVPNService
    POST /vpn/ipsec/services
    PUT /vpn/ipsec/services/<service-id>
    DELETE /vpn/ipsec/services/<service-id>

IPSecVPNSession
    POST /vpn/ipsec/sessions
    PUT /vpn/ipsec/sessions/<session-id>
    DELETE /vpn/ipsec/sessions/<session-id>

DhcpServer	
    POST /dhcp/servers
    PUT /dhcp/servers/<server-id>
    DELETE /dhcp/servers/<server-id>

DhcpStaticBinding	
    POST /dhcp/servers/static-bindings
    PUT /dhcp/servers/<server-id>/static-bindings/<binding-id>
    DELETE /dhcp/servers/<server-id>/static-bindings/<binding-id>

DhcpIpPool	
    POST /dhcp/servers/ip-pools
    PUT /dhcp/servers/<server-id>/ip-pools/<pool-id>
    DELETE /dhcp/servers/<server-id>/ip-pools/<pool-id>

DnsForwarder	
    POST /dns/forwarders
    PUT /dns/forwarders/<forwarder-id>
    DELETE /dns/forwarders/<forwarder-id>
```

You can call the following APIs to get the realized
states:

```
EdgeCluster
Request - GET /edge-clusters/<edge-cluster-id>/state?request_id=<request-id>
Response - An instance of EdgeClusterStateDto which will inherit ConfigurationState. If the edge cluster is deleted then the state will be unknown and it will return the common entity not found error.

LogicalRouter / All L3 Entites - All L3 entities can use this API to get realization state
Request - GET /logical-routers/<logical-router-id>/state?request_id=<request-id>
Response - An instance of LogicalRouterStateDto which will inherit ConfigurationState. Delete operation of any entity other than logical router can be covered by getting the state of logical router but if the logical router itself is deleted then the state will be unknown and it will return the common entity not found error.

LogicalServiceRouterCluster - All L3 entities which are the part of services can use this API to get the realization state
Request - GET /logical-routers/<logical-router-id>/service-cluster/state?request_id=<request-id>
Response - An instance of LogicalServiceRouterClusterState which will inherit ConfigurationState. 

LogicalRouterPort / DhcpRelayService / DhcpRelayProfile
Request - GET /logical-router-ports/<logical-router-port-id>/state?request_id=<request-id>
Response - An instance of LogicalRouterPortStateDto which will inherit ConfigurationState. 

IPSecVPNIKEProfile / IPSecVPNDPDProfile / IPSecVPNTunnelProfile / IPSecVPNLocalEndpoint / IPSecVPNPeerEndpoint / IPSecVPNService / IPSecVPNSession
Request - GET /vpn/ipsec/sessions/<session-id>/state?request_id=<request-id>
Response - An instance of IPSecVPNSessionStateDto which will inherit ConfigurationState. If the session is deleted then the state will be unknown and it will return the common entity not found error. When IPSecVPNService is disabled, IKE itself is down and it does not respond. It will return unknown state in such a case.

DhcpServer
Request - GET /dhcp/servers/<server-id>/state?request_id=<request-id>
Response - An instance of ConfigurationState.

DhcpStaticBinding
Request - GET /dhcp/servers/<server-id>/static-bindings/<binding-id>/state?request_id=<request-id>
Response - An instance of ConfigurationState.

DhcpIpPool
Request - GET /dhcp/servers/<server-id>/ip-pools/<pool-id>/state?request_id=<request-id>
Response - An instance of ConfigurationState.

DnsForwarder
Request - GET /dns/forwarders/<forwarder-id>/state?request_id=<request-id>
Response - An instance of ConfigurationState.
```

For more information about the APIs, see the NSX API Guide.