---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Monitoring the Health of Cloud Proxies
---

# Monitoring the Health of Cloud Proxies

You can view the status and health of your cloud proxy after you add it in VCF Operations. You can then monitor the health and view alerts and metrics of your cloud proxy using the VCF Operations cloud proxy object.

1. Log in to VCF Operations.
2. From the left menu, click AdministrationCloud Proxies.

   The list of cloud proxies is displayed.

   | Option | Description |
   | --- | --- |
   | Name | The name of the cloud proxy. |
   | IP | The IP address of the cloud proxy. |
   | Status | Status of the cloud proxy. For example, the Going Online status is displayed for a few minutes when you add a new cloud proxy. After the cloud proxy is connected to VCF Operations, the status changes to Online. If the VCF Operations is not connected, the Offline status is displayed. |
   | Version | The version used to install the cloud proxy. |
   | Accounts | The number of accounts that are created and associated with the cloud proxy. |
   | Type | Displays the cloud proxy type. |
   | Collector Group | Displays if the cloud proxy is part of the collector group. If the cloud proxy is part of the collector group, the name is displayed. Click the name to view the collector group details. No data is displayed if the cloud proxy is a standalone cloud proxy and not a part of the collector group. |
   | Network Proxy Address | The network proxy address of the cloud proxy. |
   | Network Proxy Port | The network proxy port number of the cloud proxy. |
   | Target | Displays the target location on which the cloud proxy is deployed. |
   | Data Persistence | Displays the status of data persistence for the cloud proxy. Data persistence activates the cloud proxy to store data if the connection fails between the cloud proxy and VCF Operations.  - Activated. Cloud proxy will store data. - Deactivated. Cloud proxy will not store data. To activate/deactivate data persistence for multiple cloud proxies, select the cloud proxies, click the horizontal ellipsis, and then select Activate Data Persistence or Deactivate Data Persistence.  To activate/deactivate data persistence for a single cloud proxy, select the cloud proxy, click the vertical ellipsis, and then select Activate Data Persistence or Deactivate Data Persistence.  When the connection is restored, the cloud proxy sends the stored data to VCF Operations. The stored data is displayed before the real-time data is displayed. |
   | Log Assist | Displays if log assist is activated or deactivated for the cloud proxy. |
   | Time Estimation | Displays the estimated time duration for which the cloud proxy persists data. Cloud proxy can store data for a maximum duration of one hour. If there is a lack of space or if the connection fail lasts for more than an hour, the cloud proxy rotates the stored data by deleting the oldest stored data and replacing it with the most recently collected data.  The time estimate value is displayed only if data persistence is activated. |
   | Filter | You can search the list of cloud proxies according to the following criteria: - Name - IP - Status - Version - Collector Group - Network Proxy Address - Network Proxy Port - Target - Data Persistence - Cloud Proxy Id |
3. Click the vertical ellipsis.
   1. Click Activate/Deactivate Data Persistence to activate or deactivate data persistence for the cloud proxy.
   2. Click Remove to delete the cloud proxy.
4. Click a Cloud Proxy name.

   The Cloud Proxy Details open.

   Cloud Proxy Details



   | Option | Description |
   | --- | --- |
   | Rename | Click the Rename Cloud Proxy icon to update the cloud proxy name. |
   | Proxy ID | ID of the cloud proxy. |
   | IP Address | IP address of the cloud proxy. |
   | OVA Version | The OVA file version used to install the cloud proxy. |
   | Status | Status of the cloud proxy. For example, the Getting Online status is displayed for a few minutes when you add a cloud proxy. After the cloud proxy is connected to VCF Operations, the status changes to Online. If the VCF Operations is not connected, the Offline status is displayed. |
   | Creation Date | Date of creation of the cloud proxy. |
   | Last Heartbeat | Last time stamp when VCF Operations ran a Health Check for this cloud proxy. When you click a cloud proxy to view its details, VCF Operations sends a heartbeat to check if the cloud proxy is still reachable. |
   | CPU | CPU usage. |
   | Memory | Memory usage. |
   | Number of Cloud Accounts | Displays the number of cloud accounts using the cloud proxy. Each cloud proxy might have one or more cloud accounts. You can also view the health and status of these cloud accounts from this details pane. |
5. If your cloud proxy is not collecting data, you can view the health of the cloud proxy. From the left menu, click Inventory, select the VCF Operations Cloud Proxy Object from the list, and then click Show Detail.

   For more details, see [Inventory: List of Objects](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/configuring-objects/object-discovery/managing-objects-in-your-environment/inventory-explorer-list-of-objects.html).
6. After you locate the VCF Operations cloud proxy object, you can view the object details using the Summary tab. For more information, see [Summary Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/monitoring-and-responding-to-problems/summary-tab-overview/summary-tab.html).
7. Use the [Alerts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/monitoring-and-responding-to-problems/alerts-tab-overview/alerts-tab.html) tab to monitor the health of the cloud proxy. If there are any issues, troubleshoot them using the [Metrics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/monitoring-and-responding-to-problems/evaluating-metric-information/troubleshooting-with-the-all-metrics-tab.html) tab.

   If your cloud proxy is not working properly, an alert is displayed.

   ```
   One or more VCF Operations services on a cloud proxy are down.
   ```

   To clear this alert, perform the following steps:
   - Check the network connectivity and configuration for the cloud proxy.
   - Take the cloud proxy offline and then bring it back online.For more information, see [Cloud Proxy FAQ](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-faq.html#GUID-b2afa731-63fd-4782-9d07-81747f994f25-en) and [Cloud Proxy Troubleshooting](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-troubleshooting.html#GUID-dc2ae994-1896-4bc6-8310-2790be403ec9-en).

   It is recommended that you create a notification rule for this alert so that, quick remediation steps can be taken, if necessary.
8. You can use the cloud proxy command line interface for other cloud proxy related actions. For more details, see [Using the Cloud Proxy Command-Line Interface](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy/using-the-cloud-proxy-command-line-interface-on-cloud.html#GUID-f0c4e448-9737-4cae-956e-a494847ac28d-en).

Click the Collector Groups tab to view the cloud proxies that are part of the collector groups. For more information on collector groups, see [Configuring Collector Groups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/collector-groups-managing.html).