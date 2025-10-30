---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/esx-9-0-1-0000.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > ESX
---

# ESX

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/esx-9-0-1-0000.html#GUID-2ede6222-329b-4b86-b77d-ea899710a8d0-en_id-7c76b693-3f55-4503-9551-15c0833e548d)
- [What's New](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/esx-9-0-1-0000.html#GUID-2ede6222-329b-4b86-b77d-ea899710a8d0-en_id-a745a5db-ab3a-4585-a813-c4d969149d92)
- [Patches Contained in This Release](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/esx-9-0-1-0000.html#GUID-2ede6222-329b-4b86-b77d-ea899710a8d0-en_id-38dcec5d-a1f1-4b8d-af2c-bb2a6b82526f)
- [Resolved Issues](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-9-0-1-release-notes/esx-9-0-1-0000.html#GUID-2ede6222-329b-4b86-b77d-ea899710a8d0-en_id-8282f1a1-ac77-4a1a-a57c-4beb7f179d72)

## Introduction

|  |
| --- |
| VMware ESX 9.0.1.0 | 29 SEP 2025 | Build 24957456  Check for additions and updates to these release notes. |

## What's New

- In the Resolved Issues section, see the fixes and updates that VMware ESX 9.0.1.0 provides.

## Patches Contained in This Release

## VMware ESX 9.0.1.0

**Build Details**

**VMware vSphere Hypervisor (ESX) Offline Bundle**

|  |  |
| --- | --- |
| **Download Filename**: | VMware-ESXi-9.0.1.0.24957456-depot.zip |
| **Build**: | 24957456 |
| **Download Size**: | 644.4 MB |
| **SHA256 checksum:** | fe84c9ebcff676b7eae2b0fc77561cbee0cce00c7e8a524708b81c8cfe06c1c4 |
| **Live Patchable:** | No |
| **Host Reboot Required**: | Yes |
| **Virtual Machine Migration or Shutdown Required**: | Yes |

**ESX Images**

| Name and Version | Release Date | Live Patchable: | Category | Detail |
| --- | --- | --- | --- | --- |
| ESXi\_9.0.1-0.24957456 | 29 SEP 2025 | No | Bugfix | Bugfix image |

**Image Profiles**

VMware patch and update releases contain general and critical image profiles. Application of the general release image profile applies to new bug fixes.

|  |
| --- |
| **Image Profile Name** |
| ESXi-9.0.1-0.24957456-standard |
| ESXi-9.0.1-0.24957456-no-tools |

## Patch Download and Installation

Log in to the [Broadcom Support Portal](https://support.broadcom.com) to download this patch, depending on your entitlement, [VMware vSphere Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20vSphere%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529542&viewGroup=true) or [VMware Cloud Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529537&viewGroup=true).

For download instructions, see [Download Broadcom products and software](https://knowledge.broadcom.com/external/article?articleId=142814).

See these KBs for details on the authenticated online and offline download: [390121](https://knowledge.broadcom.com/external/article/390121), [390098](https://knowledge.broadcom.com/external/article/390098), and [389276.](https://knowledge.broadcom.com/external/article/389276)

For details on updates and upgrades by using vSphere Lifecycle Manager, see [About vSphere Lifecycle Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new.html) and [vSphere Lifecycle Manager Baselines and Images](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new/vlcm-baselines-and-images.html#GUID-9A20C2DA-F45F-4C9B-9D17-A89BCB62E6EF-en). You can also update ESX hosts without the use of vSphere Lifecycle Manager by using an image profile. To do this, you must manually download the patch offline bundle ZIP file or see the KB [How to download ESXi ISO image for all releases including patch updates.](https://williamlam.com/2023/03/quick-tip-how-to-download-esxi-iso-image-for-all-releases-including-patch-updates.html)

For more information, see [Getting Started with ESXCLI](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-0/getting-started-with-esxcli-8-0/overview-of-esxcli/esxcli-syntax.html) and the [VMware ESX Upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-upgrade/overview-of-the-esxi-host-upgrade-process.html) guide.

## Resolved Issues

## ESXi\_9.0.1-0.24957456

|  |  |
| --- | --- |
| **Name** | ESX |
| **Version** | ESXi\_9.0.1-0.24957456 |
| **Release Date** | September 25, 2025 |
| **Live Patchable:** | No |
| **Category** | Bugfix |
| **Affected Components** | - ESXi Component - core ESXi VIBs - ESXi Install/Upgrade Component - VMware Host Client - Host Based Replication Server for ESX - VMware NVMe over TCP Driver - ESXi Tools Component - USB Native Driver for VMware - High Availability services for vSphere virtual machines on an ESXi host - Broadcom Emulex Connectivity Division FC and FCoE Driver - Intel NVME Driver with VMD Technology - NSX LCP Bundle |
| **PRs Fixed** | 3552243, 3538289, 3521243, 3552640, 3537103, 3547622, 3554274, 3538565, 3553087, 3547591, 3558914, 3520826, 3557349, 3559990, 3557364, 3557453, 3502821, 3552794, 3553367, 3552236, 3549613, 3544223, 3552992, 3552977, 3551935, 3553014, 3542824, 3553017, 3543517, 3542176, 3543172, 3537096, 3523290, 3525849, 3541218, 3538647, 3541101, 3540259, 3538662, 3536517, 3536512, 3535775, 3534015, 3528521, 3528518, 3528419, 3524827, 3522713, 3520895, 3518918, 3506964, 3501927, 3492318 |
| **Related CVE numbers** | N/A |

**VMware ESX 9.0.1.0 provides the following resolved issues and updates:**

**A routing issue with the Cisco Application Centric Infrastructure (ACI) switch might cause loss of vSAN traffic**

To override normal IP routing, vSAN binds all outgoing traffic on TCP sockets and traffic runs over a VMkernel adapter dedicated to vSAN. In some cases, the vSAN binding might not be set or a TCP socket might be missing, so packets are sent with the normal IP routing. In such cases, Cisco ACI devices might change the routing table based on the incoming packets, which in turn causes traffic loss on the vSAN cluster.

**A virtual machine might fail to power on if the .vmx file is changed in the backend**

In certain scenarios, when a VM is restored from a backup, applications external to the ESXi host might delete and recreate the .vmx file while the ESXi nfs41client is still accessing the file handle of the old .vmx file. As a result, a stale handle error causes the power-on of the VM to fail.

**An ESX host might fail with a purple diagnostic screen with LVMHandleDeviceAPDEvent during All Paths Down (APD) state for a device or LUN**

While a VMFS volume is closing, an APD event handler for the volume might be unregistered and relevant data structures might be freed. During this period, if the device or LUN that hosts the VMFS volume enters APD, a race condition can cause access to the freed data structure, eventually causing the ESX host to fail with a purple diagnostic screen with LVMHandleDeviceAPDEvent in the stack.

**The service on ports 2379 and 2380 does not support TLS 1.3 by default**

FIPS compliance issues with the Golang runtime prevented the service on ports 2379 and 3280 to support TLS 1.3 by default until ESX 9.0.1.0.

The service using ports 2379 and 2380 activates the TLS 1.3 protocol based on the TLS profile setting of ESX hosts.

**In the vSphere Client, ESX hardware health metrics do not refresh automatically**

If a hardware sensor information changes or a fault occurs, the ESX hardware health metrics in the vSphere Client do not reflect the changes automatically and you need to refresh them manually. This issue does not impact alarms and events.

**You cannot use public/private key pair to connect with SSH by using HTTP PUT**

You cannot use authorized public/private keys to connect to ESX hosts with SSH by using ConfigManager APIs (HTTP PUT).

**An ESX host might shut down due to Machine-Check Exception (MCE) on the virtual machine memory**

When an uncorrectable error occurs on the guest OS memory of an ESX host, the underlying hardware might trigger a MCE. If the local machine check exception (LMCE) is not enabled either by the firmware or at the ESX host, the host might shut down, which might cause downtime for applications hosted on the host VMs.

**Virtual machines cannot boot when configured with a PCI passthrough device**

VMs configured with a PCI passthrough device might consistently fail to boot, removing the device from its configuration and from the PCI device list of the ESX host.

**Changing the VM storage policy on a powered-off encrypted virtual machine causes the hostd service to fail**

When you modify the storage policy of a powered-off encrypted virtual machine, if the new policy also specifies VM encryption, the hostd service might fail.

**An ESX host might fail to enter maintenance mode or vSphere vMotion tasks might fail on a cluster with active memory tiering**

Due to conservative memory allocation by the memory tiering feature, an ESX host might fail to enter maintenance mode or vSphere vMotion tasks might fail on a cluster with active memory tiering with an error in the vmkernel.log such as:

2025-06-02T12:32:53.841Z Wa(180) vmkwarning: cpu57:3249843)WARNING: VMotionRecv: 3902: 922189911786969974 D: World 3249843 waited 15.783 seconds to leave low memory state on dest host during pre-copy. May cause unexpected VMotion failures!

**An ESX host fails with purple diagnostic screen due to overload with task management commands**

When a device receives too many task management commands to handle concurrent I/Os, some of the commands might take long to complete. As a result, the ESX host might fail with a purple diagnostic screen.

**ESX stops producing events based on VMkernel Observations (VOBs)**

In some cases, ESX might stop producing events based on VOBs, which causes missed alarms in vCenter. As a result, in the vSphere Client you do not see alarms for problems detected by the VMkernel .

**Rare memory preallocation issue might cause an ESX host to fail with a purple diagnostic screen**

For some types of VMs, such as PCIe passthrough VMs, ESX tries to preallocate memory while the VM powers on. If the VM is terminated by vSphere High Availability during the memory preallocation, the ESX host might fail with a purple diagnostic screen.

**vSphere Quick Boot support:**

ESX 9.0.1 adds vSphere Quick Boot support for the passthrough driver for Intel Gaudi 3 AI Accelerators. For more information, see KB [406262](https://knowledge.broadcom.com/external/article/406262/passthrough-driver-for-intel-gaudi-ai-ac.html). For the full list of supported servers and drivers, see the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).

**Failed quiesced snapshot of virtual machines might corrupt disk chains to vSphere Virtual Volume or vSAN disks**

If taking a quiesced snapshot of a VM with vSphere Virtual Volume or vSAN disks fails, some or all of the disk chains might be corrupted. The VM can no longer be managed properly, and data loss might occur, forcing a recovery from backup.

**Replicated virtual machines might become unresponsive during incremental sync**

The I/O capture component of vSphere Replication might not properly handle the UNMAP commands issued by the Guest OS during an incremental sync, which causes some VMs to become unresponsive.

**If the remote boot disk is in All Paths Down (APD) or Permanent Device Loss (PDL) state, the ESX host fails with a purple diagnostics screen**

In VCF 9.0, remote boot disk monitoring is active by default and if the remote boot disk experiences an APD or PDL state, the ESX host might fail with a purple diagnostics screen.

Remote boot disk monitoring is not active by default.

**VMware Tools Bundling Changes in ESX 9.0.1.0**

The following VMware Tools ISO images are bundled with ESX 9.0.1.0:

- **windows.iso**: VMware Tools 13.0.5 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.

The following VMware Tools ISO images are available for download:

- VMware Tools 12.5.4:

  - **windows.iso:** VMware Tools 12.5.4 supports 64-bit Windows versions.
  - **windows-x86.iso:** VMware Tools 12.4.9 supports 32-bit Windows versions.
  - **linux.iso**: VMware Tools 10.3.26 ISO image for Linux OS with glibc 2.11 or later.

- VMware Tools 11.0.6:

  - **windows.iso**: for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).

- VMware Tools 10.0.12:

  - **winPreVista.iso**: for Windows 2000, Windows XP, and Windows 2003.
  - **linuxPreGLibc25.iso**: supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with **glibc** version earlier than 2.5.
- **solaris.iso**: VMware Tools image 10.3.10 for Solaris.
- **darwin.iso**: Supports Mac OS X versions 10.11 and later.

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESX:

- [VMware Tools 13.0.5 Release Notes](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1305-release-notes.html)
- [VMware Tools for hosts provisioned with Auto Deploy](https://kb.vmware.com/s/article/2004018)
- [Upgrading VMware Tools](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/vmware-tools-administration/upgrading-vmware-tools.html)

**In the hostd log, you see multiple messages that the VMX scoreboard is not readable**

After creating a VM from a clone or template, the vmxstats.filename might duplicate the name of the parent VM and the host stats registry cannot read and log the stats of the new VM. As a result, in the hostd logs you see multiple messages such as Adding VM XXX failed, file /vmfs/volumes/YYY/ZZZ/ZZZ.scoreboard is not readable. This error does not affect the functionality of the new VMs in any way.

**Virtual machine migration and Dell Power Protect Data Manager (PPDM) backups might fail after a Dell Transport Snapshot Data Mover (TSDM) panic**

A panic event at Dell TSDM during a PPDM-based snapshot synchronization can stop the task in the data protection daemon due to a miscalculation error. The stopped synchronization subsequently affects PPDM backup operations on the VM and results in failure of vSphere vMotion tasks.

**ESX host might leak memory during NVMe unmap operations**

If an identify namespace call to a NVMe target fails during a NVMe unmap operation, the memory allocated for the unmap command might not be freed. As a result, you might see higher memory usage in that ESX host until you reboot it to reclaim the memory.

**NVMe over Fibre Channel (NVMe/FC) devices are not recovered after a link reset**

In extremely rare cases, due to a deadlock while discovering and connecting NVMe/FC devices in parallel, an ESX host might not be able to reconnect to all NVMe/FC devices after a link reset and performance of connected devices might also degrade.

**An ESX host might fail with a purple diagnostic screen during migration of virtual machines from a Tintri NFSv4.1 datastore**

During the migration of VMs by using vSphere vMotion from a Tintri NFSv4.1 datastore, the ESX host might fail with a purple diagnostic screen. This issue is specific to how Tintri NFSv4.1 servers handle NULL values in certain scenarios.

**You see a regression of linked clone performance due to slower VM creation**

Additional I/O tasks during VM creation might cause a noticeable regression in the latency and affect the creation of linked clones.

**A vmxnet3 virtual NIC might stop transmitting data after a reconfiguration**

A rare race between vmxnet3 vNIC reconfiguration and tx path due to heavy traffic might cause the vNIC to stop transmitting data after the reconfiguration.

**IF-MIB SNMP data intermittently reports hidden ports DVFilter Coalesce Portset and pps**

When using third-party tools, the IF-MIB SNMP data might intermittently report hidden portsets, such as pps and DVFilter Coalesce Portset, even when they are not part of the ESX host configuration.

**After a reboot of ESX hosts, you see alarms in the vSphere Client that some uplinks are down**

Due to some limitations in the VMkernel Observation (VOB) and hostd services, uplink up and down events might not be sent to vCenter in the correct order. As a result, when a task such as rebooting ESX hosts completes, in the vSphere Client you see false alerts that some uplinks are down.

**After running the Linux fstrim command on a virtual machine, the ESX host fails with a purple diagnostics screen**

A VMFS heap memory exhaustion might cause memory access violations when clearing the pointer block cache. As a result, when you run the Linux fstrim command on a virtual machine, the ESX host might fail with a purple diagnostics screen with a PB3Manager error in the backtrace.

**During a snapshot operation of a VM with IOFilter attached, the VMX might fail due to an unresponsive thread**

In very rare situations, once in 2000 snapshot operations, a race condition might occur in the I/O filter infrastructure and cause the I/O filter watchdog to stop the VMX service, and generate a VMX core dump.

**In Multi-Initiator Zoning Model setup, ESX hosts might fail with a purple diagnostics screen due to flapping initiator FC HBA port state**

In the Multi-Initiator Zoning Model, when multiple FC HBA ports in a cluster are configured in the same FC zone, if one initiator port state is flapping, then all other initiators in the zone receive frequent Registered State Change Notifications (RSCN). An issue in the lpfc driver when processing such frequent RSCNs related to another initiator might cause the ESX host to fail with a purple diagnostics screen with an error such as:

@BlueScreen: #PF Exception 14 in world XXXXXXX:lpfc\_do\_work IP 0xXXXXXXXXXXXX addr 0xXXXXXXXXXXXX.

You see the functions lpfc\_sli4\_els\_xri\_aborted or lpfc\_sli4\_delete\_els\_xri\_aborted in the stack.

**Adding new disks external to the home directory of a virtual machine might fail with an error for reaching the security policy limit**

When a disk external to the home directory of a VM is added or removed, the security domain policy of the VM updates to give or revoke access to the external directory. It is possible that if an error occurs during disk load, to avoid issues if it is resolved, external directories are no longer removed from the security policy, even after a resolution. In time, the rules in the security policy might reach the max limit. As a result, adding new disks external to the home directory of a virtual machine fails and in the sandboxd.log you see errors such as:

2025-05-11T08:14:55.306Z Er(163) sandboxd[2099161]: [Originator@6876 sub=SecurityDomainsImpl] AddUpdateFileRules: Failed to add file policies to domain :X: world ID :Y:Argument list too long

The fix makes sure that once a disk load issue is resolved, external directories are removed from the security policy. If a VM is already facing the issue, either restart the VM or migrate it to another ESX host to trigger a regeneration of the security policy.

**Activation of TLS 1.3 in ClusterStore does not persist across ESX host reboots**

The agent\_settings configuration on ESX that controls whether TLS 1.3 is active on ClusterStore, which keeps the cluster-specific configuration data, reverts to the default of not active after a reboot of the ESX host.

**A slow SCSI device scan might make a thread of the lpfc driver unresponsive and cause various issues**

A slow SCSI device scan might make unresponsive a thread of the lpfc driver, which is responsible for storage target discovery, mailbox operations, and completion of Extended Link Service (ELS) requests. Such an unresponsive thread can lead to failing ELS requests interrupting the discovery of storage targets, no response from applications and mailbox timeouts causing esxcli elxmgmt commands to fail.

The fix improves the lpfc worker thread and prevents effects from slow SCSI device scan on the lpfc threads.

**The authentication service of the Distributed Key Value Store, or ClusterStore, might cause DNS traffic overload**

An issue with the authentication service of the Distributed Key Value Store, also called ClusterStore, that might keep trying to connect to a group of ESX hosts even when that ClusterStore is no longer part of that group might cause excessive network utilization and eventually overload of certain infrastructure such as DNS.

The fix implements a rate-limiter to reduce the retry frequency and network overhead.

**Passthrough or SR-IOV-capable PCIe devices might be reported as non-passthrough capable or non-SR-IOV capable after an upgrade to ESX 9.0 or later**

Due to overly strict sanity checks, after upgrading your system to ESX 9.0 or later, some PCIe devices might be reported as non-passthrough capable or SR-IOV cannot be activated.

**ClusterStore services might crashloop due to excessive memory usage and lead to network overload**

A high default setting of a parameter in the ClusterStore component might cause the service to consume more memory than necessary and reach the memory limit over time. As a result, ClusterStore services might crashloop and cause network overload as it attempts to communicate from one ESX host to another during each startup.

**If you use ESX host keys to encrypt virtual machines, the hostd service might fail**

When you use an ESX host key to encrypt a VM, if you delete the VM or change the key, the removal of the original host key might trigger an exception that can cause the hostd service to fail. As a result, the ESX host temporary disconnects from vCenter and you might not be able to manage VMs on the host if hostd does not restart after the failure.

**Port mirroring stops working after a Storage vMotion operation with virtual machines**

After you configure local SPAN (Switched Port Analyzer) mirroring and migrate mirror destination virtual machines by using Storage vMotion, the mirror destination VMs might not receive traffic on the destination host.

**ESX NVMe/TCP controllers do not recover connectivity when a target upgrades or restarts**

When performing NVMe/TCP target upgrade or restart, controllers in an ESX host might not recover connectivity after the target is online. As a result, you do not see the respective controllers from the vSphere Client. A rare race condition between the NVMe core layer and NVMe/TCP drivers causes the issue.

**ESX performance degrades with Hitachi NVMe-oF storage target**

When using the NVMe/TCP protocol, creation and deployment of virtual machines on datastores backed by a NVMe namespace on Hitachi NVMe-oF target might be slow when using the default settings.

**Virtual machines with fixed passthrough hot-plugging enabled might fail due to misallocation of interrupts**

For VMs with fixed passthrough hot-plugging enabled, after subsequent hot-adds of passthrough NVMe drives, the functionality might fail because interrupts might not be properly allocated.

**During upgrade of ToR switches, the teamPolicyUpDelay capability of the "Route based on physical NIC load" teaming policy might not work consistently**

If you set up the Route based on physical NIC load teaming policy to provide a window for ToR switches upgrade by using the teamPolicyUpDelay capability, in some cases this capability might not work. As a result, you might see a temporary network outage as the physical network is not ready.

**If a virtual machine migrates to an ESX host undergoing NSX update, the Distributed Firewall rule might be detached from that host**

During NSX update or upgrade, ESX hosts go into maintenance mode and the Distributed Resource Scheduler might trigger mass migration of VMs. As a result, vSphere vMotion with the Distributed Firewall rule might fail on some VMs and cause the DFW rule to be detached from the host.

**Excessive logs in the nsxdavim.log might cause an overload of the syslog server**

Frequent updates from hostd on an NSX distributed virtual port group, such as add, update, and delete, might cause excessive logs in the nsxdavim.log, which in some cases might lead to an overload of the syslog server.

**You do not see an option to select more than 8 GPUs for vGPU device groups**

When setting up a vGPU VM, you do not see an option to select more than 8 GPUs for vGPU device groups. For systems such as NVIDIA HGX, there could be more than 8 physical GPUs with corresponding device groups.

The fix adds the option to select 16 GPUs.

**You do not see any vGPU device groups for NVIDIA HGX H100 systems**

The vGPU device group filtering code does not ensure that each NIC which is a candidate for a NIC-to-GPU device group has the required SR-IOV virtual function active. For NVIDIA HGX H100 systems this issue can cause all vGPU device groups to be ignored.

**ESX host server firmware might not automatically make the PCIe Atomic Operations feature available to passthrough devices**

GPU workloads on a virtual machine with AMD GPU VMDirectPath I/O might fail or hang because the ESX host server firmware might not automatically activate PCIe atomic operations for AMD GPU devices.

The fix enables enables atomic ops for AMD GPUs and exposes the PCIe Atomicops Requestor Enable bit of PCIe Device control 2 register of the passthrough AMD GPU device to the Guest OS.

**During booting or when the Intel Volume Management Device (VMD) driver first loads, NVMe devices might fail in the enumeration of namespaces**

If an NVME drive has 512 namespaces, the VMD driver runs out of memory when trying to enumerate them all.

**ESX fails to boot on systems with more than 512 logical CPUs in one NUMA node**

Prior to ESX 9.0.1.0, ESX fails to boot on systems with more than 512 logical processors, or hyperthreads, in one NUMA node. Such systems are very unusual, but configuring the NUMA Nodes per Socket BIOS setting to 0 (NPS0) and deactivating the CCX as NUMA Domain on AMD system can cause all logical processors to be in a single NUMA node.

**A virtual machine with a vSGA device with Intel Flex GPU fails to boot if Distributed Resource Scheduler (DRS) is active**

If DRS is active, a virtual machine with a vSGA device with Intel Flex GPU might power on for a while but shortly powers off and cannot boot.

**ESX 9.0.1.0 includes the following Intel microcode:**

| Code Name | FMS | Plat ID | Servicing | MCU Rev | MCU Date | Brand Names |
| --- | --- | --- | --- | --- | --- | --- |
| Nehalem EP | 0x106a5 (06/1a/5) | 0x03 | baseline | 0x1d | 5/11/2018 | Intel Xeon 35xx Series; Intel Xeon 55xx Series |
| Clarkdale | 0x20652 (06/25/2) | 0x12 | baseline | 0x11 | 5/8/2018 | Intel i3/i5 Clarkdale Series; Intel Xeon 34xx Clarkdale Series |
| Arrandale | 0x20655 (06/25/5) | 0x92 | baseline | 0x7 | 4/23/2018 | Intel Core i7-620LE Processor |
| Sandy Bridge DT | 0x206a7 (06/2a/7) | 0x12 | baseline | 0x2f | 2/17/2019 | Intel Xeon E3-1100 Series; Intel Xeon E3-1200 Series; Intel i7-2655-LE Series; Intel i3-2100 Series |
| Westmere EP | 0x206c2 (06/2c/2) | 0x03 | baseline | 0x1f | 5/8/2018 | Intel Xeon 56xx Series; Intel Xeon 36xx Series |
| Sandy Bridge EP | 0x206d6 (06/2d/6) | 0x6d | baseline | 0x621 | 3/4/2020 | Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series |
| Sandy Bridge EP | 0x206d7 (06/2d/7) | 0x6d | baseline | 0x71a | 3/24/2020 | Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series |
| Nehalem EX | 0x206e6 (06/2e/6) | 0x04 | baseline | 0xd | 5/15/2018 | Intel Xeon 65xx Series; Intel Xeon 75xx Series |
| Westmere EX | 0x206f2 (06/2f/2) | 0x05 | baseline | 0x3b | 5/16/2018 | Intel Xeon E7-8800 Series; Intel Xeon E7-4800 Series; Intel Xeon E7-2800 Series |
| Ivy Bridge DT | 0x306a9 (06/3a/9) | 0x12 | baseline | 0x21 | 2/13/2019 | Intel i3-3200 Series; Intel i7-3500-LE/UE; Intel i7-3600-QE; Intel Xeon E3-1200-v2 Series; Intel Xeon E3-1100-C-v2 Series; Intel Pentium B925C |
| Haswell DT | 0x306c3 (06/3c/3) | 0x32 | baseline | 0x28 | 11/12/2019 | Intel Xeon E3-1200-v3 Series; Intel i7-4700-EQ Series; Intel i5-4500-TE Series; Intel i3-4300 Series |
| Ivy Bridge EP | 0x306e4 (06/3e/4) | 0xed | baseline | 0x42e | 3/14/2019 | Intel Xeon E5-4600-v2 Series; Intel Xeon E5-2600-v2 Series; Intel Xeon E5-2400-v2 Series; Intel Xeon E5-1600-v2 Series; Intel Xeon E5-1400-v2 Series |
| Ivy Bridge EX | 0x306e7 (06/3e/7) | 0xed | baseline | 0x715 | 3/14/2019 | Intel Xeon E7-8800/4800/2800-v2 Series |
| Haswell EP | 0x306f2 (06/3f/2) | 0x6f | baseline | 0x49 | 8/11/2021 | Intel Xeon E5-4600-v3 Series; Intel Xeon E5-2600-v3 Series; Intel Xeon E5-2400-v3 Series; Intel Xeon E5-1600-v3 Series; Intel Xeon E5-1400-v3 Series |
| Haswell EX | 0x306f4 (06/3f/4) | 0x80 | baseline | 0x1a | 5/24/2021 | Intel Xeon E7-8800/4800-v3 Series |
| Broadwell H | 0x40671 (06/47/1) | 0x22 | baseline | 0x22 | 11/12/2019 | Intel Core i7-5700EQ; Intel Xeon E3-1200-v4 Series |
| Avoton | 0x406d8 (06/4d/8) | 0x01 | baseline | 0x12d | 9/16/2019 | Intel Atom C2300 Series; Intel Atom C2500 Series; Intel Atom C2700 Series |
| Broadwell EP/EX | 0x406f1 (06/4f/1) | 0xef | baseline | 0xb000040 | 5/19/2021 | Intel Xeon E7-8800/4800-v4 Series; Intel Xeon E5-4600-v4 Series; Intel Xeon E5-2600-v4 Series; Intel Xeon E5-1600-v4 Series |
| Skylake SP | 0x50654 (06/55/4) | 0xb7 | baseline | 0x2007006 | 3/6/2023 | Intel Xeon Platinum 8100 Series; Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series; Intel Xeon D-2100 Series; Intel Xeon D-1600 Series; Intel Xeon W-3100 Series; Intel Xeon W-2100 Series |
| Cascade Lake B-0 | 0x50656 (06/55/6) | 0xbf | baseline | 0x4003901 | 12/12/2024 | Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200 |
| Cascade Lake | 0x50657 (06/55/7) | 0xbf | baseline | 0x5003901 | 12/12/2024 | Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200 |
| Cooper Lake | 0x5065b (06/55/b) | 0xbf | baseline | 0x7002b01 | 12/12/2024 | Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 |
| Broadwell DE | 0x50662 (06/56/2) | 0x10 | baseline | 0x1c | 6/17/2019 | Intel Xeon D-1500 Series |
| Broadwell DE | 0x50663 (06/56/3) | 0x10 | baseline | 0x700001c | 6/12/2021 | Intel Xeon D-1500 Series |
| Broadwell DE | 0x50664 (06/56/4) | 0x10 | baseline | 0xf00001a | 6/12/2021 | Intel Xeon D-1500 Series |
| Broadwell NS | 0x50665 (06/56/5) | 0x10 | baseline | 0xe000015 | 8/3/2023 | Intel Xeon D-1600 Series |
| Skylake H/S | 0x506e3 (06/5e/3) | 0x36 | baseline | 0xf0 | 11/12/2021 | Intel Xeon E3-1500-v5 Series; Intel Xeon E3-1200-v5 Series |
| Denverton | 0x506f1 (06/5f/1) | 0x01 | baseline | 0x3e | 10/5/2023 | Intel Atom C3000 Series |
| Ice Lake SP | 0x606a6 (06/6a/6) | 0x87 | baseline | 0xd000404 | 1/7/2025 | Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 Series; Intel Xeon Silver 4300 Series |
| Ice Lake D | 0x606c1 (06/6c/1) | 0x10 | baseline | 0x10002d0 | 1/7/2025 | Intel Xeon D-2700 Series; Intel Xeon D-1700 Series |
| Snow Ridge | 0x80665 (06/86/5) | 0x01 | baseline | 0x4c000026 | 2/28/2024 | Intel Atom P5000 Series |
| Snow Ridge | 0x80667 (06/86/7) | 0x01 | baseline | 0x4c000026 | 2/28/2024 | Intel Atom P5000 Series |
| Tiger Lake U | 0x806c1 (06/8c/1) | 0x80 | baseline | 0xbc | 12/1/2024 | Intel Core i3/i5/i7-1100 Series |
| Tiger Lake U Refresh | 0x806c2 (06/8c/2) | 0xc2 | baseline | 0x3c | 12/1/2024 | Intel Core i3/i5/i7-1100 Series |
| Tiger Lake H | 0x806d1 (06/8d/1) | 0xc2 | baseline | 0x56 | 12/11/2024 | Intel Xeon W-11000E Series |
| Sapphire Rapids SP HBM | 0x806f8 (06/8f/8) | 0x10 | baseline | 0x2c0003e0 | 7/30/2024 | Intel Xeon Max 9400 Series |
| Sapphire Rapids SP | 0x806f8 (06/8f/8) | 0x87 | baseline | 0x2b000639 | 1/28/2025 | Intel Xeon Platinum 8400 Series; Intel Xeon Gold 6400/5400 Series; Intel Xeon Silver 4400 Series; Intel Xeon Bronze 3400 Series |
| Kaby Lake H/S/X | 0x906e9 (06/9e/9) | 0x2a | baseline | 0xf8 | 9/28/2023 | Intel Xeon E3-1200-v6 Series; Intel Xeon E3-1500-v6 Series |
| Coffee Lake | 0x906ea (06/9e/a) | 0x22 | baseline | 0xfa | 7/28/2024 | Intel Xeon E-2100 Series; Intel Xeon E-2200 Series (4 or 6 core) |
| Coffee Lake | 0x906eb (06/9e/b) | 0x02 | baseline | 0xf6 | 2/1/2024 | Intel Xeon E-2100 Series |
| Coffee Lake | 0x906ec (06/9e/c) | 0x22 | baseline | 0xf8 | 2/1/2024 | Intel Xeon E-2100 Series |
| Coffee Lake Refresh | 0x906ed (06/9e/d) | 0x22 | baseline | 0x104 | 11/14/2024 | Intel Xeon E-2200 Series (8 core) |
| Rocket Lake S | 0xa0671 (06/a7/1) | 0x02 | baseline | 0x64 | 12/1/2024 | Intel Xeon E-2300 Series |
| Granite Rapids SP R1S | 0xa06d1 (06/ad/1) | 0x20 | baseline | 0xa0000d1 | 2/7/2025 | Intel Xeon 6500P/6700P/6900P Series |
| Granite Rapids AP/SP | 0xa06d1 (06/ad/1) | 0x95 | baseline | 0x10003a2 | 2/7/2025 | Intel Xeon 6500P/6700P/6900P Series |
| Sierra Forest | 0xa06f3 (06/af/3) | 0x01 | baseline | 0x3000341 | 2/10/2025 | Intel Xeon 6700E/6900E Series |
| Raptor Lake E/HX/S | 0xb0671 (06/b7/1) | 0x32 | baseline | 0x12e | 1/15/2025 | Intel Xeon E-2400 Series |
| Raptor Lake E/HX/S | 0xb0674 (06/b7/4) | 0x32 | baseline | 0x12e | 1/15/2025 | Intel Xeon E-2400 Series |
| Emerald Rapids SP | 0xc06f2 (06/cf/2) | 0x87 | baseline | 0x210002a9 | 3/14/2025 | Intel Xeon 8500 Series; Intel Xeon Gold 6500/5500 Series; Intel Xeon Silver 4500 Series; Intel Xeon Bronze 3500 Series |

**Booting virtual machines with vGPU on an NVIDIA Blackwell GPU fails**

vGPU VMs that reference a physical NVIDIA Blackwell GPU cannot power on because the vmx process fails.

**ESX 9.0.1.0 includes the following AMD microcode:**

ESX builds provide microcode for most supported CPUs, and if the BIOS of your server has an older microcode version than the one provided with the ESX build, ESX attempts to load the newer version. Because of an AMD change in [microcode signing](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7033.html), ESX might not be able to apply the latest microcode. In such a case, ESX 9.0.1.0 applies the newest microcode that it can and if the version is not the latest, ESX issues a SysAlert such as This machine's BIOS should be updated to pick up the latest microcode. Updating to the latest BIOS is always best practice as usually the latest BIOS also carries the latest microcode.

| Code Name | FMS | MCU Rev | MCU Date | Brand Names |
| --- | --- | --- | --- | --- |
| Bulldozer | 0x00600f12 (15/01/2) | 0x0600063e | 2/7/2018 | Opteron 6200/4200/3200 Series |
| Piledriver | 0x00600f20 (15/02/0) | 0x06000852 | 2/6/2018 | Opteron 6300/4300/3300 Series |
| Zen-Naples | 0x00800f12 (17/01/2) | 0x08001278 | 11/11/2024 | EPYC 7001 Series |
| Zen2-Rome | 0x00830f10 (17/31/0) | 0x0830107c | 12/18/2023 | EPYC 7002/7Fx2/7Hx2 Series |
| Zen3-Milan | 0x00a00f11 (19/01/1) | 0x0a0011db | 11/11/2024 | EPYC 7003 Series |
| Zen3-Milan (old BIOS) | 0x00a00f11 (19/01/1) | 0x0a0011d5 | 2/23/2024 | EPYC 7003 Series |
| Zen3-Milan-X | 0x00a00f12 (19/01/2) | 0x0a001244 | 11/11/2024 | EPYC 7003X Series |
| Zen3-Milan-X (old BIOS) | 0x00a00f12 (19/01/2) | 0x0a001238 | 2/26/2024 | EPYC 7003X Series |
| Zen4-Genoa | 0x00a10f11 (19/11/1) | 0x0a101154 | 11/12/2024 | EPYC 9004 Series |
| Zen4-Genoa (old BIOS) | 0x00a10f11 (19/11/1) | 0x0a101148 | 2/23/2024 | EPYC 9004 Series |
| Zen4-Genoa-X | 0x00a10f12 (19/11/2) | 0x0a10124f | 11/12/2024 | EPYC 9004X Series |
| Zen4-Genoa-X (old BIOS) | 0x00a10f12 (19/11/2) | 0x0a101248 | 2/26/2024 | EPYC 9004X Series |
| Zen4-Bergamo/Siena | 0x00aa0f02 (19/a0/2) | 0x0aa00219 | 11/13/2024 | EPYC 8004/9004 Series |
| Zen4-Bergamo/Siena (old BIOS) | 0x00aa0f02 (19/a0/2) | 0x0aa00215 | 2/28/2024 | EPYC 8004/9004 Series |

## ESXi\_9.0.1-0.24957456-standard

|  |  |
| --- | --- |
| **Profile Name** | ESXi\_9.0.1-0.24957456-standard |
| **Build** | For build information, see Patches Contained in This Release. |
| **Vendor** | Broadcom, Inc. |
| **Release Date** | September 25, 2025 |
| **Acceptance Level** | Partner Supported |
| **Affected Components** | - VMware Host Client - ESXi Component - core ESXi VIBs - Host Based Replication Server for ESX - VMware NVMe over TCP Driver - ESXi Tools Component - USB Native Driver for VMware - ESXi Install/Upgrade Component - High Availability services for vSphere virtual machines on an ESXi host - Broadcom Emulex Connectivity Division FC and FCoE Driver - Intel NVME Driver with VMD Technology - ESXi Install/Upgrade Component - NSX LCP Bundle |
| **Affected VIBs** | - VMware\_bootbank\_esx-ui\_9.0.0.0-24910635 - VMware\_bootbank\_native-misc-drivers\_9.0.1-0.24957456 - VMware\_bootbank\_clusterstore\_9.0.1-0.24957456 - VMware\_bootbank\_crx\_9.0.1-0.24957456 - VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_9.0.1-0.24957456 - VMware\_bootbank\_esx-dvfilter-generic-fastpath\_9.0.1-0.24957456 - VMware\_bootbank\_esx-base\_9.0.1-0.24957456 - VMware\_bootbank\_esxio\_9.0.1-0.24957456 - VMware\_bootbank\_bmcal-esxio\_9.0.1-0.24957456 - VMware\_bootbank\_gc-esxio\_9.0.1-0.24957456 - VMware\_bootbank\_vds-vsip\_9.0.1-0.24957456 - VMware\_bootbank\_cpu-microcode\_9.0.1-0.24957456 - VMware\_bootbank\_vsan\_9.0.1-0.24957456 - VMware\_bootbank\_infravisor\_9.0.0-24908780 - VMware\_bootbank\_esx-xserver\_9.0.1-0.24957456 - VMware\_bootbank\_vcls-pod-crx\_9.0.1-0.24957456 - VMware\_bootbank\_esxio-combiner\_9.0.1-0.24957456 - VMware\_bootbank\_podvm-router\_9.0.1-0.24957456 - VMware\_bootbank\_vsanhealth\_9.0.1-0.24957456 - VMware\_bootbank\_native-misc-drivers-esxio\_9.0.1-0.24957456 - VMware\_bootbank\_esxio-combiner-esxio\_9.0.1-0.24957456 - VMware\_bootbank\_vdfs\_9.0.1-0.24957456 - VMware\_bootbank\_gc\_9.0.1-0.24957456 - VMware\_bootbank\_esxio-base\_9.0.1-0.24957456 - VMware\_bootbank\_trx\_9.0.1-0.24957456 - VMware\_bootbank\_drivervm-gpu-base\_9.0.1-0.24957456 - VMware\_bootbank\_bmcal\_9.0.1-0.24957456 - VMware\_bootbank\_vmware-hbrsrv\_9.0.1-0.24957456 - VMW\_bootbank\_nvmetcp\_2.0.1.1-1vmw.901.0.24957456 - VMW\_bootbank\_nvmetcp-esxio\_2.0.1.1-1vmw.901.0.24957456 - VMware\_locker\_tools-light\_13.0.5-0.24957456 - VMW\_bootbank\_vmkusb-esxio\_0.1-29vmw.901.0.24957456 - VMW\_bootbank\_vmkusb\_0.1-29vmw.901.0.24957456 - VMware\_bootbank\_esx-update\_9.0.1-0.24957456 - VMware\_bootbank\_loadesx\_9.0.1-0.24957456 - VMware\_bootbank\_vmware-fdm\_9.0.1-0.24957456 - VMW\_bootbank\_lpfc\_900.14.4.390.20-36vmw.901.0.24957456 - VMW\_bootbank\_iavmd\_9.0.0.1100-4vmw.901.0.24957456 - VMware\_bootbank\_esxio-update\_9.0.1-0.24957456 - VMware\_bootbank\_loadesxio\_9.0.1-0.24957456 - VMware\_bootbank\_nsx-context-mux-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-cfgagent\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-vdpi\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-host-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-cfgagent-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-adf-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-esx-datapath-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-mpa-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-monitoring-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-netopa-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-netopa\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsxcli-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_vsipfwlib-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsxcli\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_vsipfwlib\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-platform-client\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-platform-client-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-esx-datapath\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-python-utils\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-shared-libs-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-host\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-opsagent-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-adf\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-proto2-libs\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-cpp-libs\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-python-protobuf\_9.0.1.0-9.0.24800347 - VMware\_bootbank\_nsx-vdpi-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-snproxy-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-shared-libs\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-python-protobuf-esxio\_9.0.1.0-9.0.24800347 - VMware\_bootbank\_nsx-ids\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-nestdb-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-python-logging\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-proto2-libs-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-python-logging-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-mpa\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-nestdb\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-cpp-libs-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-context-mux\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-monitoring\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-ids-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-exporter-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-proxy-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-python-utils-esxio\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-opsagent\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-proxy\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-sfhc\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-exporter\_9.0.1.0-9.0.24952112 - VMware\_bootbank\_nsx-snproxy\_9.0.1.0-9.0.24952112   \*The same list applies for the ESXi\_9.0.1-0.24957456-no-tools image profile, except the VMware\_locker\_tools-light\_13.0.5-0.24957456 VIB. |
| **PRs Fixed** | 3552243, 3538289, 3521243, 3552640, 3537103, 3547622, 3554274, 3538565, 3553087, 3547591, 3558914, 3520826, 3557349, 3559990, 3557364, 3557453, 3502821, 3552794, 3553367, 3552236, 3549613, 3544223, 3552992, 3552977, 3551935, 3553014, 3542824, 3553017, 3543517, 3542176, 3543172, 3537096, 3523290, 3525849, 3541218, 3538647, 3541101, 3540259, 3538662, 3536517, 3536512, 3535775, 3534015, 3528521, 3528518, 3528419, 3524827, 3522713, 3520895, 3518918, 3506964, 3501927, 3492318 |
| **Related CVE numbers** | N/A |

**VMware ESX 9.0.1.0 provides the following resolved issues and updates:**

**A routing issue with the Cisco Application Centric Infrastructure (ACI) switch might cause loss of vSAN traffic**

To override normal IP routing, vSAN binds all outgoing traffic on TCP sockets and traffic runs over a VMkernel adapter dedicated to vSAN. In some cases, the vSAN binding might not be set or a TCP socket might be missing, so packets are sent with the normal IP routing. In such cases, Cisco ACI devices might change the routing table based on the incoming packets, which in turn causes traffic loss on the vSAN cluster.

**A virtual machine might fail to power on if the .vmx file is changed in the backend**

In certain scenarios, when a VM is restored from a backup, applications external to the ESXi host might delete and recreate the .vmx file while the ESXi nfs41client is still accessing the file handle of the old .vmx file. As a result, a stale handle error causes the power-on of the VM to fail.

**An ESX host might fail with a purple diagnostic screen with LVMHandleDeviceAPDEvent during All Paths Down (APD) state for a device or LUN**

While a VMFS volume is closing, an APD event handler for the volume might be unregistered and relevant data structures might be freed. During this period, if the device or LUN that hosts the VMFS volume enters APD, a race condition can cause access to the freed data structure, eventually causing the ESX host to fail with a purple diagnostic screen with LVMHandleDeviceAPDEvent in the stack.

**The service on ports 2379 and 2380 does not support TLS 1.3 by default**

FIPS compliance issues with the Golang runtime prevented the service on ports 2379 and 3280 to support TLS 1.3 by default until ESX 9.0.1.0.

The service using ports 2379 and 2380 activates the TLS 1.3 protocol based on the TLS profile setting of ESX hosts.

**In the vSphere Client, ESX hardware health metrics do not refresh automatically**

If a hardware sensor information changes or a fault occurs, the ESX hardware health metrics in the vSphere Client do not reflect the changes automatically and you need to refresh them manually. This issue does not impact alarms and events.

**You cannot use public/private key pair to connect with SSH by using HTTP PUT**

You cannot use authorized public/private keys to connect to ESX hosts with SSH by using ConfigManager APIs (HTTP PUT).

**An ESX host might shut down due to Machine-Check Exception (MCE) on the virtual machine memory**

When an uncorrectable error occurs on the guest OS memory of an ESX host, the underlying hardware might trigger a MCE. If the local machine check exception (LMCE) is not enabled either by the firmware or at the ESX host, the host might shut down, which might cause downtime for applications hosted on the host VMs.

**Virtual machines cannot boot when configured with a PCI passthrough device**

VMs configured with a PCI passthrough device might consistently fail to boot, removing the device from its configuration and from the PCI device list of the ESX host.

**Changing the VM storage policy on a powered-off encrypted virtual machine causes the hostd service to fail**

When you modify the storage policy of a powered-off encrypted virtual machine, if the new policy also specifies VM encryption, the hostd service might fail.

**An ESX host might fail to enter maintenance mode or vSphere vMotion tasks might fail on a cluster with active memory tiering**

Due to conservative memory allocation by the memory tiering feature, an ESX host might fail to enter maintenance mode or vSphere vMotion tasks might fail on a cluster with active memory tiering with an error in the vmkernel.log such as:

2025-06-02T12:32:53.841Z Wa(180) vmkwarning: cpu57:3249843)WARNING: VMotionRecv: 3902: 922189911786969974 D: World 3249843 waited 15.783 seconds to leave low memory state on dest host during pre-copy. May cause unexpected VMotion failures!

**An ESX host fails with purple diagnostic screen due to overload with task management commands**

When a device receives too many task management commands to handle concurrent I/Os, some of the commands might take long to complete. As a result, the ESX host might fail with a purple diagnostic screen.

**ESX stops producing events based on VMkernel Observations (VOBs)**

In some cases, ESX might stop producing events based on VOBs, which causes missed alarms in vCenter. As a result, in the vSphere Client you do not see alarms for problems detected by the VMkernel .

**Rare memory preallocation issue might cause an ESX host to fail with a purple diagnostic screen**

For some types of VMs, such as PCIe passthrough VMs, ESX tries to preallocate memory while the VM powers on. If the VM is terminated by vSphere High Availability during the memory preallocation, the ESX host might fail with a purple diagnostic screen.

**vSphere Quick Boot support:**

ESX 9.0.1 adds vSphere Quick Boot support for the passthrough driver for Intel Gaudi 3 AI Accelerators. For more information, see KB [406262](https://knowledge.broadcom.com/external/article/406262/passthrough-driver-for-intel-gaudi-ai-ac.html). For the full list of supported servers and drivers, see the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).

**Failed quiesced snapshot of virtual machines might corrupt disk chains to vSphere Virtual Volume or vSAN disks**

If taking a quiesced snapshot of a VM with vSphere Virtual Volume or vSAN disks fails, some or all of the disk chains might be corrupted. The VM can no longer be managed properly, and data loss might occur, forcing a recovery from backup.

**Replicated virtual machines might become unresponsive during incremental sync**

The I/O capture component of vSphere Replication might not properly handle the UNMAP commands issued by the Guest OS during an incremental sync, which causes some VMs to become unresponsive.

**If the remote boot disk is in All Paths Down (APD) or Permanent Device Loss (PDL) state, the ESX host fails with a purple diagnostics screen**

In VCF 9.0, remote boot disk monitoring is active by default and if the remote boot disk experiences an APD or PDL state, the ESX host might fail with a purple diagnostics screen.

Remote boot disk monitoring is not active by default.

**VMware Tools Bundling Changes in ESX 9.0.1.0**

The following VMware Tools ISO images are bundled with ESX 9.0.1.0:

- **windows.iso**: VMware Tools 13.0.5 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.

The following VMware Tools ISO images are available for download:

- VMware Tools 12.5.4:

  - **windows.iso:** VMware Tools 12.5.4 supports 64-bit Windows versions.
  - **windows-x86.iso:** VMware Tools 12.4.9 supports 32-bit Windows versions.
  - **linux.iso**: VMware Tools 10.3.26 ISO image for Linux OS with glibc 2.11 or later.

- VMware Tools 11.0.6:

  - **windows.iso**: for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).

- VMware Tools 10.0.12:

  - **winPreVista.iso**: for Windows 2000, Windows XP, and Windows 2003.
  - **linuxPreGLibc25.iso**: supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with **glibc** version earlier than 2.5.
- **solaris.iso**: VMware Tools image 10.3.10 for Solaris.
- **darwin.iso**: Supports Mac OS X versions 10.11 and later.

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESX:

- [VMware Tools 13.0.5 Release Notes](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1305-release-notes.html)
- [VMware Tools for hosts provisioned with Auto Deploy](https://kb.vmware.com/s/article/2004018)
- [Upgrading VMware Tools](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/vmware-tools-administration/upgrading-vmware-tools.html)

**In the hostd log, you see multiple messages that the VMX scoreboard is not readable**

After creating a VM from a clone or template, the vmxstats.filename might duplicate the name of the parent VM and the host stats registry cannot read and log the stats of the new VM. As a result, in the hostd logs you see multiple messages such as Adding VM XXX failed, file /vmfs/volumes/YYY/ZZZ/ZZZ.scoreboard is not readable. This error does not affect the functionality of the new VMs in any way.

**Virtual machine migration and Dell Power Protect Data Manager (PPDM) backups might fail after a Dell Transport Snapshot Data Mover (TSDM) panic**

A panic event at Dell TSDM during a PPDM-based snapshot synchronization can stop the task in the data protection daemon due to a miscalculation error. The stopped synchronization subsequently affects PPDM backup operations on the VM and results in failure of vSphere vMotion tasks.

**ESX host might leak memory during NVMe unmap operations**

If an identify namespace call to a NVMe target fails during a NVMe unmap operation, the memory allocated for the unmap command might not be freed. As a result, you might see higher memory usage in that ESX host until you reboot it to reclaim the memory.

**NVMe over Fibre Channel (NVMe/FC) devices are not recovered after a link reset**

In extremely rare cases, due to a deadlock while discovering and connecting NVMe/FC devices in parallel, an ESX host might not be able to reconnect to all NVMe/FC devices after a link reset and performance of connected devices might also degrade.

**An ESX host might fail with a purple diagnostic screen during migration of virtual machines from a Tintri NFSv4.1 datastore**

During the migration of VMs by using vSphere vMotion from a Tintri NFSv4.1 datastore, the ESX host might fail with a purple diagnostic screen. This issue is specific to how Tintri NFSv4.1 servers handle NULL values in certain scenarios.

**You see a regression of linked clone performance due to slower VM creation**

Additional I/O tasks during VM creation might cause a noticeable regression in the latency and affect the creation of linked clones.

**A vmxnet3 virtual NIC might stop transmitting data after a reconfiguration**

A rare race between vmxnet3 vNIC reconfiguration and tx path due to heavy traffic might cause the vNIC to stop transmitting data after the reconfiguration.

**IF-MIB SNMP data intermittently reports hidden ports DVFilter Coalesce Portset and pps**

When using third-party tools, the IF-MIB SNMP data might intermittently report hidden portsets, such as pps and DVFilter Coalesce Portset, even when they are not part of the ESX host configuration.

**After a reboot of ESX hosts, you see alarms in the vSphere Client that some uplinks are down**

Due to some limitations in the VMkernel Observation (VOB) and hostd services, uplink up and down events might not be sent to vCenter in the correct order. As a result, when a task such as rebooting ESX hosts completes, in the vSphere Client you see false alerts that some uplinks are down.

**After running the Linux fstrim command on a virtual machine, the ESX host fails with a purple diagnostics screen**

A VMFS heap memory exhaustion might cause memory access violations when clearing the pointer block cache. As a result, when you run the Linux fstrim command on a virtual machine, the ESX host might fail with a purple diagnostics screen with a PB3Manager error in the backtrace.

**During a snapshot operation of a VM with IOFilter attached, the VMX might fail due to an unresponsive thread**

In very rare situations, once in 2000 snapshot operations, a race condition might occur in the I/O filter infrastructure and cause the I/O filter watchdog to stop the VMX service, and generate a VMX core dump.

**In Multi-Initiator Zoning Model setup, ESX hosts might fail with a purple diagnostics screen due to flapping initiator FC HBA port state**

In the Multi-Initiator Zoning Model, when multiple FC HBA ports in a cluster are configured in the same FC zone, if one initiator port state is flapping, then all other initiators in the zone receive frequent Registered State Change Notifications (RSCN). An issue in the lpfc driver when processing such frequent RSCNs related to another initiator might cause the ESX host to fail with a purple diagnostics screen with an error such as:

@BlueScreen: #PF Exception 14 in world XXXXXXX:lpfc\_do\_work IP 0xXXXXXXXXXXXX addr 0xXXXXXXXXXXXX.

You see the functions lpfc\_sli4\_els\_xri\_aborted or lpfc\_sli4\_delete\_els\_xri\_aborted in the stack.

**Adding new disks external to the home directory of a virtual machine might fail with an error for reaching the security policy limit**

When a disk external to the home directory of a VM is added or removed, the security domain policy of the VM updates to give or revoke access to the external directory. It is possible that if an error occurs during disk load, to avoid issues if it is resolved, external directories are no longer removed from the security policy, even after a resolution. In time, the rules in the security policy might reach the max limit. As a result, adding new disks external to the home directory of a virtual machine fails and in the sandboxd.log you see errors such as:

2025-05-11T08:14:55.306Z Er(163) sandboxd[2099161]: [Originator@6876 sub=SecurityDomainsImpl] AddUpdateFileRules: Failed to add file policies to domain :X: world ID :Y:Argument list too long

The fix makes sure that once a disk load issue is resolved, external directories are removed from the security policy. If a VM is already facing the issue, either restart the VM or migrate it to another ESX host to trigger a regeneration of the security policy.

**Activation of TLS 1.3 in ClusterStore does not persist across ESX host reboots**

The agent\_settings configuration on ESX that controls whether TLS 1.3 is active on ClusterStore, which keeps the cluster-specific configuration data, reverts to the default of not active after a reboot of the ESX host.

**A slow SCSI device scan might make a thread of the lpfc driver unresponsive and cause various issues**

A slow SCSI device scan might make unresponsive a thread of the lpfc driver, which is responsible for storage target discovery, mailbox operations, and completion of Extended Link Service (ELS) requests. Such an unresponsive thread can lead to failing ELS requests interrupting the discovery of storage targets, no response from applications and mailbox timeouts causing esxcli elxmgmt commands to fail.

The fix improves the lpfc worker thread and prevents effects from slow SCSI device scan on the lpfc threads.

**The authentication service of the Distributed Key Value Store, or ClusterStore, might cause DNS traffic overload**

An issue with the authentication service of the Distributed Key Value Store, also called ClusterStore, that might keep trying to connect to a group of ESX hosts even when that ClusterStore is no longer part of that group might cause excessive network utilization and eventually overload of certain infrastructure such as DNS.

The fix implements a rate-limiter to reduce the retry frequency and network overhead.

**Passthrough or SR-IOV-capable PCIe devices might be reported as non-passthrough capable or non-SR-IOV capable after an upgrade to ESX 9.0 or later**

Due to overly strict sanity checks, after upgrading your system to ESX 9.0 or later, some PCIe devices might be reported as non-passthrough capable or SR-IOV cannot be activated.

**ClusterStore services might crashloop due to excessive memory usage and lead to network overload**

A high default setting of a parameter in the ClusterStore component might cause the service to consume more memory than necessary and reach the memory limit over time. As a result, ClusterStore services might crashloop and cause network overload as it attempts to communicate from one ESX host to another during each startup.

**If you use ESX host keys to encrypt virtual machines, the hostd service might fail**

When you use an ESX host key to encrypt a VM, if you delete the VM or change the key, the removal of the original host key might trigger an exception that can cause the hostd service to fail. As a result, the ESX host temporary disconnects from vCenter and you might not be able to manage VMs on the host if hostd does not restart after the failure.

**Port mirroring stops working after a Storage vMotion operation with virtual machines**

After you configure local SPAN (Switched Port Analyzer) mirroring and migrate mirror destination virtual machines by using Storage vMotion, the mirror destination VMs might not receive traffic on the destination host.

**ESX NVMe/TCP controllers do not recover connectivity when a target upgrades or restarts**

When performing NVMe/TCP target upgrade or restart, controllers in an ESX host might not recover connectivity after the target is online. As a result, you do not see the respective controllers from the vSphere Client. A rare race condition between the NVMe core layer and NVMe/TCP drivers causes the issue.

**ESX performance degrades with Hitachi NVMe-oF storage target**

When using the NVMe/TCP protocol, creation and deployment of virtual machines on datastores backed by a NVMe namespace on Hitachi NVMe-oF target might be slow when using the default settings.

**Virtual machines with fixed passthrough hot-plugging enabled might fail due to misallocation of interrupts**

For VMs with fixed passthrough hot-plugging enabled, after subsequent hot-adds of passthrough NVMe drives, the functionality might fail because interrupts might not be properly allocated.

**During upgrade of ToR switches, the teamPolicyUpDelay capability of the "Route based on physical NIC load" teaming policy might not work consistently**

If you set up the Route based on physical NIC load teaming policy to provide a window for ToR switches upgrade by using the teamPolicyUpDelay capability, in some cases this capability might not work. As a result, you might see a temporary network outage as the physical network is not ready.

**If a virtual machine migrates to an ESX host undergoing NSX update, the Distributed Firewall rule might be detached from that host**

During NSX update or upgrade, ESX hosts go into maintenance mode and the Distributed Resource Scheduler might trigger mass migration of VMs. As a result, vSphere vMotion with the Distributed Firewall rule might fail on some VMs and cause the DFW rule to be detached from the host.

**Excessive logs in the nsxdavim.log might cause an overload of the syslog server**

Frequent updates from hostd on an NSX distributed virtual port group, such as add, update, and delete, might cause excessive logs in the nsxdavim.log, which in some cases might lead to an overload of the syslog server.

**You do not see an option to select more than 8 GPUs for vGPU device groups**

When setting up a vGPU VM, you do not see an option to select more than 8 GPUs for vGPU device groups. For systems such as NVIDIA HGX, there could be more than 8 physical GPUs with corresponding device groups.

The fix adds the option to select 16 GPUs.

**You do not see any vGPU device groups for NVIDIA HGX H100 systems**

The vGPU device group filtering code does not ensure that each NIC which is a candidate for a NIC-to-GPU device group has the required SR-IOV virtual function active. For NVIDIA HGX H100 systems this issue can cause all vGPU device groups to be ignored.

**ESX host server firmware might not automatically make the PCIe Atomic Operations feature available to passthrough devices**

GPU workloads on a virtual machine with AMD GPU VMDirectPath I/O might fail or hang because the ESX host server firmware might not automatically activate PCIe atomic operations for AMD GPU devices.

The fix enables enables atomic ops for AMD GPUs and exposes the PCIe Atomicops Requestor Enable bit of PCIe Device control 2 register of the passthrough AMD GPU device to the Guest OS.

**During booting or when the Intel Volume Management Device (VMD) driver first loads, NVMe devices might fail in the enumeration of namespaces**

If an NVME drive has 512 namespaces, the VMD driver runs out of memory when trying to enumerate them all.

**ESX fails to boot on systems with more than 512 logical CPUs in one NUMA node**

Prior to ESX 9.0.1.0, ESX fails to boot on systems with more than 512 logical processors, or hyperthreads, in one NUMA node. Such systems are very unusual, but configuring the NUMA Nodes per Socket BIOS setting to 0 (NPS0) and deactivating the CCX as NUMA Domain on AMD system can cause all logical processors to be in a single NUMA node.

**A virtual machine with a vSGA device with Intel Flex GPU fails to boot if Distributed Resource Scheduler (DRS) is active**

If DRS is active, a virtual machine with a vSGA device with Intel Flex GPU might power on for a while but shortly powers off and cannot boot.

**ESX 9.0.1.0 includes the following Intel microcode:**

| Code Name | FMS | Plat ID | Servicing | MCU Rev | MCU Date | Brand Names |
| --- | --- | --- | --- | --- | --- | --- |
| Nehalem EP | 0x106a5 (06/1a/5) | 0x03 | baseline | 0x1d | 5/11/2018 | Intel Xeon 35xx Series; Intel Xeon 55xx Series |
| Clarkdale | 0x20652 (06/25/2) | 0x12 | baseline | 0x11 | 5/8/2018 | Intel i3/i5 Clarkdale Series; Intel Xeon 34xx Clarkdale Series |
| Arrandale | 0x20655 (06/25/5) | 0x92 | baseline | 0x7 | 4/23/2018 | Intel Core i7-620LE Processor |
| Sandy Bridge DT | 0x206a7 (06/2a/7) | 0x12 | baseline | 0x2f | 2/17/2019 | Intel Xeon E3-1100 Series; Intel Xeon E3-1200 Series; Intel i7-2655-LE Series; Intel i3-2100 Series |
| Westmere EP | 0x206c2 (06/2c/2) | 0x03 | baseline | 0x1f | 5/8/2018 | Intel Xeon 56xx Series; Intel Xeon 36xx Series |
| Sandy Bridge EP | 0x206d6 (06/2d/6) | 0x6d | baseline | 0x621 | 3/4/2020 | Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series |
| Sandy Bridge EP | 0x206d7 (06/2d/7) | 0x6d | baseline | 0x71a | 3/24/2020 | Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series |
| Nehalem EX | 0x206e6 (06/2e/6) | 0x04 | baseline | 0xd | 5/15/2018 | Intel Xeon 65xx Series; Intel Xeon 75xx Series |
| Westmere EX | 0x206f2 (06/2f/2) | 0x05 | baseline | 0x3b | 5/16/2018 | Intel Xeon E7-8800 Series; Intel Xeon E7-4800 Series; Intel Xeon E7-2800 Series |
| Ivy Bridge DT | 0x306a9 (06/3a/9) | 0x12 | baseline | 0x21 | 2/13/2019 | Intel i3-3200 Series; Intel i7-3500-LE/UE; Intel i7-3600-QE; Intel Xeon E3-1200-v2 Series; Intel Xeon E3-1100-C-v2 Series; Intel Pentium B925C |
| Haswell DT | 0x306c3 (06/3c/3) | 0x32 | baseline | 0x28 | 11/12/2019 | Intel Xeon E3-1200-v3 Series; Intel i7-4700-EQ Series; Intel i5-4500-TE Series; Intel i3-4300 Series |
| Ivy Bridge EP | 0x306e4 (06/3e/4) | 0xed | baseline | 0x42e | 3/14/2019 | Intel Xeon E5-4600-v2 Series; Intel Xeon E5-2600-v2 Series; Intel Xeon E5-2400-v2 Series; Intel Xeon E5-1600-v2 Series; Intel Xeon E5-1400-v2 Series |
| Ivy Bridge EX | 0x306e7 (06/3e/7) | 0xed | baseline | 0x715 | 3/14/2019 | Intel Xeon E7-8800/4800/2800-v2 Series |
| Haswell EP | 0x306f2 (06/3f/2) | 0x6f | baseline | 0x49 | 8/11/2021 | Intel Xeon E5-4600-v3 Series; Intel Xeon E5-2600-v3 Series; Intel Xeon E5-2400-v3 Series; Intel Xeon E5-1600-v3 Series; Intel Xeon E5-1400-v3 Series |
| Haswell EX | 0x306f4 (06/3f/4) | 0x80 | baseline | 0x1a | 5/24/2021 | Intel Xeon E7-8800/4800-v3 Series |
| Broadwell H | 0x40671 (06/47/1) | 0x22 | baseline | 0x22 | 11/12/2019 | Intel Core i7-5700EQ; Intel Xeon E3-1200-v4 Series |
| Avoton | 0x406d8 (06/4d/8) | 0x01 | baseline | 0x12d | 9/16/2019 | Intel Atom C2300 Series; Intel Atom C2500 Series; Intel Atom C2700 Series |
| Broadwell EP/EX | 0x406f1 (06/4f/1) | 0xef | baseline | 0xb000040 | 5/19/2021 | Intel Xeon E7-8800/4800-v4 Series; Intel Xeon E5-4600-v4 Series; Intel Xeon E5-2600-v4 Series; Intel Xeon E5-1600-v4 Series |
| Skylake SP | 0x50654 (06/55/4) | 0xb7 | baseline | 0x2007006 | 3/6/2023 | Intel Xeon Platinum 8100 Series; Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series; Intel Xeon D-2100 Series; Intel Xeon D-1600 Series; Intel Xeon W-3100 Series; Intel Xeon W-2100 Series |
| Cascade Lake B-0 | 0x50656 (06/55/6) | 0xbf | baseline | 0x4003901 | 12/12/2024 | Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200 |
| Cascade Lake | 0x50657 (06/55/7) | 0xbf | baseline | 0x5003901 | 12/12/2024 | Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200 |
| Cooper Lake | 0x5065b (06/55/b) | 0xbf | baseline | 0x7002b01 | 12/12/2024 | Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 |
| Broadwell DE | 0x50662 (06/56/2) | 0x10 | baseline | 0x1c | 6/17/2019 | Intel Xeon D-1500 Series |
| Broadwell DE | 0x50663 (06/56/3) | 0x10 | baseline | 0x700001c | 6/12/2021 | Intel Xeon D-1500 Series |
| Broadwell DE | 0x50664 (06/56/4) | 0x10 | baseline | 0xf00001a | 6/12/2021 | Intel Xeon D-1500 Series |
| Broadwell NS | 0x50665 (06/56/5) | 0x10 | baseline | 0xe000015 | 8/3/2023 | Intel Xeon D-1600 Series |
| Skylake H/S | 0x506e3 (06/5e/3) | 0x36 | baseline | 0xf0 | 11/12/2021 | Intel Xeon E3-1500-v5 Series; Intel Xeon E3-1200-v5 Series |
| Denverton | 0x506f1 (06/5f/1) | 0x01 | baseline | 0x3e | 10/5/2023 | Intel Atom C3000 Series |
| Ice Lake SP | 0x606a6 (06/6a/6) | 0x87 | baseline | 0xd000404 | 1/7/2025 | Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 Series; Intel Xeon Silver 4300 Series |
| Ice Lake D | 0x606c1 (06/6c/1) | 0x10 | baseline | 0x10002d0 | 1/7/2025 | Intel Xeon D-2700 Series; Intel Xeon D-1700 Series |
| Snow Ridge | 0x80665 (06/86/5) | 0x01 | baseline | 0x4c000026 | 2/28/2024 | Intel Atom P5000 Series |
| Snow Ridge | 0x80667 (06/86/7) | 0x01 | baseline | 0x4c000026 | 2/28/2024 | Intel Atom P5000 Series |
| Tiger Lake U | 0x806c1 (06/8c/1) | 0x80 | baseline | 0xbc | 12/1/2024 | Intel Core i3/i5/i7-1100 Series |
| Tiger Lake U Refresh | 0x806c2 (06/8c/2) | 0xc2 | baseline | 0x3c | 12/1/2024 | Intel Core i3/i5/i7-1100 Series |
| Tiger Lake H | 0x806d1 (06/8d/1) | 0xc2 | baseline | 0x56 | 12/11/2024 | Intel Xeon W-11000E Series |
| Sapphire Rapids SP HBM | 0x806f8 (06/8f/8) | 0x10 | baseline | 0x2c0003e0 | 7/30/2024 | Intel Xeon Max 9400 Series |
| Sapphire Rapids SP | 0x806f8 (06/8f/8) | 0x87 | baseline | 0x2b000639 | 1/28/2025 | Intel Xeon Platinum 8400 Series; Intel Xeon Gold 6400/5400 Series; Intel Xeon Silver 4400 Series; Intel Xeon Bronze 3400 Series |
| Kaby Lake H/S/X | 0x906e9 (06/9e/9) | 0x2a | baseline | 0xf8 | 9/28/2023 | Intel Xeon E3-1200-v6 Series; Intel Xeon E3-1500-v6 Series |
| Coffee Lake | 0x906ea (06/9e/a) | 0x22 | baseline | 0xfa | 7/28/2024 | Intel Xeon E-2100 Series; Intel Xeon E-2200 Series (4 or 6 core) |
| Coffee Lake | 0x906eb (06/9e/b) | 0x02 | baseline | 0xf6 | 2/1/2024 | Intel Xeon E-2100 Series |
| Coffee Lake | 0x906ec (06/9e/c) | 0x22 | baseline | 0xf8 | 2/1/2024 | Intel Xeon E-2100 Series |
| Coffee Lake Refresh | 0x906ed (06/9e/d) | 0x22 | baseline | 0x104 | 11/14/2024 | Intel Xeon E-2200 Series (8 core) |
| Rocket Lake S | 0xa0671 (06/a7/1) | 0x02 | baseline | 0x64 | 12/1/2024 | Intel Xeon E-2300 Series |
| Granite Rapids SP R1S | 0xa06d1 (06/ad/1) | 0x20 | baseline | 0xa0000d1 | 2/7/2025 | Intel Xeon 6500P/6700P/6900P Series |
| Granite Rapids AP/SP | 0xa06d1 (06/ad/1) | 0x95 | baseline | 0x10003a2 | 2/7/2025 | Intel Xeon 6500P/6700P/6900P Series |
| Sierra Forest | 0xa06f3 (06/af/3) | 0x01 | baseline | 0x3000341 | 2/10/2025 | Intel Xeon 6700E/6900E Series |
| Raptor Lake E/HX/S | 0xb0671 (06/b7/1) | 0x32 | baseline | 0x12e | 1/15/2025 | Intel Xeon E-2400 Series |
| Raptor Lake E/HX/S | 0xb0674 (06/b7/4) | 0x32 | baseline | 0x12e | 1/15/2025 | Intel Xeon E-2400 Series |
| Emerald Rapids SP | 0xc06f2 (06/cf/2) | 0x87 | baseline | 0x210002a9 | 3/14/2025 | Intel Xeon 8500 Series; Intel Xeon Gold 6500/5500 Series; Intel Xeon Silver 4500 Series; Intel Xeon Bronze 3500 Series |

**Booting virtual machines with vGPU on an NVIDIA Blackwell GPU fails**

vGPU VMs that reference a physical NVIDIA Blackwell GPU cannot power on because the vmx process fails.

**ESX 9.0.1.0 includes the following AMD microcode:**

ESX builds provide microcode for most supported CPUs, and if the BIOS of your server has an older microcode version than the one provided with the ESX build, ESX attempts to load the newer version. Because of an AMD change in [microcode signing](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7033.html), ESX might not be able to apply the latest microcode. In such a case, ESX 9.0.1.0 applies the newest microcode that it can and if the version is not the latest, ESX issues a SysAlert such as This machine's BIOS should be updated to pick up the latest microcode. Updating to the latest BIOS is always best practice as usually the latest BIOS also carries the latest microcode.

| Code Name | FMS | MCU Rev | MCU Date | Brand Names |
| --- | --- | --- | --- | --- |
| Bulldozer | 0x00600f12 (15/01/2) | 0x0600063e | 2/7/2018 | Opteron 6200/4200/3200 Series |
| Piledriver | 0x00600f20 (15/02/0) | 0x06000852 | 2/6/2018 | Opteron 6300/4300/3300 Series |
| Zen-Naples | 0x00800f12 (17/01/2) | 0x08001278 | 11/11/2024 | EPYC 7001 Series |
| Zen2-Rome | 0x00830f10 (17/31/0) | 0x0830107c | 12/18/2023 | EPYC 7002/7Fx2/7Hx2 Series |
| Zen3-Milan | 0x00a00f11 (19/01/1) | 0x0a0011db | 11/11/2024 | EPYC 7003 Series |
| Zen3-Milan (old BIOS) | 0x00a00f11 (19/01/1) | 0x0a0011d5 | 2/23/2024 | EPYC 7003 Series |
| Zen3-Milan-X | 0x00a00f12 (19/01/2) | 0x0a001244 | 11/11/2024 | EPYC 7003X Series |
| Zen3-Milan-X (old BIOS) | 0x00a00f12 (19/01/2) | 0x0a001238 | 2/26/2024 | EPYC 7003X Series |
| Zen4-Genoa | 0x00a10f11 (19/11/1) | 0x0a101154 | 11/12/2024 | EPYC 9004 Series |
| Zen4-Genoa (old BIOS) | 0x00a10f11 (19/11/1) | 0x0a101148 | 2/23/2024 | EPYC 9004 Series |
| Zen4-Genoa-X | 0x00a10f12 (19/11/2) | 0x0a10124f | 11/12/2024 | EPYC 9004X Series |
| Zen4-Genoa-X (old BIOS) | 0x00a10f12 (19/11/2) | 0x0a101248 | 2/26/2024 | EPYC 9004X Series |
| Zen4-Bergamo/Siena | 0x00aa0f02 (19/a0/2) | 0x0aa00219 | 11/13/2024 | EPYC 8004/9004 Series |
| Zen4-Bergamo/Siena (old BIOS) | 0x00aa0f02 (19/a0/2) | 0x0aa00215 | 2/28/2024 | EPYC 8004/9004 Series |

## ESXi\_9.0.1-0.24957456-no-tools

|  |  |
| --- | --- |
| **Profile Name** | ESXi\_9.0.1-0.24957456-no-tools |
| **Build** | For build information, see Patches Contained in This Release. |
| **Vendor** | Broadcom, Inc. |
| **Release Date** | September 25, 2025 |
| **Acceptance Level** | Partner Supported |
| **Affected Components** | - VMware Host Client - ESXi Component - core ESXi VIBs - Host Based Replication Server for ESX - VMware NVMe over TCP Driver - USB Native Driver for VMware - ESXi Install/Upgrade Component - High Availability services for vSphere virtual machines on an ESXi host - Broadcom Emulex Connectivity Division FC and FCoE Driver - Intel NVME Driver with VMD Technology - ESXi Install/Upgrade Component - NSX LCP Bundle |
| **PRs Fixed** | 3552243, 3538289, 3521243, 3552640, 3537103, 3547622, 3554274, 3538565, 3553087, 3547591, 3558914, 3520826, 3557349, 3559990, 3557364, 3557453, 3502821, 3552794, 3553367, 3552236, 3549613, 3544223, 3552992, 3552977, 3551935, 3553014, 3542824, 3553017, 3543517, 3542176, 3543172, 3537096, 3523290, 3525849, 3541218, 3538647, 3541101, 3540259, 3538662, 3536517, 3536512, 3535775, 3534015, 3528521, 3528518, 3528419, 3524827, 3522713, 3520895, 3518918, 3506964, 3501927, 3492318 |
| **Related CVE numbers** | N/A |

**VMware ESX 9.0.1.0 provides the following resolved issues and updates:**

**A routing issue with the Cisco Application Centric Infrastructure (ACI) switch might cause loss of vSAN traffic**

To override normal IP routing, vSAN binds all outgoing traffic on TCP sockets and traffic runs over a VMkernel adapter dedicated to vSAN. In some cases, the vSAN binding might not be set or a TCP socket might be missing, so packets are sent with the normal IP routing. In such cases, Cisco ACI devices might change the routing table based on the incoming packets, which in turn causes traffic loss on the vSAN cluster.

**A virtual machine might fail to power on if the .vmx file is changed in the backend**

In certain scenarios, when a VM is restored from a backup, applications external to the ESXi host might delete and recreate the .vmx file while the ESXi nfs41client is still accessing the file handle of the old .vmx file. As a result, a stale handle error causes the power-on of the VM to fail.

**An ESX host might fail with a purple diagnostic screen with LVMHandleDeviceAPDEvent during All Paths Down (APD) state for a device or LUN**

While a VMFS volume is closing, an APD event handler for the volume might be unregistered and relevant data structures might be freed. During this period, if the device or LUN that hosts the VMFS volume enters APD, a race condition can cause access to the freed data structure, eventually causing the ESX host to fail with a purple diagnostic screen with LVMHandleDeviceAPDEvent in the stack.

**The service on ports 2379 and 2380 does not support TLS 1.3 by default**

FIPS compliance issues with the Golang runtime prevented the service on ports 2379 and 3280 to support TLS 1.3 by default until ESX 9.0.1.0.

The service using ports 2379 and 2380 activates the TLS 1.3 protocol based on the TLS profile setting of ESX hosts.

**In the vSphere Client, ESX hardware health metrics do not refresh automatically**

If a hardware sensor information changes or a fault occurs, the ESX hardware health metrics in the vSphere Client do not reflect the changes automatically and you need to refresh them manually. This issue does not impact alarms and events.

**You cannot use public/private key pair to connect with SSH by using HTTP PUT**

You cannot use authorized public/private keys to connect to ESX hosts with SSH by using ConfigManager APIs (HTTP PUT).

**An ESX host might shut down due to Machine-Check Exception (MCE) on the virtual machine memory**

When an uncorrectable error occurs on the guest OS memory of an ESX host, the underlying hardware might trigger a MCE. If the local machine check exception (LMCE) is not enabled either by the firmware or at the ESX host, the host might shut down, which might cause downtime for applications hosted on the host VMs.

**Virtual machines cannot boot when configured with a PCI passthrough device**

VMs configured with a PCI passthrough device might consistently fail to boot, removing the device from its configuration and from the PCI device list of the ESX host.

**Changing the VM storage policy on a powered-off encrypted virtual machine causes the hostd service to fail**

When you modify the storage policy of a powered-off encrypted virtual machine, if the new policy also specifies VM encryption, the hostd service might fail.

**An ESX host might fail to enter maintenance mode or vSphere vMotion tasks might fail on a cluster with active memory tiering**

Due to conservative memory allocation by the memory tiering feature, an ESX host might fail to enter maintenance mode or vSphere vMotion tasks might fail on a cluster with active memory tiering with an error in the vmkernel.log such as:

2025-06-02T12:32:53.841Z Wa(180) vmkwarning: cpu57:3249843)WARNING: VMotionRecv: 3902: 922189911786969974 D: World 3249843 waited 15.783 seconds to leave low memory state on dest host during pre-copy. May cause unexpected VMotion failures!

**An ESX host fails with purple diagnostic screen due to overload with task management commands**

When a device receives too many task management commands to handle concurrent I/Os, some of the commands might take long to complete. As a result, the ESX host might fail with a purple diagnostic screen.

**ESX stops producing events based on VMkernel Observations (VOBs)**

In some cases, ESX might stop producing events based on VOBs, which causes missed alarms in vCenter. As a result, in the vSphere Client you do not see alarms for problems detected by the VMkernel .

**Rare memory preallocation issue might cause an ESX host to fail with a purple diagnostic screen**

For some types of VMs, such as PCIe passthrough VMs, ESX tries to preallocate memory while the VM powers on. If the VM is terminated by vSphere High Availability during the memory preallocation, the ESX host might fail with a purple diagnostic screen.

**vSphere Quick Boot support:**

ESX 9.0.1 adds vSphere Quick Boot support for the passthrough driver for Intel Gaudi 3 AI Accelerators. For more information, see KB [406262](https://knowledge.broadcom.com/external/article/406262/passthrough-driver-for-intel-gaudi-ai-ac.html). For the full list of supported servers and drivers, see the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).

**Failed quiesced snapshot of virtual machines might corrupt disk chains to vSphere Virtual Volume or vSAN disks**

If taking a quiesced snapshot of a VM with vSphere Virtual Volume or vSAN disks fails, some or all of the disk chains might be corrupted. The VM can no longer be managed properly, and data loss might occur, forcing a recovery from backup.

**Replicated virtual machines might become unresponsive during incremental sync**

The I/O capture component of vSphere Replication might not properly handle the UNMAP commands issued by the Guest OS during an incremental sync, which causes some VMs to become unresponsive.

**If the remote boot disk is in All Paths Down (APD) or Permanent Device Loss (PDL) state, the ESX host fails with a purple diagnostics screen**

In VCF 9.0, remote boot disk monitoring is active by default and if the remote boot disk experiences an APD or PDL state, the ESX host might fail with a purple diagnostics screen.

Remote boot disk monitoring is not active by default.

**In the hostd log, you see multiple messages that the VMX scoreboard is not readable**

After creating a VM from a clone or template, the vmxstats.filename might duplicate the name of the parent VM and the host stats registry cannot read and log the stats of the new VM. As a result, in the hostd logs you see multiple messages such as Adding VM XXX failed, file /vmfs/volumes/YYY/ZZZ/ZZZ.scoreboard is not readable. This error does not affect the functionality of the new VMs in any way.

**Virtual machine migration and Dell Power Protect Data Manager (PPDM) backups might fail after a Dell Transport Snapshot Data Mover (TSDM) panic**

A panic event at Dell TSDM during a PPDM-based snapshot synchronization can stop the task in the data protection daemon due to a miscalculation error. The stopped synchronization subsequently affects PPDM backup operations on the VM and results in failure of vSphere vMotion tasks.

**ESX host might leak memory during NVMe unmap operations**

If an identify namespace call to a NVMe target fails during a NVMe unmap operation, the memory allocated for the unmap command might not be freed. As a result, you might see higher memory usage in that ESX host until you reboot it to reclaim the memory.

**NVMe over Fibre Channel (NVMe/FC) devices are not recovered after a link reset**

In extremely rare cases, due to a deadlock while discovering and connecting NVMe/FC devices in parallel, an ESX host might not be able to reconnect to all NVMe/FC devices after a link reset and performance of connected devices might also degrade.

**An ESX host might fail with a purple diagnostic screen during migration of virtual machines from a Tintri NFSv4.1 datastore**

During the migration of VMs by using vSphere vMotion from a Tintri NFSv4.1 datastore, the ESX host might fail with a purple diagnostic screen. This issue is specific to how Tintri NFSv4.1 servers handle NULL values in certain scenarios.

**You see a regression of linked clone performance due to slower VM creation**

Additional I/O tasks during VM creation might cause a noticeable regression in the latency and affect the creation of linked clones.

**A vmxnet3 virtual NIC might stop transmitting data after a reconfiguration**

A rare race between vmxnet3 vNIC reconfiguration and tx path due to heavy traffic might cause the vNIC to stop transmitting data after the reconfiguration.

**IF-MIB SNMP data intermittently reports hidden ports DVFilter Coalesce Portset and pps**

When using third-party tools, the IF-MIB SNMP data might intermittently report hidden portsets, such as pps and DVFilter Coalesce Portset, even when they are not part of the ESX host configuration.

**After a reboot of ESX hosts, you see alarms in the vSphere Client that some uplinks are down**

Due to some limitations in the VMkernel Observation (VOB) and hostd services, uplink up and down events might not be sent to vCenter in the correct order. As a result, when a task such as rebooting ESX hosts completes, in the vSphere Client you see false alerts that some uplinks are down.

**After running the Linux fstrim command on a virtual machine, the ESX host fails with a purple diagnostics screen**

A VMFS heap memory exhaustion might cause memory access violations when clearing the pointer block cache. As a result, when you run the Linux fstrim command on a virtual machine, the ESX host might fail with a purple diagnostics screen with a PB3Manager error in the backtrace.

**During a snapshot operation of a VM with IOFilter attached, the VMX might fail due to an unresponsive thread**

In very rare situations, once in 2000 snapshot operations, a race condition might occur in the I/O filter infrastructure and cause the I/O filter watchdog to stop the VMX service, and generate a VMX core dump.

**In Multi-Initiator Zoning Model setup, ESX hosts might fail with a purple diagnostics screen due to flapping initiator FC HBA port state**

In the Multi-Initiator Zoning Model, when multiple FC HBA ports in a cluster are configured in the same FC zone, if one initiator port state is flapping, then all other initiators in the zone receive frequent Registered State Change Notifications (RSCN). An issue in the lpfc driver when processing such frequent RSCNs related to another initiator might cause the ESX host to fail with a purple diagnostics screen with an error such as:

@BlueScreen: #PF Exception 14 in world XXXXXXX:lpfc\_do\_work IP 0xXXXXXXXXXXXX addr 0xXXXXXXXXXXXX.

You see the functions lpfc\_sli4\_els\_xri\_aborted or lpfc\_sli4\_delete\_els\_xri\_aborted in the stack.

**Adding new disks external to the home directory of a virtual machine might fail with an error for reaching the security policy limit**

When a disk external to the home directory of a VM is added or removed, the security domain policy of the VM updates to give or revoke access to the external directory. It is possible that if an error occurs during disk load, to avoid issues if it is resolved, external directories are no longer removed from the security policy, even after a resolution. In time, the rules in the security policy might reach the max limit. As a result, adding new disks external to the home directory of a virtual machine fails and in the sandboxd.log you see errors such as:

2025-05-11T08:14:55.306Z Er(163) sandboxd[2099161]: [Originator@6876 sub=SecurityDomainsImpl] AddUpdateFileRules: Failed to add file policies to domain :X: world ID :Y:Argument list too long

The fix makes sure that once a disk load issue is resolved, external directories are removed from the security policy. If a VM is already facing the issue, either restart the VM or migrate it to another ESX host to trigger a regeneration of the security policy.

**Activation of TLS 1.3 in ClusterStore does not persist across ESX host reboots**

The agent\_settings configuration on ESX that controls whether TLS 1.3 is active on ClusterStore, which keeps the cluster-specific configuration data, reverts to the default of not active after a reboot of the ESX host.

**A slow SCSI device scan might make a thread of the lpfc driver unresponsive and cause various issues**

A slow SCSI device scan might make unresponsive a thread of the lpfc driver, which is responsible for storage target discovery, mailbox operations, and completion of Extended Link Service (ELS) requests. Such an unresponsive thread can lead to failing ELS requests interrupting the discovery of storage targets, no response from applications and mailbox timeouts causing esxcli elxmgmt commands to fail.

The fix improves the lpfc worker thread and prevents effects from slow SCSI device scan on the lpfc threads.

**The authentication service of the Distributed Key Value Store, or ClusterStore, might cause DNS traffic overload**

An issue with the authentication service of the Distributed Key Value Store, also called ClusterStore, that might keep trying to connect to a group of ESX hosts even when that ClusterStore is no longer part of that group might cause excessive network utilization and eventually overload of certain infrastructure such as DNS.

The fix implements a rate-limiter to reduce the retry frequency and network overhead.

**Passthrough or SR-IOV-capable PCIe devices might be reported as non-passthrough capable or non-SR-IOV capable after an upgrade to ESX 9.0 or later**

Due to overly strict sanity checks, after upgrading your system to ESX 9.0 or later, some PCIe devices might be reported as non-passthrough capable or SR-IOV cannot be activated.

**ClusterStore services might crashloop due to excessive memory usage and lead to network overload**

A high default setting of a parameter in the ClusterStore component might cause the service to consume more memory than necessary and reach the memory limit over time. As a result, ClusterStore services might crashloop and cause network overload as it attempts to communicate from one ESX host to another during each startup.

**If you use ESX host keys to encrypt virtual machines, the hostd service might fail**

When you use an ESX host key to encrypt a VM, if you delete the VM or change the key, the removal of the original host key might trigger an exception that can cause the hostd service to fail. As a result, the ESX host temporary disconnects from vCenter and you might not be able to manage VMs on the host if hostd does not restart after the failure.

**Port mirroring stops working after a Storage vMotion operation with virtual machines**

After you configure local SPAN (Switched Port Analyzer) mirroring and migrate mirror destination virtual machines by using Storage vMotion, the mirror destination VMs might not receive traffic on the destination host.

**ESX NVMe/TCP controllers do not recover connectivity when a target upgrades or restarts**

When performing NVMe/TCP target upgrade or restart, controllers in an ESX host might not recover connectivity after the target is online. As a result, you do not see the respective controllers from the vSphere Client. A rare race condition between the NVMe core layer and NVMe/TCP drivers causes the issue.

**ESX performance degrades with Hitachi NVMe-oF storage target**

When using the NVMe/TCP protocol, creation and deployment of virtual machines on datastores backed by a NVMe namespace on Hitachi NVMe-oF target might be slow when using the default settings.

**Virtual machines with fixed passthrough hot-plugging enabled might fail due to misallocation of interrupts**

For VMs with fixed passthrough hot-plugging enabled, after subsequent hot-adds of passthrough NVMe drives, the functionality might fail because interrupts might not be properly allocated.

**During upgrade of ToR switches, the teamPolicyUpDelay capability of the "Route based on physical NIC load" teaming policy might not work consistently**

If you set up the Route based on physical NIC load teaming policy to provide a window for ToR switches upgrade by using the teamPolicyUpDelay capability, in some cases this capability might not work. As a result, you might see a temporary network outage as the physical network is not ready.

**If a virtual machine migrates to an ESX host undergoing NSX update, the Distributed Firewall rule might be detached from that host**

During NSX update or upgrade, ESX hosts go into maintenance mode and the Distributed Resource Scheduler might trigger mass migration of VMs. As a result, vSphere vMotion with the Distributed Firewall rule might fail on some VMs and cause the DFW rule to be detached from the host.

**Excessive logs in the nsxdavim.log might cause an overload of the syslog server**

Frequent updates from hostd on an NSX distributed virtual port group, such as add, update, and delete, might cause excessive logs in the nsxdavim.log, which in some cases might lead to an overload of the syslog server.

**You do not see an option to select more than 8 GPUs for vGPU device groups**

When setting up a vGPU VM, you do not see an option to select more than 8 GPUs for vGPU device groups. For systems such as NVIDIA HGX, there could be more than 8 physical GPUs with corresponding device groups.

The fix adds the option to select 16 GPUs.

**You do not see any vGPU device groups for NVIDIA HGX H100 systems**

The vGPU device group filtering code does not ensure that each NIC which is a candidate for a NIC-to-GPU device group has the required SR-IOV virtual function active. For NVIDIA HGX H100 systems this issue can cause all vGPU device groups to be ignored.

**ESX host server firmware might not automatically make the PCIe Atomic Operations feature available to passthrough devices**

GPU workloads on a virtual machine with AMD GPU VMDirectPath I/O might fail or hang because the ESX host server firmware might not automatically activate PCIe atomic operations for AMD GPU devices.

The fix enables enables atomic ops for AMD GPUs and exposes the PCIe Atomicops Requestor Enable bit of PCIe Device control 2 register of the passthrough AMD GPU device to the Guest OS.

**During booting or when the Intel Volume Management Device (VMD) driver first loads, NVMe devices might fail in the enumeration of namespaces**

If an NVME drive has 512 namespaces, the VMD driver runs out of memory when trying to enumerate them all.

**ESX fails to boot on systems with more than 512 logical CPUs in one NUMA node**

Prior to ESX 9.0.1.0, ESX fails to boot on systems with more than 512 logical processors, or hyperthreads, in one NUMA node. Such systems are very unusual, but configuring the NUMA Nodes per Socket BIOS setting to 0 (NPS0) and deactivating the CCX as NUMA Domain on AMD system can cause all logical processors to be in a single NUMA node.

**A virtual machine with a vSGA device with Intel Flex GPU fails to boot if Distributed Resource Scheduler (DRS) is active**

If DRS is active, a virtual machine with a vSGA device with Intel Flex GPU might power on for a while but shortly powers off and cannot boot.

**ESX 9.0.1.0 includes the following Intel microcode:**

| Code Name | FMS | Plat ID | Servicing | MCU Rev | MCU Date | Brand Names |
| --- | --- | --- | --- | --- | --- | --- |
| Nehalem EP | 0x106a5 (06/1a/5) | 0x03 | baseline | 0x1d | 5/11/2018 | Intel Xeon 35xx Series; Intel Xeon 55xx Series |
| Clarkdale | 0x20652 (06/25/2) | 0x12 | baseline | 0x11 | 5/8/2018 | Intel i3/i5 Clarkdale Series; Intel Xeon 34xx Clarkdale Series |
| Arrandale | 0x20655 (06/25/5) | 0x92 | baseline | 0x7 | 4/23/2018 | Intel Core i7-620LE Processor |
| Sandy Bridge DT | 0x206a7 (06/2a/7) | 0x12 | baseline | 0x2f | 2/17/2019 | Intel Xeon E3-1100 Series; Intel Xeon E3-1200 Series; Intel i7-2655-LE Series; Intel i3-2100 Series |
| Westmere EP | 0x206c2 (06/2c/2) | 0x03 | baseline | 0x1f | 5/8/2018 | Intel Xeon 56xx Series; Intel Xeon 36xx Series |
| Sandy Bridge EP | 0x206d6 (06/2d/6) | 0x6d | baseline | 0x621 | 3/4/2020 | Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series |
| Sandy Bridge EP | 0x206d7 (06/2d/7) | 0x6d | baseline | 0x71a | 3/24/2020 | Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series |
| Nehalem EX | 0x206e6 (06/2e/6) | 0x04 | baseline | 0xd | 5/15/2018 | Intel Xeon 65xx Series; Intel Xeon 75xx Series |
| Westmere EX | 0x206f2 (06/2f/2) | 0x05 | baseline | 0x3b | 5/16/2018 | Intel Xeon E7-8800 Series; Intel Xeon E7-4800 Series; Intel Xeon E7-2800 Series |
| Ivy Bridge DT | 0x306a9 (06/3a/9) | 0x12 | baseline | 0x21 | 2/13/2019 | Intel i3-3200 Series; Intel i7-3500-LE/UE; Intel i7-3600-QE; Intel Xeon E3-1200-v2 Series; Intel Xeon E3-1100-C-v2 Series; Intel Pentium B925C |
| Haswell DT | 0x306c3 (06/3c/3) | 0x32 | baseline | 0x28 | 11/12/2019 | Intel Xeon E3-1200-v3 Series; Intel i7-4700-EQ Series; Intel i5-4500-TE Series; Intel i3-4300 Series |
| Ivy Bridge EP | 0x306e4 (06/3e/4) | 0xed | baseline | 0x42e | 3/14/2019 | Intel Xeon E5-4600-v2 Series; Intel Xeon E5-2600-v2 Series; Intel Xeon E5-2400-v2 Series; Intel Xeon E5-1600-v2 Series; Intel Xeon E5-1400-v2 Series |
| Ivy Bridge EX | 0x306e7 (06/3e/7) | 0xed | baseline | 0x715 | 3/14/2019 | Intel Xeon E7-8800/4800/2800-v2 Series |
| Haswell EP | 0x306f2 (06/3f/2) | 0x6f | baseline | 0x49 | 8/11/2021 | Intel Xeon E5-4600-v3 Series; Intel Xeon E5-2600-v3 Series; Intel Xeon E5-2400-v3 Series; Intel Xeon E5-1600-v3 Series; Intel Xeon E5-1400-v3 Series |
| Haswell EX | 0x306f4 (06/3f/4) | 0x80 | baseline | 0x1a | 5/24/2021 | Intel Xeon E7-8800/4800-v3 Series |
| Broadwell H | 0x40671 (06/47/1) | 0x22 | baseline | 0x22 | 11/12/2019 | Intel Core i7-5700EQ; Intel Xeon E3-1200-v4 Series |
| Avoton | 0x406d8 (06/4d/8) | 0x01 | baseline | 0x12d | 9/16/2019 | Intel Atom C2300 Series; Intel Atom C2500 Series; Intel Atom C2700 Series |
| Broadwell EP/EX | 0x406f1 (06/4f/1) | 0xef | baseline | 0xb000040 | 5/19/2021 | Intel Xeon E7-8800/4800-v4 Series; Intel Xeon E5-4600-v4 Series; Intel Xeon E5-2600-v4 Series; Intel Xeon E5-1600-v4 Series |
| Skylake SP | 0x50654 (06/55/4) | 0xb7 | baseline | 0x2007006 | 3/6/2023 | Intel Xeon Platinum 8100 Series; Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series; Intel Xeon D-2100 Series; Intel Xeon D-1600 Series; Intel Xeon W-3100 Series; Intel Xeon W-2100 Series |
| Cascade Lake B-0 | 0x50656 (06/55/6) | 0xbf | baseline | 0x4003901 | 12/12/2024 | Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200 |
| Cascade Lake | 0x50657 (06/55/7) | 0xbf | baseline | 0x5003901 | 12/12/2024 | Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200 |
| Cooper Lake | 0x5065b (06/55/b) | 0xbf | baseline | 0x7002b01 | 12/12/2024 | Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 |
| Broadwell DE | 0x50662 (06/56/2) | 0x10 | baseline | 0x1c | 6/17/2019 | Intel Xeon D-1500 Series |
| Broadwell DE | 0x50663 (06/56/3) | 0x10 | baseline | 0x700001c | 6/12/2021 | Intel Xeon D-1500 Series |
| Broadwell DE | 0x50664 (06/56/4) | 0x10 | baseline | 0xf00001a | 6/12/2021 | Intel Xeon D-1500 Series |
| Broadwell NS | 0x50665 (06/56/5) | 0x10 | baseline | 0xe000015 | 8/3/2023 | Intel Xeon D-1600 Series |
| Skylake H/S | 0x506e3 (06/5e/3) | 0x36 | baseline | 0xf0 | 11/12/2021 | Intel Xeon E3-1500-v5 Series; Intel Xeon E3-1200-v5 Series |
| Denverton | 0x506f1 (06/5f/1) | 0x01 | baseline | 0x3e | 10/5/2023 | Intel Atom C3000 Series |
| Ice Lake SP | 0x606a6 (06/6a/6) | 0x87 | baseline | 0xd000404 | 1/7/2025 | Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 Series; Intel Xeon Silver 4300 Series |
| Ice Lake D | 0x606c1 (06/6c/1) | 0x10 | baseline | 0x10002d0 | 1/7/2025 | Intel Xeon D-2700 Series; Intel Xeon D-1700 Series |
| Snow Ridge | 0x80665 (06/86/5) | 0x01 | baseline | 0x4c000026 | 2/28/2024 | Intel Atom P5000 Series |
| Snow Ridge | 0x80667 (06/86/7) | 0x01 | baseline | 0x4c000026 | 2/28/2024 | Intel Atom P5000 Series |
| Tiger Lake U | 0x806c1 (06/8c/1) | 0x80 | baseline | 0xbc | 12/1/2024 | Intel Core i3/i5/i7-1100 Series |
| Tiger Lake U Refresh | 0x806c2 (06/8c/2) | 0xc2 | baseline | 0x3c | 12/1/2024 | Intel Core i3/i5/i7-1100 Series |
| Tiger Lake H | 0x806d1 (06/8d/1) | 0xc2 | baseline | 0x56 | 12/11/2024 | Intel Xeon W-11000E Series |
| Sapphire Rapids SP HBM | 0x806f8 (06/8f/8) | 0x10 | baseline | 0x2c0003e0 | 7/30/2024 | Intel Xeon Max 9400 Series |
| Sapphire Rapids SP | 0x806f8 (06/8f/8) | 0x87 | baseline | 0x2b000639 | 1/28/2025 | Intel Xeon Platinum 8400 Series; Intel Xeon Gold 6400/5400 Series; Intel Xeon Silver 4400 Series; Intel Xeon Bronze 3400 Series |
| Kaby Lake H/S/X | 0x906e9 (06/9e/9) | 0x2a | baseline | 0xf8 | 9/28/2023 | Intel Xeon E3-1200-v6 Series; Intel Xeon E3-1500-v6 Series |
| Coffee Lake | 0x906ea (06/9e/a) | 0x22 | baseline | 0xfa | 7/28/2024 | Intel Xeon E-2100 Series; Intel Xeon E-2200 Series (4 or 6 core) |
| Coffee Lake | 0x906eb (06/9e/b) | 0x02 | baseline | 0xf6 | 2/1/2024 | Intel Xeon E-2100 Series |
| Coffee Lake | 0x906ec (06/9e/c) | 0x22 | baseline | 0xf8 | 2/1/2024 | Intel Xeon E-2100 Series |
| Coffee Lake Refresh | 0x906ed (06/9e/d) | 0x22 | baseline | 0x104 | 11/14/2024 | Intel Xeon E-2200 Series (8 core) |
| Rocket Lake S | 0xa0671 (06/a7/1) | 0x02 | baseline | 0x64 | 12/1/2024 | Intel Xeon E-2300 Series |
| Granite Rapids SP R1S | 0xa06d1 (06/ad/1) | 0x20 | baseline | 0xa0000d1 | 2/7/2025 | Intel Xeon 6500P/6700P/6900P Series |
| Granite Rapids AP/SP | 0xa06d1 (06/ad/1) | 0x95 | baseline | 0x10003a2 | 2/7/2025 | Intel Xeon 6500P/6700P/6900P Series |
| Sierra Forest | 0xa06f3 (06/af/3) | 0x01 | baseline | 0x3000341 | 2/10/2025 | Intel Xeon 6700E/6900E Series |
| Raptor Lake E/HX/S | 0xb0671 (06/b7/1) | 0x32 | baseline | 0x12e | 1/15/2025 | Intel Xeon E-2400 Series |
| Raptor Lake E/HX/S | 0xb0674 (06/b7/4) | 0x32 | baseline | 0x12e | 1/15/2025 | Intel Xeon E-2400 Series |
| Emerald Rapids SP | 0xc06f2 (06/cf/2) | 0x87 | baseline | 0x210002a9 | 3/14/2025 | Intel Xeon 8500 Series; Intel Xeon Gold 6500/5500 Series; Intel Xeon Silver 4500 Series; Intel Xeon Bronze 3500 Series |

**Booting virtual machines with vGPU on an NVIDIA Blackwell GPU fails**

vGPU VMs that reference a physical NVIDIA Blackwell GPU cannot power on because the vmx process fails.

**ESX 9.0.1.0 includes the following AMD microcode:**

ESX builds provide microcode for most supported CPUs, and if the BIOS of your server has an older microcode version than the one provided with the ESX build, ESX attempts to load the newer version. Because of an AMD change in [microcode signing](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7033.html), ESX might not be able to apply the latest microcode. In such a case, ESX 9.0.1.0 applies the newest microcode that it can and if the version is not the latest, ESX issues a SysAlert such as This machine's BIOS should be updated to pick up the latest microcode. Updating to the latest BIOS is always best practice as usually the latest BIOS also carries the latest microcode.

| Code Name | FMS | MCU Rev | MCU Date | Brand Names |
| --- | --- | --- | --- | --- |
| Bulldozer | 0x00600f12 (15/01/2) | 0x0600063e | 2/7/2018 | Opteron 6200/4200/3200 Series |
| Piledriver | 0x00600f20 (15/02/0) | 0x06000852 | 2/6/2018 | Opteron 6300/4300/3300 Series |
| Zen-Naples | 0x00800f12 (17/01/2) | 0x08001278 | 11/11/2024 | EPYC 7001 Series |
| Zen2-Rome | 0x00830f10 (17/31/0) | 0x0830107c | 12/18/2023 | EPYC 7002/7Fx2/7Hx2 Series |
| Zen3-Milan | 0x00a00f11 (19/01/1) | 0x0a0011db | 11/11/2024 | EPYC 7003 Series |
| Zen3-Milan (old BIOS) | 0x00a00f11 (19/01/1) | 0x0a0011d5 | 2/23/2024 | EPYC 7003 Series |
| Zen3-Milan-X | 0x00a00f12 (19/01/2) | 0x0a001244 | 11/11/2024 | EPYC 7003X Series |
| Zen3-Milan-X (old BIOS) | 0x00a00f12 (19/01/2) | 0x0a001238 | 2/26/2024 | EPYC 7003X Series |
| Zen4-Genoa | 0x00a10f11 (19/11/1) | 0x0a101154 | 11/12/2024 | EPYC 9004 Series |
| Zen4-Genoa (old BIOS) | 0x00a10f11 (19/11/1) | 0x0a101148 | 2/23/2024 | EPYC 9004 Series |
| Zen4-Genoa-X | 0x00a10f12 (19/11/2) | 0x0a10124f | 11/12/2024 | EPYC 9004X Series |
| Zen4-Genoa-X (old BIOS) | 0x00a10f12 (19/11/2) | 0x0a101248 | 2/26/2024 | EPYC 9004X Series |
| Zen4-Bergamo/Siena | 0x00aa0f02 (19/a0/2) | 0x0aa00219 | 11/13/2024 | EPYC 8004/9004 Series |
| Zen4-Bergamo/Siena (old BIOS) | 0x00aa0f02 (19/a0/2) | 0x0aa00215 | 2/28/2024 | EPYC 8004/9004 Series |