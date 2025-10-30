---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/troubleshooting-virtual-san/disk-group-becomes-locked-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Disk Group Becomes Locked in vSAN Cluster
---

# Disk Group Becomes Locked in vSAN Cluster

In an encrypted vSAN cluster, when communication between a host and the KMS is lost, the disk group can become locked if the host reboots.

vSAN locks a host's disk groups when the host reboots and it cannot get the KEK from the KMS. The disks behave as if they are unmounted. Objects on the disks become inaccessible.

You can view a disk group's health status on the Disk Management page in the vSphere Client. An Encryption health finding warning notifies you that a disk is locked.

ESX hosts in an encrypted vSAN cluster do not store the KEK on disk. If a host reboots and cannot get the KEK from the KMS, vSAN locks the host's disk groups.

To exit the locked state, you must restore communication with the KMS and reestablish the trust relationship.