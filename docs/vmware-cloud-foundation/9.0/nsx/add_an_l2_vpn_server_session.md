---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-server-session.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an L2 VPN Server Session
---

# Add an L2 VPN Server Session

After creating an L2 VPN Server service, you must add an L2 VPN session and attach it to an existing segment.

- You must have configured an L2 VPN Server service before proceeding. See [Add an L2 VPN Server Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-server-service.html#GUID-7c30c658-2c66-44ae-93c7-81b508220a4f-en).
- Obtain the information for the local endpoint and remote IP to use with the L2 VPN Server session you are adding. To create a local endpoint, see [Add Local Endpoints](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-local-endpoints.html#GUID-af6404f4-1d30-49a9-8752-0214143ca288-en).
- Obtain the values for the pre-shared key (PSK) and the tunnel interface subnet to use with the L2 VPN Server session.
- Obtain the name of the existing segment you want to attach to the L2 VPN Server session you are creating. See [Create an NSX Segment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-segment.html#GUID-3d1b1678-6a38-4e08-833c-5b5ca5faefb0-en) for information.

The following steps use the L2 VPN Sessions tab on the NSX Manager UI to create an L2 VPN Server session. You also select an existing local endpoint and segment to attach to the L2 VPN Server session.

You can also add an L2 VPN Server session immediately after you have successfully configured the L2 VPN Server service. You click Yes when prompted to continue with the L2 VPN Server configuration and select SessionsAdd Sessions on the Add L2 VPN Server panel. The first few steps in the following procedure assume you selected No to the prompt to continue with the L2 VPN Server configuration. If you selected Yes, proceed to step 3 in the following steps to guide you with the rest of the L2 VPN Server session configuration.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to the NetworkingVPNL2 VPN Sessions tab.
3. Select Add L2 VPNL2 VPN Server.
4. Enter a name for the L2 VPN Server session.
5. From the VPN Service drop-down menu, select the IPsec service on the same Tier-0 gateway for which the L2 VPN session is being created. 

   If you are adding this L2 VPN Server session from the Set L2VPN Server Sessions dialog box, the L2 VPN Server service is already indicated above the Add L2 Session button.
6. Select an existing local endpoint from the drop-down menu. 

   If you want to create a different local endpoint, click the three-dot menu ( ![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) and select Add Local Endpoint.
7. Enter the IP address of the remote site under Remote IP.
8. To enable or disable the L2 VPN Server session, click Admin Status. 

   By default, the value is set to Enabled, which means the L2 VPN Server session is to be configured down to the NSX Edge node.
9. Enter the secret key value in Pre-shared Key. 

   Be careful when sharing and storing a PSK value because it is considered sensitive information.
10. Enter an IP subnet address in the Tunnel Interface using the CIDR notation. 

    For example, 4.5.6.6/24. This subnet address is required.
11. Enter a value in Remote ID. 

    For peer sites using certificate authentication, this ID must be the common name in the peer site's certificate. For PSK peers, this ID can be any string. Preferably, use the IP address of the VPN or an FQDN for the VPN services as the remote ID.
12. If you want to include this session as part of a specific group, enter the tag name in Tags.
13. Click Advanced Properties. if you want to reduce the maximum segment size (MSS) payload of the TCP session during the L2 VPN connection.

    By default, TCP MSS Clamping is enabled and the TCP MSS Direction is set to Both. See [Understanding TCP MSS Clamping](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-tcp-mss-clamping.html#GUID-a45a58af-e074-4297-be5b-b6632bfa4af9-en) for more information.

    1. Enable or disable TCP MSS Clamping.
    2. Set the TCP MSS Value, if necessary. If the field is left blank, the value is automatically assigned.
14. Click Save and click Yes when prompted if you want to continue with the VPN service configuration. 

    You are returned to the Add L2VPN Sessions panel and the Segments link is now enabled.
15. Attach an existing segment to the L2 VPN Server session. 
    1. Click SegmentsSet Segments.
    2. In the Set Segments dialog box, click Set Segment to attach an existing segment to the L2 VPN Server session.
    3. From the Segment drop-down menu, select the VNI-based or VLAN-based segment that you want to attach to the session.
    4. Enter a unique value in the VPN Tunnel ID that is used to identify the segment that you selected.
    5. In the Local Egress Gateway IP text box, enter the IP address of the local gateway that your workload VMs on the segment use as their default gateway. The same IP address can be configured in the remote site on the extended segment.
    6. Click Save and then Close.

    In the Set L2VPN Sessions pane or dialog box, the system has incremented the Segments count for the L2 VPN Server session.
16. To finish the L2 VPN Server session configuration, click Close Editing.

In the VPN Services tab, the system incremented the Sessions count for the L2 VPN Server service that you configured.

If you have attached one or more segments to the session, you see the number of segments for each session in the L2 VPN Sessions tab. You can reconfigure or add segments by clicking the number in the Segments column. You do not need to edit the session. If the number is zero, it is not clickable and you must edit the session to add segments.

To complete the L2 VPN service configuration, you must also create an L2 VPN service in Client mode and an L2 VPN client session. See [Add an L2 VPN Client Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-client-service.html#GUID-5c3e0c6b-6835-4a9e-95b0-6f4b329fcd5e-en) and [Add an L2 VPN Client Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-client-session.html#GUID-db01896c-9282-4b8b-bdde-3881bc79ba62-en).