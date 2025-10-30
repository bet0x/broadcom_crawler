---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/creating-a-configuration-template.html#GUID-5c970def-f515-4db6-b6dd-d529e5170f8b-en
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Managing Configuration Templates in VCF Operations
---

# Managing Configuration Templates in VCF Operations

You can define a desired state based on your current environment using configuration templates. You can create, edit, or delete configuration templates in VCF Operations.

- If the target vCenter is not deployed as a part of the same VCF instance as the VCF Operations Console, ensure that the user is added to the vCenter Administrators group and that the account used to add vCenter to VCF Operations has administrator privileges.

  This applies only if you select user credentials when integrating a vCenter cloud account in VCF Operations. For more information, see [Configure a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html).
- Verify that the user has the required Configuration Drifts roles to access configuration templates. For more information, see the [Access Control: Roles Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/managing-user-access-control/access-control-overview/access-control-roles-tab.html).

  - Manage Privilege: for creating templates, assigning them to policy, and running configuration drift check.
  - View Privilege: for viewing template content and viewing existing configuration drifts.
- Verify that your cloud account has been assigned a collector group or a collector.

A configuration template is a set of configurations representing a desired state. A configuration template enables an administrator to define and monitor the configurations. The configuration schema defines the settings for the desired state.

The Configuration Templates tab provides an overview of all configuration templates, including the object type assigned to each template, description, number of policies assigned to each template, template author, and template creation date.

You can also manage configuration templates using a supported source control solution. For more information refer to [Managing Configuration Templates with Source Control](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/git.html).

1. To create a configuration template, from the left menu, click Fleet ManagementConfiguration Drifts and then click the Configuration Templates tab.
2. Click Create Config Template.
3. Enter a name and description for the configuration template.
4. On the Template Setup tab, select a Configuration Source vCenter from which you want to extract the configuration settings and click Next.
5. On the Configuration Schema tab, select the configuration settings that you want to include in your template and click Next.
6. (Optional) - On the Assign vCenters using Policy (Optional) tab select one or more VCF Operations policies to assign to your configuration template and then click Next.

   Assign a policy to the configuration template. If you have not assigned any policies during the configuration template creation process, follow the steps below:

   1. From the left navigation menu, click Infrastructure OperationsConfigurationsPolicy Definition.
   2. Select the policy you want to assign.
   3. Select Configuration Templates.
   4. Click on the Edit icon and select the template you want to activate.
   5. Click the drop down and click Activated to assign the configuration template for the policy.
   6. Click Save.
7. On the Review tab, a preview of your configuration template is displayed in the right pane. Review the configuration template and then click Create.

You can view the template listed on the Configuration Templates tab. You can also edit or delete the configuration template from the same page.