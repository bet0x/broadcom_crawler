---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/account-information-vmware-vsphere-solution-account-options.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring Advanced Settings for a vCenter Account
---

# Configuring Advanced Settings for a vCenter Account

To begin monitoring your environment with VCF Operations, you configure the vCenter account. The solution includes the vCenter account that collects data from the target vCenter instances. For more information, see [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html).

## Where You Find the Solution- vCenter

From the left menu, click AdministrationIntegrations tab. Click ADD, and then select vCenter.

## Advanced Settings Options for Configuring a vCenter Account

Configure and modify the vCenter account on the Account Information page.

| Option | Description |
| --- | --- |
| Advanced Settings | Provides options related to designating specific collectors to manage this account, managing object discovery and change events. |
| Auto Discovery | Determines whether new objects added to the monitored system are discovered and added to VCF Operations after the initial configuration of the account.   - If the value is true, VCF Operations collects the information about any new objects that are added to the monitored system after the initial configuration. For example, if you add more ESX hosts and virtual machines, these objects are added during the next collections cycle. This is the default value. - If the value is false, VCF Operations monitors only those objects that are present on the target system when you configure the account. |
| Process Change Events | Determines whether the account uses an event collector to collect and process the events generated in the vCenter instance.   - If the value   is true, the event collector collects and publishes events from   vCenter.   This is the default value. - If the value   is false, the event collector does not collect and publish events. |
| Process VC Tasks | Determines whether the account uses a task collector to collect and process tasks that are created in the vCenter instance.   - If the value is true, the task collector collects and publishes tasks from vCenter instance. This is the default value. - If the value is false, the event collector does not collect and publish tasks. |
| Activate Collecting vSphere Distributed Switch  Activate Collecting Virtual Machine Folder  Activate Collecting vSphere Distributed Port Group | When set to false, reduces the collected data set by omitting collection of the associated category. |
| Maximum Number Of Virtual Machines Collected | Reduces the collected data set by limiting the number of virtual machine collections.  To omit data on virtual machines and have VCF Operations collect only host data, set the value to zero. |
| Provide data to vSphere Predictive DRS | vSphere Predictive DRS proactively load balances vCenter cluster to accommodate predictable patterns in the cluster workload.  VCF Operations monitors virtual machines running in vCenter, analyzes longer-term historical data, and provides forecast data about predictable patterns of resource usage to Predictive DRS. Based on these predictable patterns, Predictive DRS moves to balance resource usage among virtual machines.  Predictive DRS must also be activated for the vSphere Clusters managed by vCenter instances monitored by VCF Operations. Refer to the [vSphere Resource Management](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-resource-management-8-0.html) for details on activating Predictive DRS on a per vSphere cluster basis.  When set to true, designates VCF Operations as a predictive data provider, and sends predicative data to vCenter . You can only register a single active Predictive DRS data provider with vCenter at a time. |
| Activate Actions | Activating this option helps in triggering the actions that are related to vCenter. |
| Cloud Type | Provides an ability to identify the type of vCenter that is used in VCF Operations. |
| vCenter ID | A globally unique identifier associated with the vCenter instance. |
| Deactivate collecting Guest File Systems with names containing | Provide comma separated list of strings. If these strings are found in any guest files system mount point name, that guest file system will not be collected. |
| Enable vSphere Supervisor Collection | Enables the collection of the auto discovered vSphere Supervisor cluster. |
| Activate vCenter -initiated metric collection | If the value is true, it enables the collection of Host and VM level GPU metrics.  Change the value to false to stop metric collection. It may take up to 10 minutes to completely disable metric collection. |
| vCenter- initiated metric collection sample interval | The sample interval in seconds between vCenter initiated metric collection. To change the sample interval, you must first disable vCenter initiated metric collection. Update the collection sample interval before restarting the metric collection. |

You can find the vSphere Hardening Guides at [VMware Security Hardening Guides](http://www.vmware.com/security/hardening-guides.html).

Click Save to finish configuration of the solution.