---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Linking vCenter instances in VCF Operations
---

# Linking vCenter instances in VCF Operations

vCenter linking in VCF Operations provides you with a single pane of glass view of all the linked vCenter instances from a single vSphere Client.

- Verify that you have vCenter version 9.0 or later.
- Ensure that there is functioning forward and reverse DNS resolution between all vCenter instances in a vCenter linking group.
- Ensure that the user used to register the vCenter account in VCF Operations has Administrator privileges.

  This applies only if you select user credentials when integrating the vCenter cloud account in VCF Operations. For more information, see [Configure a vCenter Account in VCF Operations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html)
- Verify that the user has the required vCenter Linking role assigned to access the vCenter instances. For more information, see the [Access Control: Roles Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/managing-user-access-control/access-control-overview/access-control-roles-tab.html).

  - Manage: To add, edit, or delete the vCenter linking group.
  - View Privilege: To view the vCenter linking group and its members.
- Ensure that common Identity Providers (IDP) is configured on all vCenter systems. For more information, see [Identity Providers and Protocols Supported for VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/protocols-suported-for--sso.html).
- Ensure that the IDP user has the required permission for each vCenter system.

  IDP user permissions are not shared between vCenter systems and must configured on each vCenter individually.
- Verify that the vCenter systems are not part of an Enhanced Link Mode group.

  From VMware Cloud Foundation 9.0 onward, its recommended to use vCenter linking for vSphere Client single pane of glass functionality instead of Enhanced Linked Mode (ELM). If a vCenter system is part of ELM, it cannot be added to a vCenter linking group. You must deactivate ELM before proceeding. To deactivate ELM, see [How to Deactivate Enhanced Link Mode in vCenter Without Configuration Loss](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime.html).

You can link a minimum of two and a maximum of 15 vCenter instances in a group. All the vCenter instances in a linked group must be configured with common IDP users. Once linked, you can log into any one of the linked vCenter instances using the vSphere Client, and monitor and manage the inventories of all the linked vCenter instances.

1. From the left menu, click Infrastructure OperationsConfigurations.
2. Under Logical Groupings, click vCenter Linking.
3. Click Create Group.
4. Enter the Group Name and Description, and then click Next.
5. Select the compatible vCenter instances that you want to add to the group and then click Next.

   You can view the list of compatible and incompatible vCenter systems.

   - Compatible: vCenter systems that meet the version prerequisite and are not part of any other vCenter linking group.
   - Incompatible: vCenter systems that do not meet the version prerequisite or belong to another vCenter linking group.
6. Review your selection and click Finish.

   The vCenter linking group is created.
7. If the status of any of the vCenter instances shows an error, fix the cause, and then click Reset Linking to troubleshoot.

   Some of the common errors you may face and fix before you click Reset Linking as as follows:

   - vCenter is not reachable from VCF Operations: You must fix the connection between VCF Operations and vCenter.
   - vCenter is part of Enhanced Linked Mode (ELM): You must deactivate ELM.
8. After the group is created, you can add or remove members from a group and you can also edit the group details or delete the group.

You can log in to any vSphere Client for any one of the linked vCenter systems using the IDP user that has the required permissions for all vCenter systems and view the inventory of all the vCenter systems in the group.