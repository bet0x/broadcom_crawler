---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/troubleshooting-virtual-san/vsan-stretched-cluster-configuration-error-when-adding-a-host.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Stretched Cluster Configuration Error When Adding a Host
---

# vSAN Stretched Cluster Configuration Error When Adding a Host

Before adding new ESX hosts to a vSAN stretched cluster, all current ESX hosts must be connected. If a current host is disconnected, the configuration of the new host is incomplete.

After you add a host to a vSAN stretched cluster in which some ESX hosts are disconnected, on the Summary tab for the cluster the Configuration Status for vSAN appears as Unicast agent unset on host.

When a new host joins a stretched cluster, vSAN must update the configuration on all hosts in the cluster. If one or more hosts are disconnected from the vCenter, the update fails. The new host successfully joins the cluster, but its configuration is incomplete.

Verify that all ESX hosts are connected to vCenter, and click the link provided in the Configuration Status message to update the configuration of the new host.

If you cannot rejoin the disconnected host, remove the disconnected host from the cluster, and click the link provided in the Configuration Status message to update the configuration of the new host.