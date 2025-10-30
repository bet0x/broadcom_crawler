---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-an-edge-bridge-profile/edge-bridge-does-not-get-created.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge bridge does not get created
---

# NSX Edge bridge does not get created

NSX Edge bridge does not get created.

From the NSX Edge node, when you run get bridge
summary, the output does not show the bridge is created.

VLAN ID or uplink conflict.

1. Verify that VLAN ID used for
   bridging on a specific uplink is not being used by another VLAN segment for
   configuration of any other feature.
2. Verify all NSX Edge transport
   node member of NSX Edge cluster
   configured with bridging belong to same overlay and VLAN transport zone.
3. Verify the bridge is not configured with multiple VLAN uplinks in a failover
   teaming policy.