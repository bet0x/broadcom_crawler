---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc/vmware-remote-console-130-release-notes.html
product: vmware-remote-console
version: 13.0
section: Release Notes
breadcrumb: Release Notes > VMware Remote Console 13.0 Release Notes
---

# VMware Remote Console 13.0 Release Notes

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc/vmware-remote-console-130-release-notes.html#GUID-4ff70e3e-e102-43bf-9653-0a82fa05f68b-en_id-b1eb1b78-8194-4121-b185-e318cf1fdceb)
- [About VMware Remote Console](/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/release-notes_vmrc/vmware-remote-console-130-release-notes.html#GUID-4ff70e3e-e102-43bf-9653-0a82fa05f68b-en_id-3ee6cfae-6655-46ab-82b3-1c18eaf9407e)

## Introduction

|  |
| --- |
| - VMware Remote Console 13.0 | 17 June 2025 | Build 24645870 | Mac App Store Build 24645974 - For VMware Cloud Foundation (VCF) and vSphere | Last document update 14 May 2025 - Check back for additions and updates to these release notes, marked **New**. |

## About VMware Remote Console

VMware Remote Console (VMRC) is a personal computer application that connects over a network to virtual machines running on vSphere. The accompanying manual describes how to install VMRC, use it to access VMware virtual machines, and perform operations on them.

As of version 11, VMRC requires direct access to port 443 on ESXi hosts. For more information, see Broadcom KB 316564. Compatibility with vCloud Director and VCF Automation may be limited.

## What's New

VMRC 13.0 offers a number of bug fixes, as detailed below.

VMRC 13 release does not have the **Check for Updates** option; users must download and install updates manually from the Broadcom Support Portal.

## System Compatibility

You can install VMRC on the following systems:

- Windows 11
- Windows Server 2022 and 2025
- Linux machines running kernel version up to 6.11
- MacOS 14 and above, with VMRC from the Apple store.

VMRC and VMware Workstation cannot be installed on the same computer, because they share common components. The same is true of VMRC and VMware Fusion.

## Recently Resolved Issues

The VMRC 13 release resolves the following issues.

- **After vMotion of a VM, VMRC sometimes caused a host crash.**

  In certain (no-queue) cases, VMRC called Acquire Ticket too frequently when attempting to reconnect with the VM in its new location. This was fixed both on ESX hosts and in VMRC itself.
- **Too many resources used with multiple VMRC sessions.**

  A customer reported high memory use and too many HTTP connections when many instances of VMRC were connected to the same host. This was a regression in VMRC 11, caused by calling Property Collector filters unnecessarily. Such calls are now made only when needed.
- **VMRC can crash immediately after connecting to a VM.**

  After an upgrade to vSphere 8.0 U3b, VMRC failed immediately after connecting to a VM. The cause was that vSphere failed to report vim.TaskInfo.reason during connection. In this release, VMRC ignores the missing value and continues.
- **The Japanese locale showed an English user interface.**

  When the locale was set to Japanese, the VMRC 12.0.5 user interface displayed in English. The workaround was to delete duplicate entries in the vmware.vmsg message translations. This issue is fixed in this release.
- **VMRC could fail when accepting a security certificate.**

  When a Linux X11 server was set to 32-bit color depth instead of 24-bit, VMRC would exit after asking the user to accept a security certificate. The workaround was to run X11 in 24-bit mode, but 32-bit support is improved in this release.

## Known Issues and Workarounds

These issues were also found in the previous VMRC 12 release.

- **Some device operations are not supported on MacOS.**

  When you access virtual machines using the VMRC MacOS client, you cannot perform certain device operations. For example, you cannot add new devices or display sound card settings.
- **VMRC for MacOS slow with passthrough on mass storage devices.**

  When a mass storage device is mounted and passes through a remote virtual machine, the MacOS VMRC client may freeze for several seconds. The workaround is to manually unmount the mass storage device from the host operating system before initiating passthrough in VMRC.