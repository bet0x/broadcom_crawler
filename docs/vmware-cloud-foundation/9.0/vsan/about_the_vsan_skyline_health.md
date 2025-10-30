---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/about-the-vsan-skyline-health.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > About the vSAN Skyline Health
---

# About the vSAN Skyline Health

Use the vSAN Skyline health to monitor the health of your vSAN cluster.

You can use the vSAN Skyline health to monitor the status of cluster components, diagnose issues, and troubleshoot problems. The health findings cover hardware compatibility, network configuration and operation, advanced vSAN configuration options, storage device health, and virtual machine objects.

You can use Overview to monitor the core health issues of your vSAN cluster. You can also view the following:

- Cluster health score based on the health findings
- View the health score trend for 24 hours
- View the health score trend for a particular period

Ensure that the Historical Health Service is enabled to view details of the Health score trend. Click View Details in the Health score trend chart to examine the health state of the cluster for a selected time point within 24 hours. Use Custom to customize the time range as per your requirement. If you disable Historical Health Service, the vSAN Skyline Health score trend and the past health checks data gets deleted.

You can use the vSAN Health findings to diagnose issues, troubleshoot problems, and remediate the problems.

The health findings are classified as follows:

- Unhealthy – Critical or important issue(s) being detected that needs attention.
- Healthy – There are no issues found that needs attention.
- Info – Health findings which may not impact the cluster running state but important for awareness.
- Silenced – Health findings have been silenced without triggering vSAN health alarm by intention.

To troubleshoot an issue, you can sort the findings by root cause to resolve the primary issues initially and then verify if the impacted issues can also be resolved.

vSAN periodically retests each health finding and updates the results. To run the health findings and update the results immediately, click the Retest button.

If you participate in the Customer Experience Improvement Program (CEIP), you can run health findings and send the data to VMware for advanced analysis. Click Retest with Online health and then click OK. Online notifications is enabled by default if the vCenter can connect to VMware Analytics Cloud without enrolling CEIP. If you do not want to participate in CEIP, you can still receive vSAN health notifications for software and hardware issues using Online notifications.

## Viewing vSAN Health History

The vSAN health history helps you examine health issues by querying the historical health records. You can only view the historical health data of a cluster. By default, the health history is enabled. To deactivate the health history, select the cluster and navigate to the Configure > vSAN > Services > Historical Health Service > Edit. Use the toggle Enable vSAN Historical Health Service and click Apply to deactivate the health history. If you deactivate the health history, all the health data collected on the vCenter database gets purged. The database stores the health data for up to 30 days depending on the available capacity.

Using the Skyline Health view, you can view the health history for a selected time range. The start date of the time range must not be earlier than 30 days from the current date. The end date must not be later than the current date. Based on your selection, you can view the historical health findings. Click View History Details to view the history of a health finding within a selected time period. The historical data is displayed as a graphical representation with green circles, yellow triangles, and red squares showing success, warning, and failure respectively. The detailed information about each health finding result is displayed in a table.

## Using vSAN Support Insight

vSAN support insight is a platform that helps you maintain a reliable and consistent compute, storage, and network environment. VMware support uses the vSAN support insight to monitor the vSAN performance diagnostics and resolve performance issues. vSAN uses Customer Experience Improvement Program (CEIP) to send data to VMware for analysis on a regular basis. To deactivate CEIP, click the icon next to vSphere Client > Administration > Deployment > Customer Experience Improvement Program > Leave Program.