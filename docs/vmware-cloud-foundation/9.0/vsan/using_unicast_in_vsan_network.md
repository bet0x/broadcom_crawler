---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using Unicast in vSAN Network
---

# Using Unicast in vSAN Network

Unicast traffic refers to a one-to-one transmission from one point in the network to another. vSAN uses unicast to simplify network design and deployment.

All ESX hosts use the unicast traffic, and the vCenter becomes the source for the cluster membership. The vSAN nodes are automatically updated with the latest host membership list that vCenter provides. vSAN communicates using unicast for CMMDS updates. For more information on CMMDS updates, see Broadcom knowledge base article [385769](https://knowledge.broadcom.com/external/article/385769/vsan-how-to-find-the-cmmds-and-stats-mas.html).