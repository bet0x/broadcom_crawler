---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Troubleshooting Upgrade Failures
---

# Troubleshooting Upgrade Failures

You can review the support bundle log messages to identify the upgrade problem.

You can also perform any of the following debugging tasks.

- Log in to the NSX Manager CLI as root user and navigate to the upgrade coordinator log files /var/log/upgrade-coordinator/upgrade-coordinator.log.
- Navigate to the system log files /var/log/syslog or API log files /var/log/proton/nsxapi.log.
- Configure a remote logging server and send log messages for troubleshooting. See the NSX Administration Guide.

If you are unable to troubleshoot the failure and want to revert to the previous working version of NSX, contact Broadcom support.