---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/apply-configuration-updates.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Apply VMware Cloud Foundation Configuration Updates
---

# Apply VMware Cloud Foundation Configuration Updates

VMware Cloud Foundation Configuration Updates identify and resolve any discrepancies between the intended/prescribed configuration and the actual configuration, ensuring that the deployment aligns with the recommended configuration. This process includes reconciling the configuration for 2nd party software components listed in the VMware Cloud Foundation Bill of Materials (BOM).

Configuration updates may be required after you apply software updates. Once a configuration update becomes available, you can apply it immediately or wait until after you have applied all software updates. Configuration Updates must be performed during a maintenance window.

Configuration Updates can be applied to multiple domains in parallel. However, if a Configuration Update is in progress, another configuration update on the same domain should not be attempted.

1. In the navigation pane, click InventoryWorkload Domains.
2. On the Workload Domains page, click the workload domain name and then click the Updates tab.
3. Click Run Precheck to run the upgrade precheck.

   Resolve any issues before proceeding with the upgrade.
4. Expand Available Configuration Updates, click Apply All.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/604a057f-5544-4dba-935c-9744e1d7a37e.original.png)

   - FEATURE: Configuration change required for a new feature.
   - FIX: Configuration change associated with a fix for a defect.
5. Check the progress of a configuration update by clicking the task in the Tasks panel.![SDDC Manager Tasks table showing that Config Reconcilation is Running.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/61a50510-6996-4aff-8fa9-b75efc00c7a9.original.png)
6. After the configuration updates are successfully applied, they will no longer appear in the table.![There are noi available Configuration Updates.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/abb45ef4-340b-4f79-bf0e-960326a5c92a.original.png)

   Pending Configuration Updates do not block future BOM upgrades.