---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/shutting-down-and-restarting-the-vsan-cluster/shutting-down-the-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Manually Shut Down and Restart the vSAN Cluster
---

# Manually Shut Down and Restart the vSAN Cluster

You can manually shut down the entire vSAN cluster to perform maintenance or troubleshooting.

Use the Shutdown Cluster wizard unless your workflow requires a manual shut down. When you manually shut down the vSAN cluster, do not deactivate vSAN on the cluster.

1. Shut down the vSAN cluster.
   1. Check the vSAN Skyline Health to confirm that the cluster is healthy.
   2. Power off all VMs running in the vSAN cluster, if vCenter is not hosted on the cluster. If vCenter is hosted in the vSAN cluster, do not power off the vCenter VM or service VMs (such as DNS, Active Directory) used by vCenter.
   3. If vSAN file service is enabled in the vSAN cluster, you must deactivate the file service. Deactivating the vSAN file service removes an empty file service domain. If you want to retain the empty file service domain after restarting the vSAN cluster, you must create an NFS or SMB file share before deactivating the vSAN file service.
   4. Click the Configure tab and turn off HA. As a result, the cluster does not register host shutdowns as failures.

      For vSphere 9.0 and later, enable vCLS retreat mode is deprecated. For more information, see the Broadcom knowledge base article [316514](https://knowledge.broadcom.com/external/article/316514).
   5. Verify that all resynchronization tasks are complete. 

      Click the Monitor tab and select vSAN > Resyncing Objects.
   6. If vCenter is hosted on the vSAN cluster, power off the vCenter virtual machine.

      Make a note of the host that runs the vCenter VM. It is the host where you must restart the vCenter VM.
   7. Deactivate cluster member updates from vCenter by running the following command on the ESX hosts in the cluster. Ensure that you run the following command on all the ESX hosts.

      ```
      esxcfg-advcfg -s 1 /VSAN/IgnoreClusterMemberListUpdates
      ```
   8. Log in to any host in the cluster other than the witness host.
   9. Run the following command only on that host. If you run the command on multiple ESX hosts concurrently, it may cause a race condition causing unexpected results.

      ```
      python /usr/lib/vmware/vsan/bin/reboot_helper.py prepare
      ```

      The command returns and prints the following:

      Cluster preparation is done.

      - The cluster is fully partitioned after the successful completion of the command.
      - If you encounter an error, resolve the issue based on the error message and try enabling vCLS retreat mode again.
      - If there are unhealthy or disconnected ESX hosts in the cluster, remove the ESX hosts and retry the command.
   10. Place all the ESX hosts into maintenance mode with No Action. If the vCenter is powered off, use the following command to place the ESX hosts into maintenance mode with No Action.

       ```
       esxcli system maintenanceMode set -e true -m noAction
       ```

       Perform this step on all the hosts.

       To avoid the risk of data unavailability while using No Action at the same time on multiple hosts, followed by a reboot of multiple hosts, see the Broadcom knowledge base article [60424](https://knowledge.broadcom.com/external/article?legacyId=60424). To perform simultaneous reboot of all hosts in the cluster using a built-in tool, see the Broadcom knowledge base article [70650](https://knowledge.broadcom.com/external/article?legacyId=70650).
   11. After all ESX hosts have successfully entered maintenance mode, perform any necessary maintenance tasks and power off the ESX hosts.
2. Restart the vSAN cluster.
   1. Power on the ESX hosts.

      Power on the physical box where ESX is installed. The ESX host starts, locates the VMs, and functions normally.

      If any ESX hosts fail to restart, you must manually recover the ESXhosts or move the bad hosts out of the vSAN cluster.
   2. When all the ESX hosts are back after powering on, exit all ESX hosts from maintenance mode. If the vCenter is powered off, use the following command on the ESX hosts to exit maintenance mode.

      ```
      esxcli system maintenanceMode set -e false
      ```

      Perform this step on all the ESX hosts.
   3. Log in to one of the ESX hosts in the cluster other than the witness ESX host.
   4. Run the following command only on that ESX host. If you run the command on multiple ESX hosts concurrently, it may cause a race condition causing unexpected results.

      ```
      python /usr/lib/vmware/vsan/bin/reboot_helper.py recover
      ```

      The command returns and prints the following:

      Cluster reboot/power-on is completed successfully!
   5. Verify that all the ESX hosts are available in the cluster by running the following command on each ESX host.

      ```
      esxcli vsan cluster get
      ```
   6. Enable cluster member updates from vCenter by running the following command on the ESX hosts in the cluster. Ensure that you run the following command on all the ESX hosts.

      ```
      esxcfg-advcfg -s 0 /VSAN/IgnoreClusterMemberListUpdates
      ```
   7. Restart the vCenter virtual machine if it is powered off. Wait for the vCenter virtual machine to be powered up and running. To deactivate vCLS retreat mode, see the Broadcom knowledge base article [80472](https://knowledge.broadcom.com/external/article?legacyId=80472).
   8. Verify again that all the ESX hosts are participating in the vSAN cluster by running the following command on each ESX host.

      ```
      esxcli vsan cluster get
      ```
   9. Restart the remaining VMs through vCenter.
   10. Check the vSAN Skyline Health and resolve any outstanding issues.
   11. (Optional) Enable vSAN file service.
   12. (Optional) If the vSAN cluster has vSphere Availability enabled, you must manually restart vSphere Availability to avoid the following error: Cannot find vSphere HA master agent.

       To manually restart vSphere Availability, select the vSAN cluster and navigate to:
       1. Configure > Services > vSphere Availability > EDIT > Disable vSphere HA
       2. Configure > Services > vSphere Availability > EDIT > Enable vSphere HA
3. If there are unhealthy or disconnected ESX hosts in the cluster, recover or remove the ESX hosts from the vSAN cluster. If vCenter uses service VMs such as DNS or Active Directory, note them as exceptional VMs in the Shutdown cluster wizard.

   Retry the above commands only after the vSAN Skyline Health shows all available ESX hosts in the green state.

   If you have a three-node vSAN cluster, the command reboot\_helper.py recover cannot work in a one ESX host failure situation. As an administrator, do the following:
   1. Temporarily remove the failure ESX host information from the unicast agent list.
   2. Add the ESX host after running the following command.

      ```
      reboot_helper.py recover
      ```

   Following are the commands to remove and add the ESX host to a vSAN cluster:

   ```
   #esxcli vsan cluster unicastagent remove -a <IP Address> -t node -u <NodeUuid>
   ```

   ```
   #esxcli vsan cluster unicastagent add -t node -u <NodeUuid> -U true -a <IP Address> -p 12321
   ```

Restart the vSAN cluster. See [Restart the vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/shutting-down-and-restarting-the-vsan-cluster/restart-the-vsan-cluster.html#GUID-82bac062-fd14-4690-8873-7b5f02995603-en).