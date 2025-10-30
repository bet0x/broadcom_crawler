---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/remediate-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Remediate Passwords for VMware Cloud Foundation Components 
---

# Remediate Passwords for VMware Cloud Foundation Components

To resolve any errors that might occur during password changes, you use password remediation. Password remediation synchronizes the password of the account stored in the SDDC Manager with the updated password in the component. After you reset the password in a component, you must remediate the password in VCF Operations.

- Verify that no workflows are running or are scheduled to run while you remediate the password.
- Verify that the user you log in with in the VCF Operations UI has the following permissions:
  - Fleet Management: Passwords:Manage.
  - Fleet Management: Passwords:View.

You can remediate the password for only one account at a time.

Although individual components support different password requirements, it is recommended that you set passwords following a common set of requirements across all accounts.

For information on updating passwords manually, see [Update Passwords for VMware Cloud Foundation Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/update-passwords.html).

1. In the VCF Operations console, click Fleet ManagementPasswords .
2. Click VCF Management or click VCF Instances and click a VCF Instance or VCF domain name.
3. Select a component and click Remediate Password.
4. Enter and confirm the password that was set manually on the component.
5. Click Remediate Password.

In case a VCF component loses connectivity to another VCF component due to synchronization issues (for example, the password for the service account changes on the server side, while the client side is not updated), you can manually remediate the service account on the client side by following the procedures below.

