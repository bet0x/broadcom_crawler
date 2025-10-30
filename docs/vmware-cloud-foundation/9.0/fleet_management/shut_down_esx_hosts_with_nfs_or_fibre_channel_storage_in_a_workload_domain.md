---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-esx-hosts/shut-down-esx-hosts-with-non-vsan--storage.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down ESX Hosts with NFS or Fibre Channel Storage in a Workload Domain
---

# Shut Down ESX Hosts with NFS or Fibre Channel Storage in a Workload Domain

You use the vSphere Client to shut down gracefully the clusters with non-vSAN in a workload domain.

1. Identify the vCenter instance that runs the vCenter appliance for this workload domain.

   This cluster must be shut down last.
2. Log in to vCenter for the workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. In the Hosts and Clusters inventory, for a cluster that is not running the vCenter appliance for the workload domain, put all hosts in the cluster in maintenance mode.

   These operations take several minutes to complete.
4. If a cluster is running the vCenter appliance, note down the host on which it is running and put all hosts in the cluster but this one in maintenance mode.

   You need the details about this host during the startup process too.
5. Shut down the hosts in maintenance mode
   1. Select the cluster and click the Hosts tab.
   2. Select all hosts that are in maintenance mode, right-click PowerShut Down.

      This operation takes several minutes to complete
6. Repeat Step 3 to Step 4 for all clusters with non-vSAN storage in the domain.
7. If the vCenter appliance is running on one of the ESX hosts in the cluster, shut down the vCenter appliance and the host from the VMware Host Client.
   1. Log in to the ESX host at https://<esx\_fqdn> as a user with the Administrator role.
   2. In the left plane, click Virtual Machines.
   3. Locate the vCenter appliance for the workload domain.
   4. Right-click the appliance and select PowerShut down Guest OS.
   5. In the confirmation dialog box, click Yes.

      This operation takes several minutes to complete.
   6. In the left plane, right-click on HostShut down.
   7. Read the warning and click Shut down.

      You lose connectivity to the ESX host. The shut down operation takes several minutes to complete.
8. Shut down the storage for the workload domain if there are no other workloads that use it.

   Follow vendor 's documentation to check if there are active clients and how to shut it down in a safe manner.