---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore/install-a-software-update.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Install a Software Update
---

# Install a Software Update

If you have already installed VCF Operations, you can update your software when a newer version becomes available.

- Create a snapshot of each node in your cluster. See [Create a Snapshot Before You Upgrade VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore/create-a-snapshot.html#GUID-2b1d7a23-f962-403a-bfa1-a1c3cbf64e12-en) for details.
- Obtain the PAK file for your cluster. See [Obtain the Software Update PAK File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore/obtain-the-right-pak-file-for-your-upgrade.html#GUID-6ab27788-2068-4952-930c-c3a90548f1fa-en) for details.
- Before you install the PAK file, or upgrade your VCF Operations instance, clone any customized content to preserve it. Customized content can include alert definitions, symptom definitions, recommendations, and views. Then, during the software update, you select the option named Install the PAK file even if it is already installed.
- VCF Operations update operation has a validation process that identifies issues before you start to update your software. Although it is good practice to run the pre-update check and resolve any issues found, users who have environmental constraints can deactivate this validation check.

  To deactivate the pre-update validation check, perform the following steps:

  - Edit the update file to /storage/db/pakRepoLocal/bypass\_prechecks\_VMware AriaOperationsManagerEnterprise-buildnumberofupdate.json.
  - Change the value to TRUE and run the update.

  If you deactivate the validation, you might encounter blocking failures during the update itself.

Installation might take several minutes or even a couple hours depending on the size and type of your clusters and nodes.

1. Log in to the primary node VCF Operations administrator interface of your cluster at https://primary-node-FQDN-or-IP-address/admin.
2. Click Software Update in the left pane.
3. Click Install a Software Update in the main pane.
4. Follow the steps in the wizard to locate and install your PAK file. 

   This updates the OS on the virtual appliance and restarts each virtual machine.
5. Read the End User License Agreement and Update Information, and click Next.
6. Click Install to complete the installation of software update.

   After you click Install, the installer will restart the VCF Operations administrator interface, and you will be logged out. Log in once again to the VCF Operations administrator interface when it is ready, and follow the update status in the software update page.
7. Log back into the primary node administrator interface. 

   The main Cluster Status page appears and cluster goes online automatically. The status page also displays the Bring Online button, but do not click it.
8. Clear the browser caches and if the browser page does not refresh automatically, refresh the page. 

   The cluster status changes to Going Online. When the cluster status changes to Online, the upgrade is complete.

   If a cluster fails and the status changes to offline during the installation process of a PAK file update, then some nodes become unavailable. To fix this, you can access the administrator interface and manually take the cluster offline and click Finish Installation to continue the installation process.
9. Click Software Update to check that the update is done. 

   A message indicating that the update completed successfully appears in the main pane.

   When you update VCF Operations to a latest version, all nodes get upgraded by default.

   If you are using cloud proxies, the cloud proxy upgrades start after the VCF Operations upgrade is complete successfully. For more information, see the Monitoring the Health of Cloud Proxies from the Admin UI topic in the  VMware Aria Operations Configuration Guide.

Delete the snapshots you made before the software update.

Multiple snapshots can degrade performance, so delete your pre-update snapshots after the software update completes.