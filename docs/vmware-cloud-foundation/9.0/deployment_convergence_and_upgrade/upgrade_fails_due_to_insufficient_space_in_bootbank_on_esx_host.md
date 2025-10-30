---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/upgrade-fails-due-to-insufficient-space-in-bootbank-on-esxi-host.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade Fails Due to Insufficient Space in Bootbank on ESX Host
---

# Upgrade Fails Due to Insufficient Space in Bootbank on ESX Host

NSX upgrade might fail if there is insufficient space in the bootbank or in the alt-bootbank on an ESX host.

Unused VIBs on the ESX host might be relatively large in size and therefore use up significant disk space. The unused VIBs can result in insufficient space in the bootbank or in the alt-bootbank during upgrade.

Uninstall the VIBs that are no longer required and free up additional disk space.

For more information on locating and deleting VIBs, see [Knowledge Base article 324231](https://knowledge.broadcom.com/external/article/324231/nsxt-vibs-fail-to-installupgrade-due-to.html).