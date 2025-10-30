---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/managing-vmware-cloud-foundation-operations-sso/change-the-identity-management-of-a-vcf-instance-managed-by-anotehr-instance-of-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Change the Identity Management of a VCF Instance Managed by Another VCF Instance
---

# Change the Identity Management of a VCF Instance Managed by Another VCF Instance

If a particular VCF Instance was connected to an existing Single Sign-On configuration, the identity source configuration for that instance can be managed only from within the initial VCF Instance in which it was configured. You may want to connect the identity source configuration to a different VCF Instance or create a new Single Sign-On configuration.

## **Scenario #1: Connect to a Different Single Sign-On Configuration**

If you wish to connect the components of a VCF Instance that is managed by a different VCF Instance to an alternate one, perform the following steps:

1. Navigate to the VCF Instance that you intend to connect to a different VCF Identity Broker.
2. Click Component Configuration.
3. Click Edit next to Authentication Source.
4. In the modal box that opens, from the Identity Broker drop down, select the desired VCF Identity Broker.
5. Click Continue.
6. All the registered components of this VCF Instance are now be connected to the Single Sign-On configuration of the newly selected VCF Identity Broker.

## **Scenario #2 - Deregister the VCF Instance From the Single Sign-On Configuration**

If you wish to remove the VCF Instance from the existing Single Sign-On configuration, perform the following steps:

1. Navigate to the VCF Instance that you intend to connect to a different VCF Identity Broker.
2. Click Component Configuration.
3. In the grid under Component List, all the components belonging to this VCF component are listed.
4. Use the filter 'Status' to filter the configured components.
5. Select all the configured components and click Deregister Component.
6. After all the registered components have been deregistered, the page reloads to display the following options. Choose the desired option to configure Single Sign-On for this VCF Instance.

   1. Connect to an existing Single Sign-On configuration. For more information, see [Connect а VCF Instance to an Existing VCF Single Sign-On Configuration](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/connect-to-an-existing-sso-configuration.html#GUID-d33e3bed-8a3e-4ffb-a930-6336647385a7-en_id-83426f03-d83d-47bb-b450-836778f81eb9).
   2. Create a new Single Sign-On configuration. For more information, see [Configure a New VCF Single Sign-On for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso.html#GUID-ca1a8166-f582-4e79-9850-86a413d5866c-en_id-bd995175-2932-4f80-b6e0-bdbc3bb070ff).