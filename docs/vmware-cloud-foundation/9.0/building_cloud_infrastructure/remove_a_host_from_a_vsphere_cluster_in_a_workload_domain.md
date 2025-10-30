---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/reduce-a-workload-domain-1/remove-a-host-from-a-cluster-in-a-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Remove a Host from a vSphere Cluster in a Workload Domain
---

# Remove a Host from a vSphere Cluster in a Workload Domain

You can remove a host from a vSphere cluster in the management domain or a VI workload domain through the Workload Domains page in SDDC Manager UI.

- Delete any workload virtual machines created outside VMware Cloud Foundation or move them to another host.
- You cannot remove a host from a vSphere cluster if that host is hosting an NSX Edge node.
  - Move the NSX Edge node to another host in the same vSphere cluster. You cannot move an NSX Edge node to a host that already hosts another NSX Edge node.
  - If you cannot move the NSX Edge node, delete the NSX Edge node on the host. You cannot delete NSX Edge nodes if doing so would result in an NSX Edge cluster with fewer than two NSX Edge nodes.
- You cannot remove a host from a vSphere cluster if that vSphere cluster was selected for NSX Edge node placement and the NSX Edge node deployment is still in pending state.

Before you remove a host from a vSphere cluster, ensure that you have enough hosts remaining to facilitate the configured vSAN availability. Failure to do so might result in the datastore being marked as read-only or in data loss.

You can add hosts to or remove hosts from multiple different vSphere clusters in parallel. For example, you remove three hosts from Cluster A, and while that task is running, you can start a separate task to remove (or add) four hosts to Cluster B. See [VMware Configuration Maximums](https://configmax.esp.vmware.com/home) for information about the maximum number of add/remove hosts tasks that you can run in parallel.

1. In the navigation pane, click InventoryWorkload Domains.
2. In the workload domains table, click the name of the workload domain that you want to modify.
3. Click the Clusters tab.
4. Click the name of the cluster from which you want to remove a host.
5. Click the Hosts tab.
6. Select the host to remove and click Remove Selected Hosts. 

   An alert appears, asking you to confirm or cancel the action. If the removal results in the number of hosts in the vSphere cluster being less than the minimum number of required hosts, you must click Force Remove to remove the host.
7. Click Remove to confirm the action. 

   The details page for the cluster appears with a message indicating that the host is being removed. When the removal process is complete, the host is removed from the hosts table.

Decommission the host. See [Decommission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/decommission-hosts.html#GUID-5eff3df4-8366-4ea4-82f4-5b2c80ae577d-en). After you decommission a host, you must re-image it and commission it before you can use it again.