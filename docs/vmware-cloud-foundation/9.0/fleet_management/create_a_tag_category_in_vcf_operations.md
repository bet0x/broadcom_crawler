---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management/create-a-tag-category.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Create a Tag Category in VCF Operations
---

# Create a Tag Category in VCF Operations

When you create a tag category, you must also create at least one tag in that category. After you create the category, you can create and add as many tags in it as you need.

Verify that you have TagsManage permissions in VCF Operations.

You cannot create an empty category, you must create at least one tag in the category. For each category that you create, you must specify whether a single or multiple tags are allowed per object, and which object types can be associated with this category. After you create the category, you can edit the tags added to the category. You can add more tags, delete some of the existing tags, or edit them.

You can also import existing tags and categories from vCenter instances. For more information, see [Import Tags and Categories from a vCenter Instance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management/import-tags-and-categories-from-a-vcenter-instance.html)

1. Log in to VCF Operations.
2. From the left navigation menu, click Fleet Management, and click Tags.
3. Click Create

   The Create Category dialog box appears.
4. Enter a name for the category. The name can consist of up to 128 characters.

   Once you create the category, you cannot change its name.
5. Enter a description for the category. The description can consist of up to 1024 characters.
6. To edit the tags per object and the object types that can be associated with the category, click Advanced Settings.
   1. Select the number of tags that can be assigned per associated object.

      If you select Multiple, after you create the category, you cannot change the value to Single.
   1. Select to which objects types the tags from the category can be assigned to.

      After you create the category, you can only add more object types to be associated with the category, you cannot remove the object types that you selected when creating the category. If you select All object types, after you create the category, you cannot change the value.
7. Create a tag to add to the category:
   1. Enter a name for the tag.

      Once you create the tag, you cannot change its name.
   1. Enter a description for the tag.
8. To create more tags and add them to the category, click Add Tag, and enter a unique name and description for each tag.
9. Click Create.

The category appears in the table with available categories for this VCF Operations instance.

You can edit, delete, or push the newly created category to VCF domain vCenter instances or custom groups. When you delete a category, you also delete all tags added to it. For backup purposes, you can also export all tag categories and tags available in the VCF Operations instance in JSON file format.