---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/unable-to-reach-transport-node-due-to-incorrect-credentials.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Unable to Reach Transport Node Due to Incorrect Credentials As Host is in Orphaned State
---

# Unable to Reach Transport Node Due to Incorrect Credentials As Host is in Orphaned State

- Host is not reachable. Cannot
  complete login due to an incorrect username or password.
- The Transport Node Apply Task fails
  with error Node already exists.
- Host is in orphaned state.

This
issue occurs due to a race condition under heavy traffic load. Run the API
(deprecated) GET /api/v1/transport-nodes/<TN-UUID>/status
or GET
api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/state
| status, where default values for
enforcementpoint-id and site-id is
default to review the transport node shows
transport nodes status unknown and node deployment status shows as
Failed.

All these cases occur for host TN that
did not get cleaned correctly upon initiation of NSX removal task therefore is still
registered with NSX Manager.

In this case, the GET transport node api
and GET transport node status api will fail but GET transport node state api works
and will show failure message Failed to uninstall the software on
host....

1. To fix the existence of stale entry, you must forcefully remove NSX from the
   host and also run the following api to delete stale host entries in the
   setup.
   1. (NSX Manager UI) On Hosts page, select the
      Force Delete option and click
      Remove NSX.
   2. (API) To forcefully delete NSX, run the API,
      https://{{MPIP}}/api/v1/transport-nodes/<Transport-Node-UUID>?force=true&unprepare\_host=false.
   3. (API) To remove stale entries, run the API,
      https://{{nsx-mgr-ip}}/api/v1/transport-nodes?action=clean\_stale\_entries.