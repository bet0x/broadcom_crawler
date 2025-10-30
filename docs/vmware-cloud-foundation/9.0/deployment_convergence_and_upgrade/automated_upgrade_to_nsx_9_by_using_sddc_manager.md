---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/upgrade-nsx-for-vcf-5-2.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Automated Upgrade to NSX 9 by Using SDDC Manager
---

# Automated Upgrade to NSX 9 by Using SDDC Manager

You upgrade NSX in the management domain and workload domains by using the recommended orchestration and automation that SDDC Manager provides.

You can upgrade NSX in workload domains before or after upgrading NSX in the management domain.

Prior to VMware Cloud Foundation 9.0, host clusters were upgraded as part of the NSX upgrade. In VMware Cloud Foundation 9.0, host clusters are upgraded as part of the ESX upgrade. As a result of this change, ESX hosts no longer go into maintenance mode during an NSX upgrade.

Upgrading NSX involves the following components:

- Upgrade Coordinator
- NSX Manager cluster
- NSX Edges/Clusters (if deployed)

1. In the navigation pane, click InventoryWorkload Domains.
2. On the Workload Domains page, click the domain you are upgrading and then click the Updates/Patches tab.

   When you upgrade NSX components for a selected workload domain, those components are upgraded for all workload domains that share the NSX Manager cluster.
3. Click Precheck to run the upgrade precheck.

   Resolve any issues before proceeding with the upgrade.

   The NSX precheck runs on all workload domains in your environment that share the NSX Manager cluster.
4. Configure the update.
   1. In the Available Updates section, click the Configure Update button.
   2. Review the Introduction and click Next.
   3. On the NSX Edge Clusters page, select the NSX Edge clusters you want to upgrade and click Next.

      By default, all NSX Edge clusters are upgraded. To select specific NSX Edge clusters, select the Upgrade only NSX Edge clusters check box and select the Enable edge selection option. Then select the NSX Edges you want to upgrade.
   4. On the Review page, review your settings and click Run Precheck.

      The precheck begins. Resolve any issues until the precheck succeeds.
   5. After the precheck succeeds, click Schedule Update and select an option.

      If the precheck report includes any errors or warnings, you must select the checkbox to proceed.
5. Monitor the upgrade progress. See [Monitoring VMware Cloud Foundation Updates](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/monitor-update.html).

   If a component upgrade fails, the failure is displayed across all associated workload domains. Resolve the issue and retry the failed task.

When all NSX workload components are upgraded successfully, a message with a green background and check mark is displayed.

NSX 9.0 functionality is not available until all ESX hosts in all vSphere clusters that share an NSX Manager are upgraded to 9.0 and the NSX Finalize subtask of the ESX upgrade step succeeds.

After the upgrade is complete, allow some time (approximately 15 minutes) for post-upgrade auto-reconciliation of configuration drift fixes before scheduling another upgrade. If you schedule a second upgrade to run before the remediation task completes, the upgrade may be cancelled or auto-reconciliation may fail.