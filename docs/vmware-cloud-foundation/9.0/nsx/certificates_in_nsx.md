---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Certificates in NSX
---

# Certificates in NSX

After you install NSX, the manager nodes and cluster have vCenter certificate authority (CA) certificates.

If you are using NSX Federation, additional certificates are set up to establish trust between the Local Managers and Global Manager. If you are using TLS Inspection, a CA-signed security certificate is required. For details on TLS Inspection and certificates, see the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html).

To view details of all the certificates that are installed on the system, navigate to SystemCertificates.

You can perform the following actions for certificates:

- Filter certificates based on their basic parameters (such as name or path) or based on predefined filters (such as expired certificates or used certificates)
- Import certificates
- Create a certificate signing request (CSR)
- Generate self-signed certificates

- Replace self-signed certificates
- Apply certificates to services
- Delete unused certificates
- Import a certificate revocation list (CRL)

To improve the security in the system, it is recommended that you replace the self-signed certificates with CA-signed certificates.

Starting with NSX 4.2, the Certificates page also displays a dashboard that provides a quick glance of total certificates, number of expired certificates, and total used and unused certificates in the system. Also, the following certificates have been consolidated:

- The APH, APH\_TN, and CCP certificates have been consolidated into one.
- The API services and MGMT\_CLUSTER (aka VIP) certificates have been consolidated into one.

To replace a consolidated certificate, you must follow certain considerations. For more information about these considerations, see [Replace NSX Certificates from NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-nsx-manager.html#GUID-67c93e67-e765-4cb0-bc25-bb4fec716ec3-en_GUID-09D04249-5B41-415B-AE7F-78252092680A).