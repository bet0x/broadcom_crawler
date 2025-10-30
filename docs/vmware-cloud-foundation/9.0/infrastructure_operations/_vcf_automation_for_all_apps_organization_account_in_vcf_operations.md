---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vcf-automation-management-pack.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   VCF Automation for All Apps Organization Account in VCF Operations
---

# VCF Automation for All Apps Organization Account in VCF Operations

The VCF Automation for All Apps Organization management pack expands the operational capabilities available to users, helping partners effectively meter, price, and bill their cloud services using VMware’s chargeback technology. It enables flexible segmentation of virtual environments to meet tenant requirements and supports various billing strategies. By offering accurate infrastructure monitoring and customizable pricing models, the solution ensures tenants have a transparent view of their resource consumption, making billing verification simple. Both service providers and tenants benefit from comprehensive reports, real-time alerts, and intuitive dashboards that display usage patterns, resource allocation, and pricing information.

## Overview of the VCF Automation for All Apps Organization Management Pack

The  VMware Aria Automation Management Pack for version 8.x enabled integration with VMware Aria Automation 8.x environments, providing cloud administrators with monitoring, alerting, reporting, metering, and pricing capabilities. With the strategic consolidation of VMware Cloud Director and VMware Aria Automation into VCF Automation 9.0, existing organizations will persist as VM Apps organizations, while newly created organizations will be categorized as All Apps organizations.

With the release of VMware Cloud Foundation, VCF Automation, VMware Cloud Director, and Supervisor functionality are integrated into a single product called VCF Automation 9.0. This consolidation empowers customers to effectively manage IT catalogs, multi-tenancy, and modern application development for both enterprises and service providers. When you upgrade your existing vRealize Automation 8.x environment to the latest VCF Automation 9.0 version, your existing organizations will remain unchanged and will be classified VM Apps organizations. Any new tenant created after the upgrade will be be included in the All Apps organization.

To support these enhancements you must deploy VCF Automation for All Apps Organization in clean deployments where you are deploying an instance of VMware Cloud Foundation newly and you do not have VMware Aria Automation 8.x management pack deployed. One adapter can collect information for all the organizations and resources. For more information on Chargeback, see the topic, [Performing Based Multitenancy.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/cost-and-capacity-management/performing-vcd-based-multitenancy-operations.html)

If you have a VMware vSphere Foundation license, then VCF Automation for All Apps Organization integrations is not available.