---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-a-new-vcf-fleet-or-a-new-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Start a New VCF Fleet or a New VCF Instance Deployment by Using the VCF Installer Deployment Wizard
---

# Start a New VCF Fleet or a New VCF Instance Deployment by Using the VCF Installer Deployment Wizard

You can use the VCF Installer deployment wizard to deploy a new VCF fleet or deploy a new VCF Instance within an existing fleet.

- Download the required binaries for VCF. See [Downloading Binaries to VCF Installer](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance.html).
- To deploy a new VCF instance in existing VCF fleet, you select your VCF Operations instance as existing for the new deployment.

You can download and complete the Planning and Preparation Workbook to help plan and gather all the information required for deployment. See [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html). If you plan to use an existing VCF Operations instance in your deployment, enter information about that instance in the workbook.

A VCF fleet refers to an environment consisting of one or more VCF instances and standalone vCenter instances that are managed by the same VCF Operations instance. When you deploy the first VCF instance in a VCF fleet, you can deploy a new VCF Operations instance or connect to an existing one. When you expand a VCF fleet with an additional VCF instance, you must connect to an existing VCF Operations instance.

Use the VCF Installer deployment wizard to specify deployment information specific for your environment such as networks, hosts, and other information. The VMware Cloud Foundation platform is automatically deployed and configured using the information provided.

The following procedure describes how to deploy using the deployment wizard. You can also deploy using a JSON specification file. See [Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html) for more information.

1. In a web browser, log in to the VMware Cloud Foundation Installer appliance administration interface: https://installer\_appliance\_FQDN. 

   Enter the admin@local user and password you provided when you deployed the appliance and then click Log In.
2. Click Deployment WizardVMware Cloud Foundation .
3. Select what you want to deploy.

   - A new VCF fleet
   - A VCF Instance in an existing VCF fleetSome of the options in the following steps will be different depending on which option you select.
4. Select the existing components.

   | Component | New VCF Fleet | VCF Instance in an existing VCF fleet |
   | --- | --- | --- |
   | VCF Operations | Select this option to connect the VCF fleet to an existing VCF Operations instance. Otherwise a new VCF Operations instance is deployed.  If you select a VCF Operations instance that is connected to a VCF Operations fleet management appliance or aVCF Automation instance, these components will also be added to this VCF fleet. | n/a  You connect to your existing VCF Operations later in the deployment wizard. |
   | VMware vCenter | Do not select. To use an existing vCenter, see [Deploy Components by Using VCF Installer to Complete the Converging to VCF Process](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-new-vcf-fleet-or-a-new-vcf-instance-using-the-deployment-wizard.html). | Do not select. To use an existing vCenter, see [Deploy Components by Using VCF Installer to Complete the Converging to VCF Process](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-new-vcf-fleet-or-a-new-vcf-instance-using-the-deployment-wizard.html). |

   The VCF Installer validates the selected components to ensure that they are compatible.
5. Enter the general configuration details for your deployment.

   Additional information:

   | Option | Description |
   | --- | --- |
   | VCF Instance Name | The VCF Instance Name is used to provide a unique name when creating the VMware Cloud Foundation Adapter within VCF Operations. A descriptive name provides for easy identification when you have multiple VCF Instances. |
   | Management domain name | This name is used as prefix for the default names of objects created or deployed by the VCF Installer. You can change these default names as you progress through the deployment wizard. |
   | Custom networking configuration for VCF Operations and VCF Automation | By default, the VCF Installer configures all VCF Operations and VCF Automation appliances to use the same distributed virtual port group (DVPG) as vCenter.  To specify a different configuration, select the checkbox and perform a custom deployment of VCF Operations and VCF Automation after VCF Installer deploys the other components. See [Deploying VCF Management Components with Custom Networking](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking.html).  This option is not available when deploying a VCF Instance in an existing VCF fleet or when using an existing VCF Operations instance. |
   | Deployment model | You can choose the deployment model for any new appliances that get deployed. High Availability (Three-node) is recommended for production environments. The deployment model that you select does not impact existing appliances that you are using in your VCF fleet or VCF Instance. See the VMware Cloud Foundation [Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html) documentation for more information. New appliances that get deployed are automatically configured to comply with Federal Information Processing Standards (FIPS). |
   | Password creation | If you don't want to manually enter passwords for newly installed appliances, you can auto-generate passwords. For auto-generated passwords, the complexity is the following.  - Length = 20 characters - Minimum special characters = 1 - Minimum numbers = 1 - Minimum upper case letters = 1 - Minimum lower case letters = 0 - Allowed special characters = '!', '@', '#', '$', '^' - Maximum consecutive characters= 2 After a successful deployment, you can view the generated passwords. |
   | Customer Experience Improvement Program (CEIP) | Select an option to activate or deactivate CEIP across all deployed components.  VMware's Customer Experience Improvement Program (CEIP) collects technical information from participating customers to provide better support. See [Customer Experience Improvement Program](https://www.broadcom.com/company/legal/privacy/data-usage-programs/ceip) for more information. |
