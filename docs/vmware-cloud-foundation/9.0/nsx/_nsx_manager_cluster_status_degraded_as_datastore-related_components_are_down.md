---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/nsx-manager-cluster-status-is-degraded-as-datastore-components-are-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Manager Cluster status Degraded As Datastore-related Components Are Down
---

# NSX Manager Cluster status Degraded As Datastore-related Components Are Down

NSX Manager status is degraded due to DATASTORE component and/or CORFU\_NONCONFIG component down on one or more manager nodes member of NSX Cluster.

1. SSH to NSX Manager CLI terminal as an admin.
2. To identify the manager node with components down, run get cluster status.
3. Verify underlying datastore is available with recommended disk access latency. To get and fix the disk access latency numbers, see Knowledge Base article 316654: [Storage latency causes NSX Manager cluster instability](https://knowledge.broadcom.com/external/article?articleNumber=316654).

   Datastore outage can cause NSX Manager appliance VMs to go into read-only mode. Linux does not provide a usable utility to recover from this error. Follow the KB, Recover NSX Manager upon storage outage, if appliance reboot does not fix the issue. Verify backend datastore has fully recovered before rebooting the affected NSX Manager VM.
4. To verify no disk partition consumed by NSX is full or close-to-full, run ‘get filesystem-stats'.

   Datastore specific logs can be found at var/log/corfu/corfu.9000.log and /var/log/corfu/tanuki.log.
5. Clean up disk space and / or reboot all NSX Manager nodes (after storage issues are resolved) to remove the read-only mode.
6. If components continue to be down, contact VMware Support.

   With the datastore down, the NSX Manager continues to participate in the cluster if its network connectivity is up. This state might result in the management plane and control plane to become unavailable. If datastore issue cannot be resolved, replace the impacted NSX Manager by powering off the impacted NSX Manager (as long as cluster quorum is maintained by having majority number of nodes up).
7. Remove NSX Manager node from existing NSX Manager Cluster. On the NSX Manager, run detach node <node-id>.
8. Verify the problematic node is not a member of the cluster anymore by running the get cluster status.
9. Deploy a new NSX Manager node and join it to the existing Manager Cluster.