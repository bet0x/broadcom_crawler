---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health/vcenter-services-in-vmware-infra-health/certificate-monitoring-for-vcenter-services-in-vmware-infra-health.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   vCenter Certificate Monitoring
---

# vCenter Certificate Monitoring

VMware Infrastructure Health collects and monitors the vCenter root and ESX TLS certificates on a daily basis. The certificate properties are published under the Certificate Summary group (under the vCenter application and Host System resources.

Alerts are raised based on the number of days set for critical, immediate, and warning category under the global setting. The vCenter certificates contain the following three symptoms:

- has expired or will expire shortly - for critical
- expire shortly - for immediate
- about to expire - for warning