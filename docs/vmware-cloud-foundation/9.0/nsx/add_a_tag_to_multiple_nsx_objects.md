---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/nsx-tags/add-a-tag-to-multiple-nsx-objects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Tag to Multiple NSX Objects
---

# Add a Tag to Multiple NSX Objects

You can add a tag to multiple objects simultaneously. However, this feature is
supported only for the virtual machine object.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Click InventoryTags.
3. Click Add Tag.
4. Enter a tag name.

   The maximum length of the tag name is 256 characters.
5. Enter a tag scope.

   For example, let us say, you want to tag virtual machines based on their
   operating system (Windows, Mac, Linux). Create three tags, such as Windows,
   Linux, and Mac, and set the scope of each tag to OS.

   The maximum length of the scope is 128 characters.
6. Under the Assigned
   To column, click Set Virtual
   Machines.
7. Select the virtual machines to
   which you want to assign the tag, and click Apply.

   You must assign a tag to at least one virtual machine before you can save the
   tag.
8. Click Save.

- If the tag is assigned to many virtual machines, the assignment might take
  some time. When the assignment is in progress, the Last
  Assignment Status shows
  Running. After the tag is assigned successfully
  to all the selected virtual machines, the Last Assignment
  Status column changes to
  Successful.
- If a partial assignment occurs, the system does not roll back the tag
  assignment from the VMs on which the tag is applied. For example, assume
  that you selected 100 VMs for a bulk tag assignment, and the assignment
  fails for 10 VMs. The tag that is assigned on the remaining 90 VMs is not
  rolled back.

  In such partial assignment situations, run the following API
  to retrieve the status of the tagging
  operation:

  ```
  GET /api/v1/infra/tags/tag-operations/<operation-id>/status
  ```

  You
  can also retrieve the realized status of the tagging operation with the
  following
  API:

  ```
  GET /api/v1/infra/realized-state/realized-entities?intent_path=/infra/tags/tag-operations/<operation-id>
  ```

  For more details about these
  APIs, see the NSX API Guide.

If you have a long list of tags in the
inventory, you can filter or search tags to find the tags of your interest quickly.
You can filter on source, scope, and tag (name of the tag). You can also sort tags
in the UI. However, due to the case-sensitive nature of tags, tags are sorted only
in a lexical order.

The following limitations apply to
searching or filtering tags:

- You cannot filter tags on the
  source and scope attributes simultaneously because both work on the scope
  attribute of the tag.
- The API does not support
  filtering tags with special characters, such as \*, &, /, \, and so on.
  However, you can use special characters to filter tags in the UI.