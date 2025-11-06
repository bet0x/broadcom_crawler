---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-vmware-vsphere-foundation-environment-using-the-deployment-wizard.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Converge a vCenter Instance and ESX Hosts to vSphere Foundation Platform
---

# Converge a vCenter Instance and ESX Hosts to vSphere Foundation Platform

To successfully converge your existing vCenter instance and ESX hosts, you must ensure that you comply with the prerequisites, follow the procedure, and perform the next steps.

Verify that your existing configuration is supported and you satisfy the minimum component versions. See Supported Configurations in [Converging Existing Virtual Infrastructure to a VCF or a vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-.html).

| Item | vSphere Foundation 9.0.0 Requirements | vSphere Foundation 9.0.1 Requirements |
| --- | --- | --- |
| Minimum component versions prior to running the VCF Installer workflow | - VMware vCenter 9.0 - VMware ESX 9.0 | - VMware vCenter 8.0 Update 1a - VMware ESX 8.0 Update 1a |

During the procedure, you use VCF Installer to specify deployment information for your existing vCenter instance and ESX hosts, and to deploy VCF Operations to complete the converging to VMware vSphere Foundation platform.

You can download and complete the Planning and Preparation Workbook to help plan and gather all the information required for a VMware vSphere Foundation deployment.

You can use the VCF Installer deployment wizard or a custom JSON specification file. For more information, see [Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html).

If you have existing VMware vCenter, VMware ESX, and VMware Aria Operations instance, you manually upgrade the components to version 9.0.x. See [Upgrading the vCenter Appliance](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered), [Overview of the ESX Host Upgrade Process](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-0&language=&format=rendered), and [Upgrade to VCF Operations 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/upgrade-to-vcf-operations.html). Then you use VCF Operations to license and monitor your VMware vSphere Foundation platform.

1. Ensure your vCenter instance is running the supported version for your convergence scenario.
   - If you are converging to vSphere Foundation 9.0.0, your vCenter instance must be version 9.0 or later. See [Upgrading the vCenter Appliance](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered).
   - If you are converging to vSphere Foundation 9.0.1 and your vCenter instance is version 8.0 Update 1a or later, proceed without upgrading.
2. Ensure your ESX hosts are running the supported version for your convergence scenario.
   - If you are converging to vSphere Foundation 9.0.0, your ESX hosts must be version 9.0 or later. See [Overview of the ESX Host Upgrade Process](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-0&language=&format=rendered).
   - If you are converging to vSphere Foundation 9.0.1 and your ESX hosts are version 8.0 Update 1a or later, proceed without upgrading.
3. Deploy the VCF Installer appliance.

   See [Deploy the VMware Cloud Foundation Installer Appliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/deploy-the-vmware-cloud-foundation-installer-appliance.html).
4. Download bundles for the VCF Installer appliance.

   See [Downloading Binaries to the VCF Installer Appliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance.html).
5. Use VCF Installer to deploy your vSphere Foundation platform.
   1. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN.

      Enter the admin@local user and password you provided when you deployed the appliance and click Log In.
   2. Under Deploy, select Deployment WizardVMware vSphere Foundation.
   3. On the Existing Components page, select VMware vCenter.

      When you select an existing VMware vCenter infrastructure, the Storage, Hosts, Networks, and Distributed Switch pages of the wizard are not available.
   4. On the General information page, enter the configuration details for your deployment.

      Additional information:

      | Option | Description |
      | --- | --- |
      | Password creation | You can auto-generate passwords for newly installed appliances if you don't want to manually enter passwords. After a successful deployment, you can view the generated passwords. |
      | Customer Experience Improvement Program (CEIP) | Select an option to activate or deactivate CEIP across all deployed components.  VMware's Customer Experience Improvement Program (CEIP) collects technical information from participating customers to provide better support. See [Customer Experience Improvement Program](https://www.broadcom.com/company/legal/privacy/data-usage-programs/ceip) for more information. |
   5. On the VCF Operations page, enter the required details.
   6. On the vCenter page, enter the required details of your existing vCenter instance.

      VCF Installer validates your existing vCenter instance to ensure compatibility.

      An NSX Manager cannot be connected to the vCenter.
   7. On the Review page, review the deployment information.

      To make changes, navigate back to the relevant page in the deployment wizard. You can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage.
   8. On the Validate & Deploy page, review the validation information.

      The VCF Installer validates the information you provided in the deployment wizard and reports any errors or warnings.

      |  |  |
      | --- | --- |
      | Warnings | Review any warning messages. To proceed with your deployment, address the warnings or click Acknowledge. |
      | Errors | Use the Review all failed validations and resolve the issues by using the provided remediation information.  You can navigate back to the relevant pages in the deployment wizard to make updates and then re-run the validations. Alternatively, you can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage. |
   9. Click Deploy.

      - If there are errors during the deployment progress, review the failed tasks in the Tasks panel, address the issues, and retry the deployment.
      - You can download the JSON specification file for the deployment.

        The JSON specification file does not include passwords.
      - You can click Review Passwords to review the passwords.

- Deploy the remaining components to complete your vSphere Foundation platform. See [Deploying the VCF Operations for logs Appliance for VMware vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/vcf-operations-for-logs-for-vvf-clients.html) and [Deploying VCF Operations Orchestrator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/download-and-deploy-the-vco-va.html).
- License your vSphere Foundation environment. See [Licensing Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered).
- Register your vCenter instance in VCF Operations. See [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html).