---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vmkernel-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VMkernel Detailed Design
---

# VMkernel Detailed Design

The VMkernel networking layer provides connectivity to hosts and handles the system traffic for management, vSphere vMotion, vSphere HA, vSAN, NSX Host TEPs, etc

## VMkernel Network Adapter Design

The following are the VMKernels created on the ESX hosts used by clusters in VMware Cloud Foundation.

VMkernel Network Adapter Configuration



| VMkernel Adapter Service | Connected Distributed Port Group | Activated Services | Recommended MTU Size (Bytes) |
| --- | --- | --- | --- |
| ESX Management | ESX Management Port Group | Management Traffic | 1500 (Default) |
| vMotion | vMotion Port Group | vMotion Traffic | 9000 |
| vSAN | vSAN Port Group | vSAN | 9000 |
| NFS | NFS Port Group | NFS | 9000 |
| Host TEPs | Not applicable | Not applicable | 9000 |