---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-client-session.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an L2 VPN Client Session
---

# Add an L2 VPN Client Session

You must add an L2 VPN Client session after creating an L2 VPN Client service, and attach it to an existing segment.

- You must have configured an L2 VPN Client service before proceeding. See [Add an L2 VPN Client Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-client-service.html#GUID-5c3e0c6b-6835-4a9e-95b0-6f4b329fcd5e-en).
- Obtain the IP addresses information for the local IP and remote IP to use with the L2 VPN Client session you are adding.
- Obtain the peer code that was generated during the L2 VPN server configuration. See [Download the Remote Side L2 VPN Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/download-the-remote-side-l2-vpn-configuration.html#GUID-9cea66af-4145-40af-ad6e-8c780d2b774b-en).
- Obtain the name of the existing segment you want to attach to the L2 VPN Client session you are creating. See [Create an NSX Segment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-segment.html#GUID-3d1b1678-6a38-4e08-833c-5b5ca5faefb0-en).

The following steps use the L2 VPN Sessions tab on the NSX Manager UI to create an L2 VPN Client session. You also select an existing local endpoint and segment to attach to the L2 VPN Client session.

You can also add an L2 VPN Client session immediately after you have successfully configured the L2 VPN Client service. Click Yes when prompted to continue with the L2 VPN Client configuration and select SessionsAdd Sessions on the Add L2 VPN Client panel. The first few steps in the following procedure assume you selected No to the prompt to continue with the L2 VPN Client configuration. If you selected Yes, proceed to step 3 in the following steps to guide you with the rest of the L2 VPN Client session configuration.

1. With admin privileges, log in
   to NSX Manager.
2. Select the NetworkingVPNL2 VPN Sessions.
3. Select Add L2 VPN SessionL2 VPN Client.
4. Enter a name for the L2 VPN Client session.
5. From the VPN Service drop-down menu, select the L2 VPN Client service with which the L2 VPN session is to be associated. 

   If you are adding this L2 VPN Client session from the Set L2VPN Client Sessions dialog box, the L2 VPN Client service is already indicated above the Add L2 Session button.
6. In the Local IP address text box, enter the IP address of the L2 VPN Client session.
7. Enter the remote IP address of the IPSec tunnel to be used for the L2 VPN Client session.
8. In the Peer Configuration text box, enter the peer code generated when you configured the L2 VPN Server service.
9. Enable or disable Admin Status. 

   By default, the value is set to Enabled, which means the L2 VPN Server session is to be configured down to the NSX Edge node.
10. Click Save and click Yes when prompted if you want to continue with the VPN service configuration.
11. Attach an existing segment to the L2 VPN Client session. 
    1. Select SegmentsAdd Segments.
    2. In the Set Segments dialog box, click Add Segment.
    3. From the Segment drop-down menu, select the VNI-based or VLAN-based segment you want to attach to the L2 VPN Client session.
    4. Enter a unique value in the VPN Tunnel ID that is used to identify the segment that you selected.
    5. Click Close.
12. To finish the L2 VPN Client session configuration, click Close Editing.

In the VPN Services tab, the sessions count is updated for the L2 VPN Client service that you configured.

If you have attached one or more segments to the session, you see the number of segments for each session in the L2 VPN Sessions tab. You can reconfigure or add segments by clicking the number in the Segments column. You do not need to edit the session. If the number is zero, it is not clickable and you must edit the session to add segments.