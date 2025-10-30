---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/filter-by-object-attributes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Filter by Object Attributes
---

# Filter by Object Attributes

When viewing objects in NSX Manager, you can filter the objects by one or more of
their attributes. For example, when viewing details of Tier 0 gateways you can choose to
filter by Status and view only those gateways that are
Down.

The following types of filters are
available:

- Predefined filters – A list of
  commonly used filters that you can apply to your objects.
- Text-based filter – A filter based
  on the attribute value that you enter. This filter is applicable only to the
  Name, Tag,
  Path, and Description
  attributes of the objects.
- Attribute-value pairs – An
  attribute drop-down menu that you can use to specify attribute-value pairs for
  filtering.

You can either use multiple attributes of
an object or multiple values of a single attribute to filter objects. The AND
operator is applied when you select multiple attributes whereas the OR operator is
used when you specify multiple values of a single attribute.

1. From your browser, log in with
   admin privileges to an NSX Manager
   at https://<nsx-manager-ip-address>.
2. Navigate to the tab that displays the objects you want to view.
3. Specify the attributes that you
   want to use to filter the objects.
   - Click ![Apply filter](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6899af24-0783-469a-9d57-d1942f93f9be.original.png)
     and select from a list of predefined filters.
   - Enter a value for the
     Name, Tag,
     Path, or Description
     attributes.
   - Select an attribute
     from the drop-down menu and specify its value. For example,
     Status: Down

   Objects satisfying your filter criteria are displayed.
4. Click Clear  to reset
   your filters.