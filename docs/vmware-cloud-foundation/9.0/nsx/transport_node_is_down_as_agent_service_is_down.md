---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/transport-node-is-down-as-agent-service-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node is Down as Agent Service is Down
---

# Transport Node is Down as Agent Service is Down

The agent service is
Down.

1. To view the host agent status in
   UI, go to HostTransport NodeView Details Monitor tab.
2. To view the status of three host
   agent services (nsx-cfgagent,
   nsx-opsagent, nsx-nestdb) in CLI,
   run /etc/init.d/<service-name> status.
3. To view the status of agents in API, call these APIs:

   (deprecated) GET
   api/v1/transport-nodes/<uuid>/status

   GET
   api/v1/infra/sites/<site-id>/enforcement-points/<enforcementpoint-id>/host-transport-nodes/<host-transport-node-id>/status

   The default value for enforcementpoint-id and
   site-id is default.
4. Restart service that is down by running the following CLI command:
   /etc/init.d/<service-name> start.