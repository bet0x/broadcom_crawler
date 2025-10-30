---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/using-the-vmkernel-observations-for-creating-vsan-alarms.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >  Using the VMkernel Observations for Creating vSAN Alarms
---

# Using the VMkernel Observations for Creating vSAN Alarms

VMkernel Observations (VOBs) are system events that you can use to set up vSAN alarms.

vSAN alarms are used for monitoring and troubleshooting performance and networking issues in the vSAN cluster. In vSAN, these events are known as observations.

## VMware ESX Observation IDs for vSAN

Each VOB event is associated with an identifier (ID). Before you create a vSAN alarm in the vCenter, you must identify an appropriate VOB ID for the vSAN event for which you want to create an alert. You can create alerts in the VMware ESX Observation Log file (vobd.log). For example, use the following VOB IDs to create alerts for any device failures in the cluster.

- esx.problem.vob.vsan.lsom.diskerror
- esx.problem.vob.vsan.pdl.offline

To review the list of VOB IDs for vSAN, open /usr/lib/vmware/hostd/extensions/hostdiag/locale/en/event.vmsg file located on your ESX host in the /var/log directory. The log file contains the following VOB IDs that you can use for creating vSAN alarms.

VOB IDs for vSAN



| VOB ID | Description |
| --- | --- |
| esx.audit.vsan.clustering.enabled | The vSAN clustering service is enabled. |
| esx.clear.vob.vsan.pdl.online | The vSAN device has come online. |
| esx.clear.vsan.clustering.enabled | The vSAN clustering service is enabled. |
| esx.clear.vsan.vsan.network.available | vSAN has one active network configuration. |
| esx.clear.vsan.vsan.vmknic.ready | A previously reported vmknic has acquired a valid IP. |
| esx.problem.vob.vsan.lsom.componentthreshold | vSAN reaches the near node component count limit. |
| esx.problem.vob.vsan.lsom.diskerror | A vSAN device is in a permanent error state. |
| esx.problem.vob.vsan.lsom.diskgrouplimit | vSAN fails to create a disk group. |
| esx.problem.vob.vsan.lsom.disklimit | vSAN fails to add devices to a disk group. |
| esx.problem.vob.vsan.lsom.diskunhealthy | vSAN disk is unhealthy. |
| esx.problem.vob.vsan.pdl.offline | A vSAN device is offline. |
| esx.problem.vsan.clustering.disabled | vSAN clustering services are not enabled. |
| esx.problem.vsan.lsom.congestionthreshold | vSAN device memory or SSD congestion has been updated. |
| esx.problem.vsan.net.not.ready | A vmknic is added to vSAN network configuration without a valid IP address. This happens when the vSAN network is not ready. |
| esx.problem.vsan.net.redundancy.lost | The vSAN network configuration does not have the required redundancy. |
| esx.problem.vsan.no.network.connectivity | vSAN does not have existing networking configuration, which is in use. |
| esx.problem.vsan.vmknic.not.ready | A vmknic is added to the vSAN network configuration without a valid IP address. |
| esx.problem.vob.vsan.lsom.devicerepair | The vSAN device is offline and in a repaired state because of I/O failures. |
| esx.problem.vsan.health.ssd.endurance | One or more vSAN disks exceed the warning usage of estimated endurance threshold. |
| esx.problem.vsan.health.ssd.endurance.error | A vSAN disk exceeds the estimated endurance threshold. |
| esx.problem.vsan.health.ssd.endurance.warning | A vSAN disk exceeds 90% of its estimated endurance threshold. |