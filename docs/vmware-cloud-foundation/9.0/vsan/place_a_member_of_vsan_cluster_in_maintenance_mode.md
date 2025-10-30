---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode/place-a-member-of-vsan-cluster-in-maintenance-mode.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Place a Member of vSAN Cluster in Maintenance Mode
---

# Place a Member of vSAN Cluster in Maintenance Mode

Before you shut down, reboot, or disconnect an ESX host that is a member of a vSAN cluster, you must place the ESX host in maintenance mode.

Verify that your environment has the capabilities required for the option you select.

When you place an ESX host in maintenance mode, you must select a data evacuation mode, such as Ensure accessibility, Full data migration, or No data migration. When any member ESX host of a vSAN cluster enters maintenance mode, the cluster capacity is automatically reduced, because the member ESX host no longer contributes capacity to the cluster. This also results in the vCLS VMs getting powered off and unregistered.

The vSAN file service virtual machines (FSVM) running on an ESX host are automatically powered off when an ESX host in the vSAN cluster enters maintenance mode.

Any vSAN iSCSI targets served by this ESX host are transferred to other ESX hosts in the vSphere cluster, and thus the iSCSI initiator are redirected to the new target owner.

1. In the vSphere Client, navigate to the cluster.
2. Expand the cluster, right-click the ESX host and select Maintenance Mode > Enter Maintenance Mode.
3. Select a data evacuation mode and click OK. 

   Option | Description || Ensure accessibility | This is the default option. When you power off or remove the ESX host from the cluster, vSAN migrates just enough data to ensure every object is accessible after the ESX host goes into maintenance mode. Select this option if you want to take the ESX host out of the cluster temporarily, for example, to install upgrades, and plan to have the ESX host back in the vSphere cluster. This option is not appropriate if you want to remove the ESX host from the vSphere cluster permanently.  Typically, only partial data evacuation is required. However, the virtual machine might no longer be fully compliant to a virtual machine storage policy during evacuation. That means, it might not have access to all its replicas. If a failure occurs while the ESX host is in maintenance mode and the Failures to tolerate is set to 1, you might experience data loss in the cluster. This is the only evacuation mode available if you are working with a three-host cluster or a vSAN cluster configured with three fault domains. |
   | Full data migration | vSAN evacuates all data to other ESX hosts in the vSphere cluster and maintains the current object compliance state. Select this option if you plan to migrate the ESX host permanently. When evacuating data from the last ESX host in the vSphere cluster, make sure that you migrate the virtual machines to another datastore and then place the ESX host in maintenance mode.  This evacuation mode results in the largest amount of data transfer and consumes the most time and resources. All the components on the local storage of the selected ESX host are migrated elsewhere in the vSphere cluster. When the ESX host enters maintenance mode, all virtual machines have access to their storage components and are still compliant with their assigned storage policies.  If there are objects in reduced availability state, this mode maintains this compliance state and does not guarantee that the objects will become compliant.  If a virtual machine object that has data on the host is not accessible and is not fully evacuated, the host cannot enter maintenance mode. |
   | No data migration | vSAN does not evacuate any data from this ESX host. If you power off or remove the ESX host from the vSphere cluster, some virtual machines might become inaccessible. |

   A vSphere cluster with three fault domains has the same restrictions that a three-host vSphere cluster has, such as the inability to use Full data migration mode or to reprotect data after a failure.

   Alternatively, you can place an ESX host in the maintenance mode by using ESXCLI. Before placing an ESX host in this mode, ensure that you powered off the virtual machines that running on the ESX host.

   To perform an action before entering maintenance mode, run the following command on the ESX host:

   ```
   esxcli system maintenanceMode set --enable 1 --vsanmode=<str>
   ```

   Following are the string values allowed for vsanmode:
   - ensureObjectAccessibility - Evacuate data from the disk to ensure object accessibility in the vSAN cluster, before entering maintenance mode.

     The default value is ensureObjectAccessibility. This value will be used if you do not specify any value for the vsanmode.
   - evacuateAllData - Evacuate all data from the disk before entering maintenance mode.
   - noAction - Do not move vSAN data out of the disk before entering maintenance mode.

   To verify the status of the ESX host, run the following command:

   ```
   esxcli system maintenanceMode get
   ```

   To exit maintenance mode, run the following command:

   ```
   esxcli system maintenanceMode set --enable 0
   ```

You can track the progress of data migration in the cluster.