---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/apply-cloud-foundation-5-2-update-bundle.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade SDDC Manager to 9.0
---

# Upgrade SDDC Manager to 9.0

The VMware Cloud Foundation upgrade bundle upgrades the SDDC Manager appliance and VMware Cloud Foundation services.

- Download the VMware Cloud Foundation upgrade bundle for your target release. See [Downloading VMware Cloud Foundation Upgrade Bundles for Core Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles.html#GUID-e9f8fe4e-5c5b-4f15-bddc-ef2276de7ce8-en).
- Ensure you have a recent successful backup of SDDC Manager using an external SFTP server.
- Ensure you have taken a snapshot of the SDDC Manager appliance.
- Ensure you have recent successful backups of the components managed by SDDC Manager.
- [Perform Update Precheck in SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/perform-upgrade-precheck.html) and resolve any issues.

1. In the navigation pane, click InventoryWorkload Domains.
2. On the Workload Domains page, click the management domain and then click the Updates tab.
3. In the Available Updates section, click Plan Upgrade, select a target version, and click Confirm.
4. Click Update Now or Schedule Update next to the VMware Cloud Foundation Upgrade bundle.
5. If you selected Schedule Update, select the date and time for the bundle to be applied and click Schedule.

   ![An image showing the UI for scheduling an update.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/289ed083-f016-4f47-aab8-5a3ab496be66.cq5dam.web.1280.1280.jpeg)

   If you clicked Update Now, the Update Status window displays the components that will be upgraded and the upgrade status. Click View Update Activity to view the detailed tasks. After the upgrade is completed, a green bar with a check mark is displayed.
6. Click Finish.

   When the update completes successfully, you are logged out of the SDDC Manager UI and must log in again.

If you are using an online depot, download the remaining upgrade bundles. See [Download VMware Cloud Foundation 9.0 Upgrade Bundles Using an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-from-sddc-manager.html).

After you upgrade to SDDC Manager 9.0, bundles are referred to as binaries.