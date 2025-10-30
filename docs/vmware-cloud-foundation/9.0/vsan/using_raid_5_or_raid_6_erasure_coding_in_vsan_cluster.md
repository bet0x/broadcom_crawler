---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-raid-5-6-erasure-coding-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using RAID 5 or RAID 6 Erasure Coding in vSAN Cluster
---

# Using RAID 5 or RAID 6 Erasure Coding in vSAN Cluster

You can use RAID 5 or RAID 6 erasure coding to protect against data loss and increase storage efficiency.

Erasure coding can provide the same level of data protection as mirroring (RAID 1), while using less storage capacity. RAID 5 or RAID 6 erasure coding enables vSAN to tolerate the failure of up to two capacity devices in the datastore. You can configure RAID 5 on all-flash clusters with four or more fault domains. You can configure RAID 5 or RAID 6 on all-flash clusters with six or more fault domains.

RAID 5 or RAID 6 erasure coding requires less additional capacity to protect your data than RAID 1 mirroring. For example, a virtual machine protected by a Failures to tolerate value of 1 with RAID 1 requires twice the virtual disk size, but with RAID 5 it requires 1.33 times the virtual disk size. The following table shows a general comparison between RAID 1 and RAID 5 or RAID 6.

Capacity Required to Store and Protect Data at Different RAID Levels

The following table displays the capacity requirement for a vSAN OSA cluster:



| RAID Configuration | vSAN Architecture | Failures to Tolerate | Data Size | Capacity Required |
| --- | --- | --- | --- | --- |
| RAID 1 (mirroring) | ESA, OSA | 1 | 100 GbE | 200 GbE |
| RAID 5 (erasure coding) with four fault domains | OSA | 1 | 100 GbE | 133 GbE |
| RAID 5 (erasure coding) with five fault domains | ESA | 1 | 100 GbE | 125 GbE |
| RAID 5 (erasure coding) with three fault domains | ESA | 1 | 100 GbE | 150 GbE |
| RAID 1 (mirroring) | ESA, OSA | 2 | 100 GbE | 300 GbE |
| RAID 6 (erasure coding) with six fault domains | OSA | 2 | 100 GbE | 150 GbE |
| RAID 6 (erasure coding) with six fault domains | ESA | 2 | 100 GbE | 150 GbE |

RAID 5 or RAID 6 erasure coding is a policy attribute that you can apply to virtual machine components. To use RAID 5, set Failure tolerance method to RAID-5/6 (Erasure Coding) and Failures to tolerate to 1. To use RAID 6, set Failure tolerance method to RAID-5/6 (Erasure Coding) and Failures to tolerate to 2. RAID 5 or RAID 6 erasure coding does not support a Failures to tolerate value of 3.

To use RAID 1, set Failure tolerance method to RAID-1 (Mirroring). RAID 1 mirroring requires fewer I/O operations to the storage devices, so it can provide better performance. For example, a cluster resynchronization takes less time to complete with RAID 1.

In a vSAN stretched cluster, the Failure tolerance method of RAID-5/6 (Erasure Coding) applies only to the Site disaster tolerance setting.

For a vSAN ESA cluster, depending on the number of fault domains that you use, the number of components listed under RAID 5 (Monitor > vSAN > Virtual Objects > testVM > View Placement Details) will vary. If six or more fault domains are available in the cluster, then five components will be listed under RAID 5. If five or fewer fault domains are available, then three components will be listed.

For more information about configuring policies, see [Using vSAN Policies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies.html#GUID-351a7daf-31bc-4e27-bc75-f1d5d5abbd1d-en).