---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/assigning-policies.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Assigning Policies
---

# Assigning Policies

The Policy Assignment workspace displays all the policies available in your environment.

## Where You Assign Policies

To create and modify policy assignments, from the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Assignment tile.

## How the Policy Assignment Workspace Works

You can assign policies to your environment to activate controls, view, and manage your object assignment scope.

| Option | Description |
| --- | --- |
| Left Pane: Displays the list of policies available in your environment and provides different filters to understand policy distribution. | |
| Inactive/Active | You can filter policies by active or inactive status. A policy is considered to be active only when it is assigned to an object or a custom group. |
| Visualization Type | You can sort active policies based on different criteria.  - Fixed: Displays active policies with the sections of the policies fixed and equal to each other. - By Assignments: Displays the policies based on the number of objects assigned. - By Affected Objects: Displays policies based on the affected object count.   The sorting options are available only for the active policies. |
| Type Policy Name | Type the name of the policy in the search box to filter by policy name. |
| Policies | All the policies available in your environment are displayed in the left pane. Expand the policy card to view the priority, direct assignments, custom groups, affected objects, default assignment, and hierarchy of the policy. The default assignments are displayed only for the default policy.  When you click on a policy, the objects and custom groups associated with the selected policy are displayed under Assigned Objects in the right pane. |
| Right Pane: Displays details of the selected policy and allows you to drag and drop objects or custom groups to the selected policy. | |
| Selected Policy | Displays the name of the selected policy. |
| All Objects | Displays all objects and custom groups available in your environment in the Inventory and Custom Groups tabs respectively. To add new objects to a policy:  1. In the right pane, click All ObjectsInventory. 2. Select the objects you want to assign to the policy. You can also search for the objects by typing the object name in the search box. 3. Drag the items from the Inventory tab and drop them into the policy card on the left pane. 4. In the Assign Objects window, select one of the following options:    1. Only this object: Select this if you want to apply changes only to the selected objects.    2. Include child object: Select this if you want to apply changes to the child objects. You can define the depth of change by entering a number in the Depth field. The maximum value for the Depth field is 10. 5. Click Confirm.  To add custom groups to a policy:  1. In the right pane, click All ObjectsCustom Groups. 2. Select the custom groups you want to assign to the policy in the Custom Groups tab. You can also search for the custom groups by typing the custom group name in the search box. 3. Drag the items from the Custom Groups tab and drop them into the policy card on the left pane. 4. Click Confirm. |
| Assigned Objects | Displays the objects and custom groups assigned to the selected policy.  - Name: Displays the name of the object/custom group. - Assignment Type: Displays the type of assignment. - Depth: Displays the depth of the child objects that the policy affects. Click the Edit icon to change the depth. - Action: Allows you to delete an object or custom group.  You can also drag objects/custom groups from Assigned Objects and drop them into the policy card of your choice. |