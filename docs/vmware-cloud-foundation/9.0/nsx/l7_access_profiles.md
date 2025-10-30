---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/profiles/l7-access-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > L7 Access Profiles
---

# L7 Access Profiles

An L7 access profile can contain multiple entries with different attribute types. L7
access profiles can be used in both Tier-0 and Tier-1 gateway firewall rules.

L7 access profiles have a default entry, and more entries can be added above the
default entry. Entries in the profile are evaluated in the listing order, and action
is taken upon the first match.

Before creating application firewall
rules on the Tier-0 gateway firewall, it is important to manually add gateway
firewall rules to allow routing protocols such as BGP, OSPF, and the failure
detection protocol BFD. These rules should be added before any application rules to
ensure that routing peering respective failure detection protocol is not impacted
when changing application firewall rules.

1. Select InventoryProfiles.
2. Select the L7 Access
   Profile tab, and click Add L7 Access
   Profile.
3. Enter a Profile Name,
   and optional Description.
4. In the Attribute Entities column,
   click Set.
5. Click  Add Attribute
   Type, and select one or more attributes from the drop-down menu.
   For Tier-0 gateway firewall rules, App ID is the only supported attribute type. 

   Attribute Type | Attribute Value || App ID - over 750 | To view available App IDs, scroll down the list, or select [App IDs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/attribute-types/app-ids.html#GUID-9b13de93-86d2-4064-8834-365de29aba8f-en). |
   | URL Category - 80+ categories including social media, banking, phishing, etc. | Select one or more URL categories by scrolling down the list. |
   | Custom URL - with regular expression | For more details see [Custom URLs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/attribute-types/custom-urls.html#GUID-a9f877c8-2f58-4229-b638-2bb2f571fbde-en). |
   | URL Reputation | Choose one or more of these reputations: High Risk, Suspicious, Moderate Risk, Low Risk, Trustworthy, Unknown |
6. Select the rule action:

   - Allow - allows matched
     traffic.
   - Reject - rejects matched
     traffic.
   - Reject with Response -
     rejects and sends the client the response page. This option is not
     available for the App ID attribute type. Navigate to SecurityGateway FirewallSettingsURL Filtering to view and customize the Reject with
     Response message.

     The Reject
     with Response page is sent only for http traffic.
     The response page will contain the URL (first 10 bytes show),
     Category, Source IP and message-text. Enter the message for the
     Reject with Response page. Click
     Preview Page to view the page that will
     be sent when access to a URL is blocked by a policy.
7. By default, logging is turned
   off. Toggle the button to activate logging.
8. By default the newly added entry
   is turned on. Toggle the button to deactivate the entry.
9. Click Add.
10. To edit or delete an entry,
    click the menu icon (![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)) and select
    Edit or Delete.
11. To change the settings of the
    default entry, click the menu icon (![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)) and select
    Edit. Note that the default entry cannot be turned
    off. By default, logging is turned off for the default entry. After the final
    processing of the default entry within the L7 Access Profile, the gateway
    firewalling evaluation process is stopped.
12. Click Add to activate the changed setting for the
    default entry or click Cancel.
13. Click
    Apply.
14. Click
    Save.