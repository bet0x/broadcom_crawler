---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/nsx-introduction.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   NSX Account in VCF Operations
---

# NSX Account in VCF Operations

The NSX adapter allows you to retrieve alerts and findings from NSX to VCF Operations.

The NSX adapter supports adapter configuration using VIDM for NSX versions 3.0 and above. The roles and permissions associated with the VIDM users collecting the NSX adapter data are:

| Roles | Permissions |
| --- | --- |
| Enterprise Admin | Collect all data. |
| Network engineer | - Collect all the NSX resources except the Load Balancer and collect limited routers data. Router data collected:    - Tier 0 router connected to logical switch.   - Tier 1 router created from vCloud Director. |
| - Security Engineer - Security Operator - Auditor | Collect all data except the load balancer. |
| - LB Admin - LB Auditor - Netxpartner Admin | Cannot collect any data. |