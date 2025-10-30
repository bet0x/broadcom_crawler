---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud/activating-data-persistence-in-cloud-proxy.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Activating Data Persistence in Cloud Proxy
---

# Activating Data Persistence in Cloud Proxy

Use data persistence, to avoid data gaps in case of temporary connectivity issues. You can activate data persistence to allow the cloud proxy to store data that is sent to VCF Operations, if the connection fails between the cloud proxy and VCF Operations. The cloud proxy stores all the persisted data that includes metrics and properties, along with time stamps.

Cloud proxy can store data for a maximum duration of one hour. If there is lack of space or if the connection fail lasts for more than an hour, the cloud proxy rotates the stored data by deleting the oldest stored data and replacing it with the most recently collected data. In case of lack of space, you can add additional storage, for more information, see KB article [2016022](https://kb.vmware.com/s/article/2016022).

After the connection is restored, the cloud proxy sends the stored data to VCF Operations before the real-time data. The stored data is displayed before the real-time data as data is displayed in the correct time series. If the connection loss was more than one hour, there can also be a gap in the displayed data.

You can activate data persistence when you deploy a new cloud proxy. For more information, see [Configuring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html#GUID-bd1eed2a-5668-4640-8ae3-79ce18f3d081-en). You can also activate data persistence in an existing cloud proxy. For more information, see [Monitoring the Health of Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies.html#GUID-6887a5cc-2bce-41e9-b965-603887775adb-en).