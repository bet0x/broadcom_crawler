---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints/vcf-fleet-basic-management-design/design-decisions-for-vcf-fleet-in-a-single-site-with-minimal-footprint/security-governance-and-compliance-design-elements-for-vcf-fleet-in-a-single-site-with-minimal-footprint.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Security Governance and Compliance Design Elements for VCF Fleet in a Single Site with Minimal Footprint
---

# Security Governance and Compliance Design Elements for VCF Fleet in a Single Site with Minimal Footprint

This section provides the security governance and compliance requirements and recommendations for the VCF Fleet in a Single Site with Minimal Footprint blueprint

Embedded VCF Identity Broker Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-EMB-001 | Leverage the embedded VCF Identity Broker in the first management domain vCenter. | - Simplifies the authentication configuration for the VMware Cloud Foundation platform. - Simplifies the operational overhead. | - Limits the Scale supported by the embedded model. - Limits the availability of the authentication service in a VMware Cloud Foundation platform. |
| VCF-SSO-REQD-EMB-002 | Connect the embedded VCF Identity Broker to your corporate IdP. | Provides directory service (users and group) and user authentication service to the VCF Identity Broker service. | None. |

VCF Fleet-Wide Single Sign-On Design Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-VFL-001 | Deploy VCF Identity Broker in the management domain of the first VCF Instance. | - Provides an authentication service for the first VCF Instance. - Provides VCF Single Sign-On capabilities to the first VCF Instance. | Workload domains will use the same authentication source as management domain |
| VCF-SSO-REQD-VFL-002 | Configure additional VCF Instances in the VCF fleet to consume the same VCF Identity Broker configured in the first VCF Instance. | - Provides an authentication source for all components in the VCF fleet. - Provides VCF Single Sign-On capabilities to all components in the VCF fleet. | An impact to the VCF Identity Broker service will impact the VCF fleet. |

Account and Password Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SEC-RCMD-ACT-001 | Enable scheduled password rotation in VCF Operations for all accounts supporting scheduled rotation. | - Increases the security posture of your VCF fleet. - Simplifies password management across your VCF fleet management components. | You must retrieve new passwords by using the API if you must use accounts interactively. |
| VCF-SEC-RCMD-ACT-002 | Establish operational practice to rotate passwords using VCF Operations on components that do not support scheduled rotation in VCF Operations. | Rotates passwords and automatically remediates VCF Operations databases for those user accounts. | None. |
| VCF-SEC-RCMD-ACT-003 | Establish operational practice to manually rotate passwords on components that cannot be rotated by VCF Operations. | Maintains password policies across components not handled by VCF Operations password management. | None. |

Certificate Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SEC-RCMD-CERT-001 | Replace the default VMCA or signed certificates on all management components with a certificate that is signed by an internal certificate authority. | Ensures that the communication to all management components is secure. | Replacing the default certificates with trusted CA-signed certificates from a certificate authority might increase the deployment preparation time because you must generate and submit certificate requests. |
| VCF-SEC-RCMD-CERT-002 | Use a SHA-2 algorithm or higher for signed certificates. | The SHA-1 algorithm is considered less secure and has been deprecated. | Not all certificate authorities support SHA-2 or higher. |
| VCF-SEC-RCMD-CERT-003 | Perform SSL certificate life cycle management for all management appliances by using VCF Operations. | VCF Operations supports automated SSL certificate lifecycle management rather than requiring a series of manual steps. | Certificate management for NSX Global Manager instances must be done manually. |