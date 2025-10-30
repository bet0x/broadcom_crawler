---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/vcenter-9-0-1-0000.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > vCenter
---

# vCenter

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/vcenter-9-0-1-0000.html#GUID-fdb22744-45b5-47f6-923e-2212c50dd62a-en_id-57dd8533-a05f-4532-a108-2eaeabc03b64)
- [What's New](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/vcenter-9-0-1-0000.html#GUID-fdb22744-45b5-47f6-923e-2212c50dd62a-en_id-16621565-5e6d-4ec5-b603-3efaa4298ddc)
- [Patches Contained in This Release](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/vcenter-9-0-1-0000.html#GUID-fdb22744-45b5-47f6-923e-2212c50dd62a-en_id-cb2b3293-4fa5-4537-8ec5-e87efd142c3b)
- [Resolved Issues](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/vcenter-9-0-1-0000.html#GUID-fdb22744-45b5-47f6-923e-2212c50dd62a-en_id-46421645-cda1-4188-bbbb-15566c291529)
- [Known Issues](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/vcenter-9-0-1-0000.html#GUID-fdb22744-45b5-47f6-923e-2212c50dd62a-en_id-55b80f51-d65e-4a4f-89a7-ec1c8839a439)

## Introduction

|  |
| --- |
| VMware vCenter 9.0.1.0 | 29 SEP 2025 | Build 24957454  Check for additions and updates to these release notes. |

## What's New

- This release resolves CVE-2025-41250. For more information on this vulnerability and its impact on Broadcom products, see [VMSA-2025-0016](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36150).
- This release delivers fixes listed in the Resolved Issues section.
- For vSphere Supervisor updates, see the [vSphere Supervisor Release Notes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vsphere-supervisor-services-and-standalone-components/latest/release-notes/vmware-vsphere-supervisor-release-notes.html).
- For Photon OS updates, see [VMware vCenter Appliance Photon OS Security Patches](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/release-notes/vcenter-server-appliance-photonos-security-patches.html).

## Patches Contained in This Release

## VMware vCenter 9.0.1.0

**Build Details**

|  |  |
| --- | --- |
| **Download Filename**: | VMware-vCenter-Server-Appliance-9.0.1.0.24957454-patch-FP.iso |
| **Build**: | 24957454 |
| **Download Size**: | 8626 MB |
| **SHA256 checksum:** | 3e5c7a6c4742e9703a61a486606e90b197f72c4c9c2c94477f73efc4d110aaa0 |
| **PRs fixed** | 3562866, 3511163, 3541135, 3556596, 3523086, 3562282, 3556336, 3533581, 3551915, 3538576, 3550597, 3532416, 3528346, 3550667, 3499756, 3562425, 3561285, 3550637, 3556152, 3554173, 3538272, 3543351, 3545046, 3561397, 3541344, 3550921, 3548023, 3530647, 3529430, 3545026 |
| **CVEs** | CVE-2025-41250 |

## Patch Download and Installation

Log in to the [Broadcom Support Portal](https://support.broadcom.com) to download this patch, depending on your entitlement, [VMware vSphere Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20vSphere%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529542&viewGroup=true) or [VMware Cloud Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529537&viewGroup=true).

For download instructions, see [Download Broadcom products and software](https://knowledge.broadcom.com/external/article?articleId=142814).

See these KBs for details on the authenticated online and offline download: [390121](https://knowledge.broadcom.com/external/article/390121), [390098](https://knowledge.broadcom.com/external/article/390098), and [389276.](https://knowledge.broadcom.com/external/article/389276)

For details on updates and upgrades by using vSphere Lifecycle Manager, see [About vSphere Lifecycle Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new.html) and [vSphere Lifecycle Manager Baselines and Images](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new/vlcm-baselines-and-images.html#GUID-9A20C2DA-F45F-4C9B-9D17-A89BCB62E6EF-en). You can also update ESX hosts without the use of vSphere Lifecycle Manager by using an image profile. To do this, you must manually download the patch offline bundle ZIP file or see the KB [How to download ESXi ISO image for all releases including patch updates.](https://williamlam.com/2023/03/quick-tip-how-to-download-esxi-iso-image-for-all-releases-including-patch-updates.html)

For more information, see [Getting Started with ESXCLI](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-0/getting-started-with-esxcli-8-0/overview-of-esxcli/esxcli-syntax.html) and the [VMware ESX Upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-upgrade/overview-of-the-esxi-host-upgrade-process.html) guide.

## Resolved Issues

VMware vCenter 9.0.1.0 resolves the following issues:

## vCenter and vSphere Client Issues

**Cross-cluster migration of virtual machines might fail if the source cluster is of type vSAN ESA**

Cross-cluster migration for a VM might fail when the source VM on vSAN ESA has a snapshot in native delta format and the destination is either vSAN ESA or vSAN OSA.

**In the vSphere Client, you see a warning "You have expired or expiring version 9+ licenses in your inventory"**

If you activate vSAN with a 9.0 license on a cluster and then deactivate the service for some reason, the cluster remains in the vCenter inventory as an evaluation asset. As a result, in the vSphere Client you see the warning You have expired or expiring version 9+ licenses in your inventory, but when you navigate to Administration > Licensing > Version 9+ Licenses, the vCenter instance appears as fully licensed, with no indication of any issue.

The fix adds a tab Unlicensed Clusters in Version 9+ Licenses to list vSAN clusters in the vCenter inventory that are kept as evaluation assets.

**If the Primary Network Identifier (PNID) of a vCenter instance has uppercase letters, you cannot break the Enhanced Linked Mode (ELM) topology**

If the PNID of a vCenter instance has uppercase letters, attempts to break the ELM topology from this instance, for example by running the command cmsso-util break-elm --mode, fail with the error Previous delete node task is still running.

**Adding Identity Provider users to a local Single Sign-On group fails with the error No principal with specified name exists**

In some cases, when you use the vCenter linking capability under Infrastructure Operations > Configurations in VCF Operations, adding an Identity Provider user to a local Single Sign-On group in a vCenter instance might fail with the error: No principal with specified name exists.

**The vpxd service might fail when invoking the CompatibilityChecker.checkCompatibility() API**

Invoking the CompatibilityChecker.checkCompatibility() API to evaluate the compatibility of a virtual machine connected to an NSX-backed distributed port group against a destination ESX host might cause the vpxd service to fail.

**A faulty health status of a microservice under VMware Identity Services might trigger an unexpected vCenter High Availability failover**

A false negative health status of a microservice under VMware Identity Services that occurs in very specific conditions might trigger an unexpected vCenter High Availability failover.

**Adding a standard key provider to your vCenter system from the vSphere Client fails with Vim.fault.DatabaseError**

When you try to add a key provider that does not use certificates with a rsa-sha2-256 algorithm, in the vSphere Client you see the error Vim.fault.DatabaseError.In the vmafdd.log file, you see an error such as:

<Timestamp> [vmafdd][ERROR] Certificate uses an unsupported signature algorithm (NID=ecdsa-with-SHA256). Only SHA-2 RSA algorithms are supported on the vCenter Server.

**In the Virtual Appliance Management Interface (VAMI), you see "HTTP Cannot connect to proxy server"**

In VAMI, when you configure proxy settings for vCenter to allow communication through a proxy server, the operation fails with an error such as HTTP Cannot connect to proxy server.

**In a rare race condition, the PlaceVM API might cause the vpxd service to fail if the candidate host set is empty**

In rare cases, while the PlaceVM API finds a candidate host for the Placement Spec, the task might race with a parallel task on that host for shutting down or entering maintenance mode. As a result, since PlaceVM API does not handle this corner case correctly, the vpxd service fails and might cause various issues such as failing SDDC manager prechecks.

**In the vSphere Client, you do not see the close button of global notifications with long text**

In the vSphere Client, some global notifications that you see on the header might be so long that you need to significantly resize the screen to find the **X** button to close the banner.

**The index for the Tbilisi - UTC+04:00 time zone shows as a negative value**

When you customize a virtual machine and set the time zone to Tbilisi - UTC+04:00, you see a negative value, such as -2147483577, instead of the index 170 as per the Microsoft Time Zone Index Values.

**With read-only access, you cannot extract an image from an ESX host**

In the vSphere Client, if you have just read-only access on an ESX host, you cannot extract the current image on the host to create a new image in the Image step of the Add Host wizard. If you try to extract a new image and select the Extract the image on the host option, click Next, and accept either the host certificate or thumbprint, you see the error Image not available, and the Extract Image button instead of the expected host image information.

**You see large threadmonitor<num>.log files in the vsphere-ui logs directory**

Due to a configuration issue, the threadmonitor logs might not be properly compressed and can reach up to 10 files, 100MB each.

**In the vSphere Client, you cannot set the datetime format in Browser Default**

When you select a datetime format from My Preferences > Language > Browser Default, for example English (New Zeland) with format DD/MM/yyyy, the datetime format in the vSphere Client continues to display in English (US) with format MM/DD/yyyy.

**vCenter alarms do not disappear after you click Acknowledge or Reset to Green**

In the Summary tab of the vSphere Client, vCenter alarms in the Issues and Alarms panel might not disappear after you click Acknowledge or Reset to Green.

**If a vCenter task to move a file times out, the file might be deleted from both the destination and source datastores as part of the rollback**

When you start a task to move a file from the vSphere Client, the file is copied from the source datastore to the target datastore and then deleted from the source. If the task times out, vCenter rolls back the operation, but in some cases the file in the target datastore might not be restored.

**vCenter upgrade might fail due to undecodable characters in the vCenter certificates**

If the human-readable decoded form of vCenter certificates such as VECS MACHINE\_SSL\_CERT, TRUSTED\_ROOTS, or TRUSTED\_ROOT\_CRLS, contains a string that cannot be decoded with UTF-8, such as "ñ", the first boot of the VMware Authentication Framework Service Daemon (VMAFD) might fail. As a result, you cannot complete an upgrade of your vCenter system.

## Upgrade Issues

**vCenter upgrade to version 9.0 fails with the error "Failed to get sso server certificate for validation"**

When upgrading from vCenter 8.0 Update 3 or later to vCenter 9.0, the upgrade precheck might fail with the error Failed to get sso server certificate for validation. The issue affects only vCenter 9.0.

You can use vCenter 9.0.1 or later to upgrade from from vCenter 8.0 Update 3 or later.

## vSphere Configuration Profile Issues

**Applying a vSphere Configuration Profile to a cluster fails with an error for invalid base64-encoded string**

If your vCenter instance is configured with a long-chain certificate, applying a vSphere Configuration Profile to a cluster might fail with logs such as: Configuration Profile error: Invalid base64-encoded string: number of data characters (5177) cannot be 1 more than a multiple of 4.

## Auto Deploy Issues

**Auto Deploy works inconsistently on large vCenter systems**

Due to a limit on the number of Auto Deploy HTTP connections and configured internal HTTP connections in large vCenter systems, the service might fail to respond to requests in a timely manner, resulting in slow operations or failure to deploy ESX hosts.

**Booting an UEFI-enabled stateless host might fail with Fatal error: 15 (Not found)**

Due to a discrepancy in the iPXE versions, booting an UEFI-enabled stateless host might fail with Fatal error: 15 (Not found).

**ESX hosts that boot from Auto Deploy might fail to join vCenter due to a failure of the DNS lookup**

Since Auto Deploy processes IPs for a DNS lookup sequentially, in some cases resolving IPs of VMkernel ports that are not used for management traffic might lead to a failure of the DNS lookup.

## High Availability Issues

**vCenter High Availability might intermittently fail over due to a very rare time format issue**

Due to a very rare case when the datetime format of the vCenter High Availability health status XML file contains a null value for microseconds, vCenter High Availability might intermittently fail over.

## Miscellaneous Issues

**The log partition of the vCenter appliance quickly fills up due to unhandled or orphaned log files**

Unhandled or orphaned log files, such as RPM installation backup files, stale formatted log files, and specific workflow-related log files, are often filling up the log partition of the vCenter appliance.

The fix provides a report for unhandled or orphaned log files and moves some stale log files to a temporary location for 7 days before deletion, so you can review and restore if necessary.

**After setting syslog forwarding storage, the log disk shows as full**

When you configure an external syslog server, the rsyslog service might fail to release the file descriptors of the rotated files. As a result, when you run the df command, you might see disk usage at up to 100%.

**Subscribing to an external Content Library fails with an error that the proxy cannot resolve the library host name**

When trying to subscribe to an external Content Library through a proxy, in the vSphere Client you might see the error Unable to resolve the remote library host name: wp-content.broadcom.com.

**Licensing info in a custom sysprep answer file for Windows might be in plain text**

When you use the VM Customization Specifications workflow to create a custom sysprep answer file for Windows, if the file contains licensing info, such as a key, the key might display in plain text in the file.

## vSphere Lifecycle Manager Issues

**vSphere Lifecycle Manager service might restart or stop during the pre-upgrade check for ESX standalone hosts**

During the pre-upgrade check for an ESX standalone host, either by using API or the vSphere Client, if the Hardware Support Manager reports FAILED status, the vSphere Lifecycle Manager service restarts or stops requiring a manual start of the service.

**When you add VIBs from an OEM partner to a vSphere Lifecycle Manager image that you use with vSphere Configuration Profile (VCP) to manage a cluster, image validation might fail**

Under certain conditions, the validation of a vSphere Lifecycle Manager image that you use to manage a heterogeneous cluster with VCP might fail if you add VIBs from an OEM partner.

## Storage Issues

**Hot extension of vSphere Virtual Volumes disk can fail due to a datastore accessibility check**

During a hot-extend operation on a vSphere Virtual Volumes disk, the datastore accessibility check might fail even if another ESX host on the datastore, not the one where the VM is located, is inaccessible. As a result, you see the error The operation is not supported on the object. The operation can not be performed because datastore is inaccessible.

In the vpxd logs, you see an error such as:

2025-05-06T15:36:31.731Z warning vpxd[07478] [Originator@6876 sub=provisioning opID=mabmwx1q-73097-auto-1kej-h5:70002251-2a] Datastore is not accessible from host

The fix makes sure the check includes only datastore accessibility on the VM-specific hosts where VM sharing the disk are located.

## Guest OS Issues

**You cannot customize a Linux virtual machine with installed SUSE Linux Enterprise Server 16 (SLES 16)**

Guest OS customization for SLES 16 VMs is not supported and customization tasks fail.

The fix adds guest customization support to SLES 16.

**Guest OS customization might fail on Ubuntu cloud image virtual machines**

When you deploy a virtual machine from an Ubuntu cloud image and try to customize the VM, the customization task might fail with an error that the VM network adapter is in disconnected state. In the /var/log/vmware-imc/toolsDeployPkg.log, you see that the task stops at Command: '/usr/sbin/netplan apply 2>&1'.

**Network configuration on virtual machines with Red Hat Enterprise Linux 8 (RHEL 8) and earlier might remain unchanged after the guest customization**

For VMs with RHEL 8 and earlier, the guest customization engine might only clean configuration files at /etc/sysconfig/network-scripts/ifcfg-eth\* and leave files that do not have the prefix ifcfg-eth. As a result, such files might continue to take effect, leading to inconsistent results in network connectivity for the VM.

## Known Issues

## vCenter and vSphere Client Issues

**Under the Available updates tab in the Virtual Appliance Management Interface (VAMI), values in the Type column might not display correctly**

When you click on Available updates in the VAMI, if the update is of type Bug Fix and Security, in the Type column you see vami.manage.update.type.Bug Fix and Security instead of Bug Fix and Security.

Workaround: None. This is a cosmetic issue.

## vSphere Lifecycle Manager Issues

**Creating a vSphere Lifecycle Manager image might fail even when the corresponding depots are imported**

In rare cases, when multiple offline and online depots are imported into the vSphere Lifecycle Manager, the metadata of one depot might overwrite the metadata of a previously imported depot and effectively remove the older depot. As a result, when you try to create a desired image based on the deleted depot, during draft validation, the task fails. In the logs, you see an error that depends on the depot that is missing, for example: Software Solution com.vmware.vsphere-wcp with version 9.0.1.31.6.0-24913416 cannot be found in depot. This issue is more likely to occur in VCF environments where the depots imported in the vSphere Lifecycle Manager come from multiple sources.

Workaround: See KB [412074](https://knowledge.broadcom.com/external/article/412074).