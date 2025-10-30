---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/edge-node-status-down-as-controller-is-unavailable.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Edge node status is Down As Controller Is Unavailable
---

# NSX Edge node status is Down As Controller Is Unavailable

NSX
Edge node status is Down due to controller unavailability.

NSX Edge
node status is Down with controller connectivity status ‘unavailable’ because agent
service down.

The
get manager and get controller commands
will return correct values but GET
api/v1/transport-nodes/<tn-uuid>/status shows agent-status is
Down. The error is due to the service
nsx-opsagent is not running.

1. Run
   admin cli get status nsx-opsagent to verify the service
   status.
2. Start or restart the service by running admin cli, restart | start
   service nsx-opsagent