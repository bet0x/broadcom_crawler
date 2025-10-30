---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc/vmware-remote-console-1301-release-notes.html
product: vmware-remote-console
version: 13.0
section: Release Notes
breadcrumb: Release Notes > VMware Remote Console 13.0.1 Release Notes
---

# VMware Remote Console 13.0.1 Release Notes

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc/vmware-remote-console-1301-release-notes.html#GUID-75dcb1bd-64be-49b8-be2d-4c26de533f45-en_id-883462a6-dff4-41bc-adf1-60ed846458d0)
- [About VMware Remote Console](/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc/vmware-remote-console-1301-release-notes.html#GUID-75dcb1bd-64be-49b8-be2d-4c26de533f45-en_id-ac4cf92e-9e2c-44f8-82e4-870475e04405)

## Introduction

|  |
| --- |
| - VMware Remote Console 13.0.1 | 29 Sept 2025 | Build 24954779 | Mac App Store Build 24958001 - For VMware Cloud Foundation (VCF) and vSphere 9.0.1| Last document update 29 Sept 2025 - Check back for additions and updates to these release notes, marked **New**. |

## About VMware Remote Console

VMware Remote Console (VMRC) is a personal computer application that connects over a network to virtual machines running on vSphere. The accompanying manual describes how to install VMRC, use it to access VMware virtual machines, and perform operations on them.

As of version 11, VMRC requires direct access to port 443 on ESXi hosts. For more information, see Broadcom KB [316564](https://knowledge.broadcom.com/external/article/316564/vmware-remote-console-11x-connection-er.html). Compatibility with vCloud Director and VCF Automation may be limited.

## What's New

VMRC 13.0.1 offers a number of bug fixes, as detailed below.

## System Compatibility

You can install VMRC on the following systems:

- Windows 11
- Windows Server 2022 and 2025
- Linux machines running kernel version up to 6.14
- MacOS 15 and above, with VMRC from the Apple store.

VMRC and VMware Workstation cannot be installed on the same computer, because they share common components. The same is true of VMRC and VMware Fusion.

## Recently Resolved Issues

The VMRC 13.0.1 release resolves the following issues.

- **Performed a security audit and upgraded some components.**

  In response to CVE reported security issues, the following open source components were upgraded: Freetype from 2.12 to 2.13.1, libxml2 from 2.13.3 to 2.14.3, sqlite from 3.47.0 to 3.50.2, openssl from 3.0.15 to 3.0.17, Python from 3.10.16 to 3.10.18, and libX11 from 1.7.1 to 1.8.10.

## Known Issues and Workarounds

These issues were reported against the VMRC 13.0 release.

- **Check for updates option.**

  The VMRC 13 release did not have the **Check for Updates** option, and neither does 13.0.1. Users must download and install updates manually from the Broadcom Support Portal or Apple store.
- **Power operations missing for VM launched using PowerCLI.**

  When a remote virtual machine is launched from a PowerCLI URL, the power options are grayed out in the main menu. There is no known workaround.
- **VM name not displayed on the console if launched from VCF Automation.**

  When a remote virtual machine is launched from the VCF Automation portal, the VM name does not appear on the heading bar of the VMRC application. There is no workaround at this time.

These issues were also found in the previous VMRC 12 release.

- **Some device operations are not supported on MacOS.**

  When you access virtual machines using the MacOS client, you cannot add new devices or display sound card settings.
- **VMRC for MacOS with passthrough on mass storage devices.**

  When a mass storage device is mounted and passes through a remote virtual machine, the MacOS client may freeze for several seconds. A workaround is to manually unmount the mass storage device on the host operating system before initiating passthrough.