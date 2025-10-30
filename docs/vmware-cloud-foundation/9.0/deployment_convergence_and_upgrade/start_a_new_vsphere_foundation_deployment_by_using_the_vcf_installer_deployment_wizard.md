---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-vmware-vsphere-foundation-using-the-deployment-wizard.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Start a New vSphere Foundation Deployment by Using the VCF Installer Deployment Wizard
---

# Start a New vSphere Foundation Deployment by Using the VCF Installer Deployment Wizard

You can use the VMware Cloud Foundation Installer deployment wizard to deploy a new VMware vSphere Foundation platform.

Download the required binaries for VMware vSphere Foundation. See [Downloading Binaries to VCF Installer](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance.html).

You can download and complete the Planning and Preparation Workbook to help plan and gather all the information required for a VMware vSphere Foundation deployment. See [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).

Use the VCF Installer deployment wizard to specify deployment information specific to your environment such as networks, hosts, and other information. The VMware vSphere Foundation software components are automatically deployed and configured using the information provided.

The following procedure describes how to deploy using the deployment wizard. You can also deploy using a custom JSON specification file. See [Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html) for more information.

To create a VMware vSphere Foundation environment using existing vSphere infrastructure, see [Converge a vCenter Instance and ESX Hosts to vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-vmware-vsphere-foundation-environment-using-the-deployment-wizard.html).

1. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN. 

   Enter the admin@local user and password you provided when you deployed the appliance and then click Log In.
2. Click Deployment WizardVMware vSphere Foundation .
3. Do not select any existing components.

   To use an existing vCenter to create a VMware vSphere Foundation environment, see [Converge a vCenter Instance and ESX Hosts to vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-vmware-vsphere-foundation-environment-using-the-deployment-wizard.html).
4. Enter the general configuration details for your deployment.

   Additional information:

   | Option | Description |
   | --- | --- |
   | Password creation | You can auto-generate passwords for newly installed appliances if you don't want to manually enter passwords. At the end of the deployment wizard, you can view the generated passwords. |
   | Customer Experience Improvement Program (CEIP) | Select an option to activate or deactivate CEIP across all deployed components.  VMware's Customer Experience Improvement Program (CEIP) collects technical information from participating customers to provide better support. For more information, see [Customer Experience Improvement Program](https://www.broadcom.com/company/legal/privacy/data-usage-programs/ceip). |
5. Enter the VCF Operations details.
6. Enter the vCenter details.
7. Choose a storage option and enter the storage details.

   Your selection determines the initial shared storage type for the primary cluster in the management domain.
8. Enter the ESX host details.

   The VCF Installer requires that all ESX hosts share a common password. If your ESX hosts have different passwords, you must deploy using a JSON specification file. See [Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html).
9. Enter details about the networks.

   To use the ESX Management Network information (gateway, VLAN, MTU) to create the VM Management Network distributed port group, select the checkbox. Otherwise, enter the information you want the VCF Installer to use to create a distributed port group for the VM Management Network.

   Specify IP inclusion ranges for the vSAN and vMotion networks of the management domain. IP addresses from the specified range are automatically assigned to hosts. Ensure that the IP ranges include sufficient IP addresses for the deployment. The number of IP addresses must be at least equal to the number of hosts deployed.

   As an example, if you specify the range start value as 192.168.1.1 and end as 192.168.1.20, a total of 20 IP addresses would be available. Do not use special IP addresses, such as the network or broadcast address.

   IPs for the vMotion Network must be part of the VLAN configured with the vMotion portgroup. IPs for the vSAN Network must be part of the VLAN configured for the vSAN portgroup. All IPs within the range must be available for use or IP conflicts will occur. It is a good practice to validate this prior to starting a deployment.
10. Enter the vSphere Distributed Switch details.

    | Option | Description |
    | --- | --- |
    | Default | This profile is recommended and the default configuration. It provides a unified fabric for all traffic types using a single vSphere Distributed Switch. |
    | Storage Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for storage traffic, while the other is used for all other traffic. |
    | NSX Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX (Virtual Networking) traffic, while the other is used for all other traffic. |
    | Storage Traffic and NSX Traffic Separation | This profile creates three vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX (Virtual Networking) traffic, the second switch is dedicated for storage traffic, while the third is used for all other traffic. |
    | Custom Switch Configuration | Create a custom vSphere Distributed Switch configuration. |
11. Review the deployment information.

    To make changes, navigate back to the relevant page in the deployment wizard. You can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage.
12. Review the validation information.

    The VCF Installer validates the information you provided in the deployment wizard and reports any errors or warnings.

    |  |  |
    | --- | --- |
    | Warnings | Review any warnings and either address them or click Acknowledge to proceed with deployment. |
    | Errors | Review all failed validations and resolve the issue(s) using the remediation information provided in the error message. You can navigate back to the relevant pages in the deployment wizard to make updates and then re-run the validations. You can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage. |
13. After addressing all validation errors and warnings, click Deploy.
14. Monitor the deployment progress.

    If there are errors, review the failed tasks in the Tasks panel, address the issue(s), and retry the deployment.
15. When the deployment completes successfully, you are ready for the next steps.

    - Download the JSON specification file for the deployment (optional).

      The JSON specification file does not include passwords.
    - Click Review Passwords to review the passwords.

      You can also retrieve the passwords using the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/credentials/) and [VCF Operations API](https://developer.broadcom.com/xapis/vmware-cloud-foundation-operations-api/latest/credentials/).
    - Open the VCF Operations UI to apply licensing. See [Registering VCF Operations with the VCF Business Services console](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations.html).
    - Register your vCenter instance in VCF Operations. See [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html).