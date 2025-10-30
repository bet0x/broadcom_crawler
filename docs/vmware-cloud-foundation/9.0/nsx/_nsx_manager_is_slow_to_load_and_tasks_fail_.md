---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/nsx-manager-is-slow-to-load-and-tasks-fail-with-message-server-is-overloaded.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Manager is Slow To Load And Tasks Fail 
---

# NSX Manager is Slow To Load And Tasks Fail

NSX Manager is slow to load and tasks fail with
message server is overloaded or too many
requests.

This
issue occurs upon hitting the nsx manager incoming API rate limit. The solution is to
either limit the number of incoming API requests to NSX Manager or modify the default values for Client API rate limit or
Client API concurrency limit or Global API concurrently limit from API or CLI.

1. To view current default values,
   run get cluster api-service as admin or GET API
   /api/v1/cluster/api-service.
2. To set a new API rate value, run
   set cluster api-service client-api-rate-limit or
   PUT /api/v1/cluster/api-service with updated
   values.
3. To view logs of incoming API requests, go to
   /var/log/proxy directory,
   reverse-proxy.log.

   Try to avoid configuring
   the API rate limits. Instead, design your API client to gracefully deal with
   situations where limits are exceeded.