---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Sharing Remote vSAN Datastores 
---

# Sharing Remote vSAN Datastores

Remote datastore sharing enables vSAN clusters to share their datastores with other clusters.

You can provision virtual machines running on your local cluster to use storage space on a remote datastore. When you provision a new virtual machine, you can select a remote datastore that is mounted to the client cluster. You can assign any compatible storage policy configured for the remote datastore.

Mounting a remote datastore is a cluster-wide configuration. When you mount a remote datastore to a vSAN cluster, it is available to all hosts in the cluster.

When you prepare a vSphere cluster for mounting remote datastore, select any one of the following vSAN cluster types:

- vSAN HCI cluster provides compute resources and storage resources. It can share its datastore across data centers and vCenter instances and mount datastores from other vSAN HCI clusters.
- Compute Cluster is a vSphere cluster that can mount a remote datastore from a vSAN storage cluster. These clusters are hosts in a vSphere cluster that only complies with the Broadcom Compatibility Guide for vSphere, but not for vSAN.
- vSAN storage cluster (deployment model based on vSAN ESA) provides storage resources, but not compute resources. Its datastore can be mounted by compute clusters or vSAN HCI clusters across data centers and vCenter instances.

vSAN datastore sharing has the following design considerations:

- vSAN single site and vSAN stretched clusters can share datastores across clusters in the same data center, or across clusters managed by remote vCenter instances, as long as the source and the remote vCenter instances are accessible and they pass the prechecks.
- The client hosts that are not part of a cluster are not supported. You can configure a single host compute-only cluster, however VMs running on this node are affected in the event of a host failure.
- A datastore on a vSAN storage cluster or a vSAN HCI server cluster can be shared across up to 10 client clusters.
- A client cluster can mount up to 5 remote datastores from one or more vSAN storage cluster or vSAN server clusters.
- A single datastore can be mounted by up to 128 vSAN hosts, including hosts in the local vSAN server cluster.
- All objects that make up a virtual machine must reside on the same datastore.
- For vSphere HA to work with vSAN datastore sharing, configure the following failure response for Datastore with APD on the client cluster: Power off and restart virtual machines.
- Data-in-transit encryption between a client and a remote vSAN storage cluster or HCI cluster is not supported.

The following configurations are not supported with vSAN datastore sharing:

- Remote provisioning of iSCSI volumes, or CNS persistent volumes. You can provision iSCSI volumes on the local vSAN datastore, but not on any remote vSAN datastore. For remote provisioning of CNS persistent volumes, see [vSphere Functionality Supported by vSphere Container Storage Plug-in](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/container-storage-plugin/3-0/getting-started-with-vmware-vsphere-container-storage-plug-in-3-0/vsphere-container-storage-plug-in-concepts/vsphere-functionality-supported-by-vsphere-container-storage-plug-in.html) and [Using vSphere Container Storage Plug-in for HCI Mesh Deployment](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/container-storage-plugin/3-0/getting-started-with-vmware-vsphere-container-storage-plug-in-3-0/using-vsphere-container-storage-plug-in/using-vsphere-container-storage-plug-in-for-hci-mesh-deployment.html) in the vSphere Storage guide.
- Air-gapped networks or clusters using multiple vSAN VMkernel ports
- Client cluster mounting datastores from different vSAN architectures. vSAN OSA and vSAN ESA are not compatible, and cannot share datastores with each other. If a cluster has mounted a datastore that uses vSAN OSA, it cannot mount a datastore that uses vSAN ESA.

## Disaggregated Storage with vSAN Storage Cluster

vSAN storage cluster is a fully distributed, scalable, shared storage solution for vSphere clusters and vSAN clusters. Storage resources are disaggregated from compute resources, so you can scale storage and compute resources independently.

vSAN storage cluster uses vSAN ESA and high-density vSAN Ready Nodes for increased capacity and performance.

vSAN storage cluster can be deployed by purchasing VMware Cloud Foundation or by acquiring the advanced add-on offer for VMware vSphere Foundation. Licensing for vSAN storage cluster is based on a per-TiB metric, which corresponds to the total amount of raw storage capacity needed for the environments.

A vSAN storage cluster acts as a server cluster that only provides storage. You can mount its datastore to vSphere clusters configured as compute clusters or vSAN HCI client clusters.

![Sharing vSAN datastore hosted on a vSAN storage cluster](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/94a0514c-aa0f-4132-8195-576b1b683fc2.original.png)

vSAN storage clusters have the following design considerations:

- Supported only on vSAN ESA running on vSAN Ready Nodes certified for vSAN storage clusters.
- Cannot be mounted to a vSAN OSA client cluster.
- Acts as a storage server only, not as a client. It is recommended not to run workload virtual machines on vSAN storage clusters.
- Requires a minimum of four ESX hosts, each hosts with a minimum of 20 TiB per host for space efficiency. Broadcom recommends a minimum of six ESX hosts. To optimize performance, use a uniform configuration of storage devices across all hosts.
- Supports the use of 25 GbE network connections between ESX hosts in the vSAN storage cluster, though Broadcom recommends the use of 100 GbE connections. Supports the use of 10 GbE network connections from compute clients to the vSAN storage clusters, though Broadcom recommends the use of 25 GbE connections. For best performance, enable support for jumbo frames (MTU = 9000) and ensure you have sufficient resources at the network spine. For smaller vSAN storage cluster configurations, Broadcom support the use of 10 GbE network connections between ESX hosts. For more information, see [vSAN ESA ReadyNode Hardware Guidance](https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php).
- Requires a latency below five milliseconds between the client and the server ESX hosts.
- Enable Auto-Policy management (Configure > vSAN > Services > Storage > Edit) to ensure optimal levels of resilience and space efficiency.
- Enable Automatic rebalance (Configure > vSAN > Services > Advanced Options > Edit) to ensure an evenly balanced, distributed storage system.

You can configure vSAN storage cluster only during cluster creation. You cannot convert an existing vSAN HCI cluster to a vSAN storage cluster, and you cannot convert a vSAN storage cluster to a vSAN HCI cluster. You must deactivate vSAN and reconfigure the cluster to make the conversion.

|  |  |
| --- | --- |
| Compute cluster | A compute cluster is a vSphere cluster with a small vSAN element that enables it to mount a remote datastore hosted on a vSAN storage cluster. The ESX hosts in a compute cluster do not have local storage. You can monitor the capacity, health, and performance of the remote datastore.  Compute cluster does not require vSAN Ready Nodes.  Compute clusters have the following design considerations:   - vSAN networking must be configured on ESX hosts in the compute cluster. - No vSAN storage eligible devices can be present on ESX hosts in a compute cluster. - No data management features can be configured on the compute cluster. |
| vSAN storage cluster | A vSAN storage cluster can separate the external VM traffic from the internal vSAN storage traffic by utilizing the dedicated VMkernel ports for different traffic types. With the vSAN storage cluster, you have the option to use Storage cluster client network. |

## Cross-Cluster Capacity Sharing

vSAN storage clusters or vSAN HCI clusters can share their datastores with other vSAN HCI clusters or compute clusters. A vSAN storage cluster can act as a server to provide data storage, while a vSAN HCI cluster or compute cluster can also act as a client that consumes storage from a remote datastore.

![Sharing vSAN datastore hosted on a vSAN HCI cluster](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6884eb7b-153c-4dee-93b4-a9cd442cb917.original.png)

Use the Datastore Management view to monitor and manage remote datastores mounted on the local vSAN cluster. Each client vSAN cluster or compute-only client cluster can mount remote datastores from server vSAN clusters. Each compatible vSAN cluster also can act as a server, and allow other vSAN clusters to mount its local datastore.

Monitor views for capacity, performance, health, and placement of virtual objects show the status of remote objects and datastores.

## Using Remote vCenter Instances as Datastore Sources

vSAN HCI and vSAN storage clusters can share remote datastores across vCenter instances. You can add a remote vCenter as a datastore source for clusters on the local vCenter. Client clusters on the local vCenter can mount datastores that reside on the remote vCenter.

Use the Remote Datastore Management page in vCenter to manage remote datastore sources (Configure > vSAN > > Remote Datastore Management). Click the tabs to access information about shared datastores across vCenter instances, add vCenter instances as datastores sources, and mount datastores to local clusters.

|  |  |
| --- | --- |
| Datastore Sources | View and manage datastore sources residing in remote vCenter instances. You can add or remove remote datastore sources for the local vCenter. |
| Clusters | View and manage clusters residing in the local vCenter. You can mount or unmount datastores from remote vCenter instances to the selected client cluster on the local vCenter. |
| Datastores | View all datastores available under this vCenter. |

vCenter to vCenter datastore sharing has the following design considerations:

- Each vCenter can serve up to 10 client vCenter instances.
- Each client vCenter can add up to 5 remote vCenter datastore sources.
- When a virtual machine on a client cluster managed by one vCenter uses storage from a remote server cluster managed by another vCenter, the storage policy on the client's vCenter takes precedence.