---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/steps-to-monitor-vsphere-supervisor-clusters-and-resources/enabling-the-vsphere-supervisor-collection.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Enabling Monitoring for vSphere Supervisor
---

# Enabling Monitoring for vSphere Supervisor

You enable or disable vSphere Supervisor monitoring when configuring the vCenter cloud account integration in VCF Operations. The vSphere Supervisor internal management pack is enabled or disabled based on this setting. One vCenter cloud account can have multiple Supervisors enabled. When the setting is enabled, an adapter instance for each supervisor is automatically created and monitored. When it is disabled, the adapter instance is still available, but metrics are not collected.

- Ensure that you are logged in to VCF Operations with the required permissions to add or edit a vCenter cloud account.

1. From the left menu, click AdministrationIntegrations.
2. On the Accounts tab, click Add. On the Accounts Type page, click vCenter. For more information about configuring a vCenter cloud account, see the topic, [Configure a Cloud Account.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html)
3. Alternatively, select an existing vCenter account and click Edit from the vertical ellipsis.
4. Expand Advanced Settings.
5. Verify that the value of Enable vSphere Supervisor Collection is set to true. This is the default setting.
6. Once you have configured the rest of the settings, click ADD.

After enabling vSphere Supervisor monitoring the following settings are automatically configured:

- vSphere Supervisor sends data to the Cloud Proxy VM running the Application Monitoring adapter.
- The Telegraf package defines which metrics are collected and how often they are sent.

To verify that the adapter is collecting data, go to Inventory (Detailed View)IntegrationsvSphere Supervisor and check the Summary tab in the Supervisor World object.

To see the vSphere Supervisor adapters which are configured and collecting metrics, go to Infrastructure OperationsDashboards and ReportsInventory and look for the vSphere Supervisor dashboards.