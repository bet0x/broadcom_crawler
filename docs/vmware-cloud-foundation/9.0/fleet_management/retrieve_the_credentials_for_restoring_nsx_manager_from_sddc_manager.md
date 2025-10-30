---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/prepare-for-restoring-nsx-t-manager/retrieve-the-credentials-for-restoring-nsx-manager-from-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Retrieve the Credentials for Restoring NSX Manager from SDDC Manager
---

# Retrieve the Credentials for Restoring NSX Manager from SDDC Manager

Before restoring a failed NSX Manager instance, you must retrieve the NSX Manager root and admin credentials from the SDDC Manager inventory.

Before you can query the SDDC Manager API, you must obtain an API access token by using an API service account.

1. Log in to your host machine with access to the SDDC and open a terminal.
2. Obtain the API access token.
   1. Run the command to obtain an access token by using the admin@local account credentials.

      ```
      TOKEN=`curl https://<sddc_manager_fqdn>/v1/tokens -k -X POST -H "Content-Type: application/json" -d '{"username": "admin@local","password": "admin@local_password"}' | awk -F "\"" '{print $4}'`
      ```

      The command returns an access token and a refresh token.
   2. Record the access token.
3. Retrieve the NSX Manager root and admin credentials.
   1. Run the command to retrieve the NSX Manager root and admin credentials.

      ```
      curl 'https://<sddc_manager_fqdn>/v1/credentials?resourceType=NSXT_MANAGER' -k -i -X GET -H 'Accept: application/json' -H 'Authorization: Bearer $TOKEN' | json_pp
      ```

      The command returns the NSX Manager root and admin credentials.
   2. Record the NSX Manager root and admin credentials for the instance you are restoring.