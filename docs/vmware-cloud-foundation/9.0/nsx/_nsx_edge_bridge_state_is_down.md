---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-an-edge-bridge-profile/edge-bridge-state-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge bridge state is down
---

# NSX Edge bridge state is down

NSX Edge bridge state is down.

NSX Edge bridge state has gone down.

Failure of VLAN uplink or failure of BFD
tunnel between two NSX Edge nodes
that are part of the bridge.

1. SSH to NSX Edge as admin.
2. Run get bridge summary CLI to view existing bridges
3. Run cli get bridge name <name> or get bridge
   <uuid> or get bridge vlan <vlan-id> to
   view edge device state status.
4. Run cli get bridge mac-sync-table to verify overlay segment
   mac is learned successfully.
5. run cli get edge-cluster-status to verify edge status,
   admin-state, health-check for all upink interfaces is up with no issues.
6. Verify NSX Edge bridge state is
   now active.