|  |  |  |
| --- | --- | --- |
| Created in | Used by | Procedure |
| vCenter | SDDC-M | To manually remediate the SDDC Manager service account in vCenter, use the vCenter Password API to reset the SDDC Manager service account password. You then use the remediate password functionality in SDDC Manager.   1. Create a session to vCenter.     ```    session=$(curl -ks https://<vcenter_fqdn>/api/session -u '[email protected]:password' -X POST | jq -r .)    ``` 2. Reset the service account password.     ```    curl -ks https://<vcenter_fqdn>/api/vcenter/svc-account-mgmt/password?action=reset -H "vmware-api-session-id: $session" -H 'Content-Type: application/json' -d '{ "account_name": "sddc_m_to_vcenter_service_account" }' | jq    ```     The command returns the new password. 3. Log in to SDDC Manager at https://<sddc\_manager\_fqdn> with a user assigned the Administrator role. 4. In the left pane, navigate to SecurityPassword management. 5. On the Password management page, select the vCenter service account, click the elipsis icon, and select Remediate password. 6. In the Remediate password dialog box, enter the new password and click Remediate password.   Contact Broadcom Global Support for additional assistance. |
| NSX | To manually remediate the NSX service account in vCenter, you must enter the service account credentials in the NSX UI and NSX automatically repairs the integration.   1. Log in to NSX Manager at https://<nsx\_manager\_fqdn>/login.jsp with a user assigned the Administrator role. 2. On the main navigation bar, click System. 3. In the left pane, navigate to FabricCompute managers. 4. Select the compute manager that has a Not registered status. 5. Click the message and click Resolve. 6. In the dialog box, enter the vCenter service account credentials and click Resolve. |
| VCF Operations | To manually remediate the VCF Operations service account in vCenter, you use the VCF Operations UI.  1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role. 2. In the left pane, navigate to AdministrationIntegrations. 3. On the Accounts tab, expand the VMware Cloud Foundation section. 4. Expand your VCF Instance and click the domain. 5. On the domain page, click the vCenter tab. 6. Next to System managed credentials, click Rotate.  The existing service account gets deleted and a new service account is created. The integration between VCF components is not affected during the creation of the new service account.  When VCF Operations fleet management synchronizes the inventory with VCF Operations, VCF Operations fleet management generates a new service account in vCenter through SDDC Manager. |
| VCF Operations for networks |
| VCF Operations for logs |
| VCF Operations fleet management |
| VCF Operations orchestrator | To manually remediate the VCF Operations orchestrator service account in vCenter, you log in to the VCF Operations orchestrator pod as root and reset the authentication provider by using the vracli vro authentication CLI command:   ``` vracli vro authentication set -p vsphere \ --hostname https://FQDN_SPHERE\ --username[email protected]\ --tenantvsphere.local\ --admin-groupAdministrators\ --admin-group-domainvsphere.local ```   Restart the VCF Operations orchestrator pod. |
| VCF Automation | To manually remediate the VCF Automation service account in vCenter, use the VCF Automation UI.   1. Log in to the VCF Automation interface at https://<vcf\_automation\_fqdn> with a user assigned the Administrator role. 2. In the left pane, navigate to VCF Instances. 3. On the VCF Instance page, click the vertical ellipsis next to the vCenter instance, and, from the drop-down menu, select Rotate service account.   VCF Automation deletes and recreates the service account. |
| NSX | SDDC Manager | To manually remediate the SDDC Manager service account in NSX, use the NSX API to update the SDDC Manager service account password. You then use the remediate password functionality in SDDC Manager.  1. Find the user ID for the SDDC Manager service account from the list of service accounts.     ```    curl -sk 'https://vip_nsx_manager/api/v1/node/users?filter=service' -u 'admin:admin_password' | jq    ``` 2. Reset the service account password.     ```    curl -ik 'https://vip_nsx_manager/api/v1/node/users/user_id?action=reset_password' -u 'admin:admin_password' -H 'Content-Type: application/json' -d '{ "password": "new_service_account_password" }'    ``` 3. Log in to SDDC Manager at https://<sddc\_manager\_fqdn> with a user assigned the Administrator role. 4. In the left pane, navigate to SecurityPassword management. 5. On the Password management page, select the NSX service account, click the elipsis icon, and select Remediate password. 6. In the Remediate password dialog box, enter the password you configured and click Remediate password. |
| VCF Operations | To manually remediate the VCF Operations service account in NSX, you use the VCF Operations UI.  1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role. 2. In the left pane, navigate to AdministrationIntegrations. 3. On the Accounts tab, expand the VMware Cloud Foundation section. 4. Expand your VCF Instance and click the domain. 5. On the domain page, click the NSX tab. 6. Next to System managed credentials, click Rotate.  The existing service account gets deleted and a new service account is created. The integration between VCF components is not affected during the creation of the new service account.  When VCF Operations fleet management synchronizes the inventory with VCF Operations, VCF Operations fleet management generates a new service account in vCenter through SDDC Manager. |
| VCF Operations for networks |
| VCF Automation | To manually remediate the VCF Automation service account in NSX, use the VCF Automation UI. VCF Automation deletes and recreates the service account.  1. Log in to the VCF Automation interface at https://<vcf\_automation\_fqdn> with a user assigned the Administrator role. 2. In the left pane, navigate to VCF Instances. 3. On the VCF Instance page, click the vertical ellipsis next to the NSX instance, and, from the drop-down menu, select Rotate service account. |
| SDDC Manager API keys | VCF Operations | To manually remediate the SDDC Manager API key in VCF Operations, you use the VCF Operations UI.  1. Log in to the VCF Operations interface at https://<vcf\_operations\_fqdn> with a user assigned the Administrator role. 2. In the left pane, navigate to AdministrationIntegrations. 3. On the Accounts tab, expand the VMware Cloud Foundation section. 4. Click the VCF Instance. 5. On the Account tab, in the VCF Credentials section, click Rotate.  The existing API key is deleted and a API key is created. The integration between VCF components is not affected during the creation of the new service account.  When VCF Operations fleet management synchronizes the inventory with VCF Operations, VCF Operations fleet management generates a new API key in SDDC Manager. |
| VCF Operations fleet management |
| VCF Automation | To manually remediate the SDDC Manager API key in VCF Automation, you use the VCF Automation API to delete the SDDC Manager endpoint. VCF Automation creates a new API key and adds the SDDC Manager instance during the next synchronization. Please note that this action usually takes 24 hours, during which period VCF Automation is not able to register new workload domains. |