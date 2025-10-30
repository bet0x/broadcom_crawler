---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/view-host-inventory.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > View ESX Host Inventory
---

# View ESX Host Inventory

The Hosts page in the vSphere Client displays details about all the ESX hosts in the global inventory, including CPU utilization and memory usage across all hosts, as well as the total number of hosts used and unallocated.

For each ESX host, the Hosts page displays details, including name, status, vSphere cluster, and CPU and memory usage.

The Hosts page also provides controls for commissioning hosts.

1. In the vSphere Client, click Global Inventory ListsHosts.
2. Click Assigned Hosts to see a list of ESX hosts that are assigned to a workload domain.

   You can view details about each ESX host, including name, vSphere cluster, and CPU and memory usage. Click the host name to view more details about the host in the vSphere inventory. Click the vSphere cluster name to view more details about the cluster in the vSphere inventory.
3. Click Unassigned Hosts to see a list of commissioned ESX hosts that are available to create a new workload domain or add to an existing workload domain.

   You can view details about commissioned ESX hosts and also commission and decommission ESX hosts from the Unassigned Hosts tab.