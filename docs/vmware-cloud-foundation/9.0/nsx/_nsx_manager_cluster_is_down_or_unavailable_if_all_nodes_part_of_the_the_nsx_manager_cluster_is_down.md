---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/nsx-manager-cluster-is-down-or-unavailable-if-all-or-some-of-the-cluster-nodes-are-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Manager cluster is DOWN or UNAVAILABLE if all nodes part of the the NSX Manager cluster is down or majority nodes are down
---

# NSX Manager cluster is DOWN or UNAVAILABLE if all nodes part of the the NSX Manager cluster is down or majority nodes are down

NSX Manager is down or unavailable if majority of
the nodes in the cluster are down.

NSX Manager UI will fail to load with following error
Some appliance components are not functioning properly. Component
health: POLICY:UNKNOWN, MANAGER:UNKNOWN, SEARCH:UNKNOWN, NO and
clustering related commands will fail using the CLI and API.

1. SSH to each of the affected
   NSX Manager nodes and run
   following commands: 
   1. Run
      get
      file-system-stats and verify /config and /image is not
      100% full.
   2. Run
      get
      core-dumps to verify no cores have gotten generated in
      NSX Manager.
   3. Verify there was no
      datastore outage. See
      [NSX Manager Cluster status Degraded As Datastore-related Components Are Down](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/nsx-manager-cluster-status-is-degraded-as-datastore-components-are-down.html).
   4. Check logs for
      out-of-memory errors. See
      /var/log/proton/proton-tomcat-wrapper.log
2. To restore clustering and UI,
   any two nodes in a three node cluster must be up. If you are not able to bring
   any failed node back up, but if there is a healthy node available, then do one
   of the following steps to restore clustering: 
   - Deploy a new manager
     node (as 4th member node), join the existing cluster and then detach one of
     the failed nodes using CLI cmd
     detach node
     <node-uuid> or API
     POST
     /api/v1/cluster/<node-uuid>?action=remove\_node. The
     commands should be executed from one of the healthy nodes. Alternatively,
     you can follow the next bulleted point to deactivate the cluster.
   - (Optional) Run the
     deactivate cluster command on active node such that
     you end up with single node cluster. Now continue to add the new additional
     nodes to make a 3-member
     NSX Manager cluster.

     NSX Manager nodes that are
     removed from the cluster should be powered off and deleted.