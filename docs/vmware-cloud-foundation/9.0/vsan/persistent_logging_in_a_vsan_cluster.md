---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/designing-and-sizing-a-virtual-san-cluster/persistent-logging-in-a-virtual-san-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Persistent Logging in a vSAN Cluster
---

# Persistent Logging in a vSAN Cluster

Provide storage for persistence of the logs from the hosts in the vSAN cluster.

If you install ESX on a USB or SD device and you allocate local storage to vSAN, you might not have enough local storage or datastore space left for persistent logging.

To avoid potential loss of log information, configure the ESX Dump Collector and vSphere Syslog Collector to redirect ESX memory dumps and system logs to a network server.