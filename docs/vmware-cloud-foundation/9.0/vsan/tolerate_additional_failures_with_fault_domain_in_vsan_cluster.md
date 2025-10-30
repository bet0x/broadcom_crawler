---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/tolerate-additional-failures-with-fault-domains-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Tolerate Additional Failures with Fault Domain in vSAN Cluster
---

# Tolerate Additional Failures with Fault Domain in vSAN Cluster

Fault domains in a vSAN cluster provides resilience and assures that the data is available even with failures based on policy.

With failures to tolerate (FTT) set to 1, the object can tolerate a failure. However, a temporary failure followed by a permanent failure in a cluster can result in data loss. An additional fault domain provides vSAN the ability to create a durability component without having additional FTTs for the object. vSAN triggers this extra component during planned and unplanned failures. Unplanned failures include network disconnect, disk failures, and host failures. Planned failures include Entering Maintenance Mode (EMM). For example, a 6 host cluster with RAID 6 object cannot create a durability component if there is a host failure.

vSAN ensures the data availability of the objects when the components go offline and comes back online unexpectedly based on the FTTs specified in the storage policy. During a failure, the writes of the failed component is redirected to the durability component. When the component recovers from the transient failure and comes back online, the durability component disappears and results in the resynchronization of the component.

Without the durability component in place, if there is a second permanent failure in the cluster and the mirror object is affected, the object data gets permanently lost even if the failure is resolved.