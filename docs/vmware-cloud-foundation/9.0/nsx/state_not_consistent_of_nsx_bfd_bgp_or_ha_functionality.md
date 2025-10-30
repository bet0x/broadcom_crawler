---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/state-not-consistent-of-bfd-bgp-or-ha-functionality.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > State Not Consistent of NSX BFD BGP or HA Functionality
---

# State Not Consistent of NSX BFD BGP or HA Functionality

State
Not Consistent of NSX BFD BGP or HA Functionality

Pings are
not consistent. BFD status changes occur. Edge HA failovers occur consistently.

1. Run
   admin cli Get edge-cluster history state.

   The CLI showcases history of edge
   cluster HA transition and reason. The only acceptable state is Active.
   Anything else means edge node is down and no service is able to function.
   For the purpose of identifying events leading to such HA state, focus on the
   timestamp and "Reason" line.
2. Run admin cli get diagnosis topology to view status of all
   attached interfaces and config.