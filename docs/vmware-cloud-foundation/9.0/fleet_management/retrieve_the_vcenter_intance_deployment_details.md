---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server/preparing-to-restore-a-cloud-foundation-vcenter-server/gather-vcenter-server-details.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Retrieve the vCenter Intance Deployment Details
---

# Retrieve the vCenter Intance Deployment Details

Before restoring a vCenter instance, you must retrieve the vCenter build number and deployment details from the SDDC Manager inventory. The vCenter instances in your system might be running different build numbers if the backups are taken during an upgrade process. You must restore each vCenter instance to its correct version.

Because the management domain vCenter might be unavailable to authenticate the login, you use the SDDC Manager API via the shell to retrieve this information.

1. Log in to SDDC Manager by using a Secure Shell (SSH) client.
2. Run the command to get the list of vCenter instances.

   ```
   curl http://localhost/inventory/vcenters -k | json_pp
   ```
3. For each vCenter instance, record the values of these settings.

   | Setting | Value |
   | --- | --- |
   | domainId | Id of the domain |
   | vmName | VM name of the vCenter instance |
   | datastoreForVmDeploymentSourceId | Datastore Id |
   | hostName | FQDN of the vCenter instance |
   | version | version\_number-build\_number |
4. Verify that the vCenter version retrieved from SDDC Manager is the same as the version associated with the backup file that you plan to restore.