6. Enter the VCF Operations details.

   | I'm deploying... | Details |
   | --- | --- |
   | A new VCF fleet with a new VCF Operations instance | Enter all the required information. |
   | A new VCF fleet with an existing VCF Operations instance | - Connect to your existing VCF Operations instance. - If a VCF Operations fleet management appliance is connected to the VCF Operations instance, enter the administrator password. - If no VCF Operations fleet management appliance is connected to the VCF Operations instance, enter the required information to deploy a new one. - Enter details for the new VCF Operations collector appliance. |
   | A new VCF instance with an existing VCF Operations instance | Connect to the VCF Operations instance that manages the VCF fleet in which you want to deploy this VCF Instance. After connecting, enter details for the new VCF Operations collector appliance.  The existing VCF Operations instance must be connected to VCF Automation and VCF Operations fleet management. |

   This page does not appear if you selected the custom networking option for VCF Operations and VCF Automation.
7. Enter the VCF Automation details.

   Select the I want to connect a VCF Automation instance later checkbox if you want to use an existing Aria Automation 8.x instance that needs to be upgraded to to VCF Automation 9.0. When deployment is complete, upgrade Aria Automation to VCF Automation and then use VCF Operations to import the VCF Automation instance. See [Import an Existing VMware Aria Automation Instance Into VCF Operations and Upgrade to VCF Automation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html).

   If a VCF Automation instance is connected to the VCF Operations instance, the appliance FQDN is displayed and you must enter the root password.

   This screen does not appear if you selected the custom networking option for VCF Operations and VCF Automation.

   When creating a new VCF Automation instance in a High Availability deployment, you must specify 4 node IP addresses. Three of the IP addresses are used for active nodes and the fourth IP address is used when recreating a node for upgrade purposes. The node IPs do not require DNS records.
8. Enter the vCenter details.
9. Enter the NSX Manager details.
10. Choose a storage option and enter the storage details.

    Your selection determines the initial shared storage type for the default cluster in the management domain. This initial shared storage type is known as principal storage. Once created, the principal storage type for a cluster cannot be changed. However, you can add additional clusters with different principal storage types to the management domain later.

    Option | Details || vSAN | - Select vSAN ESA or vSAN OSA. - Enter a name for the vSAN datastore or use the pre-populated name. |
    | VMFS on Fibre Channel (FC) | Enter a name for the VMFS on FC datastore or use the pre-populated name.  The datastore must already be created and mounted on all ESX hosts. |
    | NFS v3 | - Enter a name for the NFS v3 datastore or use the pre-populated name. - Enter the path to the NFS share. - Enter the IPv4 address of the NFS server. - (optional) Choose to bind the NFS datastore to the VMkernel adapter specified when the datastore gets created. Indicates whether to bind the created NFS datastore to the VMkernel NIC created based on NFS Network Spec. This is to prevent unintentional flow of NFS traffic through any other VMkernel NIC, if such connectivity exists. The NFS Server must already be created and meet the NFS Storage Guidelines and Requirements found in the [vSphere Storage Guide](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-storage.html). |
