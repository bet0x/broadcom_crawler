---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Managing the NSX Manager Cluster
---

# Managing the NSX Manager Cluster

You can reboot an
NSX Manager if
it becomes inoperable. You can also change the IP address of an
NSX Manager.

In a production environment, it
is highly recommended that the
NSX Manager
cluster has three members to provide high availability. If you delete an
NSX Manager and
deploy a new one, the new
NSX Manager can
have the same or a different IP address.

The primary NSX Manager node is the node that
you create first, before you create a manager cluster. This node cannot be deleted.
After you deploy two more manager nodes from the primary manager node's UI to form a
cluster, only the second and the third manager nodes have the option (from the gear
icon) to be deleted. For information about removing and adding a manager node, see [Change the IP Address of an NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/change-the-ip-address-of-an-nsx-manager.html#GUID-a7eb7fc6-1ca2-4954-98c6-ea7cf9e01aa9-en).