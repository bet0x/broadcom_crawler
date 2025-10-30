---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster/hardware-requirements-for-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >  Hardware Requirements for vSAN
---

# Hardware Requirements for vSAN

Verify that your ESX hosts and storage devices meet the vSAN hardware requirements.

## Storage Device Requirements

All capacity devices, drivers, and firmware versions in your vSAN configuration must be certified and listed in the vSAN section of the Broadcom Compatability Guide available at: <https://compatibilityguide.broadcom.com/>.

vSAN OSA storage device requirements



| Storage Component | Requirements |
| --- | --- |
| Cache | - One SAS or SATA solid-state disk (SSD) or PCIe flash device. - Before calculating the Failures to tolerate, check the size of the flash caching device in each disk group. For hybrid cluster, it must provide at least 10 percent of the anticipated storage consumed on the capacity devices, not including replicas such as mirrors. - vSphere Flash Read Cache must not use any of the flash devices reserved for vSAN cache. - The cache flash devices must not be formatted with VMFS or another file system. |
| Capacity | - Hybrid group configuration must have at least one SAS or NL-SAS magnetic disk. - All-flash disk group configuration must have at least one SAS, or SATA solid-state disk (SSD), or PCIe flash device. |
| Storage controllers | One SAS or SATA host bus adapter (HBA), or a RAID controller that is in passthrough mode or RAID 0 mode. To avoid issues, consider these points when the same storage controller is backing both vSAN and non-vSAN disks:  Do not mix the controller mode for vSAN and non-vSAN disks to avoid handling the disks inconsistently, which can negatively impact vSAN operation. If the vSAN disks are in RAID mode, the non-vSAN disks must also be in RAID mode.  When you use non-vSAN disks for VMFS, use the VMFS datastore only for scratch, logging, and core dumps.  Do not run virtual machines from a disk or RAID group that shares its controller with vSAN disks or RAID groups.  Do not passthrough non-vSAN disks to virtual machine guests as Raw Device Mappings (RDMs).  To learn about controller supported features, such as passthrough and RAID, refer to the Broadcom Compatibility Guide. |

vSAN ESA storage device requirements



| Storage Component | Requirements |
| --- | --- |
| Cache and capacity | Each storage pool must have at least one NVMe TLC devices. |

## Host Memory

The memory requirements for vSAN OSA depend on the number of disk groups and devices that the ESX hypervisor must manage. For more information, see [vSAN Sizer tool](https://vcf.broadcom.com/tools/vsansizer/).

vSAN ESA requires at least 128 GB host memory. The memory needed for your environment depends on the number of devices in the host's storage pool. For more information on the guidelines to use with vSAN ESA, see [vSAN ESA ReadyNode Hardware Guidance](https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php).

## Flash Boot Devices

During installation, the ESX installer creates a coredump partition on the boot device. The default size of the coredump partition satisfies most installation requirements.

- If the memory of the ESX host has 512 GB of memory or less, you can boot the host from a USB, SD, or SATADOM device. When you boot a vSAN host from a USB device or SD card, the size of the boot device must be at least 32 GB.
- If the memory of the ESX host has more than 512 GB, consider the following guidelines.

  - You can boot the host from a SATADOM or disk device with a size of at least 16 GB. When you use a SATADOM device, use a single-level cell (SLC) device.
  - If you are using vSAN, you must resize the coredump partition on ESX hosts to boot from USB/SD devices.

When you boot an ESX host from USB device or from SD card, vSAN trace logs are written to RAMDisk. These logs are automatically offloaded to persistent media during shutdown or system crash (panic). This is the only support method for handling vSAN traces when booting an ESX from a USB stick or SD card. If a power failure occurs, vSAN trace logs are not preserved.

When you boot an ESX host from a SATADOM device, vSAN trace logs are written directly to the SATADOM device. Therefore it is important that the SATADOM device meets the specifications outlined in this guide. For more information, see [ESX Hardware Requirements](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/esx-installation-and-setup/installing-and-setting-up-esxi/esxi-requirements/esxi-hardware-requirements.html).