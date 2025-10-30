---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-backups-for-sddc-manager-and-vcenter-server/export-the-configuration-of-the-vsphere-distributed-switches.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Export the Configuration of the vSphere Distributed Switches
---

# Export the Configuration of the vSphere Distributed Switches

The vCenter backup includes the configuration of the entire vCenter instance. To have a backup only of the vSphere Distributed Switch and distributed port group configurations, you export a configuration file that includes the validated network configurations. If you want to recover only the vSphere Distributed Switch, you can import this configuration file to the vCenter instance.

You can use the exported file to create multiple copies of the vSphere Distributed Switch configuration on an existing deployment, or overwrite the settings of existing vSphere Distributed Switch instances and port groups.

You must backup the configuration of a vSphere Distributed Switch immediately after each change in configuration of that switch.

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select the Networking inventory.
3. In the inventory expand the vCenter and Datacenter.
4. Right click the vSphere Distributed Switch you want to backup, and select Export Configuration.
5. In the Export configuration dialog box, select Distributed switch and all port groups.
6. In the Description text box enter the date and time of export, and click OK.
7. Copy the backup zip file to a secure location from where you can retrieve the file and use it if a failure of the appliance occurs.
8. Repeat the procedure for the other vSphere Distributed Switches.