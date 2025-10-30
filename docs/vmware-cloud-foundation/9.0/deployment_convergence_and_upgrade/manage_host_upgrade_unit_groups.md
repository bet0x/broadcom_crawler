---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/manage-hosts-nsxt.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Manage Host Upgrade Unit Groups
---

# Manage Host Upgrade Unit Groups

You can edit and delete an existing host upgrade unit group before you start the upgrade or after you pause the upgrade.

- Verify that you have configured the overall hosts upgrade. See [Configure Hosts for a Manual Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/configure-hosts-nsx-t.html#GUID-4687af2a-49d4-46c2-8148-1af0369dde97).
- If the ESX hosts are part of a disabled DRS cluster or are standalone hosts, verify that they are placed in maintenance mode.
- For ESX hosts that are part of a fully automated DRS cluster, if the host is not in maintenance mode, the upgrade coordinator requests the host to be put in maintenance mode. vSphere DRS migrates the VMs to another host in the same cluster during the upgrade and places the host in maintenance mode.
- For ESX host, for an in-place upgrade you do not need to power off the tenant VMs.

Hosts in a ESX cluster appear in one host upgrade unit group in the upgrade coordinator. You can move these hosts from one host upgrade unit group to another host upgrade unit group.

If any of the hosts are part of a vSAN enabled cluster, retain the default upgrade unit groups without recreating any groups.

1. Create a host upgrade unit group. 
   1. Click Add to include existing hosts into a host upgrade unit group.
   2. Toggle the State button to enable or disable the host upgrade unit group from the upgrade.
   3. Select an existing host and click the arrow icon to move that host to the newly created host upgrade unit group. 

      If you select an existing host that was part of a host upgrade unit group, the host is moved to the new host upgrade unit group.
   4. Select whether to upgrade the host upgrade unit group in parallel or serial mode.
   5. Select the upgrade mode. 

      See step 5 of [Configure Hosts for a Manual Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/configure-hosts-nsx-t.html#GUID-4687af2a-49d4-46c2-8148-1af0369dde97).
   6. Select Reorder from the drop-down menu to reposition the host upgrade unit groups.
   7. Select Before or After from the drop-down menu.
2. Move an existing host to another host upgrade unit group. 

   If an enabled DRS ESX cluster is part of the upgrade, then a host upgrade unit group is created for the hosts managed by this cluster.

   1. Select a host upgrade unit group.
   2. Select a host.
   3. Click the Actions tab.
   4. Select Change Group from the drop-down menu to move the host to another host upgrade unit group.
   5. Select the host upgrade unit group name from the drop-down menu to move the host to.
   6. Select Reorder from the drop-down menu to reposition the host within the host upgrade unit group.
   7. Select Before or After from the drop-down menu.
3. Delete a host upgrade unit group. 

   You cannot delete a host upgrade unit group that has hosts. You must first move the hosts to another group.

   1. Select the host upgrade unit group.
   2. Select a host.
   3. Click the Actions tab.
   4. Select Change Group from the drop-down menu to move the host to another host upgrade unit group.
   5. Select the host upgrade unit group name from the drop-down menu to move the host to.
   6. Select the host upgrade unit group you want to remove and click Delete.
   7. Accept the notification.

Upgrade the newly configured hosts. See [Upgrade NSX VIBs on Hosts Through the Upgrade Coordinator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts-nsxt.html#GUID-9ce81fe4-3dce-47e5-9001-874d9e50fbba).