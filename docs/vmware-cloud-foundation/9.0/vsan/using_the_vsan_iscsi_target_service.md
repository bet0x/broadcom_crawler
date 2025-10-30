---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/using-the-vsan-iscsi-target-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using the vSAN iSCSI Target Service
---

# Using the vSAN iSCSI Target Service

Use the iSCSI target service to enable ESX hosts and physical workloads that reside outside the vSAN cluster to access the vSAN datastore.

This feature enables an iSCSI initiator on a remote ESX host to transport block-level data to an iSCSI target on a storage device in the vSAN cluster. vSAN support Windows Server Failover Clustering (WSFC), so WSFC nodes can access vSAN iSCSI targets. For more information, see Broadcom knowledge base article [313230](https://knowledge.broadcom.com/external/article/313230).

After you configure the vSAN iSCSI target service, you can discover the vSAN iSCSI targets from a remote host. To discover vSAN iSCSI targets, use the IP address of any host in the vSAN cluster, and the TCP port of the iSCSI target. To ensure high availability of the vSAN iSCSI target, configure multipath support for your iSCSI application. You can use the IP addresses of two or more hosts to configure the multipath. vSAN iSCSI VIP is an IP address that you can use to discovery IP address for initiators to discover vSAN iSCSI target service without having to provide the underlying host vSAN iscsi vmkernel ip address details.

vSAN iSCSI target service does not support other vSphere or ESX clients or initiators, third-party hypervisors, or migrations using raw device mapping (RDMs).

vSAN iSCSI target service supports the following CHAP authentication methods:

CHAP
:   In CHAP authentication, the target authenticates the initiator, but the initiator does not authenticate the target.

Mutual CHAP
:   In mutual CHAP authentication, an extra level of security enables the initiator to authenticate the target.

For more information about using the vSAN iSCSI target service, see [iSCSI Target Usage Guide](https://www.vmware.com/docs/vmw-vsan-iscsi-target-usage-guide).

## iSCSI Targets

You can add one or more iSCSI targets that provide storage blocks as logical unit numbers (LUNs). vSAN identifies each iSCSI target by a unique iSCSI qualified Name (IQN). You can use the IQN to present the iSCSI target to a remote iSCSI initiator so that the initiator can access the LUN of the target.

Each iSCSI target contains one or more LUNs. You define the size of each LUN, assign a vSAN storage policy to each LUN, and enable the iSCSI target service on a vSAN cluster. You can configure a storage policy to use as the default policy for the home object of the vSAN iSCSI target service.

## iSCSI Initiator Groups

You can define a group of iSCSI initiators that have access to a specified iSCSI target. The iSCSI initiator group restricts access to only those initiators that are members of the group. If you do not define an iSCSI initiator or initiator group, then each target is accessible to all iSCSI initiators.

A unique name identifies each iSCSI initiator group. You can add one or more iSCSI initiators as members of the group. Use the IQN of the initiator as the member initiator name.