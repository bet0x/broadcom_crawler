---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/troubleshoot-nsx-appliance-or-nsx-clustering-issues-using-apis.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Troubelshoot NSX Appliance or NSX Clustering issues Using APIs
---

# Troubelshoot NSX Appliance or NSX Clustering issues Using APIs

Use
APIs to troubleshoot NSX appliance and clustering issues.

## Verify Cluster Status

GET
https://<nsx-manager>/api/v1/cluster/status

GET https://<nsx-manager>/api/v1/cluster/<node-id>/status

GET/api/v1/reverse-proxy/node/health

## Verify CPU Usage

GET
/api/v1/systemhealth/appliances/process/status

GET
https://<nsx-manager-ip>/api/vi/systemhealth/appliances/<appliance-id>/process/status

## Verify Network Latency

GET
https://<nsx-manager>/api/v1/systemhealth/appliances/latency/status

GET
https://<nsx-manager-ip>/api/v1/systemhealth/appliances/<appliance-id>/latency/status