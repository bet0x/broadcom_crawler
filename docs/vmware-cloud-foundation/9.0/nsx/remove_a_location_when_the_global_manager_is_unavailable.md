---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/remove-a-location/remove-a-location-using-the-api.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Remove a Location When the Global Manager is Unavailable
---

# Remove a Location When the Global Manager is Unavailable

This procedure is used only if the Global Manager has been deleted BEFORE the Local Managers (LM) are aware of its deletion.

This is a possible use case at the completion of a Federation test. In this case, the LM will constantly try to connect to its configured Global Manager (which has been deleted), and share with other Local Managers its stretch GM group members. The API calls will remove the Global Manager constructs on each LM, even when the GM has been deleted.

The below API calls on the Local Manager, will remove the Local Manager, its registration to the Global Manager, and its registration to other Local Managers.

The following API calls done on the Local Manager are disruptive.

All configurations created by the Global Manager that are not specific to this location, such as groups and firewall sections with a Global scope, will be removed from the NSX Manager at this location.

1. To remove a Global Manager that is active, a Global Manager that is standby, and other Local Managers registrations from the Local Manager use the site manager API (at the Local Manager) POST https://<LM>/api/v1/sites?action=offboard\_local..
2. To remove Global Manager objects from a Local Manager, run the Local Manager API (at the Local Manager) POST https://<LM>/policy/api/v1/infra/site?action=offboard.
3. The offboarding progress can be monitored by using the API call GET https://<LM>/policy/api/v1/infra/site/offboarding-status.