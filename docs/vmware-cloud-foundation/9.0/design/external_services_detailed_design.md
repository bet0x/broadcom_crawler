---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > External Services Detailed Design
---

# External Services Detailed Design

IP addressing scheme, name resolution, and time synchronization must support the requirements of the VMware Cloud Foundation platform.

## External Services Design Requirements for VMware Cloud Foundation

Network Time Protocol Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-NTP-001 | Configure time synchronization using an internal NTP time source for all management components. | Ensures that all management components are synchronized with a valid time source. | An operational NTP service must be available in the environment. |
| VCF-NET-REQD-NTP-002 | Set the NTP service for all management components to start automatically. | Ensures that the NTP service remains synchronized after you restart a component. | None. |