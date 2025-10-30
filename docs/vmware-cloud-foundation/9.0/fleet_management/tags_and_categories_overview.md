---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Tags and Categories Overview
---

# Tags and Categories Overview

You can create tag categories and tags in your VCF Operations instance and use them to organize and manage your inventory objects at scale.

## What Are Tags and Categories

A tag consists of a name and description that you specify. To group related tags together and manage inventory objects at scale, you create categories and tags inside the categories. When you create a category, you can specify the object types for its tags, and whether more than one tag in the category can be applied to an object. After you create the category and tags, you can apply the tags to objects in your vSphere Client inventory in order to organize and manage the objects more easily, and to tag specific inventory objects when you configure different vSphere policies.

For example, if you want to tag inventory objects with memory over-commitment, you can create a category named Compute Memory, specify that the category applies to just hosts as an object type, and then add a tag named Memory Over-Commitment. After you create the category and tag, you can assign the tag to the specific hosts from your inventory.

## VCF Operations Tags and Categories

By using VCF Operations, you can manage tags from a central place for all VCF instances managed by the VCF Operations instance. You can create new tags and categories, and import existing tags and categories from workload or management domain vCenter instances.

After you create or import categories and tags in VCF Operations, you can push them to selected VCF domain vCenter instances or vCenter instances part of custom groups. You can then use the tags and categories in existing automation scripts or to tag objects in the vSphere Client. This will ensure scalability and prevent loss of tags and their associations to objects during vMotion.

By using the vSphere Client, you apply the tags as metadata to objects in the vCenter inventory. For more information, see [How Do You Assign or Remove a vSphere Tag.](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_005&appid=vsphere-9-0&language=&format=rendered)