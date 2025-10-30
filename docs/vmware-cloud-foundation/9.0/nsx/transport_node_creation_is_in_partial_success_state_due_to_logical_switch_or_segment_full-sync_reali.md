---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/transport-node-fails-with-partial-success-status.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node Creation is in Partial Success State Due to Logical Switch or Segment Full-sync Realization Error
---

# Transport Node Creation is in Partial Success State Due to Logical Switch or Segment Full-sync Realization Error

Transport Node has
partial success status with error
LogicalSwitch full-sync realization query
skipped.

This
issue can occur if uplink profile associated with host has teaming defined with no
active uplinks or if host switch uplinks is down or if failure in creation of
VTEP.

Run transport-node state API to view more
info on failure details using one of the following API command:

- (deprecated) GET
  api/v1/transport-nodes/<uuid>/state
- GET
  api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/state,
  where default values for enforcementpoint-id and site-id is
  default.

1. Edit the uplink profile
   associated with the transport node and ensure active uplinks are selected for
   each teaming profile defined.
2. Verify PNIC link status is up by running CLI on the host: esxcli
   network nic | esxcli network nic get -n <vmnic-name>.
3. If uplink profile is active-active, verify correct number of VTEPS got created
   (rather than just one).

   Run net-vdl2 –l
   |more to verify VTEP count is correct, is assigned a valid IP
   Address, Gateway and state of each VTEP interface is
   UP.