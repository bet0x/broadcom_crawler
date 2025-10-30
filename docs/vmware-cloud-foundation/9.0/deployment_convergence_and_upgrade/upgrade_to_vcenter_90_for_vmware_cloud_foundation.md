---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vcenter-server-for-vmware-cloud-foundation-5-2.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade to vCenter 9.0 for VMware Cloud Foundation
---

# Upgrade to vCenter 9.0 for VMware Cloud Foundation

The upgrade bundle for VMware vCenter is used to upgrade the vCenter instances managed by SDDC Manager. Upgrade vCenter in the management domain before upgrading vCenter in workload domains.

- Download the VMware vCenter upgrade bundle. See [Downloading VMware Cloud Foundation Upgrade Bundles for Core Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles.html).
- Take a file-based backup of the vCenter appliance before starting the upgrade. See [On-Demand Back Up of vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-backups-for-sddc-manager-and-vcenter-server/manually-back-up-vcenter-server.html).

  After taking a backup, do not make any changes to the vCenter inventory or settings until the upgrade completes successfully.
- If your workload domain contains Workload Management (vSphere with Tanzu) enabled clusters, the supported target release depends on the version of Kubernetes (K8s) currently running in the cluster. Older versions of K8s might require a specific upgrade sequence. See [KB 92227](https://knowledge.broadcom.com/external/article?legacyId=92227) for more information.

1. In the navigation pane, click InventoryWorkload Domains.
2. On the Workload Domains page, click the domain you are upgrading and then click the Updates tab.
3. Click Precheck to run the upgrade precheck.

   Resolve any issues before proceeding with the upgrade.
4. In the Available Updates section, click Configure Update.
5. Review the upgrade mechanism information and click Next.

   A vCenter Reduced Downtime Upgrade (RDU) uses a migration-based approach. In this approach, a new vCenter appliance is deployed and the current vCenter data and configuration is copied to it.

   During the preparation phase of a reduced downtime upgrade, the source vCenter Appliance and all resources remain online. The only downtime occurs when the source vCenter Appliance is stopped, the configuration is switched over to the target vCenter, and the services are started. The downtime is expected to take approximately 5 minutes under ideal network, CPU, memory, and storage provisioning.
6. Select a backup option and click Next.
7. Provide a temporary network to be used only during the upgrade and click Next. 

   |  |  |
   | --- | --- |
   | Automatic | Automatically assign network information. |
   | Static | Enter an IP address, subnet mask, and gateway. The IP address must be in the management subnet. |
8. Schedule the update and click Next. 

   Select scheduling options for the preparation and switchover phases of the upgrade.

   If you are scheduling the switchover phase, you must allow a minimum of 4 hours between the start of preparation and the start of switchover.
9. Review the upgrade settings and click Finish.
10. Monitor the upgrade progress. See [Monitoring VMware Cloud Foundation Updates](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/monitor-update.html).

    A Cancel button is available once a vCenter RDU upgrade has started. If you cancel the upgrade, the configuration reverts to the source vCenter instance.
11. After the upgrade is complete, remove the old vCenter appliance.

    If the upgrade fails, resolve the issue and retry the failed task. If you cannot resolve the issue, restore vCenter using the file-based backup. See [Restoring a vCenter Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server.html). vCenter RDU upgrades perform automatic rollback if the upgrade fails.

After the upgrade is complete, allow some time (approximately 15 minutes) for post-upgrade auto-reconciliation of configuration drift fixes before scheduling another upgrade. If you schedule a second upgrade to run before the remediation task completes, the upgrade may be cancelled or auto-reconciliation may fail.

Once the upgrade successfully completes, use the vSphere Client to change the vSphere DRS Automation Level setting back to the original value (before you took a file-based backup) for each vSphere cluster that is managed by the vCenter. See [KB 87631](https://knowledge.broadcom.com/external/article?legacyId=87631) for information about using VMware PowerCLI to change the vSphere DRS Automation Level.

After you successfully upgrade vCenter, transition any clusters that use vSphere Lifecycle Manager baselines to use vSphere Lifecycle Manager images before upgrading ESX. See[Transitioning from vSphere Lifecycle Manager Baselines to vSphere Lifecycle Manager Images](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-.html).