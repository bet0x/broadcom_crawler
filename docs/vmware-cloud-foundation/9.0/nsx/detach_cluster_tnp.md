---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/detach-cluster-tnp.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Detach Cluster TNP
---

# Detach Cluster TNP

When you want to apply a different cluster TNP, detach the existing one before applying a new TNP.

To detach cluster TNP, perform these steps:

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricHosts.
3. Select the Clusters tab.
4. Select a cluster and click ActionsDetach Transport Node Profile.

   NSX detached the existing cluster TNP. At the end of the action, the cluster will not have any TNP applied to it.