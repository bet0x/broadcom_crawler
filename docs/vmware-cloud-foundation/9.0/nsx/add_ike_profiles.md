---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ike-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add IKE Profiles
---

# Add IKE Profiles

The Internet Key
Exchange (IKE) profiles provide information about the algorithms that are used
to authenticate, encrypt, and establish a shared secret between network sites
when you establish an IKE tunnel.

NSX provides system-generated IKE profiles that are assigned
by default when you configure an IPSec VPN or L2 VPN service. The following
table lists the default profiles provided.

Default IKE Profiles
Used for IPSec VPN or L2 VPN Services



| Default IKE Profile Name | Description |
| --- | --- |
| nsx-default-l2vpn-ike-profile | - Used for an L2 VPN   service configuration. - Configured with IKE V2, AES CBC 128 encryption   algorithm, SHA2 256 algorithm, and Diffie-Hellman   group14 key exchange algorithm. |
| nsx-default-l3vpn-ike-profile | - Used for an IPSec   VPN service configuration. - Configured with IKE V2, AES CBC 128 encryption   algorithm, SHA2 256 algorithm, and Diffie-Hellman group   14 key exchange algorithm. |

Instead of the default IKE profiles used,
you can also select one of the compliance suites supported starting with
NSX 2.5. See [About Supported Compliance Suites](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/about-supported-compliance-suites.html#GUID-26aebcc3-d15b-46d6-8ff9-e3b1a9416802-en) for more
information.

If you decide not to use the default IKE profiles or
compliance suites provided, you can configure your own IKE profile using the
following steps.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingVPN and then click the Profiles tab.
3. Select the
   IKE
   Profiles profile type, and click
   Add IKE
   Profile.
4. Enter a name for the IKE
   profile.
5. From the
   IKE
   Version drop-down menu, select the IKE version to use to set up a
   security association (SA) in the IPSec protocol suite.

   IKE
   Versions



   | IKE Version | Description |
   | --- | --- |
   | IKEv1 | When selected, the IPSec VPN initiates and responds to an IKEv1 protocol only. |
   | IKEv2 | This version is the default. When selected, the IPSec VPN initiates and responds to an IKEv2 protocol only. |
   | IKE-Flex | If this version is selected and if the tunnel establishment fails with the IKEv2 protocol, the source site does not fall back and initiate a connection with the IKEv1 protocol. Instead, if the remote site initiates a connection with the IKEv1 protocol, then the connection is accepted. |
6. Select the encryption,
   digest, and Diffie-Hellman group algorithms from the drop-down menus. You can
   select multiple algorithms to apply or deselect any selected algorithms you do
   not want to be applied.

   Algorithms
   Used



   | Type of Algorithm | Valid Values | Description |
   | --- | --- | --- |
   | Encryption | - AES 128 (default) - AES 256 - AES GCM 128 - AES GCM 192 - AES GCM 256 | The encryption algorithm used during the Internet Key Exchange (IKE) negotiation.  The AES 128 and AES 256 algorithms use the CBC mode of operation.  The AES-GCM algorithms are supported when used with IKEv2. They are not supported when used with IKEv1. |
   | Digest | - SHA2 256 (default) - SHA1 - SHA2 384 - SHA2 512 | The secure hashing algorithm used during the IKE negotiation.  If AES-GCM is the only encryption algorithm selected in the Encryption Algorithm text box, then no hash algorithms can be specified in the Digest Algorithm text box, per section 8 in RFC 5282. In addition, the Psuedo-Random Function (PRF) algorithm PRF-HMAC-SHA2-256 is implicitly selected and used in the IKE security association (SA) negotiation. The PRF-HMAC-SHA2-256 algorithm must also be configured on the peer gateway in order for the phase 1 of the IKE SA negotiation to succeed.  If more algorithms are specified in the Encryption Algorithm text box, in addition to the AES-GCM algorithm, then one or more hash algorithms can be selected in the Digest Algorithm text box. In addition, the PRF algorithm used in the IKE SA negotiation is implicitly determined based on the hash algorithms configured. At least one of the matching PRF algorithms must also be configured on the peer gateway in order for the phase 1 of the IKE SA negotiation to succeed. For example, if the Encryption Algorithm text box contains AES 128 and AES GCM 128 and SHA1 is specified in the Digest Algorithm text box, then the PRF-HMAC-SHA1 algorithm is used during the IKE SA negotiation. It must also be configured in the peer gateway. |
   | Diffie-Hellman Group | - Group 14 (default) - Group 2 - Group 5 - Group 15 - Group 16 - Group 19 - Group 20 - Group 21 | The cryptography schemes that the peer site and the NSX Edge use to establish a shared secret over an insecure communications channel. |

   When you attempt to
   establish an IPSec VPN tunnel with a GUARD VPN Client (previously QuickSec
   VPN Client) using two encryption algorithms or two digest algorithms, the
   GUARD VPN Client adds additional algorithms in the proposed negotiation
   list. For example, if you specified AES 128 and AES 256 as the encryption
   algorithms and SHA2 256 and SHA2 512 as the digest algorithms to use in the
   IKE profile you are using to establish the IPSec VPN tunnel, the GUARD VPN
   Client also proposes AES 192 (using CBC mode) and SHA2 384 in the
   negotiation list. In this case, NSX uses the first encryption algorithm you selected
   when establishing the IPSec VPN tunnel.
7. Enter a security
   association (SA) lifetime value, in seconds, if you want it different from the
   default value of 86400 seconds (24 hours).
8. Provide a description
   and add a tag, as needed.
9. Click
   Save.

A new row is added to the table of available IKE
profiles. To edit or delete a non-system created profile, click the three-dot menu (
![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) and select from the list of actions available.