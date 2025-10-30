---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/remove-a-location.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Remove a Location
---

# Remove a Location

Removing a location from the Global Manager removes all objects created from the Global Manager that have a Global scope and are not specific to this location.

Before you remove a location, you must delete all objects created from the Global Manager that are specific to this location, such as tier-0 gateway, or firewall policies.

Removing a location is disruptive.

All configurations created by the Global Manager that are not specific to this location, such as groups and firewall sections with a Global scope, will be removed from the NSX Manager at this location.

1. Log in to the Global Manager at https://global-manager-ip-fqdn.
2. Navigate to SystemLocation Manager.
3. From the location that you want to remove, click ActionsRemove.

   You see a message describing the effect of removing a location. If you have not previously removed objects created from the Global Manager that are specific to this location, such as tier-0 gateways or firewall policies, you cannot remove the location. The system automatically removes all other configurations from the NSX Manager at this location, that have a Global scope in your NSX Federation deployment.