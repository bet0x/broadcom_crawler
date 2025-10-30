---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/introduction-to-stretched-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > What Are vSAN Stretched Clusters 
---

# What Are vSAN Stretched Clusters

vSAN stretched clusters extend the vSAN cluster from a single data site to two availability zones for a better level of availability and intersite load balancing. vSAN stretched clusters are typically deployed in environments where the distance between data centers is limited, such as metropolitan or campus environments.

You can use vSAN stretched clusters to manage planned maintenance and avoid disaster scenarios, because maintenance or loss of one site does not affect the overall operation of the cluster. In a vSAN stretched cluster configuration, both data sites are active sites. If either site fails, vSAN uses the storage on the other site. vSphere HA restarts any VM that must be restarted on the remaining active site.

You must designate one site as the preferred site. The other site becomes a secondary or nonpreferred site. If the network connection between the two active sites is lost, vSAN continues operation with the preferred site. The site designated as preferred typically is the one that remains in operation, unless it is resyncing or has another issue. The site that leads to maximum data availability is the one that remains in operation.

A vSAN stretched cluster can tolerate one intersite link failure at a time without data becoming unavailable. A link failure is a loss of network connection between the two sites or between one site and the witness host. During a site failure or loss of network connection, vSAN automatically switches to fully functional sites.

vSAN stretched clusters can tolerate a witness host failure when one site is unavailable. Configure the storage policy Site disaster tolerance rule to Site mirroring - stretched cluster. If one site is down due to maintenance or failure and the witness host fails, objects become non-compliant but remain accessible.

For more information about working with vSAN stretched clusters, see the [vSAN Stretched Cluster Guide](https://www.vmware.com/docs/vsan-stretched-cluster-guide).

## Witness Host

Each vSAN stretched cluster consists of two data sites and one witness host. The witness host resides at a third site and contains the witness components of virtual machine objects. The witness host does not store customer data, only metadata, such as the size and UUID of vSAN object and components.

The witness host serves as a tiebreaker when a decision must be made regarding availability of datastore components when the network connection between the two availability zones is lost. In this case, the witness host forms a vSAN cluster with the preferred site. But if the preferred site becomes isolated from the secondary site and the witness, the witness host forms a cluster using the secondary site. When the preferred site is online again, data is resynchronized to ensure that both sites have the latest copies of all data.

If the witness host fails, all corresponding objects become noncompliant but are fully accessible.

The witness host has the following characteristics:

- The witness host can use low bandwidth/high latency links.
- The witness host cannot run virtual machines.
- A single witness host can support only one vSAN stretched cluster. Two-node vSAN clusters can share a single witness host.
- The witness host must have one VMkernel adapter with vSAN traffic enabled, with connections to all hosts in the cluster. The witness host uses one VMkernel adapter for management and one VMkernel adapter for vSAN data traffic. The witness host can have only one VMkernel adapter dedicated to vSAN.
- The witness host must be a standalone host dedicated to the vSAN stretched cluster. It cannot be added to any other cluster or moved in inventory through vCenter.

The witness host can be a physical host or an ESX host running inside a VM. The VM witness host does not provide other types of functionality, such as storing or running virtual machines. Multiple witness hosts can run as virtual machines on a single physical server. For patching and basic networking and monitoring configuration, the VM witness host works in the same way as a typical ESX host. You can manage it with vCenter, patch it and update it by using esxcli or vSphere Lifecycle Manager, and monitor it with standard tools that interact with ESX hosts.

You can use a witness virtual appliance as the witness host in a vSAN stretched cluster. The witness virtual appliance is an ESX host in a VM, packaged as an OVF or OVA. The appliance is available in different options, based on the size of the deployment. You can use a witness virtual appliance as the witness host in a vSAN stretched cluster. The witness virtual appliance is an ESX host in a VM, packaged as an OVF or OVA. Different appliances and different options are available, based on the vSAN architecture and the size of the deployment.

## vSAN Stretched Clusters and Fault Domains

vSAN stretched clusters use fault domains to provide redundancy and failure protection across sites. Each site in a vSAN stretched cluster resides in a separate fault domain.

A vSAN stretched cluster requires three fault domains: the preferred site, the secondary site, and a witness host. Each fault domain represents a separate site. When the witness host fails or enters maintenance mode, vSAN considers it a site failure.

vSAN can provide an extra level of local fault protection for virtual machine objects in vSAN stretched clusters. When you configure a vSAN stretched cluster, the following policy rules are available for objects in the cluster:

- Site disaster tolerance. For vSAN stretched clusters, this rule defines the failure tolerance method. Select Site mirroring - stretched cluster.
- Failures to tolerate (FTT). For vSAN stretched clusters, FTT defines the number of additional host failures that a virtual machine object can tolerate.
- None. Configure vSAN Storage Policy for SMP-FT VMs.
  - vSAN stretched clusters support enabling Symmetric Multiprocessing Fault Tolerance (SMP-FT) VMs only when site disaster tolerance storage policy is set to None with either Preferred or Secondary site. vSAN does not support SMP-FT VMs on a stretched cluster when site disaster tolerance storage policy is set to Site mirroring - stretched cluster.
  - vSAN ROBO clusters support enabling Symmetric Multiprocessing Fault Tolerance (SMP-FT) with FTT set to 1 only when both the data nodes are in the same physical site.

In a vSAN stretched cluster with local fault protection, even when one site is unavailable, the cluster can perform repairs on missing or broken components in the available site.

vSAN continue to serve I/O if any disks or disks on one site reach 96 percent full or 5 GbE free capacity (whichever is less) while disks on the other site have free space available. Components on the affected site are marked absent, and vSAN continues to perform I/O to healthy object copies on the other site. When disks on the affected site disk reach 94 percent capacity or 10 GbE (whichever is less), the absent components become available. vSAN resyncs the available components and all objects become policy compliant.