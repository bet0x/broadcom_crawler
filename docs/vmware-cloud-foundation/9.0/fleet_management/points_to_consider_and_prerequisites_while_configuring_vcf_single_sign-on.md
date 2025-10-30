---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Points to Consider and Prerequisites while Configuring VCF Single Sign-On
---

# Points to Consider and Prerequisites while Configuring VCF Single Sign-On

When you configure VCF Single Sign-On in VCF Operations, it is essential that you read and understand the following important points and ensure that you carry out the prerequisites.

## Points to Consider While Setting Up VCF Single Sign-On

- **SDDC Manager UI Client authentication is not compatible with VCF Single Sign-On**

  After you configure VCF Single Sign-On in the management domain vCenter, administrators are no longer able to log in to the SDDC Manager UI client with Single Sign-On users.

  - SDDC Manager UI will support logins only with local admin accounts such as @vsphere.local users.
  - The SDDC Manager APIs will support logins with VCF Single Sign-On users.
- **VCF Single Sign-On is not compatible with Enhanced Linked Mode (ELM)**

  Before you configure VCF Single Sign-On, you must deactivate ELM on all participating vCenter Instances. For more information, see [Deactivate Enhanced Link Mode from vCenter Using the cmsso-util break-elm Utililty](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime.html#GUID-de9c79e6-1990-4d11-b417-69f5b7b05f8b-en_id-15563a06-f0af-4aef-fe13-77bf898f7214). If you upgraded from VMware Cloud Foundation 5.x to 9.0, see [Deactivate Enhanced Link Mode (ELM) Using the SDDC Manager API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/deactivate-enhanced-link-mode--elm--for-upgraded-vmware-cloud-foundation-vcenters.html).
- **Manage VCF Single Sign-On only from VCF Operations and not from the individual components**

  After you configure VCF Single Sign-On from VCF Operations, you will not be able to configure any identity sources in vCenter Instances that are configured for VCF Single Sign-On.
- **PowerCLI impact**

  - PowerCLI automations will continue to work if the identity provider is configured in the management domain vCenter in embedded mode.
  - If the identity provider is configured in an alternate management domain vCenter or in appliance mode, the integration needs to be re-performed. Follow the steps in [Using Single Sign-On for PowerCLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/configure-vmware-cloud-foundation-sso--as-a-client-for-other-components/vcf-single-sign-on-for-powercli.html#GUID-8d03903c-dc78-472b-86ab-1abc6faaa2cb-en_id-9e711147-5c4d-4947-87e3-0ddcf3984a77).
- **Users configuring VCF Single Sign-On in VCF Operations must have access to all objects**

  The 'All Objects' scope must be assigned in VCF Operations. Navigate to AdministrationControl PanelAccess ControlUser Accounts/User Groups and assign the 'All Objects' scope to the required user/group.
- **Behavior of identity and access management after setting up VCF Single Sign-On**

  - The management layer of VCF Single Sign-On will always be in the VCF Operations console.
  - You can connect a standalone vCenter directly either to an identity provider that is configured within a vCenter or integrate them as part of VCF Single Sign-On using the VCF Identity Broker in VCF Operations. However, after a vCenter is configured for Single Sign-On, you must manage its configuration in VCF Operations and not directly in the vCenter.
- **VCF Components**

  - **vCenter:** After you configure VCF Single Sign-On, any existing identity provider configurations in the participating vCenter will be overridden by the VCF Single Sign-On configuration. You may be required to perform role assignments to the required users and groups again to ensure continued access.

    **Other VCF components:** VCF Single Sign-On is an additional authentication source to the existing authentication sources such as VMware Identity Manager and/or the component's native authentication source. You must provision users and groups again when you configure VCF Single Sign-On.
- **Single Component Log Out**

  - VCF Single Sign-On supports a single component logout mechanism. When you log out, the session ends exclusively for that particular VCF component within the designated browser.
- **Previously configured identity providers**

  - If you have previously configured an identity provider in the following combinations, the identity provider configurations are partially imported when you configure Single Sign-On. The combinations are:

    - Active Directory, OpenLDAP, or ADFS

      If Active Directory, OpenLDAP, or ADFS is the configured identity provider in vCenter, when configuring VCF Single Sign-On, the configuration is partially imported to VCF Identity Broker. Only the configuration details that are not imported are required to be additionally configured.
    - Okta, Entra, or Ping

      The identity provider configuration is retained if the chosen deployment mode is embedded. If the deployment mode is appliance, redo the configuration again.

  The users and groups are not migrated. You must provision the users and groups again even if you have an existing identity provider configuration in place.

## Prerequisites for Configuring VCF Single Sign-On

VCF Identity Broker will be configured in the management domain of the VCF instance. Ensure that the following prerequisites are met before you configure VCF Single Sign-On.

## Prerequisites for Configuring VCF Single Sign-On Using the Embedded Deployment Mode

If you choose the embedded deployment mode for setting up VCF Single Sign-On, ensure that the following prerequisites are met:

- The management domain vCenter must be at version 9.0 or later and have a VMware Cloud Foundation license assigned.
- The management domain vCenter must NOT be part of Enhanced Linked Mode (ELM).

Do not activate ELM in the participating vCenter instances after configuring VCF Single Sign-On in embedded mode.

You can choose appliance as the mode of deployment if the above criteria are not met. However, the integration of vCenter with VCF Single Sign-On will not be possible at a later stage without first meeting the above criteria.

## Prerequisites for Configuring VCF Single Sign-On Using the Appliance Deployment Mode

If you choose to configure VCF Single Sign-On in appliance mode, the VMware Cloud Foundation platform must meet the following minimum requirements:

- A 3-node cluster will be deployed.
- Each node will have 8 vCPUs and 16GB RAM.
- Each cluster requires a minimum of 700GB storage.