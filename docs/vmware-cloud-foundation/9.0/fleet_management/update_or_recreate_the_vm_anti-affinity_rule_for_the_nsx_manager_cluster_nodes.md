---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/update-vm-anti-affinity-rule.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update or Recreate the VM Anti-Affinity Rule for the NSX Manager Cluster Nodes
---

# Update or Recreate the VM Anti-Affinity Rule for the NSX Manager Cluster Nodes

During the NSX Manager bring-up process, SDDC Manager creates a VM anti-affinity rule to prevent the VMs of the NSX Manager cluster from running on the same ESX host. If you redeployed all NSX Manager cluster nodes, you must recreate this rule. If you redeployed one or two nodes of the cluster, you must add the new VMs to the existing rule.

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuHosts and Clusters.
3. In the inventory expand vCenterDatacenter.
4. Click the cluster object.
5. Click the Configure tab and click VM/Host Rules.
6. Update or recreate the VM anti-affinity rule.
   - If you redeployed one or two nodes of the cluster, add the new VMs to the existing rule.

     1. Click the VM anti-affinity rule name and click Edit.
     2. Click Add VM/Host rule member, select the new NSX Manager cluster nodes, and click Add.
   - If you redeployed all NSX Manager cluster nodes, click Add VM/Host rule, enter these values to create the rule, and click OK.

     | Setting | Value |
     | --- | --- |
     | Name | Enter the name of the anti-affinity rule |
     | Type | Separate virtual machines |
     | Members | Click Add VM/Host rule member, select the NSX Manager cluster nodes, and click Add. |