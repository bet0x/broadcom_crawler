---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/cloud-proxy-admin-ui.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Monitoring the Health of Cloud Proxies from the Administration UI
---

# Monitoring the Health of Cloud Proxies from the Administration UI

After you configure your cloud proxy, you can view the status, health, and upgrade history of your cloud proxy in the VCF Operations administration interface.

1. Log in to the VCF Operations administration interface at https://primary-node-fqdn/admin.
2. Click Cloud Proxies.

   Cloud Proxies Page Options



   | Option | Description |
   | --- | --- |
   | IP Address | IP address of the cloud proxy. |
   | Name | Name of the cloud proxy. |
   | Network Proxy Configuration | Determines whether the network proxy setting is configured or not. |
   | Health Status | Determines the health of the cloud proxy. |
   | Upgrade Status | Determines whether the upgrade is complete, in progress, or failed. |
   | Last Upgrade Time | Determines when was the last upgrade done. |
   | Version | Version number of the cloud proxy. |

Click the Expand icon to view the upgrade history.

Upgrade History Options



| Option | Description |
| --- | --- |
| ID | The conventional name used to identify the PAK file. It is usually the name of the PAK file and its version numbers joined together without extensions. For example, VMware Aria-Operations-Cloud-Proxy-<number>. |
| Type | The type of upgrade used for the cloud proxy. The cloud proxy can be upgraded either automatically or manually using the command-line interface. For more information, see [Using the Cloud Proxy Command-Line Interface](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy/using-the-cloud-proxy-command-line-interface-on-cloud.html). |
| Start Time | Time stamp when the upgrade started. |
| End Time | Time stamp when the upgrade ended. |
| Upgrade Status | Determines whether the upgrade is complete, in progress, or failed. For a detailed view of the upgrade status, click the row to open the Info pop-up. If the cloud proxy upgrade fails due to low disk space, the FAIL\_NO\_SPACE\_FOR\_PAK\_DOWNLOAD message appears. |
| Version | Version number of the cloud proxy PAK file. |