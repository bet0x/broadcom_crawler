---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/what-is-vsan/building-a-virtual-san-cluster/vsan-deployment-options.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Deployment Options
---

# vSAN Deployment Options

This section covers the supported deployment options for vSAN clusters.

## vSAN HCI Cluster

vSAN HCI cluster or a single site vSAN cluster consists of a minimum of three ESX hosts. Typically, all ESX hosts in a single site vSAN cluster reside at a single availability zone, and may be connected on the same Layer 2 network. All-flash configurations including vSAN ESA require network connection of minimum 10 GbE and a network latency of minimum 1 millisecond.

![Single site vSAN ESA cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/eff9c258-5e66-4a1a-b8b9-16c71459d680.original.svg)

For more information, see [Creating a Single Site vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster.html).

![Single site vSAN OSA cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b137693c-70e0-4d68-90e8-fa7864139290.original.svg)

## Two-Node vSAN Cluster

Two-node vSAN clusters are often used for remote office/branch office environments, typically running a small number of workloads that require high availability. A two-node vSAN cluster consists of two ESX hosts at the same location, connected to the same network switch or directly connected. You can configure a two-node vSAN cluster that uses a third ESX host as a witness, which can be located remotely from the branch office. Usually the witness resides at the main site, along with the vCenter. vSAN witness hosts can be shared by multiple vSAN two-node clusters.

For more information, see [Creating a vSAN Stretched Cluster or Two-Node vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster.html) and [vSAN 2-node Cluster Guide](https://www.vmware.com/docs/vmw-vsan-2-node-cluster-guide).

![Two-node vSAN cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7e8c06c5-3fe1-4fc0-8cc9-21149e2df783.original.png)

## vSAN Stretched Cluster

A vSAN stretched cluster provides resiliency against the loss of an availability zone. The ESX hosts in a vSAN stretched cluster can be distributed evenly across two sites. The two sites must have a network latency of no more than five milliseconds (5 ms) round trip (RTT). A vSAN witness ESX host resides at a third site to provide the witness function. The witness also acts as tie-breaker in scenarios where a network partition occurs between the two data sites. Only metadata such as witness components is stored on the witness. The witness and the data sites must have a witness latency of less than 200 ms RTT. Broadcom recommends a witness latency of 100 ms one way.

For more information, see [Creating a vSAN Stretched Cluster or Two-Node vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster.html).

![
          vSAN stretched cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2477f414-254c-47ab-adf4-3c8cc78bc8e3.original.png)

## Compute Cluster

In a compute cluster, ESX hosts provide only compute resources and access shared storage from a vSAN storage cluster. While the compute cluster does not need local storage for vSAN, it must be connected to the vSAN storage cluster through a 10 GbE or higher network to ensure low latency access to the storage. The compute cluster can contain two or three hosts based on the workload needs and vCenter requirements.

![Compute cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/70329c6b-309f-46d5-8704-3dcedc90cdfb.original.svg)

## vSAN Storage Cluster

A vSAN storage cluster consists of ESX hosts that contribute only storage resources and do not run virtual machine workloads. With vSAN ESA architecture, it serves as a storage pool for one or more compute clusters. It requires a minimum of four hosts to maintain storage availability and fault tolerance. A vSAN storage cluster requires a minimum of 10 GbE network. Broadcom recommends a dedicated 25 GbE or higher network for the vSAN traffic to ensure consistent performance between ESX hosts. For more information, see [vSAN ESA ReadyNode Hardware Guidance](https://partnerweb.vmware.com/comp_guide2/vsanesa_profile.php).

![
            vSAN storage cluster diagram](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c0f971b4-b949-4173-a86d-a14e7d59c017.original.svg)