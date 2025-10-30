---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/handling-failures-in-virtual-san/failure-handling-in-virtual-san/component-failure-states-in-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Component Failure States
---

# Failure States of vSAN Components

In vSAN, components that have failed can be in absent or degraded state.

According to the component state, vSAN uses different approaches for recovering virtual machine data. vSAN also provides alerts about the type of component failure. See [Using the VMkernel Observations for Creating vSAN Alarms](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/using-the-vmkernel-observations-for-creating-vsan-alarms.html#GUID-ece785b6-225d-4ec1-91e1-667f3bacaa4f-en) and [Using the vSAN Default Alarms](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/using-the-vsan-default-alarms.html#GUID-87edae6f-2d7c-44af-919c-0197b9726052-en).

vSAN supports two types of failure states for components:

Failure States of Components in vSAN



| Component Failure State | Description | Recovery | Cause |
| --- | --- | --- | --- |
| Degraded | A component is in degraded state if vSAN detects a permanent component failure and assumes that the component is not going to recover to working state. | vSAN starts rebuilding the affected components immediately if there are adequate resources in the cluster. | - Failure of a flash caching device - Magnetic or flash capacity device failure - Storage controller failure |
| Absent | A component is in absent state if vSAN detects a temporary component failure where the component might recover and restore its working state. | vSAN starts rebuilding the affected components immediately if there are adequate resources in the cluster if they are not available within a certain time interval. By default, vSAN starts rebuilding absent components after 60 minutes. | - Lost network connectivity - Failure of a physical network adapter - ESX host failure - Unplugged flash caching device - Unplugged magnetic disk or flash capacity device |