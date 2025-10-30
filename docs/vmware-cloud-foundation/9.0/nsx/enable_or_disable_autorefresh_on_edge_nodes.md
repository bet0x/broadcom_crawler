---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/enable-or-disable-autorefresh-on-edge-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enable or Disable AutoRefresh on Edge Nodes
---

# Enable or Disable AutoRefresh on Edge Nodes

Enable or Disable AutoRefresh on Edge nodes.

Starting with 3.2.4, NSX introduces an AutoRefresh flag that will override any mismatch between the state you desire for an NSX Edge node and the state NSX realizes for that NSX Edge server. NSX will not generate mismatch alarms if desired state and realized state is different. Before NSX 3.2.4, NSX generated mismatch alarms when there was a mismatch between desired and realized state.

If you are upgrading to NSX 3.2.4 or installing NSX 3.2.4, the AutoRefresh feature will be enabled by default.

1. To modify the AutoRefresh feature, run the following API.

   PATCH https://{mp}/policy/api/v1/system-config

   ```
   Sample Payload: 

   {
     "keyValuePairs": [
      {
       "key": "auto_refresh_edge_transport_nodes",
       "value": "true/false"
      }
       ]
   }
   ```

   If you set the value to false, NSX will continue to generate mismatch alarms.

   (NSX Edge nodes deployed from NSX Manager) If you change vSphere parameters from the vSphere Client UI, the desired state will be overriden with the realized state after the next Periodic Refresh task.

   If you edit an NSX Edge node from the NSX Edge UI page, mismatch alarm will be generated if there is a mismatch between desired and realized state.