---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/deregister-existing-client-configurations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Deregister Existing Component Configurations
---

# Deregister Existing Component Configurations

If you have configured components such as vCenter, NSX, VCF Operations, VCF Automation and so on as clients for VCF Single Sign-On, you can choose to deregister or remove these components from VCF Single Sign-On.

You can deregister the following component configurations:

- Deregister vCenter and NSX from VCF Single Sign-On. For more information, see [Deregister vCenter and NSX from VCF Single Sign-On](#GUID-87ec3c88-ff71-415a-a5d4-54fe1811a3d6-en_id-1b505789-4918-418f-8d83-5bbeffca3298).
- Deregister VCF Operations and/or VCF Automation, from VCF Single Sign-On. For more information, see [Deregister VCF Operations and/or VCF Automation from VCF Single Sign-On](#GUID-87ec3c88-ff71-415a-a5d4-54fe1811a3d6-en_id-cf39c675-744a-4852-9b77-a4c260f5b1b0).
- Modify VCF Operations and/or VCF Automation from VCF Single Sign-On. For more information see [Modify VCF Single Sign-On for VCF Operations and/or VCF Automation](#GUID-87ec3c88-ff71-415a-a5d4-54fe1811a3d6-en_id-9174ea1b-7ca6-45e4-e922-106766254be7).
- Deregister other components such as, VCF Operations HCX, VCF Operations for logs, VCF Operations for networks, and VCF Operations orchestrator from VCF Single Sign-On. For more information, see [Deregister VCF Single Sign-On for Other Components](#GUID-87ec3c88-ff71-415a-a5d4-54fe1811a3d6-en_id-99a72dc2-c822-48e2-d840-ee702e71ce82).

## Deregister vCenter and NSX from VCF Single Sign-On

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane on the right side, select the VCF Instance for which you have configured VCF Single Sign-On from the VCF Instances drop-down option.
3. From the Component Configuration tab on the right side, select the component you want to deregister and click the Deregister Component button.

## Deregister VCF Operations and/or VCF Automation from VCF Single Sign-On

If you have configured VCF Single Sign-On for the VCF Operations or VCF Automation, you can choose to deregister these appliances from VCF Single Sign-On. The change deactivates the previous authentication source and deletes the provisioned users and groups. This action cannot be reverted.

**To deregister VCF Single Sign-On for VCF Operations, perform the following steps:**

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select operations appliance.
3. Click Edit.
4. From the pop-up box that is displayed, click the VCF SSO Enabled toggle button to deactivate the configuration.

   The existing provisioned users and groups cannot be used in VCF Operations. Reassign the VCF Operations roles to the newly provisioned users and groups from the new authentication source.
5. Click Continue.

**To deregister VCF Single Sign-On for VCF Automation, perform the following steps:**

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane on the right side, select automation appliance.
3. Click Edit.
4. From the pop-up box that is displayed, click the VCF SSO Enabled toggle button to deactivate the configuration.

   The existing provisioned users and groups cannot be used in VCF Automation**.** Reassign the VCF Automation roles to the newly provisioned users and groups from the new authentication source.
5. Click Continue.

## Modify VCF Single Sign-On for VCF Operations and/or VCF Automation

If you have configured VCF Single Sign-On for VCF Operations and/or VCF Automation, you can choose to change the identity broker for these appliances. The change deactivates the previous authentication source and the existing provisioned users and groups cannot be used in VCF Automation. You have to reassign the VCF Automation and/or VCF Operations roles to the newly provisioned users and groups from the new authentication source. This action cannot be reverted.

**To modify VCF Single Sign-On for VCF Operations, perform the following steps:**

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select operations appliance.
3. Click Edit.
4. From the the pop-up box that is displayed, select a different identity broker from the Identity Broker drop down option.
5. Click Continue.

   The existing provisioned users and groups cannot be used in VCF Operations. Reassign the VCF Operations roles to the newly provisioned users and groups from the new authentication source.

**To modify VCF Single Sign-On for VCF Automation, perform the following steps:**

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane, select automation appliance.
3. Click Edit.
4. From the the pop-up box that is displayed, select a different identity broker from the Identity Broker drop down option.
5. Click Continue.

   The existing provisioned users and groups cannot be used in VCF Automation. Reassign the VCF Automation roles to the newly provisioned users and groups from the new authentication source.

## Deregister VCF Single Sign-On for Other Components

If you have configured VCF Single Sign-On for other components for such as VCF Operations for logs, VCF Operations for networks, VCF Operations HCX, and VCF Operations orchestrator , you can choose to deregister the component.

**Procedure**

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & Access.
2. From the Identity & Access pane on the right side, select VCF Other components.

   The list of generic components for which you have configured VCF Single Sign-On is listed.
3. Select the component you want to deregister and click Delete.

   Depending on the component for which this OIDC client was created, you can choose to delete the VCF Single Sign-On configuration from the respective component console for complete deregistration. For example, if this OIDC client was used to configure VCF Single Sign-On for VCF Operations HCX, after the client is deleted under VCF Other Components, log in to VCF Operations HCX as a local admin user and delete the VCF Single Sign-On configuration.