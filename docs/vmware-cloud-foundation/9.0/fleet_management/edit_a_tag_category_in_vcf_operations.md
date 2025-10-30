---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management/edit-tags-and-categories.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Edit a Tag Category in VCF Operations
---

# Edit a Tag Category in VCF Operations

You can edit the description of any category in VCF Operations. To edit advanced settings of the category, special conditions apply. You cannot change the category name.

- Verify that you have TagsManage permissions in VCF Operations.

1. Log in to VCF Operations.
2. From the left navigation menu, click Fleet Management, and click Tags.
3. In the table with available categories, select the check box next to the category you want to edit.

   You can edit only one category at a time.
4. Click Edit.
5. Enter a new description for the category.
6. To change the number of tags allowed per object and the object types to be associated with tags from the category, click Advanced Settings, and update the values.

   - If during the creation of a category, the tags allowed per object were set to Multiple, you cannot change that value to Single.
   - If during the creation of a category, the associable object types were set to All object types, you cannot change that value at a later time. Any object type that you selected upon creating the category cannot be deselected at a later time.
7. Click Save.