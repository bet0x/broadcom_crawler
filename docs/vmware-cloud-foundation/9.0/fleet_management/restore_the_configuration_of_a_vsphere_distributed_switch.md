---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-the-configuration-of-a-distributed-switch.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore the Configuration of a vSphere Distributed Switch
---

# Restore the Configuration of a vSphere Distributed Switch

To recover the configuration of a vSphere Distributed Switch, you can restore its settings from the configuration file that you previously exported.

This procedure restores only the vSphere Distributed Switch configuration of a vCenter instance.

The restore operation changes the settings on the vSphere Distributed Switch back to the settings saved in the configuration file. The operation overwrites the current settings of the vSphere Distributed Switch and its port groups. The operation does not delete existing port groups that are not a part of the configuration file.

The vSphere Distributed Switch configuration is part of the vCenter backup. If you want to restore the entire vCenter instance, see [Restoring a vCenter Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server.html#GUID-9ce901cc-a86a-4eaf-9dca-0ba79c06eb03-en).

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuNetworking.
3. In the inventory expand vCenterDatacenter.
4. Right-click the distributed switch and select SettingsRestore configuration.
5. On the Restore switch configuration page, click Browse, navigate to the location of the configuration file for the distributed switch, and click Open.
6. Select the Restore distributed switch and all port groups radio-button and click Next.
7. On the Ready to complete page, review the changes and click Finish.
8. Repeat these steps for the other vSphere Distributed Switch.
9. Review the switch configuration to verify that it is as you expect after the restore.