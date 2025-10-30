---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/upgrade-coordinator-user-interface-is-inaccesible.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade Coordinator User Interface is Inaccessible
---

# Upgrade Coordinator User Interface is Inaccessible

The Upgrade Coordinator user interface may not be accessible.

You cannot access the Upgrade Coordinator user interface or APIs.

Internal service dependencies may cause the Upgrade Coordinator user interface to become inaccessible.

Run the following command to restart the Upgrade Coordinator service:

```
restart service install-upgrade
```