---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/compliance-based-configurations/compliance-report-codes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Compliance Status Report Codes
---

# Compliance Status Report Codes

You can find the information about the meaning of the compliance report codes in the compliance status report.

|  |
| --- |
| For a complete list of events, see the NSX Event Catalog. |

Compliance Report Codes



| Code | Description | Compliance Status Source | Remediation |
| --- | --- | --- | --- |
| 72001 | Encryption is deactivated. | Reports this status if a VPN IPSec Profile configuration contains NO\_ENCRYPTION, NO\_ENCRYPTION\_AUTH\_AES\_GMAC\_128, NO\_ENCRYPTION\_AUTH\_AES\_GMAC\_192, or NO\_ENCRYPTION\_AUTH\_AES\_GMAC\_256 encryption\_algorithms. This status affects IPSec VPN session configurations which use the reported non-compliant configurations. | Add a VPN IPSec Profile that uses compliant encryption algorithms and use the profile in all VPN configurations. See [Add IPSec Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ipsec-profiles.html#GUID-bac00336-8901-4f87-9f42-d63493d2aec7-en). |
| 72011 | BGP messages with neighbor bypass integrity check. No message authentication defined. | Reports this status if BGP neighbors has no confgured password. This status affects the BGP neighbor configuration. | Configure a password on the BGP neighbor and update the tier-0 gateway configuration to use the password. See [Configure BGP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/configure-bgp-in-nsx.html#GUID-2929c0d8-1d38-4730-8a83-e10f415b3954-en). |
| 72012 | Communication with BGP neighbor uses weak integrity check. MD5 is used for message authentication. | Reports this status if MD5 authentication is used for the BGP neighbor password. This status affects the BGP neighbor configuration. | No remediation available as NSX supports only MD5 authentication for BGP. |
| 72021 | SSL version 3 used for establishing secure socket connection. It is recommended to run TLS v 1.1 or higher and fully deactivate SSLv3 that have protocol weaknesses. | Reports this status if SSL version 3 configuration is in the load balancer client SSL profile, load balancer server SSL profile, or load balancer HTTPS monitor. This status affects the following configurations:  - Load balancer pools that are associated with HTTPS monitors. - Load balancer virtual servers that are associated with load balancer client SSL profiles or server SSL profiles. | Configure an SSL profile to use TLS v1.1 or later and use this profile in all load balancer configurations. See [Add an SSL Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/add-an-ssl-profile.html#GUID-43856964-2dd1-484a-a28f-761288d9c987-en). |
| 72022 | TLS version 1.0 used for establishing secure socket connection. Run TLS v1.1 or higher and fully deactivate TLS v1.0 that have protocol weaknesses. | Reports this status if the load balancer client SSL profile, load balancer server SSL profile, or load balancer HTTPS monitor includes the TLS v1.0 configuration. This status affects the following configurations:  - Load balancer pools that are associated with HTTPS monitors. - Load balancer virtual servers that are associated with load balancer client SSL profiles or server SSL profiles. | Configure an SSL profile to use TLS v1.1 or later and use this profile in all load balancer configurations. See [Add an SSL Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/add-an-ssl-profile.html#GUID-43856964-2dd1-484a-a28f-761288d9c987-en). |
| 72023 | Weak Diffie-Hellman group is used. | Reports this error if a VPN IPSec Profile or VPN IKE Profile configuration includes the following Diffie-Hellman groups: 2, 5, 14, 15 or 16. Groups 2 and 5 are weak Diffie-Hellman groups. Groups 14, 15, and 16 are not weak groups, but are not FIPS-compliant. This status affects IPSec VPN session configurations which use the reported non-compliant configurations. | Configure the VPN Profiles to use Diffie-Hellman group 19, 20, or 21. See [Adding Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles.html#GUID-1dfb1b84-53e7-435b-a636-fafb300ad996-en). |
| 72025 | Quick Assist Technologies (QAT) running on Edge node is non-FIPS compliant. | QAT is a set of hardware accelerated services provided by Intel for cryptography and compression. | To turn off QAT usage, use the NSX CLI. For details, see "Intel QAT Support for IPSec VPN Bulk Cryptography" in the NSX Installation Guide. |
| 72026 | Bouncy-castle FIPS module is not ready. |  | Check to ensure your applications are running and check your logs. |
| 72200 | Insufficient true entropy available. | Reports this status if a pseudo random number generator generates the entropy rather than relying on hardware-generated entropy. NSX Manager node does not use hardware-generated entropy because is does not have the required hardware acceleration support to create sufficient true entropy. | Use newer hardware to run the NSX Manager node. Most recent hardware supports this feature. If the underlying infrastructure is virtual, you will not get true entropy. |
| 72201 | Entropy source unknown. | Reports this status when no entropy status is available for the indicated node. | This error is an internal communication error preventing the NSX Manager from being able to determine the source of entropy. Open a service request with VMware. |
| 72301 | Certificate is not CA signed. | Reports this status when one of the NSX Manager certificates is not CA signed. NSX Manager uses the following certificates:  - Syslog certificate. - API certificates for the individual NSX Manager nodes. - Cluster certificate used for the NSX Manager VIP. | Install CA-signed certificates. Refer [Certificates in NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates.html#GUID-b7714dbe-3c79-4ae3-adff-c6361c5bf9c6-en). |
| 72302 | Certificate is missing Extended Key Usage (EKU) information. | EKU extensions present in the CSR should also be present in the server certificates. | EKU needs to match the intended usage. For example, SERVER when connecting to a server, CLIENT when used as a client certificate on a server. |
| 72303 | Certificate has been revoked. |  | Validity of the certificate is in a terminal state and cannot recover. |
| 72304 | Certificate is not RSA. |  | Ensure your certificate public key is for an RSA certificate. |
| 72305 | Certificate is not Elliptic Curve. | Reports this status when your certificate fails EAL4+ compliance. | Replace your non-compliant certificates with CA-signed certificates. See [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). |
| 72306 | Certificate is missing Basic Constraints. |  | The certificate does not appear to be valid for the selected purpose or may be missing necessary fields or values.. |
| 72307 | Unable to fetch the CRL. |  |  |
| 72308 | The CRL is invalid. |  | Check CRL to determine why it has been marked invalid. |
| 72309 | The Corfu Certificate Expiry Check has been deactivated. |  |  |
| 72310 | Some Compute Manager does not have RSA certificate or the certificate key length is less than 3072 bits. | When a compute manager (for example, vCenter) is connected to the NSX Manager, it passes its certificate to NSX Manager. If the certificate is not an RSA type, or if the certificate is an RSA type, but the certificate's RSA key size is less then 3072 bits, it triggers this error. | Delete the compute manager from NSX Manager. Replace the compute manager's certificate with an RSA certificate with key size of at least 3072 bits. |
| 72401 | Gateway TLS Inspection is non-FIPS compliant. |  |  |
| 72402 | System not FIPS compliant. |  |  |
| 72403 | Principal Identity presence detected in system. Remove all the Principal Identities for EAL4 compliance. |  |  |
| 72404 | OIDC end-point presence detected in system. Remove all the OIDC end-points for EAL4 compliance. |  |  |
| 72501 | Configured user passwords are not compliant. Users must use high-quality passwords of length at least 16 characters. | Reports when user passwords fail EAL4+ compliance. | The password for local users (except for the root user) must be at least 16 characters. In other words, this means that the admin user password must be at least 16 characters. This is in addition to the password complextity check that is required when modifying the password. |
| 72502 | Unable to get synchronized users. |  |  |
| 72503 | SSH service for Manager appliance found to be in running state. |  |  |
| 72504 | Non-admin active user accounts detected. | When any user other than admin is active in the NSX Manager. | Deactivate all other users other than admin. |
| 73000 | Error occurred while gathering platform compliance data. |  |  |