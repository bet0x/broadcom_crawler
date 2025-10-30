---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/profiles/context-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Context Profiles
---

# Context Profiles

Context Profiles are used in firewall rules.

There are five attributes for use in context profiles: App ID, Custom URL, Domain (FQDN) Name, URL Category, and URL Reputation.

Select App IDs can have one or more sub attributes, such as TLS\_Version and CIPHER\_SUITE. Both App ID and FQDN can be used in a single context profile. Multiple App IDs can be used in the same profile. One App ID with sub attributes can be used - sub attributes are cleared when multiple App ID attributes are used in a single profile.

Both system defined and user defined Fully Qualified Domain Names (FQDNs) are supported. You can see the list of FQDNs when you add a new context profile of attribute type Domain (FQDN) Name.You can also see a list of FQDNs, and where they are used by navigating to Inventory Profiles FQDNs.

1. Select InventoryProfiles.
2. Select Security  Profiles.
3. Select the Context Profile tab and click Add Context Profile.
4. Enter a Profile Name, and optional Description.
5. In the Attributes column, click Set.
6. Click  Add Attribute, and select one or more attributes from the drop-down menu: App ID, Custom URL, Domain (FQDN) Name, URL Category, or URL Reputation.

   Attribute | Procedure || App ID - Advanced [App IDs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/attribute-types/app-ids.html) require a custom profile. | 1. Enter the name of the advanced App ID you'd like to use in firewall rules. 2. Click Add. 3. Click Apply. |
   | Custom URL | To create a custom URL:  1. Click the three dot menu "" and select Add Custom URL. 2. Enter the URL. 3. Click Save. |
   | Domain (FQDN) Name | Select a system FQDN by scrolling down the list. To create a user-defined FQDN:  1. Click the three dot menu "" and select Add FQDN. 2. Enter the domain name in the form \*.[hostname].[domain]. For example, \*.abracadabra.com. Do not include http:// or any other header. 3. Click Save. The newly created FQDN appears in the attribute value column. 4. Search and add additional FQDNs. 5. Click Apply. |
   | URL Category | 1. Select one or more URL categories by scrolling down the list. 2. Click Add. 3. Click Apply. |
   | URL Reputation | 1. Select one or more of the attributes by clicking in the box. 2. Click Add. 3. Click Apply. See the "FQDN Analysis Dashboard" page in the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-0/vdefend-gateway-firewall.html) for more information about URL reputation. |
7. If you have selected an attribute with sub attributes such as SSL or CIFS, click Set in the Sub Attributes/Values column. 
   1. Click Add Sub Attribute and select TLS\_VERSION, TLS\_CIPHER\_SUITE, or CIFS\_SMB\_VERSION.
   2. Select one or more sub attributes.
   3. Click Add. Another sub attribute can be added by clicking Add Sub Attribute.
   4. Click Apply.
8. Enter a tag or scope. See [NSX Tags](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/nsx-tags.html#GUID-b6ececc7-01d2-41ce-a914-9d51ba2b7f8b-en) for more information.
9. Click Save.

Apply this context profile to a layer 7 distributed firewall rule (for layer 7 or domain name), or gateway firewall rule (for layer 7).