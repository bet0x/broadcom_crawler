---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/what-is-vsan-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > What is vSAN Network Design
---

# What is vSAN Network Design

You can use vSAN to provision shared storage within vSphere. vSAN aggregates local or direct-attached storage devices of a host cluster and creates a single storage pool shared across all hosts in the vSAN cluster.

vSAN is a distributed and shared storage solution that depends on a highly available, properly configured network for vSAN storage traffic. A fast and resilient network is crucial to a successful vSAN deployment. This guide provides recommendations on how to design and configure a vSAN network.

vSAN has a distributed architecture that relies on a fast, scalable, and resilient network. All host nodes within a vSAN cluster communicate over the IP network. All hosts in the cluster must maintain IP unicast connectivity, so they can communicate over a Layer 2 or Layer 3 network. For more information on the unicast communication, see [Using Unicast in vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network.html#GUID-d363357e-f76a-4bd7-a704-c7f655ba289f-en).

## vSAN Networking Terms and Definitions

vSAN introduces specific terms and definitions that are important to understand. Before you get start designing your vSAN network, review the key vSAN networking terms and definitions.

| Terms | Definitions |
| --- | --- |
| CMMDS | The Cluster Monitoring, Membership, and Directory Service (CMMDS) is responsible for the recovery and maintenance of a cluster of networked node members. It manages the inventory of items such as host nodes, devices, and networks. It also stores metadata information, such as policies and RAID configuration for vSAN objects. |
| DOM | The Distributed Object Manager (DOM) is responsible for creating the components and distributing them across the cluster. After a DOM object is created, one of the nodes (host) is nominated as the DOM owner for that object. This host handles all IOPS to that DOM object by locating the respective child components across the cluster and redirecting the I/O to respective components over the vSAN network. DOM objects include vdisk, snapshot, vmnamespace, vmswap, vmem, and so on. |
| NIC Teaming | Network Interface Card (NIC) teaming can be defined as two or more network adapters (NICs) that are set up as a "team" for high availability and load balancing. |
| NIOC | Network I/O Control (NIOC) determines the bandwidth that different network traffic types are given on a vSphere distributed switch. The bandwidth distribution is a user configurable parameter. When NIOC is enabled, distributed switch traffic is divided into predefined network resource pools: Fault Tolerance traffic, iSCSI traffic, vMotion traffic, management traffic, vSphere Replication traffic, NFS traffic, and virtual machine traffic. |
| Objects and Components | Each object is composed of a set of components, determined by capabilities that are in use in the VM Storage Policy. A vSAN datastore contains several object types:   - VM Home Namespace - The VM Home Namespace is a virtual machine home directory where all virtual machine configuration files are stored. This includes files such as .vmx, log files, vmdks, and snapshot delta description files. - VMDK - VMDK is a virtual machine disk or .vmdk file that stores the contents of the virtual machine's hard disk drive. - VM Swap Object - VM Swap Objects are created when a virtual machine is powered on. - Snapshot Delta VMDKs - Snapshot Delta VMDKs are created when virtual machine snapshots are taken. This is applicable only for vSAN OSA cluster. - Memory Object - Memory Objects are created when the snapshot memory option is selected when creating or suspending a virtual machine. |
| RDT | The Reliable Data Transport (RDT) protocol is used for communication between hosts over the vSAN VMkernel ports. It uses TCP at the transport layer and is responsible to create and destroy TCP connections (sockets) on demand. It is optimized to send large files. |
| SPBM | Storage Policy-Based Management (SPBM) provides a storage policy framework that serves as a single unified control panel across a broad range of data services and storage solutions. This framework helps you to align storage with application demands of your virtual machines. |
| VLAN | A VLAN enables a single physical LAN segment to be further segmented so that groups of ports are isolated from one another as if they were on physically different segments. |
| Witness Component | A witness is a component that contains only metadata and does not contain any actual application data. It serves as a tiebreaker when a decision must be made regarding the availability of the surviving datastore components, after a potential failure. |