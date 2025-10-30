---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-the-esx-hosts/restart-clusters-in-a-workload-domains-without-vsan-storage.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restart the Clusters in a Workload Domains with NFS or Fibre Channel Storage Storage
---

# Restart the Clusters in a Workload Domains with NFS or Fibre Channel Storage Storage

You use the vSphere Client to restart the clusters with non-vSAN storage in a workload domain.

All hosts are started

Verify that all ESXi hosts in the cluster are connected to the workload domain vCenter Server.

1. Log in to vCenter for the workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
2. Check that all hosts in the cluster are connected to vCenter.
3. Exit maintenance mode for all hosts in the cluster.

   This operations takes several minutes to complete.
4. Repeat Step 2 and Step 3 for all clusters with non-vSAN storage in the domain.