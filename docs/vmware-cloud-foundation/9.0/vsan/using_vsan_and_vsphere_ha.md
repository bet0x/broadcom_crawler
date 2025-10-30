---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-virtual-san-and-vsphere-ha.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using vSAN and vSphere HA
---

# Using vSAN and vSphere HA

You can enable vSphere HA and vSAN on the same cluster. vSphere HA provides the same level of protection for virtual machines on vSAN datastores as it does on traditional datastores. This level of protection imposes specific restrictions when vSphere HA and vSAN interact.

## ESX Host Requirements

You can use vSAN with a vSphere HA cluster only if the following conditions are met:

- The cluster's ESX hosts all must be version 9.0 or later.
- The cluster must have a minimum of three ESX hosts, unless it is a vSAN two-host cluster. For best results, configure the vSAN cluster with four or more hosts.

vSAN supports Proactive HA. Select the following remediation method: Maintenance mode for all failures. Quarantine mode is supported, but it does not protect against data loss if the host in quarantine mode fails, and there are objects with FTT=0 or objects with FTT=1 that are degraded.

## Networking Differences

vSAN uses its own logical network. When vSAN and vSphere HA are enabled for the same cluster, the HA interagent traffic flows over this storage network rather than the management network. vSphere HA uses the management network only when vSAN is turned off. vCenter chooses the appropriate network when vSphere HA is configured on a host.

Make sure vSphere HA is not enabled when you enable vSAN on the cluster. Then you can re-enable vSphere HA.

When a virtual machine is only partially accessible in all network partitions, you cannot power on the virtual machine or fully access it in any partition. For example, if you partition a cluster into P1 and P2, the VM namespace object is accessible to the partition named P1 and not to P2. The VMDK is accessible to the partition named P2 and not to P1. In such cases, the virtual machine cannot be powered on and it is not fully accessible in any partition .

The following table shows the differences in vSphere HA networking whether or not vSAN is used.

vSphere HA Networking Differences



|  | vSAN On | vSAN Off |
| --- | --- | --- |
| Network used by vSphere HA | vSAN storage network | Management network |
| Heartbeat datastores | Any datastore mounted to more than one host, but not vSAN datastores | Any datastore mounted to more than one host |
| Host declared isolated | Isolation addresses not pingable and vSAN storage network inaccessible | Isolation addresses not pingable and management network inaccessible |

If you change the vSAN network configuration, the vSphere HA agents do not automatically acquire the new network settings. To change the vSAN network, you must re-enable host monitoring for the vSphere HA cluster:

1. Deactivate Host Monitoring for the vSphere HA cluster.
2. Make the vSAN network changes.
3. Right-click all hosts in the cluster and select Reconfigure HA.
4. Reactivate Host Monitoring for the vSphere HA cluster.

You can disable the default gateway by setting das.usedefaultisolationaddresss and das.isolationaddress0 to an address on the vSAN network. For more information, see [Using an Isolation address to ensure HA functionality in a vSAN environment](https://knowledge.broadcom.com/external/article/313763/using-an-isolation-address-to-ensure-ha.html).

## Capacity Reservation Settings

When you reserve capacity for your vSphere HA cluster with an admission control policy, this setting must be coordinated with the corresponding Failures to tolerate policy setting in the vSAN rule set. It must not be lower than the capacity reserved by the vSphere HA admission control setting. For example, if the vSAN rule set allows for only two failures, the vSphere HA admission control policy must reserve capacity that is equivalent to only one or two host failures. If you are using the Percentage of Cluster Resources Reserved policy for a cluster that has eight hosts, you must not reserve more than 25 percent of the cluster resources. In the same cluster, with the Failures to tolerate policy, the setting must not be higher than two hosts. If vSphere HA reserves less capacity, failover activity might be unpredictable. Reserving too much capacity overly constrains the powering on of virtual machines and inter cluster vSphere vMotion migrations. For information about the Percentage of Cluster Resources Reserved policy, see the [vSphere Availability](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-availability.html) guide.

## vSAN and vSphere HA Behavior in a Multiple Host Failure

After a vSAN cluster fails with a loss of failover quorum for a virtual machine object, vSphere HA might not be able to restart the virtual machine even when the cluster quorum has been restored.  vSphere HA guarantees the restart only when it has a cluster quorum and can access the most recent copy of the virtual machine object. The most recent copy is the last copy to be written.

Consider an example where a vSAN virtual machine is provisioned to tolerate one host failure. The virtual machine runs on a vSAN cluster that includes three hosts, H1, H2, and H3. All three hosts fail in a sequence, with H3 being the last host to fail.

After H1 and H2 recover, the cluster has a quorum (one host failure tolerated). Despite this quorum, vSphere HA is unable to restart the virtual machine because the last host that failed (H3) contains the most recent copy of the virtual machine object and is still inaccessible.

In this example, either all three hosts must recover at the same time, or the two-host quorum must include H3. If neither condition is met, HA attempts to restart the virtual machine when host H3 is online again.