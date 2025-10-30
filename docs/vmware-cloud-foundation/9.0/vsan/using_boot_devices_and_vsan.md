---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/using-boot-devices-and-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using Boot Devices and vSAN
---

# Using Boot Devices and vSAN

Starting an ESX installation that is a part of a vSAN cluster from a flash device imposes certain restrictions.

When you boot a vSAN host from a USB/SD device, you must use a high-quality USB or SD flash drive of 4 GbE or larger.

When you boot a vSAN host from a SATADOM device, you must use single-level cell (SLC) device. The size of the boot device must be at least 16 GbE.

During installation, the ESX installer creates a coredump partition on the boot device. The default size of the coredump partition satisfies most installation requirements.

- If the memory of the ESX host has 512 GB of memory or less, you can boot the host from a USB, SD, or SATADOM device.
- If the memory of the ESX host has more than 512 GB, consider the following guidelines.

  - You can boot the host from a SATADOM or disk device with a size of at least 16 GbE. When you use a SATADOM device, use a single-level cell (SLC) device.
  - If you are using vSAN, you must resize the coredump partition on ESX hosts to boot from USB/SD devices.

Hosts that boot from a disk have a local VMFS. If you have a disk with VMFS that runs virtual machines, you must separate the disk for an ESX boot that is not for vSAN. In this case you need separate controllers.

## Log Information and Boot Devices in vSAN

When you boot ESX from a USB or SD device, log information and stack traces are lost on host reboot. They are lost because the scratch partition is on a RAM drive. Use persistent storage for logs, stack traces, and memory dumps.

Do not store log information on the vSAN datastore. This configuration is not supported because a failure in the vSAN cluster could impact the accessibility of log information.

Consider the following options for persistent log storage:

- Use a storage device that is not used for vSAN and is formatted with VMFS or NFS.
- Configure the ESX Dump Collector and vSphere Syslog Collector on the host to send memory dumps and system logs to vCenter.