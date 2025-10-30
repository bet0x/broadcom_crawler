---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/customize-the-login-window-with-a-user-agreement-banner.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure the Login Window with a User Agreement Banner
---

# Configure the Login Window with a User Agreement Banner

You can configure a custom login message that requires a user agreement as part of
the login process for NSX.

If activated (or enabled), this agreement displays at every login and is changed only
by users with Enterprise admin roles. For Federation, each Global and Local Manager requires their own configuration.
If you have DoD or other security compliance requirements, this feature provides
such options.

1. From your browser, log in with
   admin privileges to an NSX Manager or Global Manager at
   https://<nsx-manager-ip-address>.
2. Navigate to SystemGeneral System Settings.
3. To add or remove banner
   settings, click the User Interface tab and click
   Edit for Login Consent
   Settings.
4. To activate or deactivate this option, toggle the Login Consent
   On or Off.
5. To require explicit user consent
   before the user logs in, select Yes.
6. To create a consent message that
   displays on the login page, enter the consent message title.

   This message starts with the phrase I agree to … and
   can be up to 255 characters.
7. If required, add a custom
   consent message description.

   The description limit is 64,000 characters. Users must select the title to
   view this description. HTML links are not supported.