11. Enter the ESX host details.

    ESX hosts require passwords with predefined requirements. For more information, see [ESX Passwords and Account Lockout](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-installation-and-setup/installing-and-setting-up-esxi/esxi-requirements/esxi-passwords-and-lockout.html).

    The VCF Installer requires that all ESX hosts share a common password. If your ESX hosts have different passwords, you must deploy using a JSON spec. See [Use a JSON Specification File to Deploy VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/use-a-json-specification-to-deploy-vmware-cloud-foundation-or-vmware-vsphere-foundation.html).
12. Enter details about the networks.

    To use the ESX Management Network information (gateway, VLAN, MTU) to create the VM Management Network distributed port group, select the checkbox. Otherwise, enter the information you want the VCF Installer to use to create a distributed port group for the VM Management Network.

    Specify IP inclusion ranges for the vSAN and vMotion networks of the management domain. IP addresses from the specified range are automatically assigned to ESX hosts. Ensure that the IP ranges include sufficient IP addresses for the deployment. The number of IP addresses must be at least equal to the number of ESX hosts deployed.

    As an example, if you specify the range start value as 192.168.1.1 and end as 192.168.1.20, a total of 20 IP addresses would be available. Do not use special IP addresses, such as the network or broadcast address.

    IPs for the vMotion Network must be part of the VLAN configured with the vMotion portgroup. IPs for the vSAN Network must be part of the VLAN configured for the vSAN portgroup. All IPs within the range must be available for use or IP conflicts will occur. It is a good practice to validate this prior to starting a deployment.
13. Enter the vSphere Distributed Switch details.

    | Option | Description |
    | --- | --- |
    | Default | This profile is recommended. It provides a unified fabric for all traffic types using a single vSphere Distributed Switch. |
    | Storage Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for storage traffic, while the other is used for all other traffic. |
    | NSX Traffic Separation | This profile creates two vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX Edge and overlay traffic, while the other is used for all other traffic. |
    | Storage Traffic and NSX Traffic Separation | This profile creates three vSphere Distributed Switches with separate physical NICs. One switch is dedicated for NSX Edge and overlay traffic, the second switch is dedicated for storage traffic, while the third is used for all other traffic. |
    | Custom Switch Configuration | Copy from a preconfigured profile or create a new distributed switch configuration. Multiple vSphere Distributed Switches can be configured. Each vSphere Distributed Switch can hold one or more network traffic configurations.  Some network traffic types are mandatory. Switch configuration is incomplete until these mandatory traffic types are configured.  Management, vMotion, vSAN and NSX-Overlay network types can be configured only once for a cluster.  NSX-VLAN and Public network traffic types can be configured in multiple vSphere Distributed Switches. |
14. Enter the SDDC Manager details. 

    If VCF Installer is deployed on one of the management domain ESX hosts, details populate automatically.
15. Review the deployment information.

    To make changes, navigate back to the relevant page in the deployment wizard. You can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage.
16. Review the validation information.

    VCF Installer validates the information you provided in the deployment wizard and reports any errors or warnings.

    |  |  |
    | --- | --- |
    | Warnings | Review any warnings and either address them or click Acknowledge to proceed with deployment. |
    | Errors | Review all failed validations and resolve the issue(s) using the remediation information provided in the error message. You can navigate back to the relevant pages in the deployment wizard to make updates and then re-run the validations. You can also download the JSON specification file, make the necessary changes, and then upload the modified JSON specification file from the VCF Installer homepage. |
17. After addressing all validation errors and warnings, click Deploy.
18. Monitor the deployment progress.

    If there are errors, review the failed tasks in the Tasks panel, address the issue(s), and retry the deployment.
19. When the deployment completes successfully, you are ready for the next steps.

    - Download the JSON specification file for the deployment (optional).

      The JSON specification file does not include passwords.
    - Click Review Passwords to review the passwords.

      You can also retrieve the passwords using the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/credentials/) and [VCF Operations API](https://developer.broadcom.com/xapis/vmware-cloud-foundation-operations-api/latest/credentials/).
    - Open the VCF Operations UI to apply licensing. See [Registering VCF Operations with the VCF Business Services console](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations.html).