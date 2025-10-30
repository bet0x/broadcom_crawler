---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-information-security-and-access-design-for-esxi/service-account-design-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Account Management Design
---

# Account Management Design

You design account management for your VMware Cloud Foundation platform according to industry standards and the requirements of your organization.

## Password Management Methods

Multiple methods for managing password life cycle are supported.

Password Management Methods in VMware Cloud Foundation



| Method | Description |
| --- | --- |
| Update | Update password for a single account with a manually entered password |
| Remediate | Reconcile a single account with a password that has been set manually at the component. |
| Manual | Update a password manually directly in the component. |

## Account and Password Management

VMware Cloud Foundation comprises multiple types of interactive, local, and service accounts. Each account has different attributes and can be managed in the following ways:

For more information on password complexity, account lockout or integration with additional Identity Providers, refer to the [Identity and Access Management for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vvs/1-0/identity-and-access-management-for-vmware-cloud-foundation.html).

Account and Password Management in VMware Cloud Foundation



| Component | User Account | Password Management | Additional Information |
| --- | --- | --- | --- |
| SDDC Manager/VCF Installer | admin@local | - Manual by using the SDDC Manager API. - Default Expiry: Never | - Local appliance account.API access (break-glass account). |
| vcf | - Manual by using the OS. - Default Expiry: 365 days | - Local appliance account. - OS level access. |
| root | - Manual by using the OS. - Default Expiry: 365 days | - Local appliance account. - OS level access. |
| backup | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 365 days | - Local appliance account. - OS level access. |
| [[email protected]](/cdn-cgi/l/email-protection) | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - vCenter Single Sign-On account. - Application and API access. - Additional VMware Cloud FoundationAdmin account required to perform manual password rotation. |
| NSX Local Manager | admin | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account.OS level, API, and application access. |
| root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| audit | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. - Read-only application level access. |
| svc-sddc-manager-hostname-nsx-vip-hostname-uid | - System managed. - Automatically rotated every 30 days by default. - Default Expiry: 90 | Service account between SDDC Manager and NSX. |
| svc-ops-nsx-uid | - System managed. - Default Expiry: Never | Service account between VCF Operations and NSX. |
| svc-net\_uid | - System managed. - Default Expiry: Never | Service account between VCF Operations for networks and NSX. |
| svc-vcfa\_uid | - System managed. - Default Expiry: Never | Service account between VCF Automation and NSX. |
| NSX Edge | admin | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level, API, and application access. |
| root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| audit | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. - Read-only application level access. |
| NSX Global Manager | admin | - Manual by using the NSX Global Manager UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level, API, and application access. |
| root | - Manual by using each NSX Global Manager appliance. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| audit | - Manual by using the NSX Global Manager UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. - Read-only application level access. |
| vCenter | root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. - VAMI access. |
| [[email protected]](/cdn-cgi/l/email-protection) | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - vCenter Single Sign-On account. - Application and API access. - Relevant to isolated workload domain. |
| svc-sddc-manager-hostname-vcenter-hostname@vsphere.local | - System managed. - Automatically rotated every 30 days by default. - Default Expiry: 90 | - Service account between SDDC Manager and vCenter. - Administrator role. |
| svc-nsx-manager-hostname-vcenter-hostname@vsphere.local | - System managed. - Automatically rotated every 30 days by default. - Default Expiry: 90 | - Service account between NSX Manager and vCenter. - Administrator role.svc-vcf-ops-fleet-management-hostname-vcenter-server-hostname@vsphere.localSystem managed. |
|  | - Automatically rotated every 30 days by default. - Default Expiry: None | - Service account between VCF Operations fleet management and vCenter. - Administrator role. |
| svc-ops-vc-vcf-ops-cluster-uid@vsphere.local | - System managed. - Automatically rotated every 30 days by default. - Default Expiry: None | - Service account between VCF Operations and vCenter. - Administrator role. |
| svc-vcfa\_uid@vsphere.local | - System managed - Automatically rotated every 30 days by default. - Default Expiry: None | - Service account between VCF Automation and vCenter. - Administrator role. |
| svc-vcfsp-vc-uid@vsphere.local | - System managed - Automatically rotated every 30 days by default. - Default Expiry: None | - Service account between VCF Services Platform and vCenter. - VCF Services Platform role. |
| svc-vcfsp-vc-admin-uid@vsphere.local | - System managed. - Automatically rotated every 30 days by default. - Default Expiry: None | - Service account between VCF Services Platform and vCenter. - VCF Services Platform Admin role. |
| ESX | root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 99999 (never) | Local root account. |
| svc-vcf-ESX-hostname | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 99999 (never) | Service account between SDDC Manager and the ESX host. |
| VCF Operations | admin | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: Never | API and application access. |
| root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| VCF Operations Fleet Management Appliance | admin@local | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: Never | API and application access. |
| root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| VCF Operations Collectors | root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| VCF Automation | vmware-system-user | Update or remediate by using the VCF Operations UI or API. | - Local appliance account. - OS level access. |
| VCF Identity Broker | vmware-system-user | Update or remediate by using the VCF Operations UI or API. | - Local appliance account. - OS level access. |
| VCF Operations for logs | admin | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: Never | API and application access. |
| root | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 90 days | - Local appliance account. - OS level access. |
| VCF Operations for networks | admin@local | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: Never | API and application access. |
| root | - Manual by using the OS. - Default Expiry: 99999 (never) | - Local appliance account. - OS level access. |
| support | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 99999 (never) | - Local appliance account. - OS level access. |
| consoleuser | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 99999 (never) | - Local appliance account. - cli access. |
| VCF Operations for networks collector | support | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 99999 (never) | - Local appliance account. - OS level access. |
| consoleuser | - Update or remediate by using the VCF Operations UI or API. - Default Expiry: 99999 (never) | - Local appliance account. - cli access. |
| vSphere Supervisor | vmware-system-user | Encoded in control plane namespace secret. | - Local appliance account. - OS level access. |

## Account Management Design Recommendations

In your account management design, you can apply certain best practices.

Account and Password Management Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SEC-RCMD-ACT-001 | Enable scheduled password rotation in VCF Operations for all accounts supporting scheduled rotation. | - Increases the security posture of your VCF fleet. - Simplifies password management across your VCF fleet management components. | You must retrieve new passwords by using the API if you must use accounts interactively. |
| VCF-SEC-RCMD-ACT-002 | Establish operational practice to rotate passwords using VCF Operations on components that do not support scheduled rotation in VCF Operations. | Rotates passwords and automatically remediates VCF Operations databases for those user accounts. | None. |
| VCF-SEC-RCMD-ACT-003 | Establish operational practice to manually rotate passwords on components that cannot be rotated by VCF Operations. | Maintains password policies across components not handled by VCF Operations password management. | None. |