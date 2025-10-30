---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/check-vsan-skyline-health.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Check vSAN Skyline Health
---

# Check vSAN Skyline Health

You can view the status of vSAN health findings to verify the configuration and operation of your vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, select Skyline Health to review the vSAN health finding.
4. Under Health findings, perform the following:

   - Click Unhealthy to view the issues and the details. Click Troubleshoot to troubleshoot and fix an issue. You can sort the findings by root cause to resolve the primary issues and then verify if the impacted issues can be resolved. Click the Ask VMware button to open a knowledge base article that describes the health finding and provides information about how to resolve the issue. You can also view the status history of the health finding for a given period using History Details tab.
   - Click View History Details to identify the status history of the health finding for a particular time period. The default time period is 24 hours. You can also customize the time period as per your requirement. The status of an unhealthy finding is displayed in yellow or red.
   - You can click Silence alert on a health finding, so it does not display any warnings or failures.
   - Click All to view health findings that are healthy. Click View Current Result to view the current status of the health finding. Click View History Details to identify the status history of the health finding for a particular time period. The status is displayed in green. You can also view the status history of the health finding for a given period using History Details tab.