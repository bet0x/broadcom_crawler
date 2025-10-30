---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/transport-node-failed-as-named-teaming-defined-with-no-active-uplink.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node Failed as Named Teaming Defined with No Active Uplink
---

# Transport Node Failed as Named Teaming Defined with No Active Uplink

Transport
Node configuration has failed due to named teaming defined
with no active uplink.

This
issue can occur if uplink profile associated with transport-node has named teaming
defined with no active uplinks.

1. Make
   sure active uplinks are selected for any teaming policies defined.
2. Edit the uplink profile associated with the transport node by either removing
   the teaming with no active uplink or assigning a valid uplink to teaming policy
   defined.