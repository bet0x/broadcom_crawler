---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health/monitoring-the-health-of-vcf-deployments.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Monitoring the Health of VCF Deployments
---

# Monitoring the Health of VCF Deployments

Use VMware Infrastructure Health to monitor the health of the VCF cloud account in VCF Operations. You can also monitor the VCF applications along with their services.

The VCF domains you want to monitor should have their vCenter and NSX configured in each VCF domain. For more information, see [Configuring VMware Cloud Foundation Cloud Account](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-cloud-foundation/configuring-vmware-cloud-foundation.html#GUID-2af6a9c5-76cf-47cd-8bc4-ae62af664056-en). All VCF domains are automatically discovered along with their connection details and the credentials of the underlying adapters for vCenter systems and NSX.

VMware Infrastructure Health collects data related to availability, services, virtual machines, certificates, passwords, and active alerts for each configured VCF cloud account and its domains.

To view the health information of the monitored services, navigate to Infrastructure OperationsDashboards and ReportsDashboards, expand All, expand VMware Infrastructure Health, and then click VMware Infra Management Health Overview.

To view certificate information of monitored services, navigate to Infrastructure OperationsDashboards and ReportsDashboards, expand All, expand VMware Infrastructure Health, and then click VMware Infra Certificate Overview.

## Monitoring the Management Domains

VMware Infrastructure Health will collect the following applications of the VCF management domain:

1. VCF Operations for logs application (managed by VCF Operations fleet management)
2. vCenter application
3. SDDC Manager application
4. NSX application
5. vSAN application
6. VCF Automation application (version 8.x)
7. VCF Operations application

## Monitoring the VCF Domains

VMware Infrastructure Health will collect the following applications of the VCF domain:

1. vCenter application
2. NSX application
3. vSAN application