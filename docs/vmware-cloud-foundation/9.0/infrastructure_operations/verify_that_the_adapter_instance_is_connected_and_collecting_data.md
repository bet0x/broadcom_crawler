---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsan-overview/verify-that-your-vsan-adapter-is-connected-and-collecting-data.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Verify that the Adapter Instance is Connected and Collecting Data
---

# Verify that the Adapter Instance is Connected and Collecting Data

You configured an adapter instance of vSAN with credentials for a vCenter. Now you want to verify that your adapter instance can retrieve information from vSAN objects in your environment.

To view the object types, from the left menu, click Inventory Adapter InstancesvSAN Adapter Instance<User\_Created\_Instance>.

Object Types that vSAN Discovers



| Object Type | Description |
| --- | --- |
| vSAN Adapter Instance | The vSAN instance. |
| vSAN Cluster | vSAN clusters in your data center. |
| vSAN Datastore | vSAN datastores in your data center. |
| vSAN Disk Group | A collection of SSDs and magnetic disks used by vSAN. |
| vSAN Fault Domain | A tag for a fault domain in your data center. |
| vSAN Host | vSAN hosts in your data center. |
| vSAN Witness Host | A tag for a witness host of a stretched cluster, if the stretched cluster feature is activated on the vSAN cluster. |
| vSAN World | A vSAN World is a group parent resource for all vSAN adapter instances. vSAN World displays aggregated data of all adapter instances and a single root object of the entire vSAN hierarchy. |
| Cache Disk | A local physical device on a host used for storing VM files in vSAN. |
| Capacity Disk | A local physical device on a host used for read or write caching in vSAN |

The vSAN adapter also monitors the following objects discovered by the VMware vSphere adapter.

- Cluster Compute Resources
- Host System
- Datastore

1. In the menu, click InventoryAdapter InstancesvSAN Adapter Instance.
2. Select the adapter instance name to display the list of objects discovered by your adapter instance.
3. Slide the display bar to the right to view the object status. 

   | Object Status | Description |
   | --- | --- |
   | Collection State | If green, the object is connected. |
   | Collection Status | If green, the adapter is retrieving data from the object. |
4. Deselect the adapter instance name and expand the Object Types tag. 

   Each Object Type name appears with the number of objects of that type in your environment.

If objects are missing or not transmitting data, check to confirm that the object is connected. Then check for related alerts.

To ensure that the vSAN adapter can collect all performance data, the vSAN performance service must be activated in vSphere. For instructions on how to activate the service, see Turn on vSAN Performance Service in [KB 326483](https://knowledge.broadcom.com/external/article/326483/vsan-health-service-performance-service.html).

If the vSAN performance service is deactivated or experiencing issues, an alert is triggered for the vSAN adapter instance and the following errors appear in the adapter logs.

```
ERROR com.vmware.adapter3.vsan.metricloader.VsanDiskgroupMetricLoader.collectMetrics 
   - Failed to collect performance metrics for Disk Group
com.vmware.adapter3.vsan.metricloader.VsanDiskgroupMetricLoader.collectMetrics 
   - vSAN Performance Service might be turned OFF.
com.vmware.adapter3.vsan.metricloader.VsanDiskgroupMetricLoader.collectMetrics 
   - (vim.fault.NotFound) 
   {
   faultCause = null,
   faultMessage = (vmodl.LocalizableMessage) 
      [
         com.vmware.vim.binding.impl.vmodl.LocalizableMessageImpl@98e1294
      ]
   }
```