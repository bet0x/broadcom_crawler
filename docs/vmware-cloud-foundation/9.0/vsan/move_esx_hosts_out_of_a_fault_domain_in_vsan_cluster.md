---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/move-hosts-out-of-a-fault-domain-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Move ESX Hosts out of a Fault Domain in vSAN Cluster
---

# Move ESX Hosts out of a Fault Domain in vSAN Cluster

Depending on your requirement, you can move ESX hosts out of a fault domain.

Verify that the ESX host is online. You cannot move ESX hosts that are offline or unavailable from a fault domain.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains. 
   1. Click and drag the ESX host from the fault domain to the Standalone Hosts area.
   2. Click Move to confirm.

The selected ESX host is no longer part of the fault domain. Any ESX host that is not part of a fault domain is considered to reside in its own single-host fault domain.

You can add ESX hosts to fault domains. See [Move ESX Host into Selected Fault Domain in vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/move-hosts-into-selected-fault-domain-in-vsan-cluster.html#GUID-131c852b-4d5b-4ef3-a849-bb2766717e71-en).