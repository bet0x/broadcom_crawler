---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/vsan-concepts/characteristics-of-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Characteristics of vSAN
---

# Characteristics of vSAN

The following characteristics apply to vSAN, its clusters, and datastores.

vSAN includes features to add resiliency and efficiency to your data computing and storage environment.

vSAN Features



| Supported Features | Description |
| --- | --- |
| Shared storage support | vSAN supports vSphere features that require shared storage, such as HA, vMotion, and DRS. For example, if a ESX host becomes overloaded, DRS can migrate VMs to other ESX hosts in the cluster. |
| On-disk format | vSAN on-disk virtual file format provides highly scalable snapshot and clone management support per vSAN ESA cluster. For information about the number of VM snapshots and clones supported per vSAN cluster, see the [vSphere Configuration Maximums](https://configmax.broadcom.com/home) guide. |
| All-flash configurations | vSAN can be configured for all-flash cluster. |
| Fault domains | vSAN supports configuring fault domains or rack awareness to protect ESX hosts from rack or chassis failures when the vSAN cluster spans across multiple racks or blade server chassis in a data center. |
| File service | vSAN file service enables you to create file shares in the vSAN datastore that client workstations or VMs can access. |
| iSCSI target service | vSAN iSCSI target service enables ESX hosts and physical workloads that reside outside the vSAN cluster to access the vSAN datastore. |
| vSAN Stretched clusters | vSAN supports stretched clusters that span across two availability zones. |
| Remote Branch Office (ROBO) or Two node vSAN clusters | vSAN supports two node clusters that consists of two ESX hosts and a witness host. This configuration is ideal for environments with limited resources, such as remote or branch offices. |
| Support for Windows Server Failover Clusters (WSFC) | vSAN support SCSI-3 Persistent Reservations (SCSI-3 PR) on a virtual disk level required by WSFC to arbitrate access to a shared disk between nodes. Support of SCSI-3 PRs enables configuration of WSFC with a disk resource shared between VMs natively on vSAN datastores.  Currently the following configurations are supported:  - Up to 6 application nodes per cluster. - Up to 64 shared virtual disks per node.  For more information on the supported versions, see [Windows Server Release Information](https://learn.microsoft.com/en-us/windows/release-health/windows-server-release-info). |
| vSAN Skyline health service | vSAN Skyline health service includes preconfigured health check tests to monitor, troubleshoot, diagnose the cause of cluster component problems, and identify any potential risk. |
| vSAN performance service | vSAN performance service includes statistical charts used to monitor IOPS, throughput, latency, and congestion. You can monitor performance of a vSAN cluster, ESX host, disk group, disk, and VMs. |
| Integration with vSphere storage features | vSAN integrates with vSphere data management features traditionally used with VMFS and NFS storage. These features include snapshots, linked clones, and vSphere Replication. |
| Storage Policy Based Management for Virtual Machine Storage | vSAN works with VM storage policies that control the type of storage provided for the VM, the placement of the VM within storage, and the data services the VM uses.  If you do not assign a storage policy to the VM during deployment, the vSAN Default Storage Policy is automatically assigned to the VM. |
| Rapid provisioning | vSAN rapid provisioning simplifies storage management by enabling rapid storage creation and deployment within vCenter, as part of VM creation and deployment. vSAN through its distributed shared storage, streamlines storage allocation for VMs, allowing storage provisioning without the need for manual allocation or pre-provisioning of storage. For more information, see [vSAN Space Efficiency Technologies](https://www.vmware.com/docs/vmw-vsan-space-efficiency). |
| Space Efficency: Compression | vSAN ESA enables compression by default using the vSAN storage policy. The data compression occurs at the top of the vSAN stack. By handling compression at this level, vSAN ESA eliminates the need to compress the data on other ESX hosts with object copies. This reduces the amount of data transmitted over the network.  You can use the Compression-only setting for vSAN OSA clusters with demanding workloads that cannot take advantage of deduplication techniques. |
| Space Efficiency: Deduplication | When using vSAN OSA, you can enable deduplication and compression. Deduplication is enabled at the cluster level and the data is destaged to the capacity tier. The data in the disk group initially goes through deduplication followed by compression.  Deduplication is not available in the vSAN ESA cluster. |
| Space Efficently: Trim and Unmap | vSAN has full awareness of TRIM/UNMAP commands sent from the guest operating system and can reclaim the previously allocated storage as free space. You can enable Trim and Unmap on vSAN OSA, but gets enabled by default on vSAN ESA. |
| Data-at-rest encryption | vSAN provides data-at-rest encryption. In vSAN ESA, the data is encrypted in the upper layers of vSAN and it receives incoming writes. The data goes through compression before it is encrypted resulting in lower overhead or latency. All the vSAN traffic transmitted across hosts are encrypted.  In vSAN OSA, the data is encrypted after all other processing, such as deduplication, is performed. Data-at-rest encryption protects data on storage devices, in case a device is removed from the cluster.  Ensure that you have a key management server to perform data-at-rest encryption. |
| Data-in-transit encryption | vSAN can encrypt data-in-transit across ESX hosts in the cluster. When you enable data-in-transit encryption, vSAN encrypts all data and metadata traffic between ESX hosts. vSAN OSA and vSAN ESA support multiple key rotation options such as Shallow and Deep Rekey, and uses AES-256 bit encryption for data-in-transit.  You do not need a key management server to perform data-in-transit encryption. |
| Cloud native storage | Cloud native storage integrates storage directly into the VMware vSphere platform enabling VMs and containers to use shared storage. |
| Container storage interface | The Container storage interface (CSI) is an open standard that enables container orchestration platforms like Kubernetes. It manages storage resources through a consistent plugin-based architecture. |
| Data persistence platform | The vSAN Data Persistence platform provides a framework for software technology partners to integrate with VMware infrastructure. Each partner must develop their own plug-in for VMware customers to receive the benefits of the vSAN Data Persistence platform. |
| Disaggregated HCI | The disaggregated HCI in vSAN decouples compute and storage resources. It allows compute and storage resources to scale independently within a VMware environment. It enables the use of dedicated storage-only hosts. |
| vSAN storage clusters | vSAN storage clusters are groups of ESX hosts that pool their local storage devices to create a shared, distributed datastore managed by VMware vSAN. |
| RAID5/6 | RAID 5/6 in vSAN provides data protection through erasure coding. This allows effecient storage utilization while maintaining fault tolerance.   - RAID 5: Protects against one failure. The data is split into three data block and one parity block. It requires a minimum of four hosts. - RAID 6: Protects against two simultaneous failures. The data is split into four data blocks and two parity blocks. It requires a minimum of six hosts. |
| SDK support | The VMware vSAN SDK is an extension of the VMware vSphere Management SDK. It includes documentation, libraries and code examples that help developers automate installation, configuration, monitoring, and troubleshooting of vSAN. |

For more information, see [vSAN Feature Matrix](https://www.vmware.com/docs/vmw-vsan-feature-matrix).