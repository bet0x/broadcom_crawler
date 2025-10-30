---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/nsx-edge-transport-node-connectivity-to-controller-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Edge Transport Node Connectivity to Controller is Down
---

# NSX Edge Transport Node Connectivity to Controller is Down

NSX
Edge Transport Node connectivity to controller is down.

This
issue is seen when connectivity to manager is up but connectivity to controller is
down. Admin cmd ‘get managers’ returns active manager node while cmd 'get
controllers’ does not return any active controller for this transport node with
status connected and/or session-state UP.

1. Verify
   transport node is not in NSX Maintenance Mode using admin cli get
   maintenance-mode or run the API, GET
   api/v1/transport-nodes/<tn-uuid>| state | status.
2. Verify if FQDN property (used by transport-nodes to talk with NSX
   Manager/Controller) is set by running API, GET
   /api/v1/configs/management and view value for
   publish\_FQDNS.
3. If FQDN set, verify the controller FQDN is reachable and FQDN value is being
   used to by TN to talk to controller by first running ICMP ping to controller
   FQDN followed by admin cli get controllers to verify
   controller FQDN value is getting populated correctly.
4. Verify node agent services are running by following node agent troubleshooting
   step outlined before.
5. If edge transport node is in NSX Maintenance Mode, run admin cli set
   maintenance-mode false or API POST
   /api/v1/transport-nodes/<node-id>?action=exit\_maintenance\_mode
   to take node out of NSX Maintenance Mode
6. If FQDN is set and ICMP ping works for controller FQDN then try unsetting and
   setting the FQDN property again by running API PUT
   /api/v1/configs/management with value for
   publish\_fqdns false followed by true.
7. Verify that agent services are
   running on the NSX Edge node by running get edge diagnosis
   config. If any service shows as failed, restart by running admin
   cli start service <service-name> or root cli
   etc/init.d/<service-name> start.