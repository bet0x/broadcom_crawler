---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/pre-upgrade-tasks.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Pre-Upgrade Tasks for Upgrading NSX
---

# Pre-Upgrade Tasks for Upgrading NSX

Before you upgrade NSX, perform the pre-upgrade tasks to ensure that the upgrade is successful.

1. Ensure that your transport node profiles have the appropriate transport zones added to them. NSX Manager may not display the list of transport node profiles if any transport node profiles do not have transport zones added to them.
2. Run the Certificate Analyzer, Results and Recovery (CARR) script. The goal of running the CARR script is to ensure that NSXcertificates, such as transport node (TN) certificates, do not expire within 90 days. For more information, see Broadcom KB article [369034](https://knowledge.broadcom.com/external/article?articleId=369034).
3. Ensure that you back up the NSX Manager before you start the upgrade process. See [Backing Up and Restoring NSX Manager or Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/backing-up-and-restoring-the-nsx-manager.html).
4. Ensure that your host OS is supported for NSX Manager. For more information, see the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).
5. Disable automatic backups before you start the upgrade process. For more information, see [Configure Backups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location.html).
6. Terminate any active SSH sessions or local shell scripts that you may have invoked on the NSX Manager or the NSX edge nodes, before you begin the upgrade process.
7. Ensure that the appropriate communication ports are open from the host transport nodes and edge nodes to the NSX Manager nodes. For more information on ports, see [VMware Ports and Protocols](https://ports.broadcom.com/home/NSX).
8. Delete all expired user accounts before you begin the upgrade. Upgrade for NSX on vSphere fails if your exception list for vSphere lockdown mode includes expired user accounts. If your host is part of the vLCM-enabled cluster, several users such as lldp-vim-user, nsx-user, mux-user, and da-user, are created automatically and added to the exception users list on an ESX host when NSX VIBS are installed. For more information on accounts with access privileges in lockdown mode, see Specifying Accounts with Access Privileges in Lockdown Mode in the vSphere Security Guide. For more details on these NSX user accounts on the ESX host, see [Knowledge Base article 324186](https://knowledge.broadcom.com/external/article/324186/nsxt-user-accounts-created-on-an-esxi-ho.html).
9. VCF 9.x does not support the multi NSX feature. Ensure that you switch off the multi NSX features for all the compute managers registered with NSX Manager. Alternatively, you can map the NSX Manager instances to individual vCenter instances before upgrading.
10. Starting with VCF 9.0, a service account is created on vCenter for NSX to communicate with a registered compute manager. If you are upgrading to VCF 9.0 and any of the registered compute managers do not have a service account, a pre-check error is raised. To proceed with the upgrade, you must enable the Create Service Account setting on each registered compute manager.
11. Ensure that you have the supported hardware version for your NSX edge VMs. For more information, see Knowledge Base article 319091: [NSX Edge VM Hardware Version upgrade](https://knowledge.broadcom.com/external/article?articleNumber=319091).