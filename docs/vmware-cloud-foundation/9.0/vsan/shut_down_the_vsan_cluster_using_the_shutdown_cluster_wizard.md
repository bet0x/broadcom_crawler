---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/shutting-down-and-restarting-the-vsan-cluster/shut-down-the-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Shut Down the vSAN Cluster Using the Shutdown Cluster Wizard
---

# Shut Down the vSAN Cluster Using the Shutdown Cluster Wizard

Use the Shutdown cluster wizard to gracefully shut down the vSAN cluster for maintenance or troubleshooting.

Ensure vSAN client clusters have unmounted any vSAN datastores or vSAN storage clusters that have been shared.

The Shutdown Cluster Wizard is available with vSAN 9.0 and later releases.

1. Prepare the vSAN cluster for shutdown. 
   1. Check the vSAN Skyline Health to confirm that the cluster is healthy.
   2. Power off all virtual machines stored in the vSAN cluster, except for vCenter virtual machines and file service virtual machines. If vCenter is hosted on the vSAN cluster, do not power off the vCenter virtual machine or virtual machine service virtual machines (such as DNS, Active Directory) used by vCenter.
   3. If this is an vSAN HCI Datastore Sharing server cluster, power off all client virtual machines stored on the cluster. If the client cluster's vCenter virtual machine is stored on this cluster, either migrate or power off the virtual machine. Once this server cluster is shutdown, its shared datastore is inaccessible to clients.
   4. Verify that all resynchronization tasks are complete. 

      Click the Monitor tab and select vSAN > Resyncing Objects.

   If any member ESX hosts are in lockdown mode, add the host's root account to the security profile Exception User list. For more information, see the [vSphere Security](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-security.html) guide.
2. Right-click the vSAN cluster in the vSphere Client, and select menu Shutdown cluster.

   You also can click Shutdown Cluster on the vSAN Services page.
3. On the Shutdown cluster wizard, verify that the Shutdown pre-checks are green checks. Resolve any issues that are red exclamations. Click Next. 

   If vCenter appliance is deployed on the vSAN cluster, the Shutdown cluster wizard displays the vCenter notice. Note the IP address of the orchestration host, in case you need it during the cluster restart. If vCenter uses service virtual machines such as DNS or Active Directory, note them as exceptional virtual machines in the Shutdown cluster wizard.
4. Select a reason for performing the shutdown, and click Shutdown.

   The vSAN Services page changes to display information about the shutdown process.
5. Monitor the shutdown process. 

   vSAN performs the steps to shutdown the cluster, powers off the system virtual machines, and powers off the ESX hosts.

Restart the vSAN cluster. See [Restart the vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/shutting-down-and-restarting-the-vsan-cluster/restart-the-vsan-cluster.html#GUID-82bac062-fd14-4690-8873-7b5f02995603-en).