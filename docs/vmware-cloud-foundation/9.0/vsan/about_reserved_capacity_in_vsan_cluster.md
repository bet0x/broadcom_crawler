---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-reserved-capacity-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > About Reserved Capacity in vSAN Cluster
---

# About Reserved Capacity in vSAN Cluster

vSAN requires capacity for its internal operations.

For a cluster to be able to tolerate a single ESX host failure, vSAN requires free space to restore the data of the failed host. You can reserve the amount of the largest host to ensure that that the data can be recreated. These values are represented as thresholds in the Capacity Monitor page:

- Operations threshold - Displays the space vSAN requires to run its internal operations in the cluster. If the used space exceeds the operations threshold, vSAN might not operate properly.
- Host rebuild threshold - Displays the space vSAN requires to tolerate one host failure. If the used space exceeds the host rebuild threshold and the host fails, vSAN might not successfully restore all data from the failed host.

For more information on the capacity thresholds, see [Monitor vSAN Capacity](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/monitor-vsan-capacity.html#GUID-ee5621f6-c377-4336-ab96-a03156582f0b-en).

The reserved capacity is not supported on a vSAN stretched cluster, cluster with fault domains and nested fault domains, two-node cluster, or if the number of ESX hosts in the cluster is less than four.

vSAN provides you the option to reserve the capacity in advance so that it has enough free space available to perform internal operations and to repair data back to compliance following a single host failure. By enabling reserve capacity in advance, vSAN prevents you from using the space to create workloads and intends to save the capacity available in a cluster. By default, the reserved capacity is not enabled.

If there is enough free space in the vSAN cluster, you can enable the operations reserve and/or the host rebuild reserve.

- Operations reserve - Reserved space in the cluster for vSAN internal operations.
- Host rebuild reserve - Reserved space for vSAN to be able to repair in case of a single host failure.

These soft reservations prevent the creation of new VMs or powering on VMs if such operations consume the reserved space. Once the reserved capacity is enabled, vSAN does not prevent powered on VM operations, such as I/O from the guest operating system or applications from consuming the space even after the threshold limits are reached. After you enable the reserved capacity, you must monitor the disk space health alerts and capacity usage in the cluster and take appropriate actions to keep the capacity usage below the threshold limits.

To enable reserved capacity for the host rebuild, you must first enable the operations reserve. When you enable operations reserve, vSAN reserves 5% additional capacity in the operations reserve as a buffer to ensure you have time to react to the capacity fullness before the actual threshold is reached.

vSAN indicates when the capacity usage is high in a cluster. The indications can be in the form of health alerts, capacity chart turning yellow or red, and so on. Due to the reservation, vSAN might not have enough free space left. This results in the inability to create VMs or VM snapshots, creating or extending virtual disks, and so on.

You cannot enable reserved capacity, if the cluster is at a capacity higher than the specified threshold.

## Capacity Reservation Considerations

Following are the considerations if you enable reserved capacity:

- When you enable reserved capacity with the host rebuild reserve and place a host into maintenance mode, the host might not come back online. In this case, vSAN continues to reserve capacity for another host failure, on top of the one already in maintenance mode. If the capacity usage exceeds the host rebuild threshold, this can cause operations to fail.
- When you enable reserved capacity with the host rebuild reserve and a host fails, vSAN might not start repairing the affected objects until the repair timer expires. During this time, vSAN continues to reserve capacity for another host failure. This can cause failure of operations if the capacity usage is above the current host rebuild threshold, after the first host failure. After the repairs are complete, you can deactivate the reserved capacity for the host rebuild reserve if the cluster does not have the capacity for another host failure.