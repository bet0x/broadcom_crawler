---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health/monitoring-health-for-nsx-t-using-vmware-infrastructure-health.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Monitoring NSX Services
---

# Monitoring NSX Services

You can monitor the health of NSX services with VMware Infrastructure Health.

## Resources Monitored for NSX

VMware Infrastructure Health monitors the health of the following NSX services:

- cm-inventory
- controller
- cluster-boot-manager
- http
- install-upgrade
- liagent
- mgmt-plane-bus
- nsx-ui
- ntp
- nsx-upgrade-agent
- node-mgmt
- nsx-message-bus
- migration-coordinator
- manager
- ssh
- syslog
- snmp
- search
- telemetry

## NSX Certificate Monitoring

Once the VMware Infrastructure Health collects the health of the NSX health services, it monitors the configured NSX certificates, on a daily basis.

Alerts are raised based on the number of days set for critical, immediate, and warning category under the global setting. The NSX certificates contain the following three symptoms:

- has expired or will expire shortly - for critical
- expire shortly - for immediate
- about to expire - for warning

These symptoms are triggered if the certificate expiry date has reached the threshold condition set for critical, immediate, and warning. A notification is displayed explaining the alert information.

## NSX Backup Job

The retention period for NSX backup job monitoring is set by default to the last 7 days. You cannot update the retention period for NSX.