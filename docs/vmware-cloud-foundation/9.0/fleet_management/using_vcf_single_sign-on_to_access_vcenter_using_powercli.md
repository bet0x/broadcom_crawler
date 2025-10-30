---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso/configure-vmware-cloud-foundation-sso--as-a-client-for-other-components/vcf-single-sign-on-for-powercli.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Using VCF Single Sign-On to Access vCenter using PowerCLI
---

# Using VCF Single Sign-On to Access vCenter using PowerCLI

You can configure CLI and automation tools like PowerCLI to use VCF Single Sign-On. You can configure CLI and automation tools like PowerCLI to access vCenter only, using VCF Single Sign-On. If you are an existing customer upgrading to VCF 9.0, existing automation scripts using CLI tools will not be impacted if Single Sign-On is configured in the same management domain vCenter in embedded mode. However, if Single Sign-On is configured in appliance mode, or in an alternate management domain vCenter, a new OAuth client needs to be generated for PowerCLI.

**Prerequisite**

Ensure that VCF Single Sign-On is completely configured for at least one VCF Instance. For more information, see [Configure a New VCF Single Sign-On for a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/setting-up-sso.html#GUID-ca1a8166-f582-4e79-9850-86a413d5866c-en_id-bd995175-2932-4f80-b6e0-bdbc3bb070ff).

1. From the VCF Operations navigation pane, select Fleet ManagementIdentity & AccessVCF Other Components.
2. Click Add and enter the following information:

   - Name - User friendly name for the OIDC client.
   - Identity broker - Choose the VCF Identity Broker with which you want to configure Single Sign-On.
   - Redirect URI - The endpoint to which the VCF Identity Broker needs to redirect after authentication. The URI needs to follow the HTTP schema, and be on localhost with a free port on the client machine. For example: "http://localhost:8844/auth."
   - Post logout redirect URI - Not applicable for Single Sign-On with PowerCLI.
3. Click Generate OIDC Client.
4. Copy and store the Client ID, client secret, and Identity Broker issuer URL securely in a safe place.
5. Click Save.
6. Create an OAuth security context object for PowerCLI. For example, see the following script.

   ```
   $oauthSecContext = New-OAuthSecurityContext -TokenEndpointUrl "https://<vcenter_fqdn>/acs/t/CUSTOMER/token" -
   AuthorizationEndpointUrl "https://<vcenter_fqdn>/acs/t/CUSTOMER/authorize" -RedirectUrl "http://localhost:8844/auth" -
   ClientId "powercli-native" -ClientSecret "<secret_value>"
   TokenEndpointUrl
   AuthorizationEndpointUrl
   RedirectUrl
   ClientId
   ClientSecret
   ```

   The Redirect URL should be the same as the value entered in Step 2 - Redirect URI.
7. Exchange the OAuth 2.0 security context for a SAML security context.

   ```
   $samlSecContext = New-VISamlSecurityContext -VCenterServer '<vcenter_fqdn>' -OAuthSecurityContext $oauthSecContext
   ```
8. Connect to your vCenter using the SAML security context.

   ```
   Connect-VIServer -Server '<vcenter_fqdn>' -SamlSecurityContext $samlSecContext
   ```

   Single Sign-On through CLI tools is possible only through vCenter in VCF 9.0.