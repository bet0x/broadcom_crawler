---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/configure-hosts-nsx-t.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure Hosts for a Manual Upgrade
---

# Configure Hosts for a Manual Upgrade

When performing a manual upgrade through the upgrade coordinator in NSX Manager, you can customize the upgrade sequence of the hosts, exclude certain hosts from the upgrade, or pause the upgrade at various stages of the upgrade process.

- If the ESX hosts are part of a disabled DRS cluster or are standalone hosts, verify that they are placed in maintenance mode.
- For ESX hosts that are part of a fully automated DRS cluster, if the host is not in maintenance mode, the upgrade coordinator requests the host to be put in maintenance mode. vSphere DRS migrates the VMs to another host in the same cluster during the upgrade and places the host in maintenance mode.
- For ESX host, for an in-place upgrade you do not need to power off the tenant VMs.
- Verify that the transport zone or transport node N-VDS name does not contain spaces.

  If there are spaces, create a transport zone with no spaces in the N-VDS name. You must reconfigure all the components that are associated with the old transport zone to use the new transport zone and delete the old transport zone.
- Verify that your vSAN environment is in good health before you use the in-place upgrade mode.

See the Place a Host in Maintenance Mode section of the vSphere Resource Management guide.

All the existing standalone ESX hosts, vCenter, and managed ESX hosts are grouped in separate host upgrade unit groups by default.

Before you upgrade the hosts, you can select to update the hosts in parallel or serial mode. The maximum limit for a simultaneous upgrade is twenty host upgrade unit groups and five hosts per group.

Host upgrade unit group with hosts that belong to the same vCenter cluster can be upgraded serially.

You can customize the host upgrade sequence before the upgrade. You can edit a host upgrade unit group to move a host to a different host upgrade unit group that upgrades immediately and another host to a host upgrade unit group that upgrades later. If you have a frequently used host, you can reorder the host upgrade sequence within a host upgrade unit group so it is upgraded first and move the least used host to upgrade last.

1. Enter the host upgrade plan details. 

   You can configure the overall group upgrade order to set the host upgrade unit groups to be upgraded first.

   Option | Description || Serial | Upgrade all the host upgrade unit groups consecutively.  This menu item is selected by default and applied to the overall upgrade sequence. This selection is useful to maintain the step-by-step upgrade of the host components.  For example, if the overall upgrade is set to serial and the host upgrade unit group upgrade is set to parallel, the host upgrade unit group is upgraded one after the other. The hosts within the group are updated in parallel. |
   | Parallel | Upgrade all the host upgrade unit groups simultaneously.  You can upgrade up to five hosts simultaneously. |
   | When an upgrade unit fails to upgrade | Select to pause the upgrade process if any host upgrade fails.  This selection allows you to fix the error on the host upgrade unit group and resume the upgrade. |
   | After each group completes | Select to pause the upgrade process after each host upgrade unit group finishes upgrading. |
2. Change the host upgrade unit group upgrade order. 

   If you configure the overall group upgrade in the serial order, the upgrade waits for a host upgrade unit group upgrade to finish before proceeding to upgrade the second host upgrade unit group. You can reorder the host upgrade unit group upgrade sequence to set a host upgrade unit group to upgrade first.

   1. Select the host upgrade unit group and click the Actions tab.
   2. Select Reorder from the drop-down menu.
   3. Select Before or After from the drop-down menu.
3. Remove a host upgrade unit group from the upgrade sequence. 
   1. Select the host upgrade unit group and click the Actions tab.
   2. Select Change State from the drop-down menu.
   3. Select Disabled to remove the host upgrade unit group.
4. Change the individual host upgrade unit group upgrade sequence. 

   By default, the upgrade sequence is set to the parallel order.

   1. Select the host upgrade unit group and click the Actions tab.
   2. Select Change Upgrade Order from the drop-down menu.
   3. Select Serial to change the upgrade sequence.
5. Change the host upgrade unit group upgrade mode. 
   - Select Maintenance mode.

     For standalone ESX hosts and ESX hosts that are part of a disabled DRS cluster, place the hosts into maintenance mode.

     For ESX hosts that are part of a fully automated DRS cluster, if the host is not in maintenance mode, the upgrade coordinator requests the host to be put in maintenance mode. vSphere DRS migrates the VMs to another host in the same cluster during the upgrade and places the host in maintenance mode.
   - Select In-place mode to avoid powering off and placing a host into maintenance mode before the upgrade.

     For standalone ESX hosts and ESX hosts that are part of a disabled DRS cluster, you do not need to place the hosts into maintenance mode.

     For ESX hosts that are part of a fully automated DRS cluster, you do not need to place the host into maintenance mode.

     During upgrade the host might experience a packet drop in the workload traffic.
   - Use the API call PUT https://<nsx-manager>/api/v1/upgrade/upgrade-unit-groups/<group-id> and enable the upgrade coordinator to restart the ESX host.

     The rebootless\_upgrade:true parameter states that after the ESX host upgrade, the host is not rebooted.

     By default, the upgrade coordinator does not restart the ESX host. This mode is used for troubleshooting purposes.
   - Use the API call PUT https://<nsx-manager>/api/v1/upgrade/upgrade-unit-groups/<group-id> and upgrade vCenter-managed ESX hosts that are part of a DRS cluster with vSAN configured.

     The ensure\_object\_accessibility parameter requires vSAN to assume control of data accessibility while a vCenter-managed ESX host that is part of a DRS cluster is placed in maintenance mode for the upgrade.

     The evacuate\_all\_data parameter requires vSAN to take all the data from a vCenter-managed ESX host that is part of a DRS cluster to another managed ESX host that is part of a DRS cluster while placed in maintenance mode for the upgrade.

     The no\_action parameter requires vSAN to take no action while the vCenter-managed ESX host that is part of a DRS cluster is placed in maintenance mode for the upgrade.

     For more information about the parameters, see the Update the upgrade unit group section of the NSX API Guide.
6. For vSphere Lifecycle Manager-enabled clusters, select one of the following options:
   - NSX only Upgrade: Use this option if you want to upgrade only NSX. The Upgrade Coordinator runs the entire upgrade process including the remediation of hosts.
   - Stage in vSphere Lifecycle Manager: Use this option if you want to upgrade NSX along with ESX hosts and other solutions. You need to remediate the hosts using vSphere Lifecycle Manager. After remediation, you can monitor the upgrade from the Upgrade Coordinator.
7. Click Reset to discard your custom upgrade plan and revert to the default state. 

   You cannot restore your previous upgrade configuration.

   If you register a new host transport node during the upgrade, you must click Reset to view the status of the recently added host and to continue the upgrade process.

Determine whether to add, edit, or delete host upgrade unit groups or to upgrade host upgrade unit groups. See [Manage Host Upgrade Unit Groups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/manage-hosts-nsxt.html#GUID-4bd2c853-96b1-4843-a132-40c868443c88) or [Upgrade NSX VIBs on Hosts Through the Upgrade Coordinator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts-nsxt.html#GUID-9ce81fe4-3dce-47e5-9001-874d9e50fbba).