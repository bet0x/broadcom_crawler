---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-tag-management/push-tags-and-categories-to-a-vcenter-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Push Tag Categories to a VCF Domain vCenter Instance or a Custom vCenter Group
---

# Push Tag Categories to a VCF Domain vCenter Instance or a Custom vCenter Group

After you create or import tag categories and tags into a VCF Operations instance, you can push these tag categories to other VCF domain vCenter instances or vCenter instances that are part of custom groups. To push categories to vCenter instances part of custom groups, the custom groups must be of type Tag Group.

- Verify that you have vSphere Tagging privileges for the target VCF domain vCenter instance.
- Verify that the target VCF domain vCenter instance is of version 9.0.
- Verify that you have TagsManage permissions in VCF Operations.
- If you want to push tag categories to vCenter instances that are part of custom groups, verify that there are custom groups of type Tag Groupcreated in the VCF Operations instance, and vCenter instances are added to those custom groups. Even if other object types are also added to the custom groups, tags and categories are pushed only to vCenter instances. For more information about creating custom object groups in VCF Operations, see [Managing Custom Object Groups in VCF Operations](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_149&appid=vcf-9-0&language=&format=rendered).

By using VCF Operations, you create and manage tags and categories from a single place, at scale. You can then push the created categories and the tags added to them to as many VCF domain vCenter instance as you need, instead of creating the categories manually in each vCenter instance.

When you try to push a tag category to VCF domain vCenter instances, if the tag category you try to push, has some of the same properties as a tag category in the target vCenter instance, but differences in other properties, the operations fails and the categories are displayed as conflicts. Similarly, if a tag added to the category have some of the same properties as a tag in the same category in the target vCenter instance, but differences in other properties, the operation fails and the categories are displayed as conflicts.

If you cannot see the conflict details, verify that you have the REST API read privileges assigned for the VCF Operations instance.

To proceed with pushing the categories, you must first manually resolve the conflicts by following the guidance provided in the details for each conflict. Alternatively, you can select to overwrite the category properties in the target VCF domain vCenter instance wherever a conflict is detected. The following types of conflicts can only be resolved manually, even you select the check box:

| Conflict | Resolution |
| --- | --- |
| A category or tag with the same name and ID exists both in VCF Operations, and in the vCenter instance selected for the push operation. The value for Tags per object is set to One Tag in VCF Operations, but it is set to Multiple Tags in the vCenter instance. | In VCF Operations, change the value for the Tags per object attribute to Multiple Tags. |
| A category or tag with the same name and ID exists both in VCF Operations, and in the vCenter instance selected for the push operation. The Associable object types attribute in the vCenter instance contains more object types than the Associable object types attribute in VCF Operations. | In VCF Operations, edit the values for the Associable object types attribute and verify they are the same as in the vCenter instance. |
| A category or tag with the same name but a different ID exists both in VCF Operations, and in the vCenter instance selected for the push operation. | Rename the category or tag in the vCenter instance, or delete the conflicting category or tag from VCF Operations or from the vCenter instance. |

When a task is in progress, you cannot initiate the same task again. For example, if another user or you initiate a push of categories, you cannot initiate push again before the first task is complete.

1. Log in to VCF Operations.
2. From the left navigation menu, click Fleet Management, and click Tags.
3. From the table with available tag categories, select the check box next to the tag categories you want to push.

   You can push up to 20 tag categories at a time.
4. Click Push Categories.

   The Push Categories dialog box appears.
5. Select the VCF domain vCenter instances or custom groups to which you want to push categories:
   - To push categories to specific VCF domain vCenter instances, click the VCF Domain vCenter Instances tab, and select VCF Instances or a VCF domain vCenter instances from the list.
   - To push categories to custom groups, click the Custom Groups tab, and select a custom group from the list.
6. If you want to overwrite the category properties in the target VCF domain vCenter instance when a conflict is detected, select the check box at the bottom of the dialog box.
7. Click Push.

The tag categories are pushed to the selected VCF domain vCenter instances or vCenter instances in a custom group.

You cannot see banner notifications for tasks performed by another user.

You can use the tags and categories with existing automation scripts or assign tags to inventory objects by using the vSphere Client. For more information about assigning tags to specific inventory object, see [How Do You Assign or Remove a vSphere Tag.](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_005&appid=vsphere-9-0&language=&format=rendered)