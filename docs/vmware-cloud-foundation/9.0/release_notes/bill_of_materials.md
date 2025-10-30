---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/vmware-cloud-foundation-bill-of-materials.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > Bill of Materials
---

# Bill of Materials

This document contains the following sections

- [Bill of Materials (BOM)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/vmware-cloud-foundation-bill-of-materials.html#GUID-5d0d30f1-d79b-4503-b44b-adfbd515f60d-en_id-508ffab8-2b35-47b6-a0ef-ca002e396e65)
- [Internationalization](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/vmware-cloud-foundation-bill-of-materials.html#GUID-5d0d30f1-d79b-4503-b44b-adfbd515f60d-en_id-dcee9b18-0fee-404b-9dbb-72b56ea28faf)

## Bill of Materials (BOM)

The VMware Cloud Foundation (VCF) software product is comprised of the following software components listed in the Bill of Materials (BOM) table. The components in the BOM are interoperable and compatible. You can select which components to apply in your deployment based on the impact to your environment and operational costs. The [Broadcom Support Portal](https://support.broadcom.com/group/ecx/downloads) allows you to download the appropriate set of bits based on your entitlement.

**IMPORTANT**: Review the [Deployment, Convergence, and Upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment.html) guide before you upgrade any components to VCF 9.0. For more information, see [VMware Cloud Foundation 9.0 and VMware vSphere Foundation 9.0 Feature Comparison & Upgrade Paths.](https://www.vmware.com/docs/vmware-cloud-foundation-9-0-feature-comparison-and-upgrade-paths)

|  |  |  |  |
| --- | --- | --- | --- |
| **VMware Cloud Foundation Component** | **VMware vSphere Foundation Component** | **Version** | **Build Number** |
| VCF Installer \* | Yes | 9.0.1.0 | 24962180 |
| VMware ESX | Yes | 9.0.0.0 | 24755229 |
| VMware vCenter | Yes | 9.0.0.0 | 24755230 |
| VMware vSAN ESA Witness | Yes | 9.0.0.0 | 24755427 |
| VMware vSAN File Services | Yes | 9.0.0.0 | 24755229 |
| VMware vSAN OSA Witness | Yes | 9.0.0.0 | 24755428 |
| VMware NSX |  | 9.0.0.0 | 24733065 |
| SDDC Manager |  | 9.0.0.0 | 24703748 |
| VMware Cloud Foundation Operations | Yes | 9.0.0.0 | 24695812 |
| VMware Cloud Foundation Operations orchestrator | Yes | 9.0.0.0 | 24674408 |
| VMware Cloud Foundation Operations collector | Yes | 9.0.0.0 | 24695833 |
| VMware Cloud Foundation Operations fleet management |  | 9.0.0.0 | 24695816 |
| VMware Cloud Foundation Operations for logs | Yes | 9.0.0.0 | 24695810 |
| VMware Cloud Foundation Operations for networks |  | 9.0.0.0 | 24694676 |
| VMware Cloud Foundation Operations HCX |  | 9.0.0.0 | 24699341 |
| VMware Cloud Foundation Automation |  | 9.0.0.0 | 24701403 |
| VMware vSphere Supervisor | Yes | 9.0.0.0 | 24686447 |
| VMware Kubernetes Backup & Recovery Service | Yes | 1.8.0 | 24668882 |
| [VMware vSphere Kubernetes Service](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vsphere-supervisor-services-and-standalone-components/latest/release-notes/vmware-tanzu-kubernetes-grid-service-release-notes.html) | Yes | 3.3.1 |  |
| [VMware Remote Console](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc.html) | Yes | 13.0.0.0 | 24645870 |
| [VMware Tools Async Release](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1300-release-notes.html) | Yes | 13.0.0.0 | 24696475 |
| VMware Cloud Foundation Download Tool | Yes | 9.0.1.0 | 24962179 |
| VMware Cloud Foundation Identity Broker |  | 9.0.0.0 | 24695128 |

\*VMware Cloud Foundation Installer 9.0.1.0 is required to download and deploy all VMware Cloud Foundation 9.0.0.0 and 9.0.1.0 components.

VMware Cloud Foundation add-ons are part of the Bill of Materials but are not part of the VCF SKU.

| **VMware Cloud Foundation Add-on** | **VMware vSphere Foundation Add-on** | Version | **Build Number** |
| --- | --- | --- | --- |
| VMware Private AI |  | 9.0.0.0 | activated with a VCF license |
| VMware Data Services Manager |  | 9.0.0.0 | 24713720 |
| VMware Live Recovery | Yes | 9.0.3 | 24693627 |

**Dependencies:**

- The [Product Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability) provides the upgrade order dependencies.
- VMware vSAN is included in the VMware ESX and VMware vCenter bundles.
- Third-party products from the VCF ecosystem maintain their existing dependencies at the component level. For example, OEM driver add-ons, ESX device drivers, and UI plugins.
- VCF versioning is not applicable to any component with external dependency for the version, such as the Kubernetes version.
- Clusters that don’t have active VMware Supervisor are supported, but do not support key capabilities of VCF, such as VCF Automation workflows.

## Internationalization

**VMware Cloud Foundation 9.0 is available in the following languages:**

- Japanese
- Spanish
- French

Components of VMware Cloud Foundation 9.0 do not accept non-ASCII input.