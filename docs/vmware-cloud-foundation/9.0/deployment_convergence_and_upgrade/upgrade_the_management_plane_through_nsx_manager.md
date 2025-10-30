---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-management-plane-from-nsx-3-2-1-x-and-later.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade the Management Plane Through NSX Manager
---

# Upgrade the Management Plane Through NSX Manager

The upgrade sequence upgrades the Management Plane at the beginning. If required, you can continue to make configuration changes while the Management Plane upgrade is in progress.

[Update the upgrade coordinator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-the-upgrade-coordinator.html).

NSX supports only an odd number of nodes in a cluster. A three-node cluster is the recommended configuration for fault tolerance. NSX Manager nodes are upgraded sequentially due to the rolling upgrade feature so that two nodes are up all the time.

You can push new configurations while the NSX Manager upgrade is in progress. Do not add or delete NSX Manager nodes during an upgrade.

The upgrade process also includes taking a local backup of NSX Manager nodes that can be used to restore or roll back the system. Once all pre-checks are complete, the system saves the configuration backup followed by local backup of all the nodes in the cluster. To check if the system saved the local backup, you can go to the root admin and check the following folder:

- /config\_bak/backup/<unified\_app\_version>/cluster-node-backups - if the upgrade is from NSX 4.1.0 and later versions.
- /image/backup/<unified\_app\_version>/cluster-node-backups - if the upgrade is from NSX 4.0.x versions.

The rollback backup is also saved at /config\_bak. If the local backup fails for any reason, the upgrade is stopped.

If a rollback is required, roll back the NSX Manager nodes using the backup before starting the upgrade of edge nodes and host transport nodes.

If you need to roll back the system after the upgrade of edge nodes or host transport nodes has started, you must contact Broadcom Support to first roll back the upgraded edge and host transport nodes before you can roll back the NSX Manager nodes.

Starting with VCF 9.0, the multi-NSX feature is not supported. Ensure that before upgrading to version 9.0 or later, you have switched off the multi NSX feature for compute managers added to your NSX Manager. Alternatively, you can map the NSX Manager instances to individual vCenter instances before upgrading.

When the Management Plane upgrade begins, the upgrade coordinator pins the NSX API and NSX Manager UI to the source version. This operation ensures that your access to the NSX API and NSX Manager UI remains unchanged during the upgrade process.

Some API methods removed from the target version cannot be accessed during the upgrade.

Also, when performing a rolling upgrade of NSX Manager nodes from version 4.x to version 9.0 or later, you cannot create the following types of objects during the rolling upgrade period:

- Edge transport node
- Edge cluster high-availability profile
- Failure domain

The create functionality will become available after the upgrade coordinator completes the migration of logical to policy object paths in the management plane.

1. Back up the NSX Manager.

   See the NSX Administration Guide.
2. Click Start to upgrade the Management plane.
3. Accept the upgrade notification.

   You can safely ignore any upgrade related errors such as, HTTP service disruption that appears at this time. These errors appear because the NSX Manager node may be rebooting during the upgrade. You can continue to monitor the progress of the upgrade from the UI of any of the other NSX Manager nodes.

   If you are using a Virtual IP address, the UI remains accessible but you need to re-authenticate yourself after all the nodes have been upgraded.
4. In case of upgrade errors, NSX may prompt you to roll back the upgrade. The rollback is performed on all the NSX Manager nodes:

   1. Run the following command from a root shell on all the NSX Manager nodes :

      /etc/init.d/corfu-server stop
   2. Run the following command as an admin user on all the NSX Manager nodes:

      node-rollback run-step step1\_start\_rollback
   3. Run the following command as an admin user on any one of the NSX Manager nodes:

      node-rollback run-step step2\_restore\_data

      If you encounter any errors, perform the troubleshooting steps described later on this page.
   4. Run the following command as an admin user on all the NSX Manager nodes:

      node-rollback run-step step3\_exit\_rollback

   The rollback applies only to the Management Plane upgrade. Your NSX Manager nodes return to the version prior to starting the Management Plane upgrade.

Proceed to [upgrade the edge clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-nsx-edge-cluster-nsxt.html).

After you upgrade the Management Plane, you can join the Customer Experience Improvement Program (CEIP) for NSX. See Customer Experience Improvement Program in the NSX Administration Guide for more information, including how to join or leave the program.

**Troubleshooting the Management Plane rollback**

If you encounter errors during a rollback, perform these troubleshooting steps:

1. Execute corfu\_tool\_runner to delete the record from the registry table:

   ```
   /opt/vmware/bin/corfu_tool_runner.py  -t RegistryTable -n CorfuSystem --port 9000 -o deleteRecord --keyToDelete='{"namespace": "CorfuSystem","tableName": "CompactionControlsTable"}'
   ```
2. Run compaction verification:

   ```
   /opt/vmware/bin/corfu_compactor_upgrade_runner.py --runs 3 --lock false
   ```
3. Stop corfu-server on all NSX Manager nodes.
4. Start corfu-server on all NSX Manager nodes.
5. Resume with the restore command as an admin user on any one of the NSX Manager nodes:

   node-rollback run-step step2\_restore\_data