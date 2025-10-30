---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/disaster-recovery-using-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Disaster Recovery for Global Manager
---

# Disaster Recovery for Global Manager

In an NSX Federation environment, if you lose your active Global Manager, you can switch to the standby Global Manager.

These workflows describe the following scenario where GM denotes the Global Manager appliance.

You have a GM service to federate the network and security services across your locations. This includes:

- One GM cluster in location Loc1 set Active (GM-Loc1).
- One GM cluster in location Loc2 set Standby (GM-Loc2).

## Planned Switchover to Standby Location

The active GM service is in Loc1 and the stretched tier-0/tier-1 primary routing services are also in Loc1.

1. Switch your GM service in Loc2.
   1. Log in to the standby GM – GM-Loc2.
   2. Select the Active drop-down menu and click Make Active.

      The system starts the process of making GM-Loc2 active. After the process completes, GM-Loc2 changes status to Active and GM-Loc1 changes status to Standby.

      If the planned failover is unsuccessful use the Force Option.

      If the synchronization between GM-Loc1 and GM-Loc2 is not successful for some time, you might have possible configuration data loss when GM-Loc2 is forced to be GM Active.
   3. To check if GM-Loc1 and GM-Loc2 are synchronizing, run /etc/init.d/corfu-log-replication-server status in an SSH root shell command on both GM-Loc1 and GM-Loc2. If synchronization is not running, contact technical support.
2. (Optional) Switch primary stretched tier-0/tier-1 Loc1 to Loc2.
   1. To move the stretched tier-0 and tier-1 gateways to the secondary site, follow the network recovery workflow. See [Network Recovery for Local Managers](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/working-with-site-recovery-manager-and-federation/perform-network-recovery.html#GUID-f547fe8a-6fe7-48c1-bc81-cb21131a934e-en).
   2. Recover the compute VMs using your preferred method. For example, use VMware Site Recovery Manager from Loc1 to Loc2.

## Unplanned Switchover to the Standby Location

If the site Loc1 becomes unavailable, GM-Loc1, LM-Loc1, as well as Loc1 Edge Nodes stop responding. Proceed with a forced failover.

1. Recover your GM Service in Loc2 .
   1. Log in to the standby GM – GM-Loc2.
   2. Select the Actions drop-down menu and click Make Active.

      The system starts the process of making GM-Loc2 active. After the process completes, GM-Loc2 changes status to Active and all LMs (other than LM-Loc1 unavailable) synchronizes with GM-Loc2 from the last synchronized configuration received from GM-Loc1.

      If GM-Loc1 is online after GM-Loc2 changes to active, the status of GM-Loc1 is NONE. To make GM-Loc1 standby:

      1. Log in to the active GM – GM-Loc2.
      2. From the tile where GM-Loc1 shows the status of NONE, select the Actions drop-down menu and click Make Standby.
2. Move your primary stretched tier-0/tier-1 Loc1 to Loc2.
   1. Follow the network recovery workflow to move stretched tier-0 and tier-1 gateways to the secondary site. See instructions at [Network Recovery for Local Managers](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/working-with-site-recovery-manager-and-federation/perform-network-recovery.html#GUID-f547fe8a-6fe7-48c1-bc81-cb21131a934e-en).
   2. Recover the compute VMs using your preferred method. For example,  use VMware Site Recovery Manager from to Loc2.

See the Disaster Recovery section in the [NSX Multi-location Design Guide](https://community.broadcom.com/blogs/dimitri-desmidt/2024/05/20/nsx-t-multi-location-design-guide) for more details. For details about using Site Recovery Manager, see [Working with VMware Live Site Recovery and Multisite Environments](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-multisite/working-with-vmware-site-recovery-manager-and-multisite-environments.html#GUID-7e521789-7acc-48d5-8996-61b3a9c47a83-en).