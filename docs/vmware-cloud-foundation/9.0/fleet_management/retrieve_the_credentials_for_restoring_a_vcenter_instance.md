---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-vcenter-server/preparing-to-restore-a-cloud-foundation-vcenter-server/gather-credentials-required-for-restoring-a-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Retrieve the Credentials for Restoring a vCenter Instance
---

# Retrieve the Credentials for Restoring a vCenter Instance

Before restoring a vCenter instance, you must retrieve the vCenter root and vCenter Single Sign-On administrator credentials from the SDDC Manager inventory. Before restoring the management domain vCenter instance, you must also retrieve the credentials of a healthy management domain ESX host.

If SDDC Manager is not operational, you can retrieve the required vCenter root, vCenter Single Sign-On administrator, and ESX root credentials from the file-based backup of SDDC Manager. See [Prepare for Restoring SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/vcf-52-restore-sddc-manager/preparing-to-restore-sddc-manager.html#GUID-ac82e8a4-7d84-4a18-b738-1d7a803b3a72-en).

Before you can query the SDDC Manager API, you must obtain an API access token by using admin@local account.

1. Log in to your host machine with access to the SDDC and open a terminal.
2. Obtain the API access token.
   1. Run the command to obtain an access token by using the admin@local credentials.

      ```
      TOKEN=`curl https://<sddc_manager_fqdn>/v1/tokens -k -X POST -H "Content-Type: application/json" -d '{"username": "admin@local","password": "admin@local_password"}' | awk -F "\"" '{print $4}'`
      ```

      The command returns an access token and a refresh token.
   2. Record the access token.
3. Retrieve the vCenter root credentials.
   1. Run the following command to retrieve the vCenter root credentials.

      ```
      curl https://<sddc_manager_fqdn>/v1/credentials?resourceType=VCENTER&accountType=USER -k -X GET \-H "Accept: application/json" -H "Authorization: Bearer $TOKEN" | json_pp
      ```

      The command returns the vCenter root credentials.

      | Setting | Value |
      | --- | --- |
      | domainName | Name of the domain |
      | resourceName | FQDN of the vCenter instance |
      | username | root |
      | password | vcenter\_root\_password |
   2. Record the vCenter root credentials.
4. Retrieve the vCenter Single Sign-On administrator credentials.
   1. Run the following command to retrieve the vCenter Single Sign-On administrator credentials.

      ```
      curl https://<sddc_manager_fqdn>/v1/credentials?resourceType=PSC -k -X GET \-H "Accept: application/json" -H "Authorization: Bearer $TOKEN" | json_pp
      ```

      The command returns the [[email protected]](/cdn-cgi/l/email-protection) credentials.

      | Setting | Value |
      | --- | --- |
      | domainName | Name of the domain |
      | resourceName | FQDN of the vCenter instance |
      | username | [[email protected]](/cdn-cgi/l/email-protection) |
      | password | vcenter\_sso\_admin\_password |
   2. Record the [[email protected]](/cdn-cgi/l/email-protection) credentials.
5. If you plan to restore the management domain vCenter instance, retrieve the credentials for a healthy management domain ESX host.
   1. Run the following command to retrieve the credentials for a management domain ESX host.

      ```
      curl https://<sddc_manager_fqdn>/v1/credentials?resourceType=ESXI -k -X GET \-H "Accept: application/json" -H "Authorization: Bearer $TOKEN" | json_pp
      ```

      The command returns the ESX root credentials.

      | Setting | Value for first ESX host |
      | --- | --- |
      | domainName | management domain name |
      | resourceName | FQDN of the first ESX host |
      | username | root |
      | password | esx\_root\_password |
   2. Record the ESX root credentials.