---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Network Pool Management
---

# Network Pool Management

When you create a workload domain or add an ESX host or vSphere cluster to an existing VCF domain, you do not need to enter IP addresses manually. Network pools automatically assign static IP addresses to vSAN, NFS, iSCSI, and vMotion VMkernel ports.

A network pool is a collection of subnets within a layer-2 network domain. Depending on the storage option, it includes information about subnets reserved for the vMotion and vSAN, vSAN Storage Client, NFS, or iSCSI networks that are required for adding a host to the global inventory.

Information Required for a Network Pool



| Storage Being Used | Required Networks in Network Pool |
| --- | --- |
| vSAN | vMotion and vSAN |
| vSAN compute | vMotion and vSAN |
| vSAN storage (formerly known as vSAN Max) | vMotion, vSAN, vSAN Storage Client |
| NFS | vMotion and NFS |
| vSAN and NFS | vMotion, vSAN, and NFS |
| VMFS on FC | vMotion only or vMotion and NFS |
| vVols on FC\* | vMotion only or vMotion and NFS |
| vVols on iSCSI\* | vMotion and iSCSI |
| vVols on NFS\* | vMotion and NFS |

\* Starting with VMware Cloud Foundation 9.0 and vSphere Foundation 9.0, the vSphere Virtual Volumes capability, also known as vVols, is deprecated and will be removed in a future release of VMware Cloud Foundation and vSphere Foundation. Support for vSphere Virtual Volumes will continue for critical bug fixes only for versions of vSphere 8.x, VMware Cloud Foundation and vSphere Foundation 5.x, and other supported versions until end-of-support for the respective release.

The network pool contains a range of IP addresses for each network. IP addresses from the ranges are assigned to the VMkernel ports on the ESX host. The use of IP ranges allows you to limit the IP addresses that are consumed from a given subnet. You can add more IP ranges to expand the use of the provided subnet.

A default network pool is created when you deploy VMware Cloud Foundation. This network pool is automatically associated with the management domain.

To create a workload domain with hosts in a different layer-2 network domain than the management domain, you must create a new network pool. Also, if you want to use external NFS or VMFS on FC storage, you must create a new network pool. A network pool can contain both vSAN and NFS networks.

When you create a workload domain with multiple vSphere clusters, those clusters can share a network pool or each cluster can have its own network pool.