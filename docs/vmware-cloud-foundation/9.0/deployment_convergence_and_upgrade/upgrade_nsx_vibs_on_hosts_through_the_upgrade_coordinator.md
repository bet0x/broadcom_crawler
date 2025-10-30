---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts-nsxt.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade NSX VIBs on Hosts Through the Upgrade Coordinator
---

# Upgrade NSX VIBs on Hosts Through the Upgrade Coordinator

You can upgrade the NSX VIBs on hosts in your environment using the upgrade coordinator.

- Verify that you have configured the overall hosts upgrade plan. See [Configure Hosts for a Manual Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/configure-hosts-nsx-t.html#GUID-4687af2a-49d4-46c2-8148-1af0369dde97).
- If the ESX hosts are part of a disabled DRS cluster or are standalone hosts, verify that they are placed in maintenance mode.
- For ESX hosts that are part of a fully automated DRS cluster, if the host is not in maintenance mode, the upgrade coordinator requests the host to be put in maintenance mode. vSphere DRS migrates the VMs to another host in the same cluster during the upgrade and places the host in maintenance mode.
- For ESX host, for an in-place upgrade you do not need to power off the tenant VMs.
- For a stateless ESX host, log in to vCenter and update the ESX image with the NSX kernel modules.

The upgrade coordinator only upgrades the NSX VIBs on hosts. To [upgrade ESX on hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts.html), you must use SDDC Manager instead.

1. Click Start to upgrade the hosts.
2. Click Refresh and monitor the upgrade process. 

   You can view the overall upgrade status and specific progress of each host upgrade unit group. The upgrade duration depends on the number of host upgrade unit groups you have in your environment.

   Wait until the in progress upgrade units are successfully upgraded. You can then pause the upgrade to configure the host upgrade unit group that is not upgraded and resume the upgrade.
3. Click Run Post Checks to make sure that the upgraded hosts and NSX do not have any problems.

   If a host upgrade unit failed to upgrade and you removed the host from NSX, refresh the upgrade coordinator to view all the successfully upgraded host upgrade units.

   If a host fails during the upgrade, reboot the host and try the upgrade again.
4. After the upgrade is successful, verify that the latest version of NSX packages is installed on the vSphere hosts.

   For vSphere hosts, enter esxcli software vib list | grep nsx
5. Power on the tenant VMs of standalone ESX hosts that were powered off before the upgrade.
6. Migrate the tenant VMs on hosts managed by vCenter that are part of the enabled DRS cluster to the appropriate host.
7. Power on or return the tenant VMs of ESX hosts that are part of a disabled DRS cluster that were powered off before the upgrade.

Proceed to [Finalize Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/finalize-upgrade.html).

You can finalize the upgrade only after the upgrade process finishes successfully. If some of the hosts are disabled, you must enable and upgrade them before you proceed.

If there are upgrade errors, you must resolve the errors. See [Troubleshooting Upgrade Failures](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt.html).