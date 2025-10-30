---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/esxi-traffic-types.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   ESX Traffic Types
---

# ESX Traffic Types

ESX hosts use different network traffic types to support vSAN.

Following are the different traffic types that you need to set up for vSAN.

These network traffic types are not applicable to vSAN storage clusters if the VMs are not deployed on the cluster.

Network Traffic Types



| Traffic Types | Description |
| --- | --- |
| Management network | The management network is the primary network interface that uses a VMkernel TCP/IP stack to facilitate the host connectivity and management. It can also handle the system traffic such as vMotion, iSCSI, Network File System (NFS), Fiber Channel over Ethernet (FCoE), and fault tolerance. |
| Virtual Machine network | With virtual networking, you can network VMs and build complex networks within a single ESX host or across multiple ESX hosts. |
| vMotion network | Traffic type that facilitates migration of VM from one host to another. Migration with vMotion requires correctly configured network interfaces on source and target hosts. Ensure that the vMotion network is distinct from the vSAN network. |
| vSAN network | A vSAN cluster requires the VMkernel network for the exchange of data. Each ESX host in the vSAN cluster must have a VMkernel network adapter for the vSAN traffic. For more information, see [Manually Enabling vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/enabling-virtual-san.html). |