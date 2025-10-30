---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ipsec-profiles.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add IPSec Profiles
---

# Add IPSec Profiles

The Internet
Protocol Security (IPSec) profiles provide information about the algorithms
that are used to authenticate, encrypt, and establish a shared secret between
network sites when you establish an IPSec tunnel.

NSX provides system-generated IPSec profiles that are assigned
by default when you configure an IPSec VPN or L2 VPN service. The following table
lists the default IPSec profiles provided.

Default IPSec Profiles Used
for IPSec VPN or L2 VPN Services



| Name of Default IPSec Profile | Description |
| --- | --- |
| nsx-default-l2vpn-tunnel-profile | - Used for L2   VPN. - Configured with   AES GCM 128 encryption algorithm and Diffie-Hellman   group 14 key exchange algorithm. |
| nsx-default-l3vpn-tunnel-profile | - Used for IPSec   VPN. - Configured with   AES GCM 128 encryption algorithm and Diffie-Hellman   group 14 key exchange algorithm. |

Instead of the default IPSec profile, you can also
select one of the supported compliance suites. See [About Supported Compliance Suites](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/about-supported-compliance-suites.html#GUID-26aebcc3-d15b-46d6-8ff9-e3b1a9416802-en) for more information.

If you decide not to use the default IPSec profiles or
compliance suites provided, you can configure your own using the following steps.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingVPN and then click the Profiles tab.
3. Select the
   IPSec
   Profiles profile type, and click
   Add IPSec
   Profile.
4. Enter a name for the
   IPSec profile.
5. From the drop-down
   menus, select the encryption, digest, and Diffie-Hellman algorithms. You can
   select multiple algorithms to apply.

   Deselect the ones you do not want used.

   Algorithms
   Used



   | Type of Algorithm | Valid Values | Description |
   | --- | --- | --- |
   | Encryption | - AES GCM   128 (default) - AES   128 - AES   256 - AES GCM   192 - AES GCM   256 - No Encryption Auth AES GMAC 128 - No   Encryption Auth AES GMAC 192 - No   Encryption Auth AES GMAC 256 - No   Encryption | The encryption algorithm used during the Internet Protocol Security (IPSec) negotiation.  The AES 128 and AES 256 algorithms use the CBC mode of operation. |
   | Digest | - SHA1 - SHA2   256 - SHA2   384 - SHA2   512 | The secure hashing algorithm used during the IPSec negotiation. |
   | Diffie-Hellman Group | - Group   14 (default) - Group   2 - Group   5 - Group   15 - Group   16 - Group   19 - Group   20 - Group   21 | The cryptography schemes that the peer site and NSX Edge use to establish a shared secret over an insecure communications channel. |
6. Deselect
   PFS
   Group if you decide not to use the PFS Group protocol on your VPN
   service.

   It is selected by
   default.
7. In the
   SA
   Lifetime text box, modify the default number of seconds before the
   IPSec tunnel must be re-established.

   By default, an SA
   lifetime of 24 hours (86400 seconds) is used.
8. Select the value for
   DF
   Bit to use with the IPSec tunnel.

   The value
   determines how to handle the "Don't Fragment" (DF) bit included in the data
   packet received. The acceptable values are described in the following table.

   DF Bit Values



   | DF Bit Value | Description |
   | --- | --- |
   | COPY | The default value. When this value is selected, NSX copies the value of the DF bit from the received packet into the packet which is forwarded. This value implies that if the data packet received has the DF bit set, after encryption, the packet also has the DF bit set. |
   | CLEAR | When this value is selected, NSX ignores the value of the DF bit in the data packet received, and the DF bit is always 0 in the encrypted packet. |
9. Provide a description
   and add a tag, if necessary.
10. Click
    Save.

A new row is added to the table of available IPSec
profiles. To edit or delete a non-system created profile, click the three-dot menu (
![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) and select from the list of actions available.