---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-workload-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >  Workload Automation Details
---

# Workload Automation Details

You can set the workload automation options for your policy, so that VCF Operations can optimize the workload in your environment as per your definition.

## How the Workload Automation Workspace Works

You click the lock icon to unlock and configure the workload automation options specific for your policy. When you click the lock icon to lock the option, your policy inherits the parent policy settings.

## Where You Set the Policy Workload Automation

Access this screen through the Policies pages:

1. Click Infrastructure OperationsConfigurations, and then click the Policy Definition tile.
2. Select a policy that you want to modify. Ideally, this should be an active policy. Or, click the ADD button to add a new policy.
3. Select the Workload Automation card to review the changes, or click EDIT POLICY to make changes.

Workload Automation in the Create or Edit Policies Workspace



| Option | Description |
| --- | --- |
| Workload Optimization | Select a goal for workload optimization. Select Balance when workload performance is your first goal. This approach proactively moves workloads so that the resource utilization is balanced, leading to maximum headroom for all resources.  Select Moderate when you want to minimize the workload contention.  Select Consolidate to proactively minimize the number of clusters used by workloads. You might be able to repurpose resources that are freed up. This approach is good for cost optimization, while making sure that performance goals are met. This approach might reduce licensing and power costs. |
| Cluster Headroom | Headroom establishes a required capacity buffer, for example, 20 percent. It provides you with an extra level of control and ensures that you have extra space for growth inside the cluster when required. Defining a large headroom setting limits the systems opportunities for optimization. vSphere HA overhead is already included in useable capacity and this setting does not impact the HA overhead. |
| Change Datastore | Click the lock icon to select one of the following options:  - Do not allow Storage vMotion. - Allow Storage vMotion. This is selected by default.  Using this option, you can select what type of virtual machines VCF Operations moves first to address workload. |
| Target Network Policy Setting for WLP | Click the lock icon to select the following option:  - Generate a Target Network mapping   When you select this checkbox, the Workload Placement algorithm in will automatically choose compatible target network, while making the decision to move the VM for the optimization. For choosing compatible network WLP engine will consider the segment path and logical switch UUID of the Distributed Port Group.  Workload Optimization Across networks is supported when the optimization candidate clusters are assigned with different port groups (configured with NSX). These port groups configured via NSX have same segmentID and Logical Switch UUID. To enable this ability, check the respective setting in Workload Automation policy settings. Segment ID and logical switch UUID properties are published on the VC port groups by NSX. So Worload Placement cannot provide a target network if it is not a NSX configuration and those properties are missing.  This setting is not selected by default. |