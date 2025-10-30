---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/backing-up-and-restoring-the-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Backing Up and Restoring NSX Manager or Global Manager
---

# Backing Up and Restoring NSX Manager or Global Manager

If an NSX Manager or a Global Manager appliance becomes inoperable, or if you want to restore your environment to a previous state, you can restore from a backup. NSX Managers are called Local Managers if they are managed with a Global Manager using NSX Federation.

You can restore an NSX configuration back to the captured state in any of the backups. While the appliance is inoperable, the data plane is not affected, but you cannot make configuration changes.

Note the following:

- For NSX backup authentication to connect to the SFTP backup server, you can use the user name and password method or have the NSX Manager use an SSH private key.
- You must restore the same version you have backed up from your NSX appliance, to the new NSX appliances.
- Use the same key size for backup and restore. If the key size is different at time of the backup and restore, the backup does not appear in the list of available backups. Support includes key size 256-bit, 384-bit, and 521-bit.
- Storing libraries during backup is not supported in NSX backup. During restore NSX will always have default version libraries. If you are using NSX Application Platform, you must upload Kubernetes tools if requested.
- NSX Manager or Global Manager restore can use the same IP or a different IP address.
  - If you use an NSX Manager or Global Manager IP address to restore, then you must use the same IP address as in the backup.
  - For managers with different IP addresses, you must configure an FQDN. If you use an NSX Manager or a Global Manager FQDN to restore, then you must use the same FQDN as in the backup. Use a lowercase FQDN only for backup and restore.
- If both the active and standby or only the active Global Manager fail, you need to:

| Issue | Solution | Result |
| --- | --- | --- |
| Both the active and standby fail. | 1. Delete both active and standby Global Managers. Ensure there are no Global Manager appliances up in any other clusters. 2. Deploy a new Global Manager with the same IP address/FQDN as old active Global Manager. 3. Restore the active Global Manager from backup. If any Local Managers are present, they sync to the new active Global Manager. 4. Deploy a new Global Manager on another site and onboard it to the restore Global Manager. | - The active Global Manager syncs with any Global Manager on the network. - The standby Global Manager syncs with the active Global Manager. |
| The active Global Manager fails and the standby Global Manager is up. | If standby Global Manager is in a good state, it automatically becomes the active Global Manager. | Standby Global Manager becomes active Global Manager. A new standby Global Manager must be manually added for backup. After the new active Global Manager is online, the Local Manager syncs up and ensures configuration replication. |