---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/types-of-certificates.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Types of Certificates in NSX
---

# Types of Certificates in NSX

There are three categories of self-signed certificates in NSX.

- Platform Certificates
- NSX Services Certificates
- Principal Identity Certificates

Refer to the following sections for details on each certificate category. Other types of certificates might be present in NSX. Refer to that component or application documentation for details on their certificates.

Starting in NSX and NSX Federation 4.2, many certificates used to support RPC traffic (APH and CCP) have been combined to improve serviceability. There now are only three certificates for each NSX Manager node instead of nine. You can replace the self-signed internal certificates with CA-signed certificates using ECDSA-based certificates that get generated using AES 256 encryption. For a list of replaceable certificates, refer to [Certificates for NSX and NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html#GUID-c283012b-c8e5-4e1e-b479-40005684524c-en). For command details, see the NSX API Guide.

Though NSX supports secp256k1 keys for all certificates, do not use this key if your environment requires only FIPS-approved cryptographic keys.

## Platform Certificates

After you install NSX, navigate to System Certificates to view the platform certificates created by the system. By default, these self-signed X.509 RSA 2048/SHA256 certificates get used for internal communication within NSX and for external authentication when you use NSX Manager to access the APIs or the UI.

The internal certificates are not viewable or editable.

When you deploy NSX through the default VMware Cloud Foundation™ (VCF) workflow, the default NSX API and Cluster certificates get replaced with CA certificates signed by the VMware Certificate Authority (VMCA) from vCenter. The API and Cluster certificates might still display in the certificate list, but are not used. Replace the CA-signed certificates using the procedure in the VCF Administration Guide. After you perform the replacement, your NSX Manager stores in the UI contain the API and Cluster certificates, the VMCA CA certificates, and the signed certificates by the third-party organization. From then on, the NSX Manager uses the signed certificate from your organization.

Platform Certificates in NSX



| Naming Convention in NSX Manager | Purpose | Replaceable? | Default Validity |
| --- | --- | --- | --- |
| API (previously known as tomcat) | This serves as a server certificate for the API/UI client reaching the NSX Manager HTTPS port (port 443). | Yes. See [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en) | 825 days |
| Cluster (previously known as mp-cluster) | This certificate serves as a server certificate for API/UI client reaching the HTTPS port of the cluster VIP (port 443) when a VIP is used for an NSX Manager cluster. | Yes. See [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en) | 825 days |
| Other certificates | Certificates specifically for other purposes including NSX Federation, Cluster Boot Manager (CBM), and Central Control Plane (CCP). | See [Certificates for NSX and NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html#GUID-c283012b-c8e5-4e1e-b479-40005684524c-en) for details on self-signed certificates auto-configured for NSX and NSX Federation environments. | Varies |

## NSX Service Certificates

NSX service certificates are user-facing for services such as load balancer, VPN, and TLS Inspection. The policy API manages service certificates. Non-service certificates are used by the platform for tasks such as cluster management. The management plane (MP) or truststore APIs manage non-service certificates.

When adding service certificates using the policy API, the certificate gets sent to the MP/truststore API, but not with the relationship reversed.

NSX service certificates cannot be self signed. You must import them. See [Importing Certificates for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates.html#GUID-9030cb7f-2c7c-4e42-bcc5-66d2efecb207-en) for instructions.

You can generate a root certificate authority (CA) certificate and a private key based on RSA. CA certificates are able to sign other certificates.

You can use a certificate signing request (CSR) as an NSX service certificate if it is signed by a CA (a local CA or a public CA like Verisign). Once the CSR is signed, you can import that signed certificate into NSX Manager. A CSR can be generated on NSX Manager or outside of NSX Manager. The Service Certificate flag is deactivated for CSRs generated on NSX Manager. Therefore, the signed CSRs cannot be used as service certificates, but only as platform certificates.

Platform and NSX service certificates are stored separately within the system and certificates imported as NSX service certificate cannot be used for platform or the reverse.

## Principal Identity (PI) Certificates

API requests use PI certificates. PI certificates are one of the NSX Manager authentication mechanisms. Any NSX Manager client can create and use a PI certificate. It is the preferred approach for machine-to-machine communication.

PI for Cloud Management Platforms (CMP), such as Openstack, uses X.509 certificates that are uploaded when onboarding a CMP as a client. For information on assigning roles to Principal Identity and replacing PI certificates, see [Add a Role Assignment or Principal Identity](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/add-role-assignment-or-principal-identity.html#GUID-b639913c-fa8a-49d1-9047-cbef10ba4317-en)

PI for NSX Federation uses X.509 platform certificates for the Local Manager and Global Manager appliances. See [Certificates for NSX and NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html#GUID-c283012b-c8e5-4e1e-b479-40005684524c-en) for details on self-signed certificates auto-configured for NSX Federation.