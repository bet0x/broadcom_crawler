---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-dpd-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add DPD Profiles
---

# Add DPD Profiles

A DPD (Dead Peer Detection) profile provides information about the number of seconds to wait in between probes to detect if an IPSec peer site is alive or not.

NSX provides a system-generated DPD profile, named nsx-default-l3vpn-dpd-profile, that is assigned by default when you configure an IPSec VPN service. This default DPD profile is a periodic DPD probe mode.

If you decide not to use the default DPD profile provided, you can configure your own using the following steps.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to NetworkingVPNProfiles.
3. Select DPD Profiles from the Select Profile Type drop-down menu, and click Add DPD Profile.
4. Enter a name for the DPD profile.
5. From the DPD Probe Mode drop-down menu, select Periodic or On Demand mode.

   For a periodic DPD probe mode, a DPD probe is sent every time the specified DPD probe interval time is reached.

   For an on-demand DPD probe mode, a DPD probe is sent if no IPSec packet is received from the peer site after an idle period. The value in DPD Probe Interval determines the idle period used.
6. In the DPD Probe Interval text box, enter the number of seconds you want the NSX Edge node to wait before sending the next DPD probe. 

   For a periodic DPD probe mode, the valid values are between 3 and 360 seconds. The default value is 60 seconds.

   For an on-demand probe mode, the valid values are between 1 and 10 seconds. The default value is 3 seconds.

   When the periodic DPD probe mode is set, the IKE daemon running on the NSX Edge sends a DPD probe periodically. If the peer site responds within half a second, the next DPD probe is sent after the configured DPD probe interval time has been reached. If the peer site does not respond, then the DPD probe is sent again after waiting for half a second. If the remote peer site continues not to respond, the IKE daemon resends the DPD probe again, until a response is received or the retry count has been reached. Before the peer site is declared to be dead, the IKE daemon resends the DPD probe up to a maximum of times specified in the Retry Count property. After the peer site is declared dead, the NSX Edge node then tears down the security association (SA) on the dead peer's link.

   When the on-demand DPD mode is set, the DPD probe is sent only if no IPSec traffic is received from the peer site after the configured DPD probe interval time has been reached.
7. In the Retry Count text box, enter the number of retries allowed.

   The valid values are between 1 and 100. The default retry count is 5.
8. Provide a description and add a tag, as needed.
9. To enable or disable the DPD profile, click the Admin Status toggle.

   By default, the value is set to Enabled. When the DPD profile is enabled, the DPD profile is used for all IPSec sessions in the IPSec VPN service that uses the DPD profile.
10. Click Save.

A new row is added to the table of available DPD profiles. To edit or delete a non-system created profile, click the three-dot menu ( ![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) and select from the list of actions available.