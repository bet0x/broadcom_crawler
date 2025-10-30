---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/intra-cluster-traffic.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Intra-Cluster Traffic
---

# Intra-Cluster Traffic

In unicast mode, the primary node
addresses all the cluster nodes as it sends the same message to all the vSAN nodes in a
cluster.

For example, if N is the number of vSAN nodes,
then the primary node sends the messages N number of times. This results in a slight increase
of vSAN CMMDS traffic. You might not notice this slight increase of traffic
during normal, steady-state operations.