---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/compliance-based-configurations/view-compliance-report.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View Compliance Status Report
---

# View Compliance Status Report

You can view a compliance report for NSX features. You can use the report to configure your NSX environment to adhere to your IT policies and industry standards.

The compliance report includes information about each non-compliant configuration.

Compliance Report Information



| Compliance Report Column | Description | Example |
| --- | --- | --- |
| Non Compliance Code | Code to identify the type of non-compliance. | 72301 |
| Description | Description of the type of non-compliance. | Certificate is not CA signed. |
| Compliance Standard | The compliance standard or program that the resource has violated. | EAL4+ |
| Resource By | Name or ID of the affected resource. | nsx-manager-1 |
| Resource Type | Type of resource affected. | CertificateComplianceReporter |
| Affected Resources | Number of affected resources. The number can be 0 if there are non-compliant configurations present, but the feature is not used. | 1 |

You can also retrieve the report using the API: GET /policy/api/v1/compliance/status.

1. From your browser, log in with
   admin privileges to an NSX Manager
   at https://<nsx-manager-ip-address>.
2. From the Home page, click Monitoring DashboardsCompliance Report.