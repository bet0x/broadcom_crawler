---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/esx-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > ESX Detailed Design
---

# ESX Detailed Design

In the design of the ESX host configuration for your VMware Cloud Foundation platform, consider the resources, networking, and security policies that are required to support the virtual machines in each workload domain cluster.

## ESX Hardware and Sizing Considerations

For more information on host sizing, refer to the Planning and Preparation workbook, and the VMware Cloud Foundation Sizer.

ESX Hardware and Sizing Considerations



| Hardware Element | Considerations |
| --- | --- |
| BIOS/Firmware | Ensure the ESX host hardware is on the HCL and that you are running the latest supported BIOS & firmware. |
| CPU | - Total CPU requirements for the workloads that are running in the cluster. - Host failure and maintenance scenarios.  Keep the over-commitment ratio vCPU-to-pCPU less than or equal to 2:1 for the management domain and less than or equal to 8:1 for workload domains. - Number of physical cores, not logical cores.    - Simultaneous multi-threading (SMT) in CPUs improve CPU performance however the performance enhancement will not be equivalent to 100% more CPU power. |
| Memory | - Total memory requirements for the workloads that are running in the cluster. - When sizing memory for the ESX hosts in a cluster, to reserve the resources of one host for failover or maintenance, set the admission control setting to N+1, which reserves the resources of one host for failover or maintenance. - vSAN OSA.    - To support the maximum number of disk groups, you must provide 32 GB of RAM. - vSAN ESA.    - You must provide 512 GB of RAM. |
| Storage | - Use high-endurance devices such as a hard drive or SSD for boot device. - Use a 128GB or greater boot device to maximize the space available for ESX-OS Data. - Use hosts with homogeneous configuration. |
| Network | - Use multiple physical NICs connected to multiple ToR switches to ensure redundancy. - 25GbE is recommended |
| Power | - Use redundant power supplies, preferably connected to separate circuits to ensure availability. - Consider the impact of enabling Power Management on your ESX hosts. In order to allow ESX to control CPU power-saving features you need to set power management in the BIOS to OS Controlled Mode. |

## ESX Design Requirements and Recommendations

In your ESX design, you apply certain best practices.

ESX Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-ESX-REQD-CFG-001 | Install no less than the minimum number of ESX hosts required for the vSphere cluster model being deployed. | - Ensures availability requirements are met. - If one of the ESX hosts is not available because of a failure or maintenance event, the CPU over-commitment ratio becomes 2:1. | None. |
| VCF-ESX-REQD-CFG-002 | Ensure each ESX host matches the required CPU, memory and storage specification. | Ensures workloads will run without contention even during failure and maintenance conditions. | Assemble the server specification and number according to the sizing in [VMware Cloud Foundation Planning and Preparation Workbook](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/VMware%20Cloud%20Foundation%205.2%20Planning%20and%20Preparation%20Workbook.xlsx) which is based on projected deployment size. |
| VCF-ESX-REQD-SEC-001 | Regenerate the certificate of each ESX host after assigning the ESX host an FQDN. | Establishes a secure connection with the VCF Installer during the initial deployment and prevents man-in-the-middle (MiTM) attacks. | You must manually regenerate the certificates of the ESX hosts before the deployment. |

ESX Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-ESX-RCMD-CFG-001 | When using vSAN as primary storage in the management domain, use vSAN ReadyNodes for each ESX host. | Your management domain is fully compatible with vSAN at deployment.  For information about the models of physical servers that are vSAN-ready, see [vSAN Compatibility Guide for vSAN ReadyNodes](https://www.vmware.com/resources/compatibility/pdf/vi_vsan_rn_guide.pdf). | - Hardware choices might be limited. - If you plan to use a server configuration that is not a vSAN ReadyNode, your CPU, disks, and I/O modules must be listed on the VMware Compatibility Guide under CPU Series and vSAN Compatibility List aligned to the ESX version. |
| VCF-ESX-RCMD-CFG-002 | Allocate ESX hosts with uniform configuration across the default management vSphere cluster. | A balanced vSphere cluster has these advantages:   - Predictable performance even during hardware failures. - Minimal impact of resynchronization or rebuild operations on performance. | You must apply vendor sourcing, budgeting, and procurement considerations for uniform server nodes on a per cluster basis. |
| VCF-ESX-RCMD-CFG-003 | When sizing CPU, do not consider multi-threading technology and associated performance gains. | Although multi-threading technologies increase CPU performance, the performance gain depends on running workloads and differs from one case to another. | Because you must provide more physical CPU cores, costs increase and hardware choices become limited. |
| VCF-ESX-RCMD-CFG-004 | Install and configure all ESX hosts in the default management vSphere cluster to boot using a 128-GB device or larger. | Provides ESX hosts that have large memory, that is, greater than 512 GB, with enough space for the scratch partition when using vSAN. | None. |
| VCF-ESX-RCMD-CFG-005 | Use the default configuration for the scratch partition on all ESX hosts in the default management vSphere cluster. | - If a failure in the vSAN cluster occurs, the ESX hosts remain responsive and log information is still accessible. - It is not possible to use a vSAN datastore for the scratch partition. | None. |
| VCF-ESX-RCMD-CFG-006 | For workloads running in the default management vSphere cluster, save the virtual machine swap file at the default location. | Simplifies the configuration process. | Increases the amount of replication traffic for management workloads that are recovered as part of the disaster recovery process. |
| VCF-ESX-RCMD-NET-001 | Place the ESX hosts in each management domain vSphere cluster on the ESX management network that is separate from the VM management network. | - Enables the separation of the physical VLAN between ESX hosts and the other management components for security reasons. - The VM management network is not required for a multi-rack compute-only cluster in a workload domain. | Increases the number of VLANs required. |
| VCF-ESX-RCMD-NET-002 | Place the ESX hosts in each workload domain on a separate ESX host management VLAN-backed network. | Enables the separation of the physical VLAN between the ESX hosts in different workload domains for security reasons. | Increases the number of VLANs required. For each workload domain, you must allocate a separate management subnet. |
| VCF-ESX-RCMD-NET-003 | Use dedicated VLANs for each traffic type. | Enables the separation of the physical VLAN for vSAN, vMotion, NFS & backup traffic. | Increases the number of VLANs required. For each traffic type you must allocate a separate VLAN and subnet. |
| VCF-ESX-RCMD-SEC-001 | Set the advanced setting UserVars.SuppressShellWarning to 0 across all ESX hosts in the management domain. | - Ensures compliance with the vSphere Security Configuration Guide and with security best practices - Enables the warning message that appears in the vSphere client every time SSH access is activated on an ESX host. | You must turn off SSH enablement warning messages manually when performing troubleshooting or support activities. |