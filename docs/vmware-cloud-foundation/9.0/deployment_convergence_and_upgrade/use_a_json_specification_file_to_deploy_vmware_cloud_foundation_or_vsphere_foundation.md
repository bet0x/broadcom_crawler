---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation
---

# Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation

VCF Installer can deploy your platform by using a JSON file instead of the deployment wizard.

Download the required binaries for VMware Cloud Foundation or VMware vSphere Foundation. See [Downloading Binaries to VCF Installer](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance.html).

You can download and complete the Planning and Preparation Workbook to help plan and gather all the information required for a VCF or VMware vSphere Foundation deployment. See [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html). If you plan to use any existing components in your deployment, enter information about those components in the workbook.

A JSON specification file can be used to:

- Deploy a new VCF fleet
- Deploy a new VCF Instance
- Converge existing vSphere infrastructure to a new VCF fleet
- Converge existing vSphere infrastructure to a new VCF Instance
- Deploy a new vSphere Foundation platform
- Converge existing vSphere infrastructure to a new vSphere Foundation platform

Using a JSON specification file allows for additional levels of customization that are not available in the deployment wizard. For example, the deployment wizard assumes that your ESX hosts share the same root password. If your ESX hosts have different root passwords, use the JSON specification file to deploy your environment.

In addition, if you are deploying multiple platforms, you may find it easier to start with an existing JSON specification file and modify it for additional deployments.

See the [VMware Cloud Foundation Installer API Reference Guide](https://developer.broadcom.com/xapis/vcf-installer-api/latest/) for information about the properties and parameters you can use to create a JSON specification file. For reference, see the following [example JSON file](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/dita/vmware/vcf/vcf-90/installation/resources/domainSpec-sfo-m01-example01.json) with predefined values.

The following table provides some guidance on certain properties you should specify, depending on the type of environment you want to create and what existing components you are using:

| I want to... | workflowType property | VCF Operations  vcfOperationsSpec  useExistingDeployment property | VMware vCenter vcenterSpec  useExistingDeployment property | VCF Operations fleet management  vcfOperationsFleetManagementSpec  useExistingDeployment property | VCF Automation  vcfAutomationSpec  useExistingDeployment property | NSX Manager nsxtSpec  useExistingDeployment property |
| --- | --- | --- | --- | --- | --- | --- |
| Deploy a new VCF fleet | VCF | optional (true or false) | false | optional (true or false) | optional (true or false) | n/a |
| Deploy a new VCF instance | VCF\_EXTEND | true | false | true | true | n/a |
| Converge existing vSphere infrastructure to a new VCF fleet | VCF | optional (true or false) | true | optional (true or false) | optional (true or false) | false |
| Converge existing vSphere infrastructure to a new VCF instance | VCF\_EXTEND | true | true | true | true | false |
| Deploy a new vSphere Foundation platform | VVF | false | false | n/a | n/a | n/a |
| Converge existing vSphere infrastructure to a new vSphere Foundation platform | VVF | false | true | n/a | n/a | n/a |

1. Refer to the VMware Cloud Foundation Installer API Reference Guide to create a JSON specification file using the information from your Planning and Preparation Workbook.
2. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN. 

   Enter the admin@local user and password you provided when you deployed the appliance and then click Log In.
3. Click Deploy Using JSON Spec and upload the file.
4. Review the Summary and JSON Preview and click Next.
5. Review the validation information.

   The VCF Installer validates the information you provided in the JSON specification and reports any errors or warnings.

   |  |  |
   | --- | --- |
   | Warnings | Review any warnings and either address them or click Acknowledge to proceed with deployment. |
   | Errors | Review all failed validations and resolve the issue(s) using the remediation information provided in the error message. You can modify and reupload the JSON specification file. |
6. After addressing all validation errors and warnings, click Deploy.
7. Monitor the deployment progress.

   If there are errors, review the failed tasks in the Tasks panel, address the issue(s), and retry the deployment.
8. When the deployment completes successfully, you are ready for the next steps.

   - Download the JSON specification file for the deployment (optional).

     The JSON specification file does not include passwords.
   - Click Review Passwords to review the passwords.

     You can also retrieve the passwords using the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/credentials/) and [VCF Operations API](https://developer.broadcom.com/xapis/vcf-operations-api/latest/credentials/).
   - Open the VCF Operations UI to apply licensing and perform other post-deployment configuration.