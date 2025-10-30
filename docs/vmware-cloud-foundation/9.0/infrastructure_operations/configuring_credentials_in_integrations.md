---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/configuring-credentials-in-integrations.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring Credentials in Integrations
---

# Configuring Credentials in Integrations

Credentials are the user accounts that VCF Operations uses to activate one or more integrations and associated adapters, and to establish communication with the target data sources. The credentials are supplied when you configure each adapter. You can create new credentials and modify the credential settings outside the adapter configuration or during adapter configuration to accommodate changes to your environment.

If you are modifying credentials to accommodate changes based on your password policy, you must validate your connection so that the adapters configured with these credentials begin using the new user name and password to communicate between VCF Operations and the target system.

Another use of credential management is to remove misconfigured credentials. If you delete valid credentials that were in active use by an adapter, you disable the communication between the two systems. You cannot delete an active credential that is being used by an adapter instance.

If you need to change the configured credential to accommodate changes in your environment, you can edit the credential settings without being required to configure a new adapter instance for the target system. To edit credential settings, from the left menu, click AdministrationIntegrations. In the Accounts tab, click Credentials .

You could only view, add, modify, or delete credentials that you created or were assigned to you. You can view and use unassigned credentials only if you had the required permissions. You can also deactivate the Credential Ownership Enforcement option from Global Settings page to be able to modify credentials created and owned by others. For more information, see [List of Global Settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/modifying-global-settings/list-of-global-settings.html).

## Where You Find Credentials

From the left menu, click Administration Integrations. In the Accounts tab, click Credentials.

Credentials Options



| Option | Description |
| --- | --- |
| Toolbar options | Manages the selected credential.  - Add: Adds new credentials for an adapter type that you can later apply when configuring an adapter. - Click the Vertical Ellipses to perform any one of the following actions:   - Edit: Modifies the selected credentials, usually when the user name and password require a change. The change is applied to the current adapter credentials after you validate the connection and the data source continues to communicate with VCF Operations.   - Delete: Removes the selected credentials from VCF Operations. If you have an adapter that uses these credentials, the communication fails and you cease monitoring the objects that the adapter was configured to manage. Commonly used to delete misconfigured credentials. You cannot delete an active credential that is being used by an adapter instance. |
| Filtering options | Limits the displayed credentials based on the adapter or credential kinds. |
| Credential name | Description of user-defined name that you provide to manage the credentials. Not the account user name. |
| Adapter Type | Adapter type for which the credentials are configured. |
| Credential Kind | The type of credentials associated with the adapter. Some adapters support multiple types of credentials. For example, one type can define a user name and password, and another can define a pass code and key phrase. |