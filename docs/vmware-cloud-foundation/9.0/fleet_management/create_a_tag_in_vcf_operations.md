---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management/create-a-tag-and-add-it-to-a-category.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Create a Tag in VCF Operations
---

# Create a Tag in VCF Operations

Verify that you have TagsManage permissions in VCF Operations.

In VCF Operations, you can only create tags inside an existing tag category or at the time when you create a new category.

1. Log in to VCF Operations.
2. From the left navigation menu, click Fleet Management, and click Tags.
3. Click the arrow icon next to category, in which you want to create a tag.

   A table with all tags added to this category appears.
4. Click Create.

   The Create Tag dialog box appears.
5. Enter a unique name for the tag. The name can consist of up to 128 characters.
6. Enter a description for the tag. The description can consist of up to 1024 characters.
7. To create more tags and add them to the category, click Add Tag, and enter a name and description for each tag.
8. Click Create.

The tag appears in the table with the available tags for the category.

You can edit or delete the tag. You can also export all tag categories and tags available in the VCF Operations instance in JSON file format.

When an export is in progress, initiated by you or another user, you cannot initiate the export again before the first export is complete.

To assign tags to specific inventory objects, use the vSphere Client. For more information, see [How Do You Assign or Remove a vSphere Tag.](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_005&appid=vsphere-9-0&language=&format=rendered)