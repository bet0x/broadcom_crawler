---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/before-you-upgrade-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Before You Upgrade vSAN
---

# Before You Upgrade vSAN

Plan and design your upgrade to be fail-safe.

Before you attempt to upgrade vSAN, verify that your environment meets the vSphere hardware and software requirements.

## Upgrade Prerequisite

Consider the aspects that might delay the overall upgrade process. For guidelines and best practices, see the [vCenter Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered) guide.

Review the key requirements before you upgrade your cluster.

Upgrade Prerequisite



| Upgrade Prerequisites | Description |
| --- | --- |
| Software, hardware, drivers, firmware, and storage I/O controllers | Verify that the new version of vSAN supports the software and hardware components, drivers, firmware, and storage I/O controllers that you plan on using. Supported items are listed on the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>. |
| vSAN version | Verify that you are using the latest version of vSAN. You cannot upgrade from a beta version to the new vSAN. When you upgrade from a beta version, you must perform a fresh deployment of vSAN. |
| Disk space | Verify that you have enough space available to complete the software version upgrade. The amount of disk storage needed for the vCenter installation depends on your vCenter configuration. |
| vSAN disk format | vSAN disk format is a metadata upgrade that does not require data evacuation or rebuilding. |
| vSAN hosts | Verify that you have placed the vSAN hosts in maintenance mode and selected the Ensure data accessibility or Evacuate all data option. You can use the vSphere Lifecycle Manager for automating and testing the upgrade process. However, when you use vSphere Lifecycle Manager to upgrade vSAN, the default evacuation mode is Ensure data accessibility. When you use the Ensure data accessibility mode, your data is not protected, and if you encounter a failure while upgrading vSAN, you might experience unexpected data loss. However, the Ensure data accessibility mode is faster than the Evacuate all data mode, because you do not need to move all data to another host in the cluster. |
| Virtual Machines | Verify that you have backed up your virtual machines. |

## Recommendations

Consider the following recommendations when deploying ESX hosts for use with vSAN:

- If ESX hosts are configured with memory capacity of 512 GbE or less, use SATADOM, SD, USB, or hard disk devices as the installation media.
- If ESX hosts are configured with memory capacity greater than 512 GbE, use a separate magnetic disk or flash device as the installation device. If you are using a separate device, verify that vSAN is not claiming the device.
- When you boot a vSAN host from a SATADOM device, you must use a single-level cell (SLC) device and the size of the boot device must be at least 16 GbE.
- To ensure your hardware meets the requirements for vSAN, see [Hardware Requirements for vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/requirements-for-creating-a-virtual-san-cluster/hardware-requirements-for-virtual-san.html).

vSAN 9.0 and later enables you to adjust the boot size requirements for an ESX host in a vSAN cluster.

## Upgrading the Witness Host in a Two Host or vSAN Stretched Cluster

The witness host for a two host cluster or vSAN stretched cluster is located outside of the vSAN cluster, but it is managed by the same vCenter. You can use the same process to upgrade the witness host as you use for a vSAN data host.

Upgrade the witness host before you upgrade the data hosts.

Using vSphere Lifecycle Manager to upgrade hosts in parallel can result in the witness host being upgraded in parallel with one of the data hosts. To avoid upgrade problems, configure vSphere Lifecycle Manager so it does not upgrade the witness host in parallel with the data hosts.