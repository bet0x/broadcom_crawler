---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/troubleshooting-virtual-san/cannot-add-or-remove-the-witness-host-in-vsan-stretched-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Cannot Add or Remove the Witness Host in vSAN Stretched Cluster 
---

# Cannot Add or Remove the Witness Host in vSAN Stretched Cluster

Before adding or removing the witness host in a vSAN stretched cluster, all current ESX hosts must be connected. If a current host is disconnected, you cannot add or remove the witness host.

When you add or remove a witness host in a vSAN stretched cluster in which some ESX hosts are disconnected, the operation fails with an error status: The operation is not allowed in the current state. Not all ESX hosts in the cluster are connected to Virtual Center.

When the witness host joins or leaves a stretched cluster, vSAN must update the configuration on all ESX hosts in the cluster. If one or more ESX hosts are disconnected from the vCenter, the witness host cannot be added or removed.

Verify all ESX hosts are connected to vCenter, and retry the operation. If you cannot rejoin the disconnected host, remove the disconnected host from the cluster, and then you can add or remove the witness host.