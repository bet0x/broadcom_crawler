---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > vSphere
---

# vSphere

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html#GUID-9bfea8cc-6a54-448f-874f-f8e4f5bbe4ac-en_id-7b7221e7-0896-446d-a1af-3d25e1cb92f0)
- [Compatibility](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html#GUID-9bfea8cc-6a54-448f-874f-f8e4f5bbe4ac-en_id-3beb75ff-6b11-4746-87b9-0170a0c1664e)
- [Install and Upgrade Notes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html#GUID-9bfea8cc-6a54-448f-874f-f8e4f5bbe4ac-en_id-19060fcf-71fd-4f7c-9ec4-16ae1d5861d5)
- [Security](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html#GUID-9bfea8cc-6a54-448f-874f-f8e4f5bbe4ac-en_id-bfe00dc7-f1a4-4cfe-a21d-280fe59b2b98)
- [ESX New Features:](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html#GUID-9bfea8cc-6a54-448f-874f-f8e4f5bbe4ac-en_id-04c8dc53-9df2-4702-92be-0b318a8531d6)
- [vCenter New Features:](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html#GUID-9bfea8cc-6a54-448f-874f-f8e4f5bbe4ac-en_id-3f50831a-d9c4-48ec-b395-de68777a654f)

## Introduction

|  |
| --- |
| VMware Cloud Foundation 9.0 | 17 JUN 2025 | Build 24755599  ESX 9.0| 17 JUN 2025 | Build 24755229  vCenter 9.0| 17 JUN 2025 | Build 24755230  Check for additions and updates to these release notes. |

## Compatibility

This product incorporates open source software. For applicable license and copyright information, please refer to the Broadcom [Customer Support Portal](https://support.broadcom.com/).

**Virtual Machine Compatibility for ESX**

Virtual machines that are compatible with ESX 4.x and later (hardware version 7) are supported with ESX 9.0. Virtual machines that are compatible with ESX 3.x and later (hardware version 4) are not supported. To use such virtual machines on ESX 9.0, upgrade the virtual machine compatibility. See the [ESX Upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-upgrade.html) documentation.

**Guest Operating System Compatibility for ESX**

To determine which guest operating systems are compatible with vSphere 9.0, use the ESX 9.0 information in the [Broadcom Compatibility Guide.](https://compatibilityguide.broadcom.com/)

The following guest operating system releases are deprecated or terminated in this release. Future releases will not support these guest operating systems:

- Windows Server 2000, 2003 / R2, 2008, Windows XP, Windows Vista : Deprecated
- Oracle Linux 5.x: Deprecated
- Oracle Linux 4.9: Terminated
- RedHat: RHEL 4, RHEL 5: Deprecated
- CentOS 6.x, 7.x and 8.x: Deprecated
- Asianux 3.0: Deprecated
- SUSE Linux Enterprise Server 10 SP4 and 11.x : Deprecated
- SUSE Linux Enterprise Desktop 12: Deprecated
- Ubuntu releases 22.10: Deprecated
- Debian 7.x and 8.x: Deprecated
- Photon OS 3.0: Deprecated
- Flatcar Container Linux non-LTS releases: Terminated
- All OS X and macOS releases: Terminated
- FreeBSD 9.x, 10.x and 11.x: Deprecated
- Solaris 10.x and 11.x : Deprecated
- All eComStation releases: Terminated
- All SCO releases: Terminated
- All CoreOS releases: Terminated

**Device Compatibility for ESX**

To determine which devices are compatible with ESX 9.0, use the ESX 9.0 information in the [Broadcom Compatibility Guide.](https://compatibilityguide.broadcom.com/)

**Hardware Compatibility for ESX**

To view a list of processors, storage devices, SAN arrays, and I/O devices that are compatible with vSphere 9.0, use the ESX 9.0 information in the [Broadcom Compatibility Guide.](https://compatibilityguide.broadcom.com/)

**ESX and vCenter Version Compatibility**

The [Broadcom Product Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability) provides details about the compatibility of current and earlier versions of vSphere components, including ESX, vCenter, and optional products. Check the [Broadcom Product Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability) also for information about supported management and backup agents before you install ESX or vCenter. The vSphere Lifecycle Manager and vSphere Client are packaged with vCenter.

**Before You Begin**

vSphere 9.0 requires a minimum of 16 cores per CPU even if a CPU has fewer than 16 cores. If a CPU has more than 16 cores, additional CPU licenses are required as announced in [Update to VMware’s per-CPU Pricing Model](https://news.vmware.com/company/cpu-pricing-model-update-feb-2020). Prior to upgrading ESX hosts, you can determine the number of licenses required using the license counting tool described in [Counting CPU licenses needed under new VMware licensing policy.](https://kb.vmware.com/s/article/77098)

To determine which guest operating systems are compatible with ESX 9.0, use the ESX 9.0 information in the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).

## Install and Upgrade Notes

**Unified VCF Versioning:**

The VCF unified versioning removes any user-facing labels such as Update 2a or U3b that were used for vCenter and ESX releases.

Versioning for ISO and depot bundles in ESX 9.x have the following format:

- VMware-VMvisor-Installer-<x.y.z.a.bld>.x86\_64.iso
- VMware-ESX-<x.y.z.a.bld>-depot.zip where:

  - x = GA version
  - y = Update version equivalent
  - z = Patch with a refresh of the VCF Bill of Materials, regular maintenance release
  - a = Patch without a refresh of the VCF Bill of Materials, patch release

**Increased minimum boot-bank size for ESX to 1 GB:**

With ESX 9.0, the minimum boot-bank size for ESX is up from 500 MB to 1 GB. ESX 9.0 boot-banks are provisioned at 1GB or 4GB to accommodate essential system software. Environments upgraded from previous versions with a 500 MB boot-bank automatically migrate to the new 1 GB or 4 GB boot-bank during the installation process. A minimum of 32 GB of system disk space is required for proper operation. For more information, see [ESX System Storage Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_009&appid=vsphere-9-0&language=&format=rendered).

**Reduced downtime upgrade is integrated with vCenter High Availability (HA) deployment:**

The reduced downtime upgrade is integrated with the vCenter HA automatic and manual configuration deployment, including self-managed vCenter and non-self-managed vCenter. You can use the vSphere Client or API to perform a reduced downtime upgrade in a HA environment. For more information, see [Reduced Downtime Upgrade in High Availability Environments](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_015&appid=vsphere-9-0&language=&format=rendered).

**RDU with CLI support**

You can use the CLI installer to perform the reduced downtime upgrade of a vCenter appliance. The CLI upgrade process includes downloading the vCenter appliance installer to the network virtual machine or physical server from which you want to perform the upgrade, preparing a JSON configuration file with the upgrade information, and running the upgrade command. For more information, see [Reduced Downtime CLI Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_014&appid=vsphere-9-0&language=&format=rendered).

**For vCenter patches, Update Type and Release Type fields replace Priority and Severity:**

When patching vCenter, you no longer see the Priority and Severity fields but the Update Type and Release Type fields. The Update Type field indicates the type of the update, including: bug fix, security, bug fix and security, enhancement, and informational. The Release Type values are update or patch. For more information, see [Install vCenter Patches.](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_016&appid=vsphere-9-0&language=&format=rendered)

## Security

**GNU C Library update to v2.34:**

In ESX 9.0, the GNU C Library, commonly known as glibc, is updated to version 2.34 to meet product support timeframe.

**Script Sandboxing:**

With ESX 9.0, you can define and package sandboxes for Python and shell scripts on application level, such as the VMkernel Access Control Subsystem, not on domain level, such as superDom. For more information, see Host Extensions Development Kit (HEXDK) Release Notes, Daemon Software Development Kit (DSDK) 9.0 Release Notes, and VMware vSphere APIs for I/O Filtering Development Kit (VAIODK).

**Support for AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP):**

ESX 9.0 enhances memory integrity protection by adding support for SEV-SNP for VMs, which prevents malicious hypervisor-based modifications.

**Support for Intel Trusted Domain Extensions (TDX):**

ESX 9.0 supports TDX for initial intercept mode that guarantees encryption and attestation, and also protects virtual machines from disclosure or modification.

**NVMe-oF Auth Support:**

ESX 9.0 adds support for the discovery of unique NVMe Qualified Names (NQN) and the Non-Volatile Memory Express (NVMe) TP 8006, which is in-band authentication for NVMe over Fabrics (NVMe-oF). This new implementation enables enhanced security for ESX environments by supporting Diffie-Hellman HMAC Challenge-Handshake Authentication Protocol (DH-HMAC CHAP) for authentication during NVMe communications. For more information, see [NVMe over Fabrics Authentication](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_022&appid=vsphere-9-0&language=&format=rendered).

**Support for managing UEFI Secure Boot and execInstalledOnly enforcement using vSphere Configuration Profiles:**

With ESX 9.0, by using vSphere Configuration Profiles you can activate and deactivate UEFI Secure Boot enforcement and execInstalledOnly enforcement for a secure ESX configuration. For more information, see [Configuration Profiles.](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_843&appid=vsphere-9-0&language=&format=rendered)

**Support for wrapped key mode for VM encryption:**

You can use wrapped key mode for VM encryption, which conserves Key Management Server (KMS) resources by allowing a single raw key to encrypt multiple wrapped keys and by using the wrapped keys for VM encryption. Read more [here](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_023&appid=vsphere-9-0&language=&format=rendered).

**Virtual Trusted Platform Module (vTPM) supports Trusted Platform Module (TPM) Library Specification Family 2.0 Revision 1.59:**

ESX 9.0 supports TPM 2.0 library specification Revision 1.59 thus enhancing your cyber security protection in the cases when you add a vTPM device to a VM with hardware version 22.

**TLS 1.3 support for port 443 and TLS 1.3-specific NIST\_2024 profile:**

ESX 9.0 introduces a NIST\_2024\_TLS\_13\_ONLY profile to guarantee that the mapping of TLS 1.3 parameters satisfies the NIST 2024 standard across ESX releases and the reverse proxy on port 443 is FIPS-certified for TLS 1.3. If in earlier ESX versions you have configured manual overrides to allow non-FIPS TLS 1.3 on port 443, revert such changes by following the steps in KB [312033](https://knowledge.broadcom.com/external/article/312033). For more information, see [vSphere TLS Configuration](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_024&appid=vsphere-9-0&language=&format=rendered).

**Running custom-signed operating systems or drivers with active Secure Boot:**

ESX 9.0 allows you to run custom-signed operating systems or drivers while keeping Secure Boot enabled. For more information on how to use custom certificates, see KB [377306](https://knowledge.broadcom.com/external/article/377306).

## ESX New Features:

## Licensing

To license your vCenter instance, assign either the VCF or vSphere Foundation license to your vCenter from VCF Operations. All components, including the vCenter instance, that are connected to that vCenter instance become licensed automatically. Until the vCenter is licensed, it can be used for up to 90 days in evaluation mode.

## CPU

**Support Intel Hardware Performance States (HWP) on Sapphire Rapids and later CPUs:**

Starting with ESX 9.0, and starting with Intel Sapphire Rapids processors, the ESX default is to enable HWP, which allows an operating system to offload the P-states management to the BIOS, rather than manage the P-states in software. You must configure the BIOS to provide HWP functionality and make this option available to the operating system. If HWP is not enabled in the BIOS and the OS is allowed to manage P-states, the ESX power management code continues to manage P-states, including for Intel processor versions earlier than Sapphire Rapids.

**Support for 5th generation AMD EPYC processors:**

ESX 9.0 adds support for 5th generation AMD EPYC processors, formerly codenamed Turin.

**Support for Intel Granite Rapids Series processors:**

ESX 9.0 CPU scheduler adds support for Intel Granite Rapids Series processors designed for high-performance computing applications.

## Accelerators

**Memory Tiering:**

ESX 9.0 officially launches the Memory Tiering capability, which enables you to add NVMe devices locally to an ESX host as tiered memory. Memory tiering over NVMe optimizes memory utilization by allocating and moving VM memory pages between faster dynamic random access memory (DRAM) and NVMe devices on the host. This allows you to improve the host CPU utilization by increasing memory footprint and workload capacity, while reducing the total cost of ownership. For more information, see [Memory Tiering over NVMe](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_011&appid=vsphere-9-0&language=&format=rendered).

**Device Selection Policies for Enhanced vGPU Devices:**

With ESX 9.0, you can use the vSphere Client to configure device selection policies, which gives you greater control over how vGPU devices are allocated in the graphic policies. You can choose a performance-focused policy, which evenly distributes Virtual Functions (VFs) across physical devices, or a consolidation-focused policy, which packs VFs onto fewer devices to provide more flexibility. This feature helps optimize hardware utilization based on your specific workload and operational goals.

**Automated Device Reconfiguration for Enhanced DirectPath I/O:**

ESX 9.0 introduces support for the automatic reconfiguration of Enhanced DirectPath I/O devices with multiple profiles or capabilities, such as GPUs or crypto/compression accelerators. This eliminates the need for system administrators to manually configure such devices to the desired profile or capability. Reconfiguration is performed transparently, when needed, during VM power-on or migration, based on the VM requirements and attributes.

**vSphere vMotion Optimizations for vGPU Workloads:**

ESX 9.0 enables vSphere vMotion optimizations for vGPU devices that utilizes IOMMU Dirty Bit technology from Intel and AMD CPUs. This optimization reduces vGPU VM down time.

**Enhanced DirectPath I/O support for non-checkpointable devices:**

ESX 9.0 extends Enhanced DirectPath I/O functionality to virtual machines with non-checkpointable devices. For VMs with Enhanced DirectPath I/O, you can hot-add memory, vCPUs, virtual devices (NICs), activate VM debugging or statistics capabilities, and use Storage vMotion. Examples of devices that benefit from this feature include Intel's Dynamic Load Balancer (DLB) and the AMD MI200 GPU.

**Virtual IOMMU Support for Enhanced DirectPath I/O:**

ESX 9.0 adds support for Virtual Input-Output Memory Management Units (vIOMMU) for VMs using Enhanced DirectPath I/O, increasing the security of guest OS applications.

## Guest Platform for Workloads

**The following guest operating system releases are new for ESX 9.0:**

- Pardus
- Red Hat Core OS
- Miracle Linux
- ProLinux
- Kylin Linux
- FusionOS
- RHEL 10
- Oracle Linux 10
- Debian 13
- FreeBSD 15

**Virtual Hardware Version 22:**

vCenter 9.0 introduces virtual hardware version 22 to to ensure support for the latest guest operating system versions and increase maximums as follows:

Supported maximums:

- 960 logical processors
- 960 cores per socket

  For more information, see [Hardware Features Available with Virtual Machine Compatibility Settings](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_012&appid=vsphere-9-0&language=&format=rendered).

New Supported Operating Systems:

- ProLinux
- FusionOS
- Kylin
- Miracle Linux

Enablements:

- Peer-to-Peer for all Passthrough Devices
- NVMe 1.4
- Intel Trust Domain Extensions (TDX)
- Next Generation of AMD Secure Encrypted Virtualization SEV-SNP (Secure Nested Paging)
- New Instruction Set (ISA) support introduced in Intel Granite Rapids and AMD 5th generation EPYC processors, formerly codenamed Turin.
- Support for 4KN VMDK and 4KN Local Drives
- Virtual I/O MMU for Enhanced DirectPath I/O
- Real-Time Virtual Switch

**Span Limit Policy:**

The Span Limit policy allows you to establish the affinity relationship between a group of virtual machines and a specified number of hosts without explicitly identifying the hosts. For more information, see [Using Span Limit Policy.](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_013&appid=vsphere-9-0&language=&format=rendered)

## Drivers

**Supported drive configuration for Broadcom 9700 series RAID Controller Cards and Enhanced Host Bus Adapters (eHBA):**

- RAID: SAS SSD, NVMe SSD
- eHBA: SAS HDD, SAS SSD, SATA HDD, SATA SSD

**Zero memory reservation for drivers:**

To reduce memory overhead, with ESX 9.0, the initial memory reservation of drivers is reduced to zero, except for drivers where zero reservation is not feasible or applicable.

**ESX 9.0 adds the following driver updates:**

**Drivers updated with new features and bugs fixed:**

- Broadcom: bcm\_mpi3
- Broadcom: lsi\_msgpt35
- Broadcom: lsi\_mr3
- Broadcom: lpfc
- Cisco: nfnic
- Cisco: nenic-ens
- Intel: i40en
- Intel: iavmd
- Marvell: qlnativefc
- Mellanox: nmlx5
- Microchip: smartpqi
- Pensando: ionic\_en
- VMware: vmxnet3\_ens

**Broadcom Driver Updates:**

- **Broadcom bcm\_mpi3 driver:** Adds support for SSDs in 4K native mode.

**Cisco Driver Updates:**

- **Cisco nenic\_ens driver:** Inbox support for Enhanced Data Path (EDP).

**Intel Driver Updates:**

- **Intel icen driver:** Adds support for NetQ RSS for Enhanced Data Path.

**Nvidia Mellanox Updates**

- **Mellanox nmlx5 driver:** 400G support, scale and performance optimizations, NSX Tunnel End Point (TEP) support, NSX in-place upgrade, VXLAN UDP ports for TX/RX.

**VMware Driver Updates**

- **VMware vmxnet3\_ens (Native vmxnet3 ENS) driver:** Upgrades the vmxnet3 virtual hardware standard from version 3 to 6, providing capabilities for offload to Generic Network Virtualization Encapsulation (Geneve), VXLAN offload, RSS, and LRO.

**Routine driver updates and bug fixes:**

- Broadcom lsi\_mr3 driver
- Broadcom lsi\_msgpt35 driver
- Cisco nfnic driver
- Intel i40en driver
- Intel iavmd driver
- Marvell qlnativefc driver
- Microchip smartpqi driver
- Pensando ionic\_en driver

**Support for Communication Device Class Network Control Model (CDC-NCM) in the ESX USB driver:**

The ESX USB driver supports the CDC-NCM protocol for compatibility with HPE Gen12 iLO Virtual NIC and interoperability with HPE Agentless Management (AMS), Integrated Smart Update Tools (iSUT), the iLORest config tool, Intelligent Provisioning, and DPUs.

**Support for Windows Display Driver Model (WDDM) 2.0:**

ESX 9.0 adds support for WDDM 2.0 on Windows guest OS.

## Storage

**Boot over NVMe/FC SAN:**

ESX 9.0 adds support for booting over with the latest implementation of NVMe/Fibre Channel (FC). This feature enables seamless boot operations from remote NVMe storage over FC networks, providing enhanced flexibility and performance for environments that rely on SAN-based storage. For more information, see [Booting ESX from NVMe Storage](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_021&appid=vsphere-9-0&language=&format=rendered).

**Boot over NVMe/TCP SAN:**

ESX 9.0 supports device specification TP-8012 for NVMe/TCP. This new implementation enables support for boot from NVMe/TCP storage, offering more flexibility for booting over a SAN, and providing new opportunities to leverage remote NVMe/TCP storage in your environment, making it easier to deploy and manage your storage solutions. For more information, see [Booting ESX from NVMe Storage](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_021&appid=vsphere-9-0&language=&format=rendered).

**Snapshot enhancements:**

ESX 9.0 enhances virtual snapshot tasks by adding more precise tracking of the progress of consolidation tasks and the ability to resume snapshot consolidation for offline VMs.

**Namespace Write Protection and Write Zeros support for virtual NVMe:**

ESX 9.0 introduces support for Namespace Write Protection (read-only disks), which allows hot-adding independent-nonpersistent disks to a VM without the need to create a delta disk. This enhancement benefits workloads that require faster application delivery.

**Support for remote boot devices with ESX-OSdata partition:**

ESX 9.0 adds support for remote boot devices that contain the ESX-OSData partition and monitoring for critical failures on such devices. Remote boot devices that contain the ESX-OSData partition must have high availability but can still fail due to critical failures such as All-Paths-Down (APD) or Permanent Device Loss (PDL). To avoid ESX corruption, if such a failure occurs and the device does not recover, ESX stops with a purple diagnostic screen and message as described in KB [380716](http://kb.vmware.com/s/article/380716).

## Networking

**NSX VIBs Included with ESX and Live Patch Support**

Virtual networking ESX kernel modules (VIBs) are included with ESX by default. This reduces the complexity and time required to install and upgrade virtual networking features. With this change, NSX VIBs on ESX Hosts now support ESX Live Patch in addition to the ESX maintenance upgrade. With Live Patch, the upgrades can happen without the need to put hosts into maintenance mode, and with no impact on vMotion or DRS operations.

## VMware Tools

**VMware Tools Bundling Changes in ESX 9.0**

The following VMware Tools ISO images are bundled with ESX 9.0:

- **windows.iso**: VMware Tools 13.0.0 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.

The following VMware Tools ISO images are available for download:

- VMware Tools 12.5.1:

  - **windows-x86.iso:** VMware Tools 12.4.6 supports 32-bit Windows versions.
  - **linux.iso**: VMware Tools 10.3.26 ISO image for Linux OS with **glibc** 2.11 or later.

- VMware Tools 11.0.6:

  - **windows.iso**: for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).

- VMware Tools 10.0.12:

  - **winPreVista.iso**: for Windows 2000, Windows XP, and Windows 2003.
  - **linuxPreGLibc25.iso**: supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with **glibc** version earlier than 2.5.
- **solaris.iso**: VMware Tools image 10.3.10 for Solaris.
- **darwin.iso**: Supports Mac OS X versions 10.11 and later.

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESX:

- [VMware Tools 13.0.0 Release Notes](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1300-release-notes.html)
- [What Every vSphere Admin Must Know About VMware Tools](https://blogs.vmware.com/vsphere/2017/11/every-vsphere-admin-must-know-vmware-tools.html)
- [VMware Tools for hosts provisioned with Auto Deploy](https://kb.vmware.com/s/article/2004018)
- [Upgrading VMware Tools](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/vmware-tools-administration-13-0-0/upgrading-vmware-tools.html)

## Configuration Management

**Unified Configuration Management**

With this release, the NSX configuration is integrated with vSphere Config Profiles (VCP), which allows for unified configuration management for ESX, VDS, and NSX at the cluster level. The ownership of NSX-specific configurations remains with NSX as part of the Transport Node Profile. But with this integration, users can manage the NSX configuration (at a cluster level) across these two solutions from one central place, allowing for ease of management and configuration compliance at a cluster level. In essence, this change provides a single-pane-of-glass solution for configuration. See [Guidelines for Upgrading NSX](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx14&appid=vcf-9-0&language=&format=rendered).

## vSphere Lifecycle Manager

**Desired Image for Mixed-Hardware Clusters:**

With VCF 9.0, vSphere Lifecycle Manager clusters can support mixed hardware images in the same desired state image. This feature allows to create cluster desired state image by adding multiple component images with different vendor add-ons or components that are applicable to a subset of hosts in the cluster.

**Additional Coverage for Security Vulnerability Live Patching:**

VCF 9.0 adds additional Live Patch coverage, which includes user-space live patching and NSX transport node live patching without ESX reboot.

**Parallel ESX Host Lifecycle Operations from vCenter and Data Center:**

You can save time with parallel ESX host lifecycle operations with multi-select vCenter clusters when applying operations such as attaching image from an image catalog, running pre-checks, staging an image, and remediating clusters and hosts from vCenter or a data center.

**VCF Image Authoring:**

With the ESX image library, you can optimize your vCenter management by creating an ESX image at vCenter level instead of creating an image for every cluster. You can use the ESX image creation workflow to author an image and save it in the ESX image library, so the same image can be used to provision ESX hosts on multiple clusters in the vCenter system. You can import such images into the VCF image catalog and use it for VCF lifecycle workflows.

## vCenter New Features:

## Licensing

To license your vCenter instance, assign either the VCF or vSphere Foundation license to your vCenter from VCF Operations. All components, including the vCenter instance, that are connected to that vCenter instance become licensed automatically. Until the vCenter is licensed, it can be used for up to 90 days in evaluation mode.

## vSphere Client

**vSphere Client enhancements:**

- Virtual infrastructure (VI) admins can move a cluster of datastores to a different folder in the inventory with a simple drag-and-drop.
- In the **Monitor > Events** grid:

  - the max number of entities displayed per page is increased from 100 to 300.
  - the queue of events is no longer limited to 1,000 or 10 pages. You can see all historic events since the deployment of the vCenter instance.
- In the **Virtual Machines** grid:

  - Adds a **Snapshots** column, displaying the number of snapshots taken for each VM to help you as a VI admin find the VMs with excessive number of snapshots. You can clean up unnecessary snapshots and free resources with scheduled automatic deletion.
  - Visual indicators for the required fields in all vSphere Client forms.

**Change the host name of ESX hosts from the vSphere Client:**

With vCenter 9.0, in the vSphere Client, when you right-click an ESX host in any workload domain, you can change the host name of the hosts by just selecting Rename, as opposed to a number of steps you had to preform in earlier releases, as described in [Changing the host name of an ESX host](https://knowledge.broadcom.com/external/article?legacyId=1010821).

## vCenter Appliance

**PhotonOS version 5.0:**

vCenter 9.0 comes with PhotonOS version 5.0 that adds the following enhancements:

- Photon 5.0 Kernel Cryptographic Module has the [FIPS 140-3 certification](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4865).
- Photon 5.0 Kernel Entropy Source has Entropy Source Validation (ESV) certificate: [VMware’s Linux Kernel CPU Time Jitter RNG Entropy Source](https://csrc.nist.gov/projects/cryptographic-module-validation-program/entropy-validations/certificate/115). The Photon 5.0 kernel entropy is a significant security advantage, because it is compliant with SP 800-90B, which NIST recommends for Random Bit Generation from the FIPS module. You can use this entropy source with other cryptographic modules.
- Photon 5.0 has a certified OpenSSL FIPS Provider 3.0.8.

For more information, see [What is New in Photon OS 5.](https://vmware.github.io/photon/docs-v5/whats-new/)

**VMware Update Manager Download Service (UMDS) becomes part of the VMware Cloud Foundation Download Tool:**

With vCenter 9.0, the VMware Update Manager Download Service (UMDS) becomes part of the VMware Cloud Foundation Download Tool, formerly known as Offline Bundle Transfer Utility (OBTU). With the combined functionality of UMDS and OBTU, you can download all binaries of VMware Cloud Foundation components. The standalone UMDS tool is deprecated and will be removed in a future vCenter release.

**The Managed Object Browser is not active by default:**

In vCenter 9.0, to comply with Security Technical Implementation Guide (STIG) requirements, the Managed Object Browser (MOB) service is not active by default. You can still use MOB, but you must explicitly activate it by changing the configuration of the vpxd service.

**Default log partition of 50 GB:**

With vCenter 9.0, the default size of the log partition is 50 GB for any vCenter deployment.

**Faster cold migration of data disks without impact on management network traffic:**

vCenter 8.0 introduced Unified Data Transport (UDT) that enhanced cold migration of data disks. UDT speeds up cold migration but might cause network saturation on the provisioning network when it is shared with the management traffic. With vCenter 9.0, Network Input/Output Control (NIOC) enables you to manage the provisioning traffic related to UDT and benefit from a much faster cold migration without any impact on critical operations over the management network. For more information, see [Network I/O Control for Provisioning Traffic](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_017&appid=vsphere-9-0&language=&format=rendered).

**vCenter Service Registry (VSR) log rotation enhancements:**

With vCenter 9.0, the central registry for services and their properties on vCenter, VSR, adds new log rotation guidelines and verification of configs to avoid failure on builds and help with handling exceptions. The enhancements also include generation of a log config from VSR, which is stored in /etc/vmware/log\_configurations/lr\_configs for log rotate and in /etc/vmware/log\_configurations/non\_lr\_configs for non-rotate mechanisms. Service-owners can read the log configs from these directories on service startup.

**Broadcom branding on the object and component icons in vCenter:**

vCenter 9.0 introduces the Broadcom branding scheme for the inventory objects and other graphically presented infrastructure components in all user interfaces, such as the vSphere Client, ESX Direct Console, VI Configuration wizard, Virtual Appliance Management Interface, VCF Installer, PowerCLI, and vCenter Converter.

**vSphere Client alarms for exceeding vCenter connections:**

To prevent a vCenter system to become unresponsive due to exceeding the connections limit, you see yellow or red alarms in the vSphere Client when utilization of connections reaches 50% or 90% respectively.

## Resource Management

**Accelerator Capacity Visualization:**

With the Accelerator Capacity Visualization capability, you can define and visualize in the vSphere Client the capacity metrics for many accelerator devices, including Nvidia vGPU Profiles, in a uniform way at a cluster and ESX host level. Along with monitoring the available capacity, the capability also monitors workloads that use such capacity and enables you to make informed decisions on the optimal use of accelerators for different workloads.

**Overhead memory for accelerator placement:**

With the Overhead memory for accelerator placement capability, you can get accurate calculations of the overhead memory required by DRS to successfully place VMs with accelerators such as GPU VMs. With this capability, you can predictably place and power-on Supervisor VM-Service VMs with accelerators in your environment, or use it as a building block for other capabilities, such as GPU Reservations.

**GPU reservations:**

Enterprises and Cloud Service Providers can use the GPU Reservations capability in the DRS and vSphere Supervisor to reserve the expensive GPU capacity before use in an Enterprise or Cloud Services Provider environment. With GPU Reservations in place, Cloud Service Providers can further reserve and sell chunks of capacity to customers and tenants, who want to deploy GPU workloads.

## Content Library

**Support for hardware accelerators in Content Library:**

vCenter 9.0 adds support for the use of hardware accelerators such as SR-IOV, assignable hardware, and vGPU with Content Library to support VMware Private AI Foundation with NVIDIA images, such as the Deep Learning VM.

**Support for deploying Content Library templates with Storage Policy and Encryption Profile:**

With vCenter 9.0, while you deploy OVF and OVA templates from a Content Library, you can select a storage policy and encryption profile, such as VM Encryption Policy by using a Native Key Provider or an external key provider.

**Support for storage migration of Content Libraries:**

Starting with vCenter 9.0, you as a VI admin can migrate the datastore of local and published content libraries to a different datastore without changing the library identifier and the item identifiers within the library, so that the subscribed libraries to the published library continue to work after the migration. You no longer need to migrate the storage backing of a published library, create a new published library, migrate the content to the new library, and re-create all the subscribed content libraries. With the same identifiers, the corresponding subscribed libraries continue to work without a re-sync after the migration. For more information, see [Migrate a Content Library to Another Datastore](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_010&appid=vsphere-9-0&language=&format=rendered).

## Networking

**NSX Edge Platform Usability**

The installation and configuration of NSX Edge Nodes and Edge Clusters have been significantly streamlined through vCenter. [This enhancement](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=nsx2&appid=vcf-9-0&language=&format=rendered) simplifies workflows, reduces complexity, and improves operational efficiency for VPC environments.

**Virtual Private Cloud (VPC) in vCenter**

VCF 9.0 introduces Virtual Private Cloud (VPC) support in vCenter, enabling administrators to create VPCs and define subnets, either private or publicly advertised, to expose VMs externally by using external IPs. This capability delivers a unified networking framework that aligns with industry standards and supports VPC consumption by vCenter, VKS NSX, and VCF Automation.Additionally, Envoy Proxy is integrated into vSphere, which enables VI admins to access VPC (NSX Policy) APIs directly by a vCenter endpoint, using the same vCenter authentication and session. This provides a consistent experience for customers consuming VPC functionality by API, similar to what is available through the vSphere Client.

**Support for VXLAN packets with different VXLAN ports:**

To enhance interoperability, vCenter 9.0 adds support for both the default VXLAN port, 4789, and the legacy VXLAN UDP port, 8472.

## vSphere vMotion

**vGPU cold data precopy:**

vMotion introduces a sequential vGPU cold data pre-copy algorithm. During vMotion, vGPU pre-copy is a first class citizen like memory pre-copy and gets its own stage. If a VM has multiple vGPUs, vMotion iterates through each vGPU and copies its cold data before starting memory pre-copy. Sequential vGPU cold data pre-copy reduces the vGPU checkpoint transferred during vMotion downtime by 65% to 80% for various GPU profiles. The new algorithm might reduce downtime by 40% to 60% during vMotion, based on multiple Llama vMotion experiments on L40S and H100 vGPU profiles. The capability is effective for Gen AI inferencing workloads but has no impact for graphics and training workloads. It is available for all types of passthrough devices such as vGPU and DVX.

**Custom Enhanced vMotion Compatibility (EVC):**

Starting with vCenter 9.0, you can create a custom EVC mode and apply it to your clusters or virtual machines. The custom EVC mode feature set is based on the highest set of features available in all selected hosts. If your vCenter instances are part of an Enhanced Linked Mode group, you can select hosts or clusters from any vCenter instance part of the Enhanced Linked Mode group. For more information, see [CPU Compatibility and vSphere Enhanced vMotion Compatibility](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_004&appid=vsphere-9-0&language=&format=rendered).

## Storage

**4K native support:**

vCenter 9.0 adds the capability for virtual machines to send a 4K I/O through the 4Kn VMDK to the backend device. This also means that the VM understands the device is 4Kn. This release enables 4Kn support for VMFS-local (SCSI, NVMe), vSAN, and NFS datastores. For more information, see [Device Sector Formats](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_018&appid=vsphere-9-0&language=&format=rendered).

**VAAI-NAS support for Unmap with NFS3:**

Starting with vCenter 9.0, the Unmap primitive enables space reclamation for VMs running on thin-provisioned NFS 3 datastores. For more information, see [vSphere Hardware Acceleration on NAS Devices](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_019&appid=vsphere-9-0&language=&format=rendered).

**NFS 4.1 support for Kerberos krb5p security model:**

With vCenter 9.0, in addition to identity verification and data integrity, krb5p provides end-to-end encryption for NFS. With krb5p, the system encrypts NFS packets before sending them over the wire. Replies are decrypted before the system processes the results. For more information, see [Using Kerberos for NFS 4.1 with ESX](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_020&appid=vsphere-9-0&language=&format=rendered).