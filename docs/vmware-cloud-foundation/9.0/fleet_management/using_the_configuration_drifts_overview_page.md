---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/using-the-configuration-management-dashboard.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Using the Configuration Drifts Overview Page
---

# Using the Configuration Drifts Overview Page

The Configuration Drift dashboard allows you to view and monitor vCenter and vSphere cluster drift statuses.

You can view and compare configuration drifts and identify settings that have changed.

A configuration drift notifies you of any deviation from assigned configuration template values. Use the Configuration Enabled Objects Summary bar to view the total number of objects and their enabled statues. Enabled objects are comprised of all the vCenter at version 9.0 or greater that have a configuration template attached to them and include vSphere clusters with Configuration Profiles enabled.

The vCenter Instances Drift Status and Cluster Drift Status charts represent the state of the enabled vCenter instances and vSphere clusters at a given point in time. All the potential drift statuses and their definitions are listed below:

- Not Drifted: This state shows vCenter instances and vSphere clusters with no drifts from the desired state.
- Drift Detected: This state shows when vCenter instances or vSphere clusters have deviated from the desired standard configurations.
- Drift Check Failed: This state occurs under the following scenario's

  - vCenter instances or vSphere clusters are unavailable.
  - The drift computation is in progress
  - The drift has not been computed against that specific resource.
  - An internal error has occurred.
- Unavailable: This state shows a list of vCenter instances and vSphere clusters that are either

  - Below version 9.0
  - Not registered with the cloud proxy.

Additionally, you can view the Configuration Templates assigned to your vCenter instances and view all Objects.