---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/vsan-stretched-cluster-site-fails-or-loses-network-connection.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Stretched Cluster Site Fails or Loses Network Connection
---

# vSAN Stretched Cluster Site Fails or Loses Network Connection

A vSAN stretched cluster manages failures that occur due to the loss of a network connection between sites or the temporary loss of one site.

## vSAN Stretched Cluster Failure Handling

In most cases, the vSAN stretched cluster continues to operate during a failure and automatically recovers after the failure is resolved.

How vSAN Stretched Cluster Handles Failures



| Type of Failure | Behavior |
| --- | --- |
| Network Connection Lost Between Active Sites | If the network connection fails between the two active sites, the witness host and the preferred site continue to service storage operations, and keep data available. When the network connection returns, objects protected by a policy with a site tolerance attribute are resynchronised |
| Secondary Site Fails or Loses Network Connection | If the secondary site goes offline or becomes isolated from the preferred site and the witness host, the witness host and the preferred site continue to service storage operations, and keep data available, objects protected by a policy with a site tolerance attribute are resynchronised |
| Preferred Site Fails or Loses Network Connection | If the preferred site goes offline or becomes isolated from the secondary site and the witness host, the secondary site continues storage operations if it remains connected to the witness host, objects protected by a policy with a site tolerance attribute are resynchronised |
| Witness Host Fails or Loses Network Connection | If the witness host goes offline or becomes isolated from the preferred site or the secondary site, objects become noncompliant but data remains available. VMs that are currently running are not affected. |