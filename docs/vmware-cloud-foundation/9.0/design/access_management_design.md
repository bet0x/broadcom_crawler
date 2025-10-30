---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-information-security-and-access-design-for-esxi/access-management-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Access Management Design
---

# Access Management Design

Each component in a VMware Cloud Foundation platform has specific access methods. From a security perspective, you must be aware of these access methods to ensure you only grant access to each component to the right users.

Access Methods for each VCF Component



| Component | Access Method | Additional Information |
| --- | --- | --- |
| SDDC Manager | - UI - API - SSH | SSH is active by default. root user access is not permitted. |
| NSX Local Manager | - UI - API - SSH | SSH is deactivated by default. |
| NSX Edge | - API - SSH | SSH is deactivated by default. |
| NSX Global Manager | - UI - API - SSH | SSH setting is defined during deployment. |
| vCenter | - UI - API - SSH - VAMI | SSH is active by default. |
| ESX | - Direct Console User Interface (DCUI) - ESX Shell - SSH - VMware Host Client | SSH and ESX shell are deactivated by default. |
| VCF Operations | - UI - API - SSH | SSH is active by default. |
| VCF Operations fleet management | - API - SSH | SSH is active by default. |
| VCF Operations collector | - API - SSH | SSH is active by default. |
| VCF Operations for logs | - UI - API - SSH | SSH is active by default. |
| VCF Operations for networks | - UI - API - SSH | SSH is active by default. root user access is not permitted. |
| VCF Automation | - UI - API - SSH | SSH is active by default. |
| VCF Identity Broker | - API - SSH | SSH is active by default. |
| vSphere Supervisor | - UI - API - CLI - SSH | - UI is via vCenter - CLI requires Kubernetes CLI Tools - SSH is active by default. |