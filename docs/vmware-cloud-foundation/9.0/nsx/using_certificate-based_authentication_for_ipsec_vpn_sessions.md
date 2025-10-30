---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/using-certificate-based-authentication-for-ipsec-vpn-sessions.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using Certificate-Based Authentication for IPSec VPN Sessions
---

# Using Certificate-Based Authentication for IPSec VPN Sessions

When you use certificate-based authentication for an IPSec VPN session, you must
configure the certificate details for the IPSec session in the associated local
endpoint.

Wildcard certificates are not supported for IPSec VPN.

Refer to the following workflow for details on how to configure the certificate details
for a IPSec VPN session.

## Configure Certificate-Based Authentication for an IPSec VPN Session

1. Create and enable an IPSec VPN service
   using an existing Tier-0 or Tier-1 gateway. See [Add an IPSec VPN Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html#GUID-fa3387e6-8188-4db8-913c-c1fa71b9db5a-en).
2. If you do not have the necessary
   server certificates or CA certificates in NSX Manager,
   import the certificates. See [Import a Self-signed or CA-signed Certificate for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-certificate.html#GUID-7c651d93-4af8-45f8-a5a4-0ce67739291c-en)
   and [Import a CA Certificate for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-ca-certificate.html#GUID-4da8a492-310f-4459-8245-ea63125c6105-en).
3. Use [Add Local Endpoints](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-local-endpoints.html#GUID-af6404f4-1d30-49a9-8752-0214143ca288-en)
   to create a VPN server hosted on the logical router and select the certificates
   for it.

   The local ID is derived
   from the certificate associated with the local endpoint and depends on the
   X509v3 extensions present in the certificate. The local ID can be either the
   X509v3 extension Subject Alternative Name (SAN) or Distinguished Name (DN).
   The Local ID is not required and the ID specified
   there is ignored. However, for the remote VPN gateway, you need to configure
   the local ID as remote ID in the peer VPN gateway.

   - If X509v3 Subject
     Alternative Name is found in the certificate, then one of
     the SAN strings is taken as the local ID value.

     If the certificate has
     multiple SAN fields, then following order is used to select the
     local ID.

     | Order | SAN Field |
     | --- | --- |
     | 1 | IP Address |
     | 2 | DNS |
     | 3 | Email Address |

     For
     example, if the configured site certificate has the following SAN
     fields,

     ```
     X509v3 Subject Alternative Name:
     DNS:Site123.vmware.com, email:[email protected], IP Address:1.1.1.1
     ```

     then the IP address
     1.1.1.1 is used as the local ID. If the IP
     address is not available, then the DNS string is used. And if the IP
     address and the DNS are not available, then the email address is
     used.
   - If X509v3 Subject
     Alternative Name is not present in the certificate, then
     the Distinguished Name (DN) is used as the local ID value.

     For example, if the
     certificate does not have any SAN fields, and its DN string
     is

     ```
     C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123
     ```

     then the DN string
     automatically becomes the local ID. The local ID is the peer ID on
     the remote site.

   If the certificate
   details are not properly configured, it might cause the VPN session to go
   down with the Down alarm of Authentication
   failed.
4. Configure either a policy-based or
   route-based IPSec VPN session. See [Add a Policy-Based IPSec Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/add-a-policy-based-ipsec-session.html#GUID-b54c8bc3-155d-4776-ac8c-552fb895bf23-en)
   or [Add a Route-Based IPSec Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/add-a-route-based-ipsec-session.html#GUID-283768dd-af07-48cc-91fb-2fc169f4bf4f-en).

   Make sure to configure the
   following settings.

   1. From the
      Authentication Mode drop-down menu, select
      Certificate.
   2. In the Remote
      ID textbox, enter a value to identify the peer site.

      The remote ID must be a
      distinguished name (DN), IP address, DNS, or an email address used
      in the peer site's certificate.

      If the peer site's
      certificate contains an email address in the DN string, for
      example,

      ```
      C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123/[email protected]
      ```

      then enter the
      Remote ID value using the following
      format as an example.

      ```
      C=US, ST=California, O=MyCompany, OU=MyOrg, CN=Site123, [email protected]
      ```