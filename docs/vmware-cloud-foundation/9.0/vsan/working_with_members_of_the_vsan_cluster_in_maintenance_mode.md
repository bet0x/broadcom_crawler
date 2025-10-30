---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Working with Members of the vSAN Cluster in Maintenance Mode
---

# Working with Members of the vSAN Cluster in Maintenance Mode

Before you shut down, reboot, or disconnect an ESX host that is a member of a vSAN cluster, you must put the ESX host in maintenance mode.

When working with maintenance mode, consider the following guidelines:

- When you place an ESX host in maintenance mode, you must select a data evacuation mode, such as Ensure accessibilityFull data migration or No data migration. Ensure accessibility is the default option and moves data, if necessary.
- When any member ESX host of a vSAN cluster enters maintenance mode, the cluster capacity automatically reduces as the member ESX host no longer contributes storage to the vSAN cluster.
- A virtual machine's compute resources might not reside on the ESX host that is being placed in maintenance mode, and the storage resources for virtual machines might be located anywhere in the vSAN cluster.
- The Ensure accessibility mode is faster than the Full data migration mode because the Ensure accessibility migrates only the components from the hosts that are essential for running the virtual machines. When in this mode, if you encounter a failure, the availability of your virtual machine is affected. Selecting the Ensure accessibility mode does not reprotect your data during failure and you might experience unexpected data loss.
- The Enhanced durability mode helps to store the incremental data writes in case an unexpected host failure occurs within your cluster while a host is in the maintenance mode. The ESX host can enter maintenance mode when the objects in the cluster use failure to tolerate (FTT) of 1 and Ensure accessibility evacuation mode.
- When you select the Full data migration mode, your data is automatically reprotected against a failure, if the resources are available and the Failures to tolerate set to 1 or more. When in this mode, all components from the ESX host are migrated and, depending on the amount of data you have on the ESX host, the migration might take longer. With Full data migration mode, your virtual machines can tolerate failures, even during planned maintenance.
- When working with a three-host cluster, you cannot place a server in maintenance mode with Full data migration. Consider designing a vSAN cluster with four or more ESX hosts for maximum availability.

Before you place an ESX host in maintenance mode, you must verify the following:

- If you are using Full data migration mode, verify that the cluster has enough ESX hosts and capacity available to meet the Failures to tolerate policy requirements.
- Verify that enough flash capacity exists on the remaining ESX hosts to handle any flash read cache reservations. To analyze the current capacity use per ESX host, and whether a single ESX host failure might cause the cluster to run out of space and impact the vSAN cluster capacity, cache reservation, and cluster components, use the data migration pre-check tests. For more information, see [Check the Data Migration Capabilities of an ESX Host in the vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode/check-the-data-migration-capabilities-of-a-host-in-the-vsan-cluster.html).
- Verify that you have enough capacity devices in the remaining ESX hosts to handle stripe width policy requirements, if selected.
- Make sure that you have enough free capacity on the remaining ESX hosts to handle the amount of data that must be migrated from the ESX host entering maintenance mode.

The Confirm Maintenance Mode dialog box provides information to guide your maintenance activities. You can view the impact of each data evacuation option.

- Whether or not sufficient capacity is available to perform the operation.
- How much data will be moved.
- How many objects will become non-compliant.
- How many objects will become inaccessible.