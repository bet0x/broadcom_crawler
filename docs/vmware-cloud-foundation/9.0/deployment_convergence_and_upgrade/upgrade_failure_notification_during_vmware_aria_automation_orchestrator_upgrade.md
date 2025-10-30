---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-a-standalone-or-clustered-vrealize-orchestrator-8-0-1-deployment-with-iso-image/the-vrealize-orchestrator-upgrade-fails-but-the-appliance-containers-are-up-and-running.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade Failure Notification During VMware Aria Automation Orchestrator Upgrade
---

# Upgrade Failure Notification During VMware Aria Automation Orchestrator Upgrade

The upgrade log indicates that the upgrade process has failed, but the individual nodes of the deployment are upgraded.

After the upgrade script finishes running, you receive the following message in your Automation Orchestrator Appliance indicating that the upgrade has failed:

```
Upgrade failed and left the system in non-working state. Check the error report below to correct the problem. Once addressed, you can continue the upgrade by running 'vracli upgrade exec --resume'
```

However, the upgrade log lists that the nodes of your Automation Orchestrator deployment are upgraded.

```
Hostname:               <your_orchestrator_node_FQDN>
Status:                 Upgraded
Cluster Member:         Yes
Version Before:         <build_before_upgrade>
Version After:          <build_after_upgrade>
Description:            The node is upgraded successfully.
```

To resolve this problem, verify that the nodes are running, and resume the upgrade.

1. Verify that your Automation Orchestrator nodes are running.

   ```
               kubectl get all pods
   ```
2. If your Automation Orchestrator nodes are running, resume the upgrade process.

   ```
               vracli upgrade exec --resume
   ```