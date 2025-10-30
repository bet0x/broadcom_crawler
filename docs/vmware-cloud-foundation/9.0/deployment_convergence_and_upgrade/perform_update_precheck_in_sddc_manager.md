---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/perform-upgrade-precheck.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Perform Update Precheck in SDDC Manager
---

# Perform Update Precheck in SDDC Manager

You must perform a precheck in SDDC Manager before applying an update to ensure that your environment is ready for the update.

Bundle-level pre-checks for vCenter are available in VMware Cloud Foundation.

Because ESX bundle-level pre-checks only work in minor-version upgrades (for example: from ESX 8.x through 8.y), these prechecks do not run in VMware Cloud Foundation.

If you silence a vSAN Skyline Health alert in the vSphere Client, SDDC Manager skips the related precheck and indicates which precheck it skipped. Click RESTORE PRECHECK to include the silenced precheck. For example:![An example of an alert that was silenced in vSAN Skyline Health.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8813397d-e90b-493c-bf31-bab4b746f531.original.png)

You can also silence failed vSAN prechecks in the SDDC Manager UI by clicking Silence Precheck. Silenced prechecks do not trigger warnings or block upgrades.

Only silence alerts if you know that they are incorrect. Do not silence alerts for real issues that require remediation.

1. In the navigation pane, click InventoryWorkload Domains.
2. On the Workload Domains page, click the workload domain where you want to run the precheck.
3. On the domain summary page, click the Updates tab. 

   It is recommended that you precheck your workload domain prior to performing an upgrade.
4. Click RUN PRECHECK to select the components in the workload domain you want to precheck.
   1. You can select to run a Precheck only on vCenter or the vSphere cluster. All components in the workload domain are selected by default. To perform a precheck on certain components, choose Custom selection.

      ![All components are selected to precheck.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/21ad5705-9d6f-4936-af61-06277b5f5d8a.original.png)
   2. If there are pending upgrade bundles available, then the "Target Version" dropdown contains "General Upgrade Readiness" and the available VMware Cloud Foundation versions to upgrade to. If there is an available VMware Cloud Foundation upgrade version, there will be extra checks - bundle-level prechecks for hosts, vCenter, and so forth. The version specific prechecks will only run prechecks on components that have available upgrade bundles downloaded.!["Target Version" dropdown](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0018a866-2b72-465f-88e6-9aabdc31196a.original.png)
5. When the precheck begins, a progress message appears indicating the precheck progress and the time when the precheck began.

   ![Precheck shows In Progress and is 72% completed, along with the date and time when Precheck was started.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e7185641-3ea8-4488-ad03-dff53cf3e028.original.png)

   Parallel precheck workflows are supported. If you want to precheck multiple domains, you can repeat steps 1-5 for each of them without waiting for step 5 to finish.
6. Once the Precheck is complete, the report appears. Click through ALL, ERRORS, WARNINGS, and SILENCED to filter and browse through the results.

   ![Precheck report shows the number of resources that passed, errors, warnings, and silenced.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c08acbaf-9420-4ca1-9074-e1861584d542.original.png)
7. To see details for a task, click the expander arrow.

   If a precheck task failed, fix the issue, and click Retry Precheck to run the task again. You can also click RETRY ALL FAILED RESOURCES to retry all failed tasks.
8. If the workload domain contains a host that includes pinned VMs, the precheck fails at the Enter Maintenance Mode step. If the host can enter maintenance mode through the vCenter UI, you can suppress this check for NSX and ESX in VMware Cloud Foundation by following the steps below.

   1. Log in to SDDC Manager by using a Secure Shell (SSH) client with the user name vcf and password.
   2. Open the /opt/vmware/vcf/lcm/lcm-app/conf/application-prod.properties file.
   3. Add the following line to the end of the file:

      lcm.nsxt.suppress.dry.run.emm.check=true

      lcm.esx.suppress.dry.run.emm.check.failures=true
   4. Restart the lcm service by typing the following command in the console window.

      systemctl restart lcm
   5. After the lcm service is restarted, run the precheck again.

The precheck result is displayed at the top of the Upgrade Precheck Details window. If you click Exit Details, the precheck result is displayed at the top of the Precheck section in the Updates tab.

Ensure that the precheck results are green before proceeding. Although a failed precheck will not prevent the upgrade from proceeding, it may cause the update to fail.