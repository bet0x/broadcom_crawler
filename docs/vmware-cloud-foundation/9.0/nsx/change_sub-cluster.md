---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/change-sub-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Change Sub-cluster
---

# Change Sub-cluster

When you want to apply a different networking configuration to a host in a sub-cluster, such as a different uplink profile, move the host to a different Sub-cluster.

To change Sub-cluster a host belongs to, perform these steps:

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricHosts.
3. Select the Clusters tab.
4. Select a node and click ActionsChange Sub-cluster.
5. In the Change Sub-cluster window, select a Sub-cluster that the host must be moved to.
6. Click Save.