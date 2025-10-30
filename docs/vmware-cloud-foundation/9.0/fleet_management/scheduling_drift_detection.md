---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/using-the-configuration-management-dashboard/scheduling-drift-detection.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Scheduling Drift Detection
---

# Scheduling Drift Detection

You can automate the drift detection process and schedule drift detection in VCF Operations.

Scheduling drift detection enables you to run automatic drift checks on your vCenter instances at an interval of your choice.

1. To schedule drift checks, from the left menu, click Fleet ManagementConfiguration DriftsSchedule Drift Detection.
2. Enter a name and description in the Configuration Drift Check Information pane and click Next.

   You can schedule drifts only for vCenter object types.
3. Select an object from the Select Scope window on the right and drag it into the left Scope window to add vCenter instances and click Next.

   If you select a VCF folder as the scope, all VCF instances belonging to the folder get automatically added to the scope.
4. Click Preview Scope to confirm the vCenter instances that the drift check will run on, and then click Next.
5. You can filter the criteria and add multiple criterias for the vCenter object type and then click Next.
6. Set the Schedule and click Create.

   A new job is created to run scheduled drift detection in the automation central page. For more information see [Configuring Automation Jobs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-automation-using-jobs.html).