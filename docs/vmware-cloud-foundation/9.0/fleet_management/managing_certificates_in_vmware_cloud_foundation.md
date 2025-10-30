---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Managing Certificates in VMware Cloud Foundation
---

# Managing Certificates in VMware Cloud Foundation

Manage certificates for VMware Cloud Foundation components according to industry standards and the requirements of your organization. You can use the VCF Operations console to view and manage the certificates for all VMware Cloud Foundation components.

Access to all management component interfaces must be over a Secure Socket Layer (SSL) connection. During deployment, each component is assigned a certificate from a default signing Certificate Authority. You should replace the default certificates for the management domain components with trusted enterprise CA-signed certificates to provide secure access to each component.

In addition, you should replace certificates when:

- A certificate has expired or is nearing its expiration date.
- A certificate has been revoked by the issuing certificate authority.
- Optionally, when you create a new workload domain.

Use the VCF Operations console to:

- View certificates and certificate alerts.
- Enable automatic renewal of certificates.
- Configure a certificate authority (CA).
- Generate certificate signing requests (CSRs).
- Replace certificates.

You can manage certificates for the VCF Management components and for the components in a VCF Instance or VCF domain.

| VCF Management Components | VCF Instance/domain Components |
| --- | --- |
| - Fleet Management - VCF Automation - VCF Identity Broker - VCF Operations - VCF Operations for logs - VCF Operations for networks | - ESX - NSX Manager - SDDC Manager - vCenter |

For Non-Disruptive Certificate updates, you must manage the following certificates from VCF Operations. You can enable auto renewal for these certificates to avoid any disruption caused during certificate renewal.

| Certificate | Component Product |
| --- | --- |
| ESX SSL | ESXi |
| vCenter machine SSL | vCenter |
| NSX LM and VIP | NSX |
| SDDC M SSL | SDDC Manager |
| VCF Identity Broker | VIDB |
| VCF Operations | VCF Operations |
| VCF Automation | VCF Automation |
| VCF Operations for logs | VCF Operations for logs |
| VCF Operations for networks | VCF Operations for networks |
| Fleet Management | VCF Operations Fleet Management |