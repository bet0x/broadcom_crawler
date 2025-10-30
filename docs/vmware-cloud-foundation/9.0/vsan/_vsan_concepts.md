---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/vsan-concepts.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Concepts
---

# vSAN Concepts

VMware vSAN is an easy to manage, object-based enterprise software distributed storage (SDS) system designed to leverage the capabilities of modern hardware.

vSAN pools disk space from multiple ESX hosts in a cluster to create a single shared datastore. You can configure vSAN to work as either a hybrid or all-flash cluster. In hybrid clusters, flash devices are used for the cache layer and magnetic disks are used for the storage capacity layer. In all-flash clusters, flash devices are used for both cache and capacity.

You can turn on vSAN on existing vSphere clusters, or when you create a new cluster. vSAN aggregates the storage capacity of eligible devices from multiple ESX hosts in a cluster into a single, shared datastore. Expanding capacity in vSAN is simple and can be done by the following:

- Expand storage capacity only: Add storage devices to existing ESX hosts in the vSAN cluster.
- Expand compute capacity only: Add new ESX hosts without local storage devices to the existing vSAN cluster.
- Expand compute and storage capacity: Add new ESX hosts with local storage to the existing vSAN cluster.

vSAN works best when all ESX hosts in the vSphere cluster share similar or identical configurations across all cluster members, including similar or identical storage configurations. ESX hosts without any local devices also can participate and run their VMs on the vSAN datastore.

With the availability of vSAN Express Storage Architecture (ESA), all storage devices claimed by vSAN contribute to capacity and performance. Each ESX host's storage devices claimed by vSAN form a storage pool. The storage pool represents the amount of caching and capacity provided by the ESX host to the vSAN datastore.

vSAN storage cluster is a disaggregated storage solution available with vSAN ESA. It pools storage devices across dedicated ESX hosts, separating storage resources from compute hosts.

For vSAN Original Storage Architecture (OSA), each ESX host that contributes storage devices to the vSAN datastore must provide at least one device for flash cache and at least one device for capacity. The devices on the contributing ESX host form one or more disk groups. Each disk group contains one flash cache device, and one or more capacity devices for persistent storage. Each ESX host can be configured to use multiple disk groups.

vSAN ESA also provides performance, efficiency, and scalability improvements. The hardware requirements for vSAN ESA is different from vSAN OSA. For more information on vSAN ESA and vSAN OSA, see [Comparing vSAN OSA to vSAN ESA](https://blogs.vmware.com/cloud-foundation/2022/08/31/comparing-the-original-storage-architecture-to-the-vsan-8-express-storage-architecture/).

vSAN storage cluster is a distributed storage system that provides vSAN ESA capabilities while functioning as a storage-only cluster. For more information, see [Introducing vSAN Storage Cluster.](https://blogs.vmware.com/cloud-foundation/2023/08/22/introducing-vsan-max/)

For best practices, capacity considerations, and general recommendations about designing and sizing a vSAN cluster, see the [VMware vSAN Design Guide](https://www.vmware.com/docs/vmware-vsan-design-guide).