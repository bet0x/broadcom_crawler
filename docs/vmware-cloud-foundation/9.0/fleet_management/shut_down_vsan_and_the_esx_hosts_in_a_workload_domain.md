---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-esx-hosts/shut-down-vsan-and-the-esxi-hosts-in-the-virtual-infrastructure-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down vSAN and the ESX Hosts in a Workload Domain
---

# Shut Down vSAN and the ESX Hosts in a Workload Domain

You use the vSAN shutdown cluster wizard in the vSphere Client to shut down gracefully the vSAN clusters in a workload domain. The wizard shuts down the vSAN storage and the ESX hosts added to the cluster.

You perform this operation on all vSAN clusters in all workload domains.

1. Identify the vCenter instance that runs the vCenter VM for this workload domain.

   If the vCenter VM is running on the infrastructure that it manages, note down the cluster in which it is running. This cluster must be stopped last.
2. Log in to vCenter for the workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. For a vSAN cluster, verify the vSAN health and resynchronization status.
   1. Select the cluster and click the Monitor tab.
   2. In the left pane, navigate to vSANSkyline health and verify the status of each vSAN health check category.
   3. In the left pane, under vSANResyncing objects, verify that all synchronization tasks are complete.
4. If any member host is in lockdown mode, add the host's root account to the Exception Users list.
   1. Select the host in the inventory and click the Configure tab.
   2. In the left pane, select SystemSecurity Profile.
   3. In the Lockdown Mode pane, click the Edit button.
   4. On the Exception Users page, enter root and click Add User.
   5. Click OK.
5. Shut down the vSAN cluster.
   1. In the inventory, right-click the vSAN cluster and select vSANShutdown cluster.
   2. In the Shutdown Cluster wizard, verify that all pre-checks are green and click Next.
   3. Review the vCenter Server notice and click Next.
   4. If vCenter is running on the selected cluster, note the orchestration host details.

      Connection to vCenter is lost because the vSAN shutdown cluster wizard shuts it down. The shutdown operation is complete after all ESXi hosts are stopped.
   5. Enter a reason for performing the shutdown, and click Shutdown.
6. Repeat Step 3 to Step 5 for other vSAN clusters in the domain.