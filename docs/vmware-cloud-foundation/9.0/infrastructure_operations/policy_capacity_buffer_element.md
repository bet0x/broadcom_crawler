---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-capacity-details/policy-capacity-buffer-element.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Policy Capacity Buffer Element
---

# Policy Capacity Buffer Element

The capacity buffer element lets you add buffer for capacity and cost calculation. For vCenter objects, you can add buffer to CPU, Memory, and Disk Space for the Demand and Allocation models. You can add capacity buffer to datastores, clusters and datastore clusters. The values that you define here affect the cluster cost calculation. The time remaining, capacity remaining, and recommended values are calculated based on the buffer. For WLP, capacity buffer is first considered and then the headroom that you have defined is considered.

## Where You Define the Capacity Buffer

To view and override the policy Capacity Buffer analysis setting, from the left menu click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the <policy name> [Edit] workspace, click the Capacity card. The Capacity Buffer for the object type that you selected appears in the workspace. Click the lock icon to unlock the section and make changes.

How the Capacity Buffer Element Works

The Capacity Buffer element determines how much extra headroom you have and ensures that you have extra space for growth inside the cluster when required. The value of the usable capacity reduces by the buffer amount that you specify here. The default buffer value is zero. If you are upgrading from a previous version of VCF Operations, the buffer values are carried forward to the new version.

The capacity buffer value that you specify for the Allocation model is considered only if you have activated allocation model in the policy.

Starting from version 8.6, capacity buffer is depreciated from cluster compute resources. The overcommit ratio setting (from the allocation model) and buffer settings, if set for the datastore object, takes precedence for the disk space related to datastore cluster and cluster objects. If these settings are not set, then, from a cost calculation perspective, the settings of datastore cluster and cluster (if the settings are missing for the datastore cluster as well), are used. The allocation and buffer settings made on the cluster does not impact the underlying datastores (as they do not inherit these settings), and the same works vice-versa, settings made for datastores are not propagated to the cluster.

The following tables display the capacity buffer that you can define based on the vCenter Adapter object types:

| Object Type | Valid Models for Capacity Buffer |
| --- | --- |
| CPU | Demand Allocation |
| Memory | Demand Allocation |
| Disk Space | Demand Allocation |