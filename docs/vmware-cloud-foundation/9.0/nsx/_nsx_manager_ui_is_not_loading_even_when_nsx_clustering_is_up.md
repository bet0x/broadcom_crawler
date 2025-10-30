---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/nsx-manager-ui-is-not-loading-even-when-nsx-clustering-is-up.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Manager UI is not loading even when NSX Clustering is up
---

# NSX Manager UI is not loading even when NSX Clustering is up

NSX Manager is slow to load and tasks fail with
message server is overloaded or too many
requests.

1. SSH to one of the NSX Manager
   that is a member of the cluster.
2. Run admin CLI get cluster status.
3. If cluster status is stable, run get services or
   get service <service-name> and verify that the
   following services are running: http,
   manager, search,
   ui-service.
4. To restart or start the stopped service, run restart | start service
   <service-name>.