---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-esx-hosts-and-vcenter-server-in-management-domain/start-vsan-and-the-esxi-hosts-in-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start vSAN and the ESX Hosts in the Management Domain
---

# Start vSAN and the ESX Hosts in the Management Domain

You start the ESX hosts using an out-of-band management interface, such as, ILO or iDRAC to connect to the hosts and power them on. Then, restarting the vSAN cluster starts automatically vCenter and vSAN.

You perform this operation on all vSAN clusters in the management domain. You must start with the cluster that hosts the management vCenter.

1. Power on the first ESX host in the management domain.
   1. Log in to the first ESX host in the domain by using the out-of-band management interface.
   2. Power on the ESX host according to the hardware vendor guide.
2. Repeat the previous step to start all the remaining ESX hosts in the management domain.

   This operation takes several minutes to complete.

   vCenter is started automatically. Wait until vCenter is running and the vSphere Client is available again.
3. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
4. Restart the vSAN cluster.
   1. In the Hosts and Clusters inventory, right-click the vSAN cluster and select vSANRestart cluster.
   2. In the Restart Cluster dialog box, click Restart. 

      The vSAN Services page on the Configure tab changes to display information about the restart process.
5. After the cluster has been restarted, check the vSAN health service and resynchronization status, and resolve any outstanding issues.
   1. Select the cluster and click the Monitor tab.
   2. In the left pane, under vSANResyncing objects, verify that all synchronization tasks are complete.
   3. In the left pane, navigate to vSANSkyline health and verify the status of each vSAN health check category.
6. If you have added the root user of the ESXi hosts to the Exception Users list for lockdown mode during shutdown, remove the user from the list on each host. 
   1. Select the host in the inventory and click the Configure tab.
   2. In the left pane, select SystemSecurity Profile.
   3. In the Lockdown Mode pane, click the Edit button.
   4. On the Exception Users page, from the vertical ellipsis menu in front of the root user, select Remove User and click OK.