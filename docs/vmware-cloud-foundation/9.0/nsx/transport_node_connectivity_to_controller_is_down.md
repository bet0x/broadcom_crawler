---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/transport-node-connectivity-to-controller-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node Connectivity to Controller is Down
---

# Transport Node Connectivity to Controller is Down

The issue is seen when a transport
node's connectivity to NSX Manager is
Up but its controller is
Down. When you run get managers,
NSX returns active manager node, while get controllers does not
return any active controller for this transport node, which is in Connected state and
its session state is also Up.

1. Verify transport node is not in
   NSX Maintenance Mode via admin cli get
   maintenance-mode.
2. Call one of the following
   API:
   1. (Deprecated) GET
      API/v1/transport-nodes/<uuid>/status
   2. GET
      api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/status,
      where default values for <site-id> and
      <enforcementpoint-id> is default.
3. Verify FQDN property (used by
   transport nodes to talk with NSX Manager or controller) is set by running API: GET
   /api/v1/configs/management and view value for
   publish\_fqdns.

   If FQDN is set, verify the controller FQDN is reachable and FQDN value is
   being used to by the transport node to talk to controller by first running ICMP
   ping to controller FQDN followed by admin cli get controllers
   to verify controller FQDN value is getting populated correctly.
4. Verify host agent services are running by following host agent troubleshooting
   step mentioned above.
5. Verify
   controller.xml file exists and contains Host transport
   node as its member:
   /etc/vmware/nsx/controller-info.xml.
6. If host is in NSX Maintenance Mode, run admin cli set
   maintenance-mode false or API to take host out of NSX maintenance
   mode: POST
   /api/v1/transport-nodes/<node-id>?action=exit\_maintenance\_mode.
7. If FQDN set and ICMP ping works for controller FQDN then try unsetting and
   setting the FQDN property again by running API PUT
   /api/v1/configs/management with value for
   publish\_fqdns as false and then
   run the API again with value true.
8. Start agent services on the host (if any stopped) by running the CLI command
   etc/init.d/<service-name> start.
9. If controller.xml file has incorrect data, restart
   nsx-proxy service on the host to trigger re-creation of
   file.