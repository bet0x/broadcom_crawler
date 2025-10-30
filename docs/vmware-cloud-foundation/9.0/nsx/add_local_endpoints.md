---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-local-endpoints.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Local Endpoints
---

# Add Local Endpoints

You must configure
a local endpoint to use with the IPSec VPN that you are configuring.

- If you are using a certificate-based
  authentication mode for the IPSec VPN session that is to use the local endpoint
  you are configuring, obtain the information about the certificate that the local
  endpoint must use.
- Ensure that you have configured an
  IPSec VPN service to which this local endpoint is to be associated.

The following steps use the Local Endpoints tab
on the NSX Manager UI. You can also create a local
endpoint while in the process of adding an IPSec VPN session by clicking the
three-dot menu ( ![Three black dots aligned vertically. Clicking this icon displays a menu of sub-commands.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) ) and selecting Add
Local Endpoint. If you are in the middle of configuring an IPSec VPN
session, proceed to step 3 in the following steps to guide you with creating a new
local endpoint.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to and click Add Local
   Endpoint.
3. Enter a name for the local
   endpoint.
4. From the VPN Service
   drop-down menu, select the IPSec VPN service to which this local endpoint is to
   be associated.
5. Enter an IP address for
   the local endpoint.

   For
   an IPSec VPN service running on a Tier-0 gateway, the local endpoint IP
   address must be different from the Tier-0 gateway's uplink interface IP
   address. The local endpoint IP address you provide is associated with the
   loopback interface for the Tier-0 gateway and is also published as a
   routable IP address over the uplink interface.

   For an
   IPSec VPN service running on a Tier-1 gateway, the local endpoint IP address
   must be different from the Tier-1 gateway's uplink interface IP address. For
   the local endpoint IP address to be routable, the route advertisement for
   IPSec local endpoints must be enabled in the Tier-1 gateway configuration.
   See [Add an NSX Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html#GUID-2567f98d-7076-468c-8afc-285870869371-en) for more
   information.
6. If
   you are using a certificate-based authentication mode for the IPSec VPN
   session, from the
   Site
   Certificate drop-down menu, select the certificate that is to be
   used by the local endpoint.
7. Optionally add a description in Description.
8. Enter the Local ID value
   that is used for identifying the local NSX Edge instance. 

   This
   local ID is configured as remote ID on the remote site. The local ID must either
   be the IP address or FQDN of the local site. For IPSec VPN sessions with
   certificate-based authentication and are associated with the local endpoint, the
   Local ID is derived from the certificate associated
   with the local endpoint. The ID specified in the Local ID text
   box is ignored. The local ID derived from the certificate for a VPN session
   depends on the extensions present in the certificate.
   - If the X509v3 extension
     X509v3
     Subject Alternative Name is not present in the
     certificate, then the Distinguished Name (DN) is used as the local
     ID value.

     For example, if the
     certificate does not have any Subject Alternative Name (SAN) fields
     and its DN string is:

     ```
     C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123
     ```

     then the DN string is
     used as the local ID. This local ID is the peer ID on the remote
     site.
   - If the X509v3 extension
     X509v3
     Subject Alternative Name is found in the certificate,
     then one of the SAN fields is taken as the local ID value.

     If the certificate has
     multiple SAN fields, then the following order is used to select the
     local ID.

     | Order | SAN Field |
     | --- | --- |
     | 1 | IP Address |
     | 2 | DNS |
     | 3 | Email Address |

     For example, if the
     configured site certificate has the following SAN fields:

     ```
     x509v3 Subject Alternative Name:
     DNS:Site123.vmware.com, email:[email protected], IP Address:1.1.1.1
     ```

     then the IP address
     1.1.1.1 is used as the local ID. If the IP
     address is not available, then the DNS string is used. And if the IP
     address and DNS are not available, then the email address is
     used.

   To see the local ID that is used
   for an IPSec VPN session, do the following:

   1. Navigate to NetworkingVPN and then click the IPSec Sessions
      tab.
   2. Expand the IPSec VPN
      session.
   3. Click Download
      Config to download the configuration file which contains
      the local ID as the remote ID to be configured at the remote VPN
      endpoint.
9. From the Trusted CA
   Certificates and Certificate Revocation
   List drop-down menus, select the appropriate certificates that
   are required for the local endpoint.
10. Specify a tag.
11. Click Save.