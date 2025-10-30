---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Network Characteristics
---

# vSAN Network Characteristics

vSAN is network-dependent. Understanding and configuring the right vSAN network settings is critical to avoiding performance and stability issues.

A reliable and robust vSAN network has the following characteristics:

vSAN Network Traffic

vSAN network traffic is primarily made up of cluster, metadata, and storage replication traffic. A VM can access its storage resources from any host within a vSAN cluster. It is not necessary for that data to be locally available, thus allowing a VM to access its data on another node.

Unicast

vSAN uses unicast for communication. Unicast traffic is a one-to-one transmission of IP packets from one point in the network to another point. Unicast transmits the heartbeat sent from the primary host to all other hosts each second. This ensures that the hosts are active and indicates the participation of hosts in the vSAN cluster. You can design a simple unicast network for vSAN. For more information on the unicast communication, see [Using Unicast in vSAN Network](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network.html).

If possible, always use the latest version of vSAN.

Layer 2 and Layer 3 Network

All hosts in the vSAN cluster must be connected through a Layer 2 (L2) or Layer 3 (L3) network.

VMkernel Network

Each ESX host in a vSAN cluster must have a network adapter for vSAN communication. All the intra cluster communication happens through the vSAN VMkernel port.

VMkernel Interface

Each ESX host in a vSAN cluster must have a VMkernel interface used for vSAN traffic to handle data replication, I/O traffic, and cluster health monitoring.

Virtual Switch

vSAN supports the following types of virtual switches:

- The Standard Virtual Switch provides connectivity from VMs and VMkernel ports to external networks. This switch is local to each ESX host.
- A vSphere Distributed Switch provides central control of the virtual switch administration across multiple ESX hosts. A distributed switch also provides networking features such as Network I/O Control (NIOC) that can help you set Quality of Service (QoS) levels on vSphere or virtual network. vSAN includes vSphere Distributed Switch irrespective of the vCenter version.

Network Interfaces

vSAN can have dedicated physical network interfaces to secure vSAN storage traffic and to provide bandwidth and resources. vSAN traffic can share physical network adapters with other system traffic types, such as vSphere vMotion traffic, vSphere HA traffic, and virtual machine traffic. To guarantee the amount of bandwidth required for vSAN, configure Network I/O control on the distributed switch.

Bandwidth

In vSAN environments that share physical resources with other traffic, use Network I/O Control to allocate bandwidth among traffic types. Assigning shares to vSAN traffic ensures that it receives sufficient bandwidth during network contention. This prioritizes vSAN traffic and prevents other traffic types from affecting its performance when the physical NIC is saturated.

Avoid using reservations or limits in vSAN environments. Reservations can leave unused bandwidth inaccessible to VMs, while limits restrict traffic even when additional bandwidth is available.

vSAN recommends the usage of shares to allocate bandwidth for vSAN traffic. This offers the most balanced and efficient use of shared physical NICs.

For information about using Network I/O Control to configure bandwidth allocation for vSAN traffic, see the [vSphere Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-networking.html) guide.