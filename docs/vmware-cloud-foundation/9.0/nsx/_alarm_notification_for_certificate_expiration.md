---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/alarm-notification-for-certificate-expiration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >  Alarm Notification for Certificate Expiration
---

# Alarm Notification for Certificate Expiration

NSX generates alarms when
a certificate is nearing its expiry or if a certificate has already expired. Service
certificates generate an alarm only if expiring or expired and in use by a component.
Non-service certificates always generate an alarm, whether in use or not.

NSX generates alarms under following events. The defaults are
listed below, but are configurable.

- Medium severity alarm starting 30
  day before certificate expiry.

- High severity alarm starting 7 days
  prior to expiry.
- Critical severity alarm after
  certificate expires.

Certificate Expiry alarms contains details on
certificate ID, severity, node, first/last report time, and recommended action.

As a remedial, you must replace the expiring
External Platform certificate with a new valid certificate and delete expiring
certificate.