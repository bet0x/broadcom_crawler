---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-esxi-for-vmware-cloud-foundation-5-2-1.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade to ESX 9.0 for VMware Cloud Foundation
---

# Upgrade to ESX 9.0 for VMware Cloud Foundation

Prior to VMware Cloud Foundation 9.0, the product supported both vSphere Lifecycle Manager baseline clusters and vSphere Lifecycle Manager image clusters. Starting with VMware Cloud Foundation 9.0, only vSphere Lifecycle Manager image clusters are supported.

- All vSphere clusters in a workload domain must be managed by vSphere Lifecycle Manager images before they can be upgraded to ESX 9.0. If any clusters are still using legacy vSphere Lifecycle Manager baselines, they must be transitioned to use vSphere Lifecycle Manager images before proceeding. See [Transitioning from vSphere Lifecycle Manager Baselines to vSphere Lifecycle Manager Images](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-.html).
- Confirm that the ESX passwords are valid.
- Ensure that the domain for which you want to perform cluster-level upgrade does not have any ESX hosts or vSphere clusters in an error state. Resolve the error state or remove the ESX hosts and vSphere clusters with errors before proceeding.
- You must upgrade NSX Manager and vCenter before you can upgrade ESX hosts with a vSphere Lifecycle Manager image.
- Create a vSphere Lifecycle Manager image using the vSphere Client. See [Working with Image Library.](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/working-with-image-library.html)
  - Use the ESX version specified in the VMware Cloud Foundation BOM.
  - You can create a composite image for a cluster that has hosts from different vendors or from the same vendor but different generations, family, or model. A composite image contains one default image and one or more alternative images. All images in a composite image contain the same base image and solutions, but may include different vendor or firmware and driver add-ons. When you create alternate images, you also specify the rules that are used to filter the hosts to which the alternative image is assigned.
  - If you plan to use the Import from a file option to import a vSphere Lifecycle Manager image, you must first export the files from the vSphere Client.

The process of upgrading to ESX 9.0 involves the following steps:

- Importing one or more images into SDDC Manager from vSphere.
- Using that image to upgrade to ESX 9.0.

For the 9.0 release, VMware ESXi has been rebranded to VMware ESX.

Starting with VMware Cloud Foundation 9.0, NSX kernel modules (VIB files) are installed as part of ESX host cluster upgrades.

If you are using external (non-vSAN) storage, the following procedure updates the ESX hosts attached to the external storage. However, updating and patching the storage software and drivers is a manual task and falls outside of SDDC Manager lifecycle management. To ensure supportability after an ESX upgrade, consult the vSphere HCL and your storage vendor.

You can configure multiple cluster update tasks with different schedules without having to wait for the first cluster update to complete. For example, you could schedule an update for cluster-1 and cluster-2 to run immediately and then configure another update task for cluster-3 and schedule it to run overnight.

1. Import a vSphere Lifecycle Manager image into SDDC Manager.
   1. In the SDDC Manager UI, click Lifecycle ManagementImage Management .
   2. Click Import Image.
   3. Select the import method, provide the required information, and click Import.

      | Option | Description |
      | --- | --- |
      | Import from a vCenter | Select the vCenter where you created the image from the drop-down menu.  Select the upgrade image. |
      | Import from a file | Enter a name for the image and then click Select File to import each of the required files.  Select the JSON, ZIP, and ISO files from your local computer. The ISO file is optional. |

      You can view status in the Tasks panel.
2. In the navigation pane, click InventoryWorkload Domains.
3. On the Workload Domains page, click the domain you are upgrading and then click the Updates tab.
4. Click Precheck to run the upgrade precheck.

   Resolve any issues before proceeding with the upgrade.
5. In the Available Updates section, click Configure Update for ESX.
6. Read the introductory information and click Next.
7. Select the clusters to update and click Next.

   The default setting is to upgrade all clusters. To upgrade specific clusters, select Custom selection and select the clusters to upgrade.

   For VCF 9.0, if you are upgrading a stretched cluster, a virtual vSAN Witness Host is also upgraded. A physical vSAN Witness Host must be upgraded manually, before upgrading the ESX hosts in the stretched cluster.

   For VCF 9.0.1, you must manually upgrade the vSAN Witness Host, before upgrading the ESX hosts in the stretched cluster.
8. Click Assign Image, select an imported image to assign to the selected clusters, and click Next.
9. Select the upgrade options and click Next.

   By default, the selected clusters are upgraded in parallel. If you selected more than ten clusters to be upgraded, the first ten are upgraded in parallel and the remaining clusters are upgraded sequentially. To upgrade all selected clusters sequentially, select Enable sequential cluster upgrade.

   Select Enable Quick Boot to reduce the upgrade time by skipping the physical reboot of the host.

   Select Migrate Powered Off and Suspended VMs to migrate the suspended and powered off virtual machines from the hosts that must enter maintenance mode to other hosts in the cluster.

   Select Enforce Live Patch when the cluster image includes a Live Patch. With the Enforce Live Patch option, vSphere Lifecycle Manager does not place the hosts in the cluster into maintenance mode, hosts are not rebooted, and there is no need to migrate the virtual machines running on the hosts in the cluster.
10. Review the settings, and click Finish or Run Precheck.

    VMware Cloud Foundation runs a cluster image hardware compatibility and compliance precheck. Resolve any reported issues before proceeding.
11. After the precheck succeeds, click Schedule Update, select a scheduling option, and click Finish. 

    If the precheck report includes any errors or warnings, you must select the checkbox to proceed.
12. Monitor the upgrade progress. See [Monitoring VMware Cloud Foundation Updates](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/monitor-update.html#GUID-5444f0ec-f2fa-49fa-970c-e3c8bb460287-en).

    If you are upgrading multiple clusters in parallel and one or more of the cluster upgrades fails, the upgrade continues on the remaining clusters. In addition, you can configure a new upgrade task for the failed cluster(s) without having to wait for the original upgrade task to finish.

    NSX 9.0 functionality is not available until all ESX hosts in all vSphere clusters that share an NSX Manager are upgraded to 9.0 and the NSX Finalize subtask of the ESX upgrade step succeeds. If the NSX Finalize subtask fails, the ESX upgrade can still reach completion but a subtask error is displayed in the task panel.

After the upgrade is complete, allow some time (approximately 15 minutes) for post-upgrade auto-reconciliation of configuration drift fixes before scheduling another upgrade. If you schedule a second upgrade to run before the remediation task completes, the upgrade may be cancelled or auto-reconciliation may fail.

Upgrade the vSAN Disk Format for vSAN clusters. The disk format upgrade is optional. Your vSAN cluster continues to run smoothly if you use a previous disk format version. For best results, upgrade the objects to use the latest on-disk format. The latest on-disk format provides the complete feature set of vSAN. See [Upgrade vSAN On-Disk Format Versions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vsan-on-disk-format-versions.html).