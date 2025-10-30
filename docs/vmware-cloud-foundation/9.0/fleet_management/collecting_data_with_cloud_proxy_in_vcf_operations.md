---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Collecting Data with Cloud Proxy in VCF Operations
---

# Collecting Data with Cloud Proxy in VCF Operations

You can use cloud proxies in VCF Operations to collect and monitor data from your on-premises data centers across different geographical locations.

Cloud proxies provide high availability within your VCF Operations environment, you can group two or more cloud proxies to form a collector group. The cloud proxy collector group ensures that there is no single point of failure in your cloud environment. If one of the cloud proxies experiences a network interruption or becomes unavailable, the other cloud proxy from the collector group takes charge and ensures that there is no downtime. All other user-initiated manual operations on the collector, such as to stop or restart the collector manually, do not result in automated re-balancing. For more information, see [Configuring ClouConfiguring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html).

To configure cloud proxy using VCF Operations Fleet Management, see [Add Nodes to VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/scaling-up-and-scaling-out-management-nodes-in-vcf/scale-up-vrealize-suite-products.html).

When a node within the collector group goes down, high availability failover occurs, so that data collection is not impacted. However some data loss is expected before the failover is complete.

You can also use cloud proxies to re-balance the resources in your collector group. The re-balance option is available as part of the Edit menu in the Collector Groups page.

You can use the re-balance option before vCenter initiates data collection. After the data collection starts, the re-balance option is disabled.

FIPS mode is supported in a cloud proxy. To leverage this functionality, make sure your cluster is in FIPS mode.

You can upgrade your cloud proxy. For more information, see [Upgrading](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy.html).

You can deploy a cloud proxy based on your sizing requirements. For more information, see KB article [324340](https://knowledge.broadcom.com/external/article?articleNumber=324340).

Cloud Proxy Types



| Cloud Proxy Type | VM Scale Requirements | CPU Requirements | Memory Requirements |
| --- | --- | --- | --- |
| Classic Small Cloud Proxy | Up to 16,000 VMs | 2 vCPUs | 8GB |
| Classic Large Cloud Proxy | Between 16,000 to 80,000 VMs | 4 vCPUs | 32GB |
| Unified Small Cloud Proxy | Up to 16,000 VMs | 4 vCPUs | 16GB |
| Unified Large Cloud Proxy | Between 16,000 to 80,000 VMs | 8 vCPUs | 48 GB |

Use a classic cloud proxy in VCF Operations, to collect and monitor data from your remote data centers. In addition to data collection, you can use your cloud proxy to collect logs into the Log Cluster and to collect and upload support bundles to the Broadcom support portal site. Use unified cloud proxy for log collection or log assist. For more information on log assist, see [Log Assist](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_889&appid=vcf-9-0&language=&format=rendered). For more information on log collection, see [Configuring and Analyzing Logs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/log-analysis.html).