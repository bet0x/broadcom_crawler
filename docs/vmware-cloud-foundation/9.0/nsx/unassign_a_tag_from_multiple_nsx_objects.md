---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/nsx-tags/unassign-a-tag-from-multiple-nsx-objects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Unassign a Tag from Multiple NSX Objects
---

# Unassign a Tag from Multiple NSX Objects

You can unassign a tag from multiple objects simultaneously. However, this feature is
supported only for virtual machines.

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Click InventoryTags.
3. Next to the tag name, click
   ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Edit.
4. In the Assigned
   To column, click the number of virtual machines that are
   assigned this tag.
5. Click the
   X icon for each virtual machine that you want to
   unassign this tag.

   - You can do a bulk
     unassignment of a tag on a maximum of 1000 virtual machines at one
     go.
   - When a tag is
     unassigned from all objects, the tag is deleted automatically from
     the inventory after five days.
6. Click
   Apply, and then click
   Save.