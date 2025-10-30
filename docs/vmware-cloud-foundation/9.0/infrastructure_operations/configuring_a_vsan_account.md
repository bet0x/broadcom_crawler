---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsan-overview/configure-a-vsan-adapter-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring a vSAN Account
---

# Configuring a vSAN Account

You can manage and monitor the health and performance of your vSAN clusters and remediate alerts in VCF Operations.

- You must have a vCenter Adapter instance configured and monitoring the same vCenter instance that is used to monitor the vSAN and Storage Devices.

Only vCenter systems that are configured for both vCenter adapter and vSAN adapter appear in the inventory tree under the vSAN and storage devices. Verify that vCenter that you use to configure the vSAN adapter instance is also configured as a vCenter adapter instance for the VMware vSphere solution. If not, add a vCenter adapter instance for that vCenter. For more information, see [Configuring a Account in .](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html)

- You must open port 5989 between the host and any VMware Cloud Foundation Operations node on which the vSAN adapter resides. This is applicable when the vSAN version in vSphere is 6.6 or lower.

1. From the left menu, select AdministrationIntegrations and then click Add.
2. From the Account Types page, select the vCenter instance.

   You must configure the vCenter instance before you configure vSAN on it. To configure the vCenter instance, see [Configuring a Account](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html).
3. Click the vSAN tab and click the vSAN configuration toggle switch to activate vSAN.

   Once the vSAN adapter instance is activated and saved, the activated vSAN configuration option is not visible.
4. The credentials provided for the vCenter instance are also used for vSAN adapter instance. If you do not want to use these credentials, you can click Use alternate credentials option.
   1. Click the plus sign next to the Credential field and enter the details in the Manage Credentials dialog box.
   2. Enter the credential name, vCenter user name, and password and click OK.
5. Choose Enable SMART data collection, to activate SMART data collection for physical disk devices.
6. Click Validate Connection to validate the connection with your vCenter instance.
7. Accept the vCenter security certificate.
8. Click Add to save the configurations.

   Newly created vCenter account with vSAN activated do not start monitoring the data automatically and you must manually initiate the data collection.
9. On the Accounts tab, locate the vCenter account, click the vertical ellipsis and then click Start Collecting All.

The vSAN account starts collecting data. The newly connected vSAN account information will appear on all vSAN dashboards after five minutes. You can get an overview of the vSAN health and performance in the Storage Operations page. For more information see [Monitoring Storage Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/monitoring-storage-operations(1).html). To view vSAN performance for each cluster individually and to drill down info specific performance criteria, use the vSAN Performance dashboard.

To verify that the adapter is configured and collecting data from vSAN objects, wait a few collection cycles, then view application-related data.

- Inventory. Verify that all the objects related to the vSAN instance are listed. Objects should be in the collecting state and receiving data.
- Dashboards. Verify that vSAN Capacity Overview, Migrate to vSAN, vSAN Operations Overview, and Troubleshoot vSAN, are added to the default dashboards.
- Under InventoryvSAN and Storage Devices, verify that the vSAN hierarchy includes the following related vCenter system objects:

  - vSAN World
  - Cache Disk
  - Capacity Disk
  - vSAN-activated vCenter clusters
  - vSAN Fault Domains (optional)
  - vSAN-activated Hosts
  - vSAN Data stores
  - vSAN Disk Groups
  - vSAN Data store related VMs
  - vSAN Witness Hosts (optional)