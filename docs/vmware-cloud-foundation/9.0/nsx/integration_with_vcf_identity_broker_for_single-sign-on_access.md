---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-workspace-one-access-broker-for-single-sign-on-access.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Integration with VCF Identity Broker for Single-Sign-On Access
---

# Integration with VCF Identity Broker for Single-Sign-On Access

You can allow users access to log in to NSX Managers, Local Managers, and Global Managers by connecting VMware NSX to the VCF Identity Broker in vCenter, version 8.0 U3, for federated authentication. To configure this capability, it is recommended to use the VMware Cloud Foundation SDDC Manager. For NSX Global Managers and standalone NSX Managers, follow the procedure described in [Knowledge Base article 3875053: Procedure to configure Single Sign-On on standalone NSX](https://knowledge.broadcom.com/external/article?articleNumber=387503).

OpenID Connect (OIDC) is a simple identity layer on top of the OAuth 2.0 protocol. OIDC provides a secure way to authenticate users by allowing different organizations to participate in authentication. For example, one organization can verify user identities while another organization decides whether to give users access to various services based on the groups to which that user belongs. OIDC can also obtain basic profile information about the user across applications.

Some organizations involved in an acquisition scenario can use OIDC to allow employees from either company to log into NSX.

For details on how to configure this capability, see [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html).

Validate the OIDC authentication to ensure that your user can log in to the NSX Manager and has access to their Enterprise Admin capabilities such as the Tier-0 Gateways menu. For details about log in options, see [Logging in to NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/logging-in-to-nsx-manager.html#GUID-5bc3b944-a1f6-4a2b-8144-5034575b5d2f-en).