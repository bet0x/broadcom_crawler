---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/add-a-route-based-ipsec-session.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Route-Based IPSec Session
---

# Add a Route-Based IPSec Session

When you add a route-based IPSec VPN, tunneling is provided on traffic that is based on routes that were learned dynamically over a virtual tunnel interface (VTI) using a preferred protocol, such as BGP. IPSec secures all the traffic flowing through the VTI.

- You must have configured an IPSec VPN service before proceeding. See [Add an NSX IPSec VPN Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html#GUID-fa3387e6-8188-4db8-913c-c1fa71b9db5a-en).
- Obtain the information for the local endpoint, IP address for the peer site, and tunnel service IP subnet address to use with the route-based IPSec session you are adding. To create a local endpoint, see [Add Local Endpoints](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-local-endpoints.html#GUID-af6404f4-1d30-49a9-8752-0214143ca288-en).
- If you are using a Pre-Shared Key (PSK) for authentication, obtain the PSK value.
- If you are using a certificate for authentication, ensure that the necessary server certificates and corresponding CA-signed certificates are already imported.

  See [Certificates in NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates.html#GUID-b7714dbe-3c79-4ae3-adff-c6361c5bf9c6-en).
- If you do not want to use the default values for the IPSec tunnel, IKE, or dead peer detection (DPD) profiles provided by NSX, configure the profiles you want to use instead. See [Adding Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles.html#GUID-1dfb1b84-53e7-435b-a636-fafb300ad996-en) for information.

The steps described in this topic use the IPSec Sessions tab to create a route-based IPSec session. You also add information for the tunnel, IKE, and DPD profiles, and select an existing local endpoint to use with the route-based IPSec VPN.

You can also add the IPSec VPN sessions immediately after the IPSec VPN service is successfully configured. Click Yes when prompted to continue with the IPSec VPN service configuration and select SessionsAdd Sessions on the Add IPSec Service panel. The first few steps in the following procedure assume you selected No to the prompt to continue with the IPSec VPN service configuration. If you selected Yes, proceed to step 3 to guide you with the rest of the route-based IPSec VPN session configuration.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to NetworkingVPNIP Sec Sessions.
3. Select Add IPSec SessionRoute Based.
4. Enter a name for the route-based IPSec session.
5. From the VPN Service drop-down menu, select the IPSec VPN service to which you want to add this new IPSec session.

   If you are adding this IPSec session from the Add IPSec Sessions dialog box, the VPN Service name is already indicated above the Add IPSec Session button.
6. Select an existing local endpoint from the drop-down menu.

   The local endpoint value is required and identifies the local NSX Edge node. If you want to create a different local endpoint, click the three-dot menu ( ![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) and select Add Local Endpoint.
7. In the Remote IP text box, enter the IP address of the remote site.

   This is a required value.
8. Enter an optional description for this route-based IPSec VPN session.

   The maximum length is 1024 characters.
9. To enable or disable the IPSec session, click Admin Status.

   By default, the value is set to Enabled, which means the IPSec session is to be configured down to the NSX Edge node.
10. From the Compliance suite drop-down menu, select a security compliance suite.

    Compliance suite support is provided beginning with NSX 2.5. See [About Supported Compliance Suites](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/about-supported-compliance-suites.html#GUID-26aebcc3-d15b-46d6-8ff9-e3b1a9416802-en) for more information.

    The default value is set to None. If you select a compliance suite, the Authentication Mode is set to Certificate and in the Advanced Properties section, the values for IKE profile and IPSec profile are set to the system-defined profiles for the selected compliance suite. You cannot edit these system-defined profiles.
11. Enter an IP subnet address in Tunnel Interface in the CIDR notation. 

    This address is required.
12. If the Compliance Suite is set to None, select a mode from the Authentication Mode drop-down menu. 

    The default authentication mode used is PSK, which means a secret key shared between NSX Edge and the remote site is used for the IPSec VPN session. If you select Certificate, the site certificate that was used to configure the local endpoint is used for authentication.

    For more information about certificate-based authentication, see [Using Certificate-Based Authentication for IPSec VPN Sessions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/using-certificate-based-authentication-for-ipsec-vpn-sessions.html#GUID-06709cbc-a214-4757-bda1-6cecafbda350-en).
13. If you selected PSK for the authentication mode, enter the key value in the Pre-shared Key text box.

    This secret key can be a string with a maximum length of 128 characters.

    Be careful when sharing and storing a PSK value because it contains some sensitive information.
14. Enter a value in Remote ID.

    For peer sites using PSK authentication, this ID value must be the IP address or the FQDN of the peer site. For peer sites using certificate authentication, this ID value must be the common name (CN) or distinguished name (DN) used in the peer site's certificate.

    If the peer site's certificate contains an email address in the DN string, for example,

    ```
    C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123/[email protected]
    ```

    then enter the Remote ID value using the following format as an example.

    ```
    C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123, [email protected]"
    ```

    If the local site's certificate contains an email address in the DN string and the peer site uses the strongSwan IPsec implementation, enter the local site's ID value in that peer site. The following is an example.

    ```
    C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123, [email protected]"
    ```
15. If you want to include this IPSec session as part of a specific group tag, enter the tag name in Tags.
16. To change the profiles, initiation mode, TCP MSS clamping mode, and tags used by the route-based IPSec VPN session, click Advanced Properties.

    By default, the system-generated profiles are used. Select another available profile if you do not want to use the default. If you want to use a profile that is not configured yet, click the three-dot menu ( ![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) to create another profile. See [Adding Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles.html#GUID-1dfb1b84-53e7-435b-a636-fafb300ad996-en).

    1. If the IKE Profiles drop-down menu is enabled, select the IKE profile.
    2. Select the IPsec tunnel profile, if the IPSec Profiles drop-down menu is not disabled.
    3. Select the preferred DPD profile if the DPD Profiles drop-down menu is enabled.
    4. Select the preferred mode from the Connection Initiation Mode drop-down menu.

       Connection initiation mode defines the policy used by the local endpoint in the process of tunnel creation. The default value is Initiator. The following table describes the different available connection initiation modes.

       Connection Initiation Modes



       | Connection Initiation Mode | Description |
       | --- | --- |
       | Initiator | The default value. In this mode, the local endpoint initiates the IPSec VPN tunnel creation and responds to incoming tunnel setup requests from the peer gateway. |
       | On Demand | Do not use with the route-based VPN. This mode applies to policy-based VPN only. |
       | Respond Only | The IPSec VPN never initiates a connection. The peer site always initiates the connection request and the local endpoint responds to that connection request. |
17. If you want to reduce the maximum segment size (MSS) payload of the TCP session during the IPSec connection, enable TCP MSS Clamping, select the TCP MSS direction value, and optionally set the TCP MSS Value.

    See [Understanding TCP MSS Clamping](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-tcp-mss-clamping.html#GUID-a45a58af-e074-4297-be5b-b6632bfa4af9-en) for more information.
18. If you want to include this IPSec session as part of a specific group tag, enter the tag name in Tags.
19. Click Save.

When the new route-based IPSec VPN session is configured successfully, it is added to the list of available IPsec VPN sessions. It is in read-only mode.

- Verify that the IPSec VPN tunnel status is Up. See [Monitor and Troubleshoot VPN Sessions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/troubleshooting-vpn-issues-in-nsx-t-data-center/monitor-and-troubleshoot-vpn-sessions.html#GUID-f750d696-5d77-44d8-958a-2e8e7c087878-en) for information.
- Configure routing using either a static route or BGP. See [Configure an NSX Static Route](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-an-nsx-static-route.html#GUID-bb885458-8e27-40fd-be65-aae5d1268838-en) or [Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en).
- If necessary, manage the IPSec VPN session information by clicking the three-dot menu ( ![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) on the left-side of the session's row. Select one of the actions you can perform.
- To configure the peer VPN device, see [Download the Remote Side IPSec VPN Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/download-the-remote-side-ipsec-vpn-configuration-file.html).