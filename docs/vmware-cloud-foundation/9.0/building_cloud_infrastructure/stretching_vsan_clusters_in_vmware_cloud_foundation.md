---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Stretching vSAN Clusters in VMware Cloud Foundation
---

# Stretching vSAN Clusters in VMware Cloud Foundation

You can stretch a vSAN cluster in a workload domain across two availability zones within a region. Both availability zones must contain an equal number of hosts to ensure failover in case any of the availability zones goes down.

VMware Cloud Foundation 9.0 supports stretching the following types of vSAN clusters using the SDDC Manager API:

- vSAN ESA/OSA
- vSAN compute
- vSAN storage (formerly known as vSAN Max)

In addition to stretching existing clusters, you can use the SDDC Manager API to create a stretched vSAN compute cluster. The following procedures provide the prerequisites and steps for stretching existing clusters, as well as creating a stretched vSAN compute cluster. You can use the examples as the basis for performing these tasks in your own environment. For more information about all the available parameters see the SDDC Manager API Reference Guide.

The default management domain vSphere cluster must be stretched before a workload domain cluster can be stretched. This ensures that the NSX control plane and management VMs (vCenter, NSX management cluster, and SDDC Manager) remain accessible if the stretched cluster in the primary availability zone goes down.

You cannot stretch a cluster in the following conditions:

- The cluster shares a vSAN Storage Policy with any other clusters.
- The cluster includes DPU-backed hosts.
- The cluster includes hosts from different subnets or networks (L3).

Some use cases for stretching a cluster are described below.

- Planned maintenance

  You can perform a planned maintenance on an availability zone without any downtime and then migrate the applications after the maintenance is completed.
- Automated recovery

  Stretching a cluster automatically initiates VM restart and recovery, and has a low recovery time for the majority of unplanned failures.
- Disaster avoidance

  With a stretched cluster, you can prevent service outages before an impending disaster.

For design details about stretched clusters, see [vSphere Stretched Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/cluster-models/single-instance-multiple-availability-zones.html).