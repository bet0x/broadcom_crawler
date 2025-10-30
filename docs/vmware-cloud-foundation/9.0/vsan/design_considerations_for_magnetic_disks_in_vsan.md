---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/sizing-a-virtual-san-datastore/design-consideration-for-magnetic-disks-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Design Considerations for Magnetic Disks in vSAN
---

# Design Considerations for Magnetic Disks in vSAN

Plan the size and number of magnetic disks for capacity in hybrid configurations by following the requirements for storage space and performance.

## SAS and NL-SAS Magnetic Devices

Use SAS or NL-SAS magnetic devices by following the requirements for performance, capacity, and cost of the vSAN storage.

- Compatibility. The model of the magnetic disk must be certified and listed in the vSAN section of the Broadcom Compatibility Guide availalble at: <https://compatibilityguide.broadcom.com/>.
- Performance. SAS and NL-SAS devices have faster performance.
- Capacity. The capacity of SAS or NL-SAS magnetic disks for vSAN is available in the vSAN section of the Broadcom Compatibility Guide. Consider using a larger number of smaller devices instead of a smaller number of larger devices.
- Cost. SAS and NL-SAS devices can be expensive.

## Magnetic Disks as vSAN Capacity

Plan a magnetic disk configuration by following these guidelines:

- For better performance of vSAN, use many magnetic disks that have smaller capacity.

  You must have enough magnetic disks that provide adequate aggregated performance for transferring data between cache and capacity. Using more small devices provides better performance than using fewer large devices. Using multiple magnetic disk spindles can speed up the destaging process.

  In environments that contain many virtual machines, the number of magnetic disks is also important for read operations when data is not available in the read cache and vSAN reads it from the magnetic disk. In environments that contain a small number of virtual machines, the disk number impacts read operations if the Number of disk stripes per object in the active VM storage policy is greater than one.
- For balanced performance and predictable behavior, use the same type and model of magnetic disks in a vSAN datastore.
- Dedicate a high enough number of magnetic disks to satisfy the value of the Failures to tolerate and the Number of disk stripes per object attributes in the defined storage policies. For information about the VM storage policies for vSAN, see [What are vSAN Policies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/about-vsan-policies.html).