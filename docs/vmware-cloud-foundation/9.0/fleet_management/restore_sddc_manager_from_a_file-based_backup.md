---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/vcf-52-restore-sddc-manager/restore-sddc-manager-from-a-file-based-backup.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Restore SDDC Manager from a File-Based Backup
---

# Restore SDDC Manager from a File-Based Backup

First, you deploy a new SDDC Manager appliance by using the OVA file that you downloaded during the preparation for the restore. After that, you restore the file-based backup on the newly deployed SDDC Manager appliance.

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuVMs and templates.
3. In the inventory expand vCenterDatacenter.
4. Right-click the management folder and select Deploy OVF template.
5. On the Select an OVF template page, select Local file, click Upload files, browse to the location of the SDDC Manager OVA file, click Open, and click Next.
6. On the Select a name and folder page, in the Virtual machine name text box, enter a virtual machine name, and click Next.
7. On the Select a compute resource page, click Next.
8. On the Review details page, review the settings and click Next.
9. On the License agreements page, accept the license agreement and click Next.
10. On the Select storage page, select the vSAN datastore and click Next.

    The datastore must match the vsan\_datastore value in the metadata.json file that you downloaded during the preparation for the restore.
11. On the Select networks page, from the Destination network drop-down menu, select the management network distributed port group and click Next.

    The distributed port group must match the port\_group value in the metadata.json file that you downloaded during the preparation for the restore.
12. On the Customize template page, enter the following values and click Next.

    | Setting | Description |
    | --- | --- |
    | Enter root user password | You can use the original root user password or a new password. |
    | Enter Local user password | You can use the original Local user password or a new password. |
    | Host Name | The FQDN must match the hostname value in the metadata.json file that you downloaded during the preparation for the restore. |
    | NTP Servers | The NTP server details for the appliance. |
    | Enable FIPs | Selected |
    | Network 1 IP address | The IP address for the appliance. |
    | Network 1 Subnet Mask | The subnet mask for the appliance. |
    | Network Default Gateway | The default gateway for the appliance. |
    | DNS Domain Name | The domain name for the appliance. |
    | Domain search path | The domain search path(s) for the appliance. |
    | Domain name servers | The DNS servers for the appliance. |
13. On the Ready to complete page, click Finish and wait for the process to complete.
14. Once the SDDC Manager appliance deployment completes, expand the management folder.
15. Right-click the SDDC Manager appliance and select SnapshotsTake Snapshot.
16. Right-click the SDDC Manager appliance, select PowerPower On.
17. On the host machine, copy the encrypted backup file to the /tmp folder on the newly deployed SDDC Manager appliance by running the following command. When prompted, enter the vcf\_user\_password.

    ```
    scp filename-of-restore-file vcf@sddc_manager_fqdn:/tmp/
    ```
18. On the host machine, obtain the authentication token from the SDDC Manager appliance in order to be able to execute the restore process by running the following command:

    ```
    TOKEN=`curl https://<sddc_manager_fqdn>/v1/tokens -k -X POST -H "Content-Type: application/json" -d '{"username": "admin@local","password": "<admin@local_password>"}' | awk -F "\"" '{ print $4}'`
    ```
19. On the host machine with access to the SDDC Manager, open a terminal and run the command to start the restore process.

    ```
    curl https://<sddc_manager_fqdn>/v1/restores/tasks -k -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
        -d '{
      "elements" : [ {
        "resourceType" : "SDDC_MANAGER"
      } ],
      "backupFile" : "<backup_file>",
      "encryption" : {
        "passphrase" : "<encryption_password>"
      }
    }'
    ```

    The command output contains the ID of the restore task.
20. Record the ID of the restore task.
21. Monitor the restore task by using the following command until the status becomes Successful.

    ```
    curl https://<sddc_manager_fqdn>/v1/restores/tasks/<restore_task_id> -k -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN"
    ```

Refresh the SSH keys that are stored in the SDDC Manager inventory. See [VMware Cloud Foundation SDDC Manager Recovery Scripts (79004)](https://kb.vmware.com/s/article/79004).