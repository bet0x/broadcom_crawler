---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/esx/esx-9-0-0-0100.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > VMware ESX 9.0.0.0100 Release Notes
---

# VMware ESX 9.0.0.0100 Release Notes

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/esx/esx-9-0-0-0100.html#GUID-a51d69f7-3e77-44b1-98da-8581b5d3e605-en_id-ff7d428e-764e-4767-a4dd-d2aa78a55cb8)
- [What's New](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/esx/esx-9-0-0-0100.html#GUID-a51d69f7-3e77-44b1-98da-8581b5d3e605-en_id-0a6834d4-7e07-4550-aa83-88a19b1cfdc9)
- [Patches Contained in This Release](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/esx/esx-9-0-0-0100.html#GUID-a51d69f7-3e77-44b1-98da-8581b5d3e605-en_id-7f7cd6c0-827f-4b6b-8072-7b246d9d9d58)
- [Resolved Issues](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/esx/esx-9-0-0-0100.html#GUID-a51d69f7-3e77-44b1-98da-8581b5d3e605-en_id-f6487e02-7c50-4c85-b68a-107c418362da)

## Introduction

|  |
| --- |
| VMware ESX 9.0.0.0100 | 15 JUL 2025 | Build 24813472  Check for additions and updates to these release notes. |

## What's New

This [live-patchable](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/configuring-vlcm-remediation-settings-1/how-to-apply-live-patches-to-the-hosts-in-a-cluster-managed-with-images.html) release resolves CVE-2025-41237. For more information on this vulnerability and its impact on Broadcom products, see [VMSA-2025-0013](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877).

## Patches Contained in This Release

## VMware ESX 9.0.0.0100

**Build Details**

**VMware vSphere Hypervisor (ESX) Offline Bundle**

|  |  |
| --- | --- |
| **Download Filename**: | VMware-ESXi-9.0.0.0100.24813472-depot.zip |
| **Build**: | 24813472 |
| **Download Size**: | 657.7 MB |
| **SHA256 checksum:** | b9732fbb436634ba5247a97114cdf7a1e96254dff2cb904ab4da9d392351ba50 |
| **Live Patchable** | Yes |
| **Host Reboot Required**: | No |
| **Virtual Machine Migration or Shutdown Required**: | No |

**ESX Images**

| Name and Version | Release Date | Category | Live Patchable | Detail |
| --- | --- | --- | --- | --- |
| ESXi-9.0.0.0100-24813472 | 15 JUL 2025 | Security | Yes | Security only image |

**Image Profiles**

VMware patch and update releases contain general and critical image profiles. Application of the general release image profile applies to new bug fixes.

|  |
| --- |
| **Image Profile Name** |
| ESXi-9.0.0.0100-24813472-standard |
| ESXi-9.0.0.0100-24813472-no-tools |

## Patch Download and Installation

Log in to the [Broadcom Support Portal](https://support.broadcom.com) to download this patch, depending on your entitlement, [VMware vSphere Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20vSphere%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529542&viewGroup=true) or [VMware Cloud Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529537&viewGroup=true).

For download instructions, see [Download Broadcom products and software](https://knowledge.broadcom.com/external/article?articleId=142814).

See these KBs for details on the authenticated online and offline download: [390121](https://knowledge.broadcom.com/external/article/390121), [390098](https://knowledge.broadcom.com/external/article/390098), and [389276.](https://knowledge.broadcom.com/external/article/389276)

For details on updates and upgrades by using vSphere Lifecycle Manager, see [About vSphere Lifecycle Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new.html) and [vSphere Lifecycle Manager Baselines and Images](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new/vlcm-baselines-and-images.html#GUID-9A20C2DA-F45F-4C9B-9D17-A89BCB62E6EF-en). You can also update ESX hosts without the use of vSphere Lifecycle Manager by using an image profile. To do this, you must manually download the patch offline bundle ZIP file or see the KB [How to download ESXi ISO image for all releases including patch updates.](https://williamlam.com/2023/03/quick-tip-how-to-download-esxi-iso-image-for-all-releases-including-patch-updates.html)

For more information, see [Getting Started with ESXCLI](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-0/getting-started-with-esxcli-8-0/overview-of-esxcli/esxcli-syntax.html) and the [VMware ESX Upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-upgrade/overview-of-the-esxi-host-upgrade-process.html) guide.

## Resolved Issues

## ESXi 9.0.0.0100 - 24813472

|  |  |
| --- | --- |
| **Name** | ESX |
| **Version** | ESXi 9.0.0.0100 - 24813472 |
| **Release Date** | July 15, 2025 |
| **Category** | Security |
| **Live Patchable** | Yes |
| **Affected Components** | - ESXi Component - core ESXi VIBs |
| **PRs Fixed** | N/A |
| **Related CVE numbers** | CVE-2025-41237 |

This release resolves CVE-2025-41237. For more information on this vulnerability and its impact on Broadcom products, see [VMSA-2025-0013](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877).

## ESXi-9.0.0.0100-24813472-standard

|  |  |
| --- | --- |
| **Profile Name** | ESXi-9.0.0.0100-24813472-standard |
| **Build** | For build information, see Patches Contained in This Release. |
| **Vendor** | Broadcom, Inc. |
| **Release Date** | July 15, 2025 |
| **Acceptance Level** | Partner Supported |
| **Affected Hardware** | N/A |
| **Affected Software** | N/A |
| **Affected VIBs** | - VMware\_bootbank\_esx-base\_9.0.0-0100.24813472 - VMware\_bootbank\_esxio-base\_9.0.0-0100.24813472 |
| **PRs Fixed** | N/A |
| **Related CVE numbers** | CVE-2025-41237 |

**This patch updates the following issue:**

This release resolves CVE-2025-41237. For more information on this vulnerability and its impact on Broadcom products, see [VMSA-2025-0013](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877).

## ESXi-9.0.0.0100-24813472-no-tools

|  |  |
| --- | --- |
| **Profile Name** | ESXi-9.0.0.0100-24813472-no-tools |
| **Build** | For build information, see Patches Contained in This Release. |
| **Vendor** | Broadcom, Inc. |
| **Release Date** | July 15, 2025 |
| **Acceptance Level** | Partner Supported |
| **Affected Hardware** | N/A |
| **Affected Software** | N/A |
| **Affected VIBs** | - VMware\_bootbank\_esx-base\_9.0.0-0100.24813472 - VMware\_bootbank\_esxio-base\_9.0.0-0100.24813472 |
| **PRs Fixed** | N/A |
| **Related CVE numbers** | CVE-2025-41237 |

**This patch updates the following issue:**

This release resolves CVE-2025-41237. For more information on this vulnerability and its impact on Broadcom products, see [VMSA-2025-0013](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877).