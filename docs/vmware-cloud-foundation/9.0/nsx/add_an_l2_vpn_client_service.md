---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-client-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an L2 VPN Client Service
---

# Add an L2 VPN Client Service

After configuring the L2 VPN Server service, configure the L2 VPN service in the client mode on another NSX Edge instance.

1. With admin privileges, log in
   to NSX Manager.
2. If an IPSec VPN service does not exist yet on either a Tier-0 or Tier-1 gateway that you want to configure as the L2 VPN client, create the service using the following steps. 
   1. Navigate to the NetworkingVPNVPN Services tab and select Add ServiceIP Sec.
   2. Enter a name for the IPSec VPN service.
   3. From the Tier-0/Tier-1 Gateway drop-down menu, select a Tier-0 or Tier-1 gateway to use with the L2 VPN client.
   4. If you want to use values different from the system defaults, set the rest of the properties on the Add IPSec Service pane, as needed.
   5. Click Save and when prompted if you want to continue configuring the IPSec VPN service, select No.
3. Navigate to the NetworkingVPNVPN Services tab and select Add ServiceL2 VPN Client.
4. Enter a name for the L2 VPN Client service.
5. From the Tier-0/Tier-1 Gateway drop-down menu, select the same Tier-0 or Tier-1 gateway that you used with the route-based IPSec tunnel you created a moment ago.
6. Optionally set the values for Description and Tags.
7. Click Save. 

   After the new L2 VPN client service is created successfully, you are asked whether you want to continue with the rest of the L2 VPN client configuration. If you click Yes, you are taken back to the Add L2 VPN Client pane and the Session link is enabled. You can use that link to create an L2 VPN client session or use the NetworkingVPNL2 VPN Sessions tab.

After one or more L2 VPN sessions are added, the number of sessions for each VPN service will appear in the VPN Services tab. You can reconfigure or add sessions by clicking the number in the Sessions column. You do not need to edit the service. If the number is zero, it is not clickable and you must edit the service to add sessions.

Configure an L2 VPN client session for the L2 VPN Client service that you configured. Use the information in [Add an L2 VPN Client Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-client-session.html#GUID-db01896c-9282-4b8b-bdde-3881bc79ba62-en) as a guide.