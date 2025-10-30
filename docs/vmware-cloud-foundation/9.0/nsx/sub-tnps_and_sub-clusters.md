---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/sub-tnps-and-sub-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Sub-TNPs and Sub-clusters
---

# Sub-TNPs and Sub-clusters

A Sub-TNP is a template to define configuration that is applied to hosts that are part of a Sub-cluster. To accommodate different cluster configurations required for sub-clusters, create sub-TNPs.

## Sub-Transport Node Profile

Starting with NSX 3.2.2, you can configure Sub-TNPs and Sub-clusters.

The maximum number of Sub-TNPs under a hostswitch in a TNP is 16.

While a TNP represents the global configuration applied to a Host Switch, a sub-TNP represents the local configuration applied to a sub-cluster. When you apply a sub-TNP to a sub-cluster, the host switch is overriden on the sub-cluster.

You can only apply a sub-TNP to a VDS switch. A sub-TNP can only override the following fields of a host switch: VDS Host Switches ID, uplink profiles and IP assignment.

![Add a Sub-Transport Node Profile that will be applied to a sub-cluster.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/3174da71-564f-4fb3-8a5d-b34b01e7ef55.original.png)

NSX Manager prepares the hosts in sub-clusters where the sub-TNP is applied and installs the NSX components on all the hosts. Transport nodes for the hosts are created based on the configuration specified in the transport node profile.

To delete a Sub-TNP, you must first detach the global TNP profile from the associated cluster. The existing transport nodes are not affected. New hosts added to the cluster are no longer automatically converted into transport nodes.

## Sub-clusters

Each cluster can have up to 16 sub-clusters.

To manage a cluster that is stretched across different subnets or L3 domains, some hosts will need different configuration, such as a some hosts will need to be in the TEP subnet-1, whereas some other hosts will need to be in TEP subnet-2. So, hosts with similar configuration requirements can be placed in one sub-cluster. And that sub-cluster can be applied with a sub-TNP that provides configuration.

In the following image, the cluster has three hosts: one in each sub-cluster and the last host is not part of any sub-cluster.

![On the Clusters tab, you can set sub-clusters and also know cluster hosts that belong to sub-clusters.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/508ca6af-c19e-400e-b156-55b53f6afb3e.original.png)

## Moving Hosts Between Sub-clusters

1. Move host from sub-cluster1 to sub-cluster2.
2. Sub-TNP config of sub-cluster1 is removed from the host.
3. Sub-TNP config of sub-cluster2 is applied to the host.

## Limitations of using Sub-clusters

- Sub-clusters can have hosts only from the cluster under which it is created.
- Sub-cluster cannot have hosts which are part of other sub-clusters.
- Maximum number of sub-clusters under a cluster is 16.
- Sub-cluster cannot be deleted if it has some hosts in it. After removing the hosts, sub-cluster can be deleted.
- Minimum supported ESX version for this feature is 7.0.0.
- Stateless hosts cannot be added to a sub-cluster.