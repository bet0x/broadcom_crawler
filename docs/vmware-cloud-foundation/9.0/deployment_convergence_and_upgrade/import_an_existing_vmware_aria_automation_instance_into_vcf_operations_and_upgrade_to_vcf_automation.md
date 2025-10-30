---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Import an Existing VMware Aria Automation Instance Into VCF Operations and Upgrade to VCF Automation 9.0
---

# Import an Existing VMware Aria Automation Instance Into VCF Operations and Upgrade to VCF Automation 9.0

To upgrade to VCF Automation 9.0, you first import VMware Aria Automation into VCF Operations and then use VCF Operations to manage the upgrade to VCF Automation.

Before starting the import and upgrade:

- If your VMware Identity Manager certificate is due to expire within one year of date of import, replace the certificate. This allows VMware Aria Suite Lifecycle to retrust the VMware Identity Manager certificate within VMware Aria Automation before VMware Aria Automation is removed from VMware Aria Suite Lifecycle as part of the import process. See [Replace your Workspace ONE Access certificate by using VMware Aria Suite Lifecycle](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-suite-lifecycle/8-18/vmware-aria-suite-lifecycle-installation-upgrade-and-management-8-18/configuring-vmware-aria-suite-lifecycle/manage-certificates/replace-your-vidm-certificate.html). NOTE: Workspace ONE Access is another name for VMware Identity Manager.
- Because the upgrade introduces architectural changes that could affect existing cloud account and integration configurations, verify that that your environment does not include any unsupported endpoints by reviewing the precheck requirements and remediation steps outlined in [KB 389563](https://knowledge.broadcom.com/external/article/389563).
- Verify that the upgrade binaries for VCF Automation have been downloaded successfully. See [Downloading VCF Management Components into Binary Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).

## Import the Aria Automation 8.x Instance In VCF Operations 9.0

As part of the import process, you choose an Aria Automation instance to bring into VCF Operations. That is the instance that you will upgrade to VCF Automation 9.0.

On the Overview tab under Fleet ManagementLifecycle, click Add on the tile for VCF Automation. The import moves through the following stages.

1. Deployment Settings: Select Import from legacy Fleet Management.
2. VMware Aria Suite Lifecycle Configuration: Enter values for your existing legacy environment.

   - FQDN. The VMware Aria Suite Lifecycle FQDN that is managing the Aria Automation instance that you would like to upgrade.
   - Username: admin@local
   - Admin Password: Password for admin@local
   - Root Password: Root password for VMware Aria Suite Lifecycle.
3. Select Aria Automation Instance:

   Select the Aria Automation instance to be deployed. Only the first instance can be managed by this VCF Operations fleet management appliance. Any subsequent Aria Automation instances must be imported into other VCF Operations fleets or other VCF deployments.

   If multiple Aria Automation deployments exist, select the most critical deployment and click Next. For any additional Aria Automation deployments, repeat the import and upgrade process with a separate VCF Operations deployment.
4. Review

   - From VMware Aria Suite Lifecycle : FQDN of the Aria Suite Lifecycle legacy environment that the component is being imported from.
   - To VCF Operations: FQDN of the VCF Operations fleet that the component is being imported into.
   - Component VMware Aria Automation: FQDN of the Aria Automation instance that is to be imported and integrated.

After reviewing the details of the components and environments that are being integrated, check the box to consent to the integration and trigger the import of VMware Aria Automation into VCF Operations.

As the import process progresses, control of VMware Aria Automation is transferred from VMware Aria Suite Lifecycle to VCF Operations, and after the import completes, the Automation tile no longer appears in VMware Aria Suite Lifecycle .