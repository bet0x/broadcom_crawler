---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-vsan-cluster-resynchronization.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > About vSAN Cluster Resynchronization
---

# About vSAN Cluster Resynchronization

You can monitor the status of virtual machine objects that are being resynchronized in the vSAN cluster.

When a hardware device, ESX host, or network fails, or if a ESX host is placed into maintenance mode, vSAN initiates resynchronization in the vSAN cluster. However, vSAN waits 60 minutes for the failed components to come back online before initiating resynchronization tasks.

The following events trigger resynchronization in the cluster:

- Editing a virtual machine (VM) storage policy. When you change VM storage policy settings, vSAN might initiate object recreation and subsequent resynchronization of the objects.

  Certain policy changes such as changing the stripe width might cause vSAN to create another version of an object and synchronize it with the previous version. When the synchronization is complete, the original object is discarded.

  vSAN ensures that VMs continue to run and are not interrupted by this process. This process might require additional temporary capacity.
- Restarting an ESX host after a failure.
- Recovering ESX hosts from a permanent or long-term failure. If an ESX host is unavailable for more than 60 minutes (by default), vSAN creates copies of data to recover the full policy compliance.
- Evacuating data by using the full data migration mode before you place a ESX host in maintenance mode.
- Exceeding the utilization threshold of a capacity device. Resynchronization is triggered when capacity device utilization in the vSAN cluster approaches or exceeds the threshold level of 80 percent.

If a VM is not responding due to latency caused by resynchronization, you can throttle the IOPS used for resynchronization. For more information, see the Broadcom knowledge base article [326830](https://knowledge.broadcom.com/external/article?articleNumber=326830).