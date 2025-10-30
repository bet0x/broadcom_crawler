---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool/verify-nsx-manager-clustering.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Verify NSX Manager Clustering
---

# Verify NSX Manager Clustering

Verify
whether individual nodes are listed as members of the NSX Manager cluster.

Log in to any one of the nodes and perform one of
these steps to verify whether all nodes are listed as members of the NSX Manager cluster.

1. To
   verify NSX Manager cluster
   status from CLI, perform these steps:
   1. Log in as an admin to any one of the NSX Manager nodes.
   2. run 'get cluster status' to view the correct number of manager nodes
      are listed as members of the cluster and cluster status is STABLE.
2. To verify NSX Manager cluster
   status from UI, perform these steps:
   1. Go to System ? Appliances. Verify the Cluster status is
      STABLE and a correct number of nodes
      are shown to be part of the cluster.
3. To verify NSX Manager cluster
   status from API, run these commands:

   - GET
     /api/v1/cluster/status
   - GET
     api/v1/cluster/nodes or GET
     api/vi/cluster/<node-id>