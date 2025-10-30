---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Upgrading Cloud Proxy
---

# Upgrading Cloud Proxy

Cloud Proxies are upgraded to a compatible cluster version automatically after the cluster upgrade. Expect a downtime of one or two cycles, as cloud proxies do not collect any data during this period. Data collection resumes after the upgrade is complete. The upgrade process runs concurrently for up to ten cloud proxies. If you have more than ten cloud proxies, the upgrade process will continue sequentially and the next cloud proxy upgrade will start as soon as any one of the ten running upgrades completes or fails the upgrade process. In case the automatic upgrade fails, upgrade your cloud proxy manually using the CLI.

When your cloud proxies are upgraded, the cloud proxy internal certificates also get renewed. After each upgrade, the cloud proxies will have a new CA signed certificate with a five year validity period.

For more information on what data gets collected, see [VMware vSphere Solution in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere.html).

You can manually upgrade your cloud proxy [Using the Cloud Proxy Command-Line Interface](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy/using-the-cloud-proxy-command-line-interface-on-cloud.html).