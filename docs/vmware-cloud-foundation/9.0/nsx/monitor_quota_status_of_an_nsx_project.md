---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/monitor-quota-status-of-an-nsx-project.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Monitor Quota Status of an NSX Project
---

# Monitor Quota Status of an NSX Project

Project users can periodically check the quotas status of their projects to know the
percentage of quota that is used, view any alarms that might have been raised, and decide
whether any troubleshooting actions are required to resolve those alarms.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Click
   Default, and then click
   Manage.
3. Ensure that you are in the Projects tab.
4. In the Quota
   Status column, click Check Status.

   - If the status changes to
     OK, it means that the number of
     user-created objects in the project is within the limit.
   - If the status changes to
     Error, it means that the quota has
     reached (that is, 100% of quota is used).
   - If the status changes to
     Not Set, it means that no quota is
     defined for the project.

   Use the information that is
   displayed in the Alarms column to know whether any
   alarms are raised. Alternatively, you can navigate to HomeAlarms and view the active alarms, if any.

   When the quota limit is reached,
   a Creation Count Limit Reached event is
   displayed on the Alarms page.

   The alarm due to this event is
   visible to both the Enterprise Admin and the Project Admin. View the details
   of this event to learn about the recommended actions.

   For the Creation
   Count Limit Reached event, the threshold value is currently not
   configurable. System-defined threshold value is used, by default.
5. To know more about the quota
   details of a project, click the value (OK or
   Error) in the Quota
   Status column.

   The Quota
   Status window displays quota details, such as the limits set for
   the various object types in the quota, the quota name, the percentage of quota
   used, and other details.