---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/remove-selected-fault-domains-from-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >  Remove Selected Fault Domains from vSAN Cluster
---

# Remove Selected Fault Domains from vSAN Cluster

When you no longer need a fault domain, you can remove it from the vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains.
4. Click the Actions icon on the right side of the fault domain, and select Delete.
5. Click Delete to confirm.

All ESX hosts in the fault domain are removed and the selected fault domain is deleted from the vSAN cluster. Each ESX host that is not part of a fault domain is considered to reside in its own single-host fault domain.