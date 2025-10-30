---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/upgrade-fails-due-to-a-timeout.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade Fails Due to a Timeout
---

# Upgrade Fails Due to a Timeout

An event during the upgrade process fails and the message from the Upgrade Coordinator indicates a timeout error.

During the upgrade process, the following events might fail because they do not complete within a specific time. The Upgrade Coordinator reports a timeout error for the event and the upgrade fails.

| Event | Timeout Value |
| --- | --- |
| Putting a host into maintenance mode | 4 hours |
| Waiting for a host to reboot | 32 minutes |
| Waiting for the NSX service to be running on a host | 13 minutes |

- For the maintenance mode issue, log in to vCenter and verify the status of tasks related to the host. Resolve any problems.
- For the host reboot issue, check the host to see why it failed to reboot.
- For the NSX service issue, log in to the NSX Manager UI, select SystemAppliances and see if the host has an installation error. If so, you can resolve it from the NSX Manager UI. If the error cannot be resolved, you can refer to the upgrade logs to determine the cause of the failure.