---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/using-two-host-vsan-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > What Are Two-Node vSAN Clusters 
---

# What Are Two-Node vSAN Clusters

A two-node vSAN cluster has two hosts at the same location. The witness function is performed at a second site on a dedicated virtual appliance.

Two-node vSAN clusters are often used for remote office/branch office environments, typically running a small number of workloads that require high availability. A two-node vSAN cluster consists of two hosts at the same location, connected to the same network switch or directly connected. A third host acts as a witness host, which can be located remotely from the branch office. Usually the witness host resides at the main site, with the vCenter.

A single witness host can support up to 64 two-node vSAN clusters. The number of clusters supported by a shared witness host is based on the host memory.

When you configure a two-node vSAN cluster in Quickstart or with the Configure vSAN wizard, you can select a witness host. To assign a new witness host for your cluster, right-click the cluster in the vSphere Client and select menu vSAN > Assign Shared Witness.