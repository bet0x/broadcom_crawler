---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-server-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an L2 VPN Server Service
---

# Add an L2 VPN Server Service

To configure an L2 VPN Server service, you must configure the L2 VPN service in server mode on the destination NSX Edge to which the L2 VPN client is to be connected.

1. With admin privileges, log in
   to NSX Manager.
2. If an IPSec VPN service does not exist yet on either a Tier-0 or Tier-1 gateway that you want to configure as the L2 VPN server, create the service using the following steps. 
   1. Navigate to the NetworkingVPNVPN Services tab and select Add ServiceIP Sec.
   2. Enter a name for the IPSec VPN service.
   3. From the Tier-0/Tier-1 Gateway drop-down menu, select the gateway to use with the L2 VPN server.
   4. If you want to use values different from the system defaults, set the rest of the properties on the Add IPSec Service pane, as needed.
   5. Click Save and when prompted if you want to continue configuring the IPSec VPN service, select No.
3. Navigate to the NetworkingVPNVPN Services tab and select Add ServiceL2 VPN Server to create an L2 VPN server.
4. Enter a name for the L2 VPN server.
5. From the Tier-0/Tier-1 Gateway drop-down menu, select the same Tier-0 or Tier-1 gateway that you used with the IPSec service you created a moment ago.
6. Enter an optional description for this L2 VPN server.
7. Enter a value for Tags if you want to include this service in a tag group.
8. Enable or disable the Hub & Spoke property. 

   By default, the value is set to Disabled, which means the traffic received from the L2 VPN clients is only replicated to the segments connected to the L2 VPN server. If this property is set to Enabled, the traffic from any L2 VPN client is replicated to all other L2 VPN clients.
9. Click Save. 

   After the new L2 VPN server is created successfully, you are asked whether you want to continue with the rest of the L2 VPN service configuration. If you click Yes, you are taken back to the Add L2 VPN Server pane and the Session link is enabled. You can use that link to create an L2 VPN server session or use the tab.

After one or more L2 VPN sessions are added, the number of sessions for each VPN service will appear in the VPN Services tab. You can reconfigure or add sessions by clicking the number in the Sessions column. You do not need to edit the service. Note that if the number is zero, it is not clickable and you must edit the service to add sessions.

Configure an L2 VPN server session for the L2 VPN server that you configured using information in [Add an L2 VPN Server Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-server-session.html#GUID-0285324c-755a-4f29-9514-40678dd0f5d6-en) as a guide.