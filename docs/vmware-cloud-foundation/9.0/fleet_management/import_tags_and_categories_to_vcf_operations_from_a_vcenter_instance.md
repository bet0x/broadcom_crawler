---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management/import-tags-and-categories-from-a-vcenter-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Import Tags and Categories to VCF Operations from a vCenter Instance
---

# Import Tags and Categories to VCF Operations from a vCenter Instance

You can import existing tags and tag categories from your VCF domain vCenter instances to VCF Operations. Importing tags into VCF Operations enables you to manage tags and categories for more than one vCenter instance from a single place.

- Verify that the VCF domain vCenter instance from which you want to import tags and tag categories is of version 9.0.
- Verify that the VCF domain vCenter instance from which you want to import tags has a valid VCF 9.0 license.
- Verify that the VCF domain vCenter instance from which you want to import tags and tag categories is integrated with this VCF Operations instance.
- Verify that you have TagsManage permissions in VCF Operations.

After you import tags and categories to your VCF Operations instance, you can push them to other vCenter instances in order to have to have consistent tagging across you VCF Fleet.

If you cannot see the conflict details, verify that you have the REST API read privileges assigned.

When a task is in progress, you cannot initiate the same task again. For example, if another user or you initiate an import, you cannot initiate import again before the first task is complete.

1. Log in to VCF Operations.
2. From the left navigation menu, click Fleet Management, and click Tags.
3. Click Import.

   The Import Categories dialog box appears, and you can see a list of all VCF domains integrated with your VCF Operations instance.
4. Select a VCF domain from which you want to import tags and tag categories, and click Import.

   You cannot initiate an import task if the task is already in progress, you must wait for the task to complete to initiate it again.

   If another user initiated an import task and it is in progress, a warning appears.

The tags and categories are imported from the VCF domain vCenter instance. If some of the categories cannot be imported, click View Conflict Details or View Import Details in the banner to view a list with the import conflict or error reasons and possible resolutions. Once you dismiss the banner notification, you cannot view it again.

You cannot see banner notifications for tasks performed by another user.