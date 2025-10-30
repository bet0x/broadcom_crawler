---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-information-security-and-access-design-for-esxi/certificate-management-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Certificate Management Design
---

# Certificate Management Design

You design certificate management for VMware Cloud Foundation according to industry standards and the requirements of your organization.

Access to all management component interfaces must be over a Secure Socket Layer (SSL) connection. During deployment, each component is assigned a certificate from a default signing CA. Replace the default certificate with a trusted enterprise CA-signed certificate to provide secure access to each component.

Certificate Management in VMware Cloud Foundation



| Component | Default Signing CA | Life cycle for CA-Signed Certificates |
| --- | --- | --- |
| SDDC Manager | Management domain VMCA | VCF Operations |
| NSX Local Manager | Management domain VMCA | VCF Operations |
| NSX Edges | Not applicable | Not applicable |
| NSX Global Manager | Self Signed | Manual |
| vCenter | Local workload domain VMCA | VCF Operations |
| ESX | Local workload domain VMCA | VCF Operations |
| VCF Operations | VCF Operations fleet management locker | VCF Operations |
| VCF Operations fleet management appliance | VCF Operations fleet management locker | VCF Operations |
| VCF Automation | VCF Operations fleet management locker | VCF Operations |
| VCF Operations logs | VCF Operations fleet management locker | VCF Operations |
| VCF Operations networks | VCF Operations fleet management locker | VCF Operations |
| vSphere Supervisor | Local workload domain VMCA | Automatic / Manual |

Certificate Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SEC-RCMD-CERT-001 | Replace the default VMCA or signed certificates on all management components with a certificate that is signed by an internal certificate authority. | Ensures that the communication to all management components is secure. | Replacing the default certificates with trusted CA-signed certificates from a certificate authority might increase the deployment preparation time because you must generate and submit certificate requests. |
| VCF-SEC-RCMD-CERT-002 | Use a SHA-2 algorithm or higher for signed certificates. | The SHA-1 algorithm is considered less secure and has been deprecated. | Not all certificate authorities support SHA-2 or higher. |
| VCF-SEC-RCMD-CERT-003 | Perform SSL certificate life cycle management for all management appliances by using VCF Operations. | VCF Operations supports automated SSL certificate lifecycle management rather than requiring a series of manual steps. | Certificate management for NSX Global Manager instances must be done manually. |