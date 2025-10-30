---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server/restore-the-management-domain-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore a vCenter Instance from a File-Based Backup
---

# Restore a vCenter Instance from a File-Based Backup

If a vCenter instance fails, you can restore it from its file-based backup. If the management domain vCenter instance and the workload domain vCenter instance are both in a failed state, you must restore the management domain vCenter instance before restoring the workload domain vCenter instance.

- Download the vCenter ISO file for the version of the failed instance. See [Retrieve the vCenter Intance Deployment Details](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server/preparing-to-restore-a-cloud-foundation-vcenter-server/gather-vcenter-server-details.html#GUID-0cbaa0d6-85ca-4b50-a2e3-298d565d3fd6-en).
- If you are recovering a workload domain vCenter instance, verify that the management domain vCenter instance is available.

You deploy a new vCenter appliance and perform a file-based restore. If you are restoring the management domain vCenter instance, you deploy the new appliance on a healthy ESX host in the management domain cluster. If you are restoring the workload domain vCenter instance, you deploy the new appliance in the management domain vCenter instance.

1. Mount the vCenter ISO image to your host machine with access to the SDDC and run the UI installer for your operating system.

   For example, for a Windows host machine, open the dvd-drive:\vcsa-ui-installer\win32\installer application file.
2. Click Restore.
3. Complete the Restore - Stage 1: Deploy vCenter wizard.
   1. On the Introduction page, click Next.
   2. On the End user license agreement page, select the I accept the terms of the license agreement check box and click Next.
   3. On the Enter backup details page, enter these values and click Next.

      | Setting | Value |
      | --- | --- |
      | Location or IP/hostname | sftp://sftp\_server\_ip/backups/vCenter/sn\_vc\_fqdn/backup\_folder/ |
      | User name | SFTP Server Username |
      | Password | sftp-user-password |
   4. On the Review backup information page, review the backup details, record the vCenter configuration information, and click Next.

      You use the vCenter configuration information at a later step to determine the deployment size for the new vCenter appliance.
   5. On the vCenter deployment target page, enter the values by using the information that you retrieved during the preparation for the restore, and click Next.

      | Setting | Value for Management Domain vCenter Instance | Value for Workload Domain vCenter Instance |
      | --- | --- | --- |
      | ESX host or vCenter name | FQDN of the first ESX host | FQDN of the management vCenter instance |
      | HTTPS port | 443 | 443 |
      | User name | root | [[email protected]](/cdn-cgi/l/email-protection) |
      | Password | esx\_root\_password | vcenter\_sso\_admin\_password |
   6. In the Certificate warning dialog box, click Yes to accept the host certificate.
   7. On the Set up target vCenter VM page, enter the values by using the information that you retrieved during the preparation for the restore, and click Next.

      | Setting | Value |
      | --- | --- |
      | VM name | vCenter instance VM name |
      | Set root password | vcenter\_root\_password |
      | Confirm root password | vcenter\_root\_password |
   8. On the Select deployment size page, select the deployment size that corresponds with the vCenter configuration information from Step 3.d and click Next.

      Refer to vSphere documentation to map CPU count recorded from Step 3.d to a vSphere configuration size.
   9. On the Select datastore page, select these values, and click Next.

      | Setting | Value |
      | --- | --- |
      | Datastore | Datastore name |
      | Enable thin disk mode | Selected |
   10. On the Configure network settings page, enter the values by using the information that you retrieved during the preparation for the restore, and click Next.

       | Setting | Value |
       | --- | --- |
       | Network | Name of the vSphere distributed switch portgroup |
       | IP version | IPV4 |
       | IP assignment | static |
       | FQDN | FQDN of the vCenter |
       | IP address | IP address of the vCenter |
       | Subnet mask or prefix length | 24 |
       | Default gateway | Default gateway IP address |
       | DNS servers | Comma separated list of DNS server IP addresses |
   11. On the Ready to complete stage 1 page, review the restore settings and click Finish.
   12. When stage 1 of the restore process completes, click Continue.
4. Complete the Restore - Stage 2: vCenter wizard.
   1. On the Introduction page, click Next.
   2. On the Backup details page, in the Encryption password text box, enter the encryption password of the SFTP server and click Next.
   3. On the Ready to complete page, review the restore details and click Finish.
   4. In the Warning dialog box, click OK to confirm the restore.
   5. When stage 2 of the restore process completes, click Close.

Refresh the SSH keys that are stored in the SDDC Manager inventory. See [VMware Cloud Foundation SDDC Manager Recovery Scripts (79004)](https://kb.vmware.com/s/article/79004).