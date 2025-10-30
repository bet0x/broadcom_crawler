---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/vtep-maintenance-mode.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > VTEP Maintenance Mode
---

# VTEP Maintenance Mode

You can put a VTEP in maintenance mode provided there is an alternate healthy VTEP on
the host.

- Ensure at least one healthy
  VTEP is present on the host.

1. To put a VTEP in Administrative
   Down mode, call the following API:

   POST
   https://<nsx-mgr>/policy/api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/vteps/actions

   ```
   {
        "type": "TransportNodeVtepAdminStateMgmtRequest",
        "device_name": "vmk10"
        "admin_state_up": <state>
   }
   ```

   where,

   state is false for configuring
   VTEP in Administrative Down mode.

   state is true for configuring VTEP
   in non-Administrative Down mode, which is to bring VTEP back up from
   Administrative Down mode to normal state.

   This operation does not persist after restarting the transport node.
2. Move the VM vNIC of the VTEP that is Administrative Down mode to another
   healthy VTEP.

VM vNIC from VTEP in
Administrative Down mode is moved to another healthy VTEP.