---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/nsx-tags/add-tags-to-an-nsx-object.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add Tags to an NSX Object
---

# Add Tags to an NSX Object

You can select existing tags that are
available in the NSXinventory or create new
tags to add to an object.

The following procedure explains the steps for
adding tags to a single object. For this documentation, the segment object is
considered. The steps for adding tags to other objects remain the same. You can
navigate to the specific object page, and follow similar steps to add tags to that
object.

For information about the maximum number of tags
supported for objects in NSX, see the
VMware Configuration Maximums tool at <https://configmax.vmware.com/home>.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Ensure that you are in the edit mode
   of an object to assign tags to it. Objects can be segments, groups, tier-0
   gateways, tier-1 gateways, and so on.

   For example, to tag segments,
   click NetworkingSegments. Next to the segment that you want to edit, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
3. In the
   Tag drop-down menu, enter a tag name. When you are
   done, click Add Item(s).

   The maximum length of the tag name is 256 characters.

   If tags exist in the inventory,
   the Tag drop-down menu displays a list of the
   available tags and their scope. You can select an existing tag from the
   drop-down menu and assign it to the segment.

   If you
   are assigning a tag to the virtual machine, do not assign the Edge\_NSGroup
   tag to the VM. The system automatically assigns this tag to edge VMs for
   including them in the DFW exclusion list.
4. Enter a tag scope.

   For example, let us say, you want to tag segments based on department
   names, such as sales, marketing, finance, and so on, in your organization.
   Create tags such as sales, marketing, and finance, and set the scope of each tag
   to department.

   The maximum length of the scope is 128 characters.

   If you selected an existing tag
   from the inventory, the scope of the selected tag is applied automatically.
   Otherwise, you can enter a scope for the new tag that you are
   creating.
5. Click the +
   icon or press Enter.

   The tag is added to the segment.
6. Add more tags to the segment, if
   required.
7. Click
   Save.