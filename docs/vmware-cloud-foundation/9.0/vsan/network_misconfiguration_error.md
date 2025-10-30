---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/troubleshooting-virtual-san/network-misconfiguration-error-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Network Misconfiguration Error
---

# Network Misconfiguration Status in vSAN Cluster

After you enable vSAN on a cluster, the datastore is not assembled correctly because of a detected network misconfiguration.

After you enable vSAN on a cluster, a vSAN Alarm triggers on the Summary tab indicating a network partition.

One or more members of the cluster cannot communicate because of either of the following reasons:

- A host in the cluster does not have a VMkernel adapter for vSAN.
- The ESX hosts cannot connect each other in the network.

Troubleshoot network partition errors using the vSAN Skyline Health and the Broadcom knowledge base article [318839](https://knowledge.broadcom.com/external/article/318839).