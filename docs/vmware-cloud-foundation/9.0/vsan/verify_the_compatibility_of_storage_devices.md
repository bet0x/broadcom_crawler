---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/preparing-storage-devices/selecting-or-verifying-the-compatibility-of-storage-devices.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Verify the Compatibility of Storage Devices
---

# Verify the Compatibility of Storage Devices

Consult the Broadcom Compatability Guide to verify that your storage devices, drivers, and firmware are compatible with vSAN.

By using the vSAN section of the Broadcom Compatibility Guide available at <https://compatibilityguide.broadcom.com/>, you can select a magnetic disk, flash device, and storage controllers, or check the compatibility of your storage devices for vSAN.

You can choose from several options for vSAN compatibility.

- Use a vSAN ReadyNode server, a physical server that OEM vendors and VMware validate for vSAN compatibility.
- Assemble a node by selecting individual components from validated device models.

  | Broadcom Compatibility Guide Section | Component Type for Verification |
  | --- | --- |
  | Systems | Physical server that runs ESX. |
  | vSAN | - Magnetic disk SAS model for hybrid configurations. - Flash device model that is listed in the Broadcom Compatibility Guide. Certain models of PCIe flash devices can also work with vSAN. Consider also write endurance and performance class. - Storage controller model that supports passthrough.  vSAN can work with storage controllers that are configured for RAID 0 mode if each storage device is represented as an individual RAID 0 group. - For vSAN ESA, NVMe TLC drives on Broadcom HCL with capacity 1.6 TB or higher, performance class F higher, and an endurance class of 1 Drive Writes Per Day (DWPD). For more information see [vSAN ESA ReadyNode Hardware Guidance](https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php). |