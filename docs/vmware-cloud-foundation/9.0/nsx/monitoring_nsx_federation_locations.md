---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui/monitoring-nsx-federation-locations.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitoring NSX Federation Locations
---

# Monitoring NSX Federation Locations

To monitor the configuration flow between all Global Managers (GM) and Local Managers (LM) across a single NSX Federation federated domain for on-premises solutions you can use the System > Location Manager menu or the Location drop-down menu on the GM page. After you configure Locations, alarms display any communication issues between the GM and the LM on the Location Manager page.

You must already have a Location added. See "Add a Location" in the NSX Installation Guide.

Use the Location Manager to view latency data, monitor communication synchronizations, check policies, and get better visibility into the health between the different components of the federated domain. The Global Manager View of Location Manager figure shows the Global and Local Manager details. For callout details, see the Callouts for Global Manager View of Location Manager table.

Global Manager View of Location Manager

![Global Manager view of Location Manager with details in the following table. ](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/45b71d61-ab30-4ccd-8738-8907b901fbfa.original.png)

Callouts for Global Manager View of Location Manager



| ID | Options | Description |
| --- | --- | --- |
| 1 | Set location view. | Switch to different GM-active and LM views by selecting dropdown. After logging into the active GM, this drop-down indicates what instance you are logged into and lets you switch to other LM locations views. You can also switch to the standby GM, not using this dropdown, but by selecting the Actions menu in the Standby pane and clicking Access Standby GM. |
| 2 | Active GM information. | - GM-Active details. - Tasks such as GM Active Name. |
| 3 | GM Standby information. | - GM Standby details such as Sync Status. - Other details such as GM Standby Name, Access Standby GM View, and Remove GM Standby. |
| 4 | LM pane information. | - LM details such as Latency Data, Sync Status, and Networking RTEP configuration. - Tasks such as edit settings, remove, evacuate location, and import to GM. Evacuate location allows network recovery for sites that have not lost communication. For example, if you want to migrate a data center or perform a disaster recovery test. Import to GM allows the former LM configuration to be pushed up to GM (see "Importing Configurations from Local Manager" in the NSX Installation Guide. |
| 5 | LM More Info pane. | - View detailed Full Sync from GM Active to LM information such as Start Time, End Time, and Reason. - View detailed Delta Sync from GM Active to LM information such as Message Queues on GM and LM. |

The Local Manager View of Location Manager figure shows an example of the window details. For callout details, see the Callouts for Local Manager View table.

Local Manager View of Location Manager

![Shows Local Manager dashboard with Global Manager and cluster details.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ce1f1442-bfdf-405e-a50a-30f076b4f85e.original.png)

Callouts for Local Manager View of Location Manager



| ID | Task | Description |
| --- | --- | --- |
| 1 | View LM details. | NSX version, cluster IPs and names, status of full sync and when it completed. |
| 2 | View related active GM details. | - Software versions, latency details between GM and LM, cluster details, and color-coded sync status. - Green is communication is OK. Orange is some backlog in the queue based on threshold. Red is sync is not occurring. - To see the full sync details including status, start and end times, ID, and status reasons, click More Info. |
| 3 | View remote location details. | Cluster details, including View More information, latency data between LM and GM, and current status. |

The Supported Communication Channel Details table provides details about the Location Manager displays.

Supported Communication Channel Details



| Supported Communication Channels | Display Details |
| --- | --- |
| All channels | - Status (color-coded)   - Green - OK.   - Orange - Sync between active GM and Standby GM is in progress.   - Red - Communication is lost. - When latency is over 500 ms, an alarm gets raised. For NSX Federation events, see the [Event Catalog](https://docs.vmware.com/en/VMware-NSX-Event-Catalog/index.html). |
| On a GM and LM UI for each remote LM | - Current queue levels contain the number of queued messages compared to the queue size. - Last measured latency - Uses ICMP or TCP traffic between the local LM and the remote LM to measure the network round trip in milliseconds (ms). |
| On a LM UI for a GM active cluster and a GM standby cluster | - Current queue levels contain the number of queued messages compared to the queue size for GM active only. - Last measured latency - Measures the network round trip in ms using ICMP or TCP traffic between the local LM and the active and standby GM. - When latency is over 500 ms, an alarm gets raised. |
| On an active GM UI for a standby GM cluster | - When Active-Standby GM replication is not working, an alarm gets raised. |