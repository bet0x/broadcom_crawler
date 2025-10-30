---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/additional-configurations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Additional Component Configurations
---

# Additional Component Configurations

You can connect additional vCenter and NSX components to the VCF Identity Broker for Single Sign-On-based access. You can also connect additional VCF components such as VCF Operations for logs, VCF Operations for networks, and VCF Operations HCX to the VCF Identity Broker for Single Sign-On-based access.

**Procedure**

- Add additional vCenter and NSX components
- From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
- From the Identity & Access pane, navigate to VCF Instances and select the relevant VCF Instance for which you have configured VCF Single Sign-On.
- Select the Component Configuration tab on the right side, and in the grid below, use the filter and search for components that are 'Not Configured'. Select them and click Configure Component.
- Add additional components like VCF Operations for logs, VCF Operations for networks, and VCF Operations HCX
- From the Identity & Access pane, navigate to VCF Other Components and follow the steps in [Step 6: (Optional) Configure VCF Single Sign-On for other VCF Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/configure-vmware-cloud-foundation-sso--as-a-client-for-other-components.html#GUID-f9656887-2632-4d33-88e8-a7989b2b5221-en_id-a9b269b6-1c1d-49d2-953a-78cc84e4a4c4).

  As an administrator, after you complete configuring VCF Single Sign-On in the VCF Operations console, you must log in to the individual components such as, vCenter , NSX, and others and assign the required roles and permissions for users or groups. For more information, see [Step 7. Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html#GUID-40a7ccb8-1e83-4926-b7ef-2365a865f889-en_id-5e7caad9-e3b7-41d2-f85d-f7cf7a76a0d5).