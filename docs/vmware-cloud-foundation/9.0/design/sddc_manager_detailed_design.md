---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > SDDC Manager Detailed Design
---

# SDDC Manager Detailed Design

SDDC Manager provides fleet management capabilities for the underlying virtual infrastructure and uses binaries to deploy new workload domains, and to patch and upgrade existing ones.

## SDDC Manager Binary Management

SDDC Manager uses binaries to deploy, patch or upgrade the underlying virtual infrastructure and provides users with flexibility in how they obtain and consume the binaries.

| Mode | Details | Benefits | Implications |
| --- | --- | --- | --- |
| Connected Mode | SDDC Manager maintains a live connection to Broadcom depot via the internet and regularly updates the unified manifest. | Reduced operational overhead. | An outbound internet connection to the Broadcom depot is required for Connected Mode. |
| Disconnected Mode | Offline registration of SDDC Manager with an internal depot. | - Internet connection is not required for SDDC Manager instances. - Internal centrally managed depot. - Increased security posture. | Operational overhead of manual binary download management to populate the offline depot. |
| Manual | Manual download of binaries and upload to an SDDC Manager instance. | Increased security posture. | Operational overhead of manual binary download management. |

SDDC Manager Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-SDDCM-REQD-CFG-001 | Deploy a new SDDC Manager with each new VCF Instance. | The VCF Installer will automatically install new SDDC Manager with each new management domain. | None. |
| VCF-SDDCM-REQD-CFG-002 | Deploy an SDDC Manager system in the first availability zone of the management domain. | SDDC Manager is required to perform VMware Cloud Foundation capabilities, such as provisioning workload domains, deploying solutions, patching, upgrading, and others. | None. |
| VCF-SDDCM-REQD-CFG-003 | Place the SDDC Manager appliance on the VM management network. | - Simplifies IP addressing for management VMs by using the same VLAN and subnet. - Provides simplified secure access to management VMs in the same VLAN network. | None. |