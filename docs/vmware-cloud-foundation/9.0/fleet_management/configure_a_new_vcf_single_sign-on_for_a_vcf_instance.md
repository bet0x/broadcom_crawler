---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configure a New VCF Single Sign-On for a VCF Instance
---

# Configure a New VCF Single Sign-On for a VCF Instance

You can configure VCF Single Sign-On across components within a single VCF Instance, across a set of VCF Instances, and/or across an entire VCF fleet of VCF Instances.

Ensure that you have completed the prerequisites and read the list of important points to consider before you set up VCF Single Sign-On. For more information, see [Points to Consider and Prerequisites while Setting up Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso.html#GUID-ec2c7e12-e532-46bf-b08f-6de789b83e3c-en_id-3bbe57a7-fc88-42f2-99c7-f6b50f9a8a51).

The following flowchart describes the high-level steps to configure VCF Single Sign-On.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5c1c6bf3-d17f-4422-8e80-a4795277cad7.original.svg)

Follow these high-level steps to configure VCF Single Sign-On:

1. **Select a VCF Instance for which you want to configure VCF Single Sign-On.**

   For more information, see [Step 1: Select a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/select-a-vcf-instance.html).
2. **Choose the deployment mode you wish to use.**

   Select whether you want to use the VCF Identity Broker embedded or the VCF Identity Broker appliance deployment mode. For information about selecting a deployment mode, [Step 2: Choose the Deployment Mode](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/choose-the-deployment-mode.html).
3. **Select and configure the identity provider.**

   Set up your preferred identity provider using modern or directory-based authentication. For more information, see [Step 3: Configure an Identity Provider](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/cofigure-vmware-cloud-foundation-identity-provider.html).
4. **Configure VCF Single Sign-On for NSX and vCenter.**

   For more information, see [Step 4: Configure VCF Single Sign-On for NSX and vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/connect-components.html).
5. **Configure VCF Single Sign-On for VCF Operations and VCF Automation.**

   Connect the components to the VCF Identity Broker for Single Sign-On-based access. For more information, see [Step 5: Configure VCF Single Sign-On for VCF Operations and VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/configure-vmware-cloud-foundation-sso-for-the-operations-and-automation-appliance(1).html#GUID-8462e8c0-2ec4-4bde-97e7-6a7387a7daf6-en_id-38e6282c-8001-49df-a075-d36085457703).
6. **(Optional) Configure VCF Single Sign-On for other VCF Components.**

   Connect the components for Single Sign-On-based access. For more information, [Step 6: (Optional) Configure VCF Single Sign-On for other VCF Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/configure-vmware-cloud-foundation-sso--as-a-client-for-other-components.html#GUID-f9656887-2632-4d33-88e8-a7989b2b5221-en_id-a9b269b6-1c1d-49d2-953a-78cc84e4a4c4).
7. **Assign required roles and permissions for users or groups.**

   For more information, see [Step 7. Assigning Roles and Permissions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/assigning-roles-and-permissions.html).