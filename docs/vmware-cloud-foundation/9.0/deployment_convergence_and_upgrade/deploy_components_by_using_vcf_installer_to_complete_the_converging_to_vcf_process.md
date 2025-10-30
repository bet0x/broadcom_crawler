---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-new-vcf-fleet-or-a-new-vcf-instance-using-the-deployment-wizard.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy Components by Using VCF Installer to Complete the Converging to VCF Process
---

# Deploy Components by Using VCF Installer to Complete the Converging to VCF Process

By using VMware Cloud Foundation Installer, you use your existing vSphere and Aria infrastructure to converge it to a new VCF fleet or a new VCF Instance in an existing VCF fleet. During the process, VCF Installer deploys all required components that you do not have in your existing environment and uses your vCenter instance and ESX hosts to create the management domain for the new instance.

Verify that you meet the requirements and have completed the pre-requisite tasks based on your converge scenario. See [Supported Scenarios to Converge to VCF](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/supported-scenarios-to-converge-to-vcf.html).

A VCF fleet refers to an environment consisting of one or more VCF Instances and standalone vCenter instances that are managed by the same VCF Operations instance. If you have a VCF fleet, you can converge your infrastructure to a new VCF Instance within the fleet by connecting to your existing VCF Operations instance or you can deploy a new VCF Operations instance to create a new VCF fleet. If you have an existing VCF Operations instance, you can also use it to create a new VCF fleet.

You can use the VCF Installer deployment wizard or a custom JSON specification file. For more information, see [Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html).

1. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN.

   Enter the admin@local user and password you provided when you deployed the appliance and click Log In.
2. Under Deploy, select Deployment WizardVMware Cloud Foundation .
3. Select Deploy a new VCF fleet or Deploy a VCF Instance in an existing VCF fleet.
4. On the Existing Components page, select your existing infrastructure components.

   When you connect to your existing components, VCF Installer validates them to ensure compatibility.

   When you select an existing VMware vCenter infrastructure, the Storage, Hosts, Networks, and Distributed Switch pages of the wizard are not available.
5. On the General information page, enter the configuration details for your deployment.

   | Option | Description |
   | --- | --- |
   | VCF Instance Name | The VCF Instance Name is used to provide a unique name when creating the VMware Cloud Foundation Adapter within VCF Operations. A descriptive name provides for easy identification when you have multiple VCF Instances. |
   | Management domain name | This name is used as prefix for the default names of objects created or deployed by the VCF Installer. You can change these default names as you progress through the deployment wizard. |
   | Custom networking configuration for VCF Operations and VCF Automation | By default, the VCF Installer configures all VCF Operations and VCF Automation appliances to use the same distributed virtual port group (DVPG) as vCenter.  To specify a different configuration, select the checkbox and perform a custom deployment of VCF Operations and VCF Automation after VCF Installer deploys the other components. See [Deploying VCF Management Components with Custom Networking](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking.html).  This option is not available when deploying a VCF Instance in an existing VCF fleet or when using an existing VCF Operations instance. |
   | Deployment model | You can choose the deployment model for any new appliances that get deployed. High Availability (Three-node) is recommended for production environments. The deployment model that you select does not impact existing appliances that you are using in your VCF fleet or VCF Instance. See the VMware Cloud Foundation [Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html) documentation for more information. New appliances that get deployed are automatically configured to comply with Federal Information Processing Standards (FIPS). |
   | Password creation | You can auto-generate passwords for newly installed appliances if you don't want to manually enter passwords. After a successful deployment, you can view the generated passwords. |
   | Customer Experience Improvement Program (CEIP) | Select an option to activate or deactivate CEIP across all deployed components.  VMware's Customer Experience Improvement Program (CEIP) collects technical information from participating customers to provide better support. See [Customer Experience Improvement Program](https://www.broadcom.com/company/legal/privacy/data-usage-programs/ceip) for more information. |
6. On the VCF Operations page, enter the required details.

   | Scenario | Details |
   | --- | --- |
   | A new VCF fleet with a new VCF Operations instance | Enter all the required information. |
   | A new VCF fleet with an existing VCF OperationsVCF Operations instance | 1. Connect to your existing VCF Operations instance, provide the required details, and confirm the certificate thumbprint.     - If a VCF Operations fleet management appliance is connected to the VCF Operations instance, enter the administrator password.    - If no VCF Operations fleet management appliance is connected to the VCF Operations instance, enter the required information to deploy a new one. 2. Enter details for the new VCF Operations collector appliance. If you use a Load Balancer, verify that you use the Primary node IP. |
   | A new VCF Instance with an existing VCF Operations instance | 1. Connect to the VCF Operations instance that manages the VCF fleet in which you want to deploy this VCF Instance. 2. Enter details for the new VCF Operations collector appliance. Your existing VCF Operations instance must be connected to VCF Automation and VCF Operations fleet management. |

   The VCF Operations page does not appear if you selected the Advanced: Custom networking configuration for VCF Operations and VCF Automation check box.
7. If you deploy a new VCF fleet without existing VCF Operations, on the VCF Automation page, enter the required details.

   If a VCF Automation instance is connected to the VCF Operations instance, the appliance FQDN is displayed and no additional information is required.

   The VCF Automation page does not appear if you selected Advanced: Custom networking configuration for VCF Operations and VCF Automation check box on the General information page or if VCF Automation is not discovered within your VCF Operation instance.

   When creating a new VCF Automation instance in a High Availability deployment, you must specify 4 node IP addresses. Three of the IP addresses are used for active nodes and the fourth IP address is used when recreating a node for upgrade purposes. The node IPs do not require DNS records.
8. On the vCenter page, enter the required details of your existing vCenter instance.
9. On the NSX Manager page, enter the required details for NSX Manager appliance.

   If you selected an existing VMware NSX Manager on the Existing Components page, the NSX Manager page is not available.
10. On the SDDC Manager page, enter the required details.
11. On the Review page, review the deployment information.

    To make changes, navigate back to the relevant page in the deployment wizard. You can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage.
12. On the Validate & Deploy page, review the validation information.

    The VCF Installer validates the information you provided in the deployment wizard and reports any errors or warnings.

    |  |  |
    | --- | --- |
    | Warnings | Review any warning messages. To proceed with your deployment, address the warnings or click Acknowledge. |
    | Errors | Use the Review all failed validations and resolve the issues by using the provided remediation information.  You can navigate back to the relevant pages in the deployment wizard to make updates and then re-run the validations. Alternatively, you can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage. |
13. Click Deploy.

- If there are errors during the deployment progress, review the failed tasks in the Tasks panel, address the issues, and retry the deployment.
- You can download the JSON specification file for the deployment.

  The JSON specification file does not include passwords.
- Click Review Passwords to review the passwords. You can also retrieve the passwords using the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/credentials/) and [VCF Operations API](https://developer.broadcom.com/xapis/vmware-cloud-foundation-operations-api/latest/credentials/).