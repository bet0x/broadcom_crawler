---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-the-esx-hosts-in-management-domain/shut-down-esx-hosts-without-vsan-storage.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down ESX Hosts with NFS or Fibre Channel Storage in the Management Domain
---

# Shut Down ESX Hosts with NFS or Fibre Channel Storage in the Management Domain

You use the vSphere Client to shut down gracefully the clusters in a management domain with a principal storage that is differnet from vSAN.

1. Identify the cluster that hosts the management vCenter for this management domain.

   This cluster must be shut down last.
2. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. In the Hosts and Clusters inventory, for a cluster that is not running the management vCenter, put all hosts in the cluster in maintenance mode.

   These operations take several minutes to complete.
4. If a cluster is running the management vCenter, note down the host on which it is running and put all hosts in the cluster but this one in maintenance mode.

   You need the details about this host during the startup process too.
5. Shut down the hosts in maintenance mode.
   1. Select the cluster and click the Hosts tab.
   2. Select all hosts that are in maintenance mode, right-click PowerShut Down

      This operation takes several minutes to complete.
6. Repeat Step 3 to Step 5 for all clusters with NFS and Fibre Channel storage in the domain.
7. If vCenter is running on one of the ESX hosts in the cluster, shut down the vCenter appliance and the host from the VMware Host Client.
   1. Log in to the ESX host at https://<esx\_fqdn> as a user with the Administrator role.
   2. In the left pane, click Virtual Machines.
   3. Locate the vCenter appliance for the domain.
   4. Right-click the virtual machine and select PowerShut down Guest OS.
   5. In the confirmation dialog box, click Yes.

      This operation takes several minutes to complete.
   6. In the left plane, right-click on HostShut down.
   7. Read the warning and click Shut down.

      You lose connectivity to the ESX host. The shutdown operation takes several minutes to complete.
8. Shut down the storage for the management domain if there are no other workloads that use it.

   Follow vendor 's documentation to check if there are active clients and how to shut it down in a safe manner.