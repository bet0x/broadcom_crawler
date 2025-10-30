---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-nsx-edge-cluster-nsxt.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade the NSX Edge Cluster Through NSX Manager
---

# Upgrade the NSX Edge Cluster Through NSX Manager

After the Management Plane upgrade is complete, the NSX Manager upgrade coordinator upgrades the NSX edge cluster based on the ordering of upgrade unit groups that you have defined. Upgrade unit groups consist of edge nodes from the same cluster. You can reorder upgrade unit groups and add or remove an upgrade unit group from the upgrade sequence.

- Verify that the edge nodes are members of an NSX edge cluster.

  Any edge nodes that are not members of an NSX edge cluster are flagged during the upgrade coordinator pre-check and prevent the upgrade from proceeding.
- Familiarize yourself with the upgrade impact during and after the edge cluster upgrade. See [Operational Impact of the Upgrade by Using Upgrade Coordinator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/operational-impact-of-nsx-t-upgrade.html).
- [Upgrade the Management Plane](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-management-plane-from-nsx-3-2-1-x-and-later.html).

You cannot move an edge node from one upgrade unit group to another because the upgrade unit group membership adheres to the edge cluster membership before the upgrade.

The edge nodes are upgraded in serial mode so that when the upgrading node is down, the other nodes in the edge cluster remain active to continuously forward traffic.

The maximum limit of simultaneous upgrade of Edge upgrade unit groups is twenty.

NSX edge virtual machine hardware will be upgraded to version vmx-20 during the edge upgrade.

1. Enter the edge cluster upgrade plan details.

   Option | Description || Serial | Upgrade all the Edge upgrade unit groups consecutively.  This menu item is selected by default. This selection is applied to the overall upgrade sequence. |
   | Parallel | Upgrade all the Edge upgrade unit groups simultaneously.  For example, if the overall upgrade is set to the parallel order, the Edge upgrade unit groups are upgraded together and the edge nodes are upgraded one at a time.  The maximum limit of simultaneous upgrade of Edge upgrade unit groups is five. |
   | When an upgrade unit fails to upgrade | Selected by default so that you can fix an error on the edge node and continue the upgrade.  You cannot deselect this setting. |
   | After each group completes | Select to pause the upgrade process after each Edge upgrade unit group finishes upgrading. |
2. Reorder the upgrade sequence of an Edge upgrade unit group. 

   For example, if you configure the overall group upgrade as serial, you can reorder the Edge upgrade unit groups serving internal networks or Edge upgrade unit groups interfacing with external networks to be upgraded first.

   It is recommended to follow an order so that critical standby nodes are upgraded before active nodes. This order allows only one failover to occur during upgrade for critical nodes.

   1. Select the Edge upgrade unit group and click the Actions tab.
   2. Select Reorder from the drop-down menu.
   3. Select Before or After from the drop-down menu.
   4. Click Save.

   You can also do this with the following REST API. Reorder an upgrade unit within the upgrade unit group by placing it before/after the specified upgrade unit.

   | METHOD | POST |
   | --- | --- |
   | URI | https://<nsx-mgr>/api/v1/upgrade/upgrade-unit-groups/<groupId>/upgrade-unit/<upgrade-unit-id>?action=reorder |
   | Payload | { "id": "<upgrad-uniti-id>", "is\_before": "false" } |
3. Click Reset to revert to the default state. 

   After reset, you cannot restore your previous configuration. Also, a reset causes the Edge upgrade unit group order to allow Edge nodes with standby logical routers to be upgraded first and followed by Edge nodes with active logical routers. This order reduces failovers.
4. Click Start to upgrade the edge cluster.
5. Monitor the upgrade process. 

   You can view the overall upgrade status and progress details of each Edge upgrade unit group. The upgrade duration depends on the number of Edge upgrade unit groups you have in your environment.

   You can pause the upgrade to configure the Edge upgrade unit group that is not upgraded and restart the upgrade.
6. Click Run Post Checks to verify whether the Edge upgrade unit groups were successfully upgraded. 

   If some Edge upgrade unit groups failed to upgrade, resolve the errors.
7. In the NSX Manager, select SystemOverview and verify that the product version is updated on each edge node.

If the process is successful, you can proceed to [upgrade vCenter and ESX hosts through SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts.html). Alternatively, you can use NSX Manager to [upgrade only the NSX VIBs on the hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts-nsxt.html).

If there are upgrade errors, you must resolve the errors. See [Troubleshooting Upgrade Failures](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt.html).