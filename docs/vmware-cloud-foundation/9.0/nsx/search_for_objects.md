---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/search-by-objects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Search for Objects
---

# Search for Objects

You can search for
objects using various criteria throughout the
NSX inventory.

The search results are sorted
by relevance and you can filter these results based on your search query.

If you have special
characters in your search query that also function as operators, then you must
add a leading backslash. The characters that function as operators are: +, -,
=, &&, ||, <, >, !, (, ), {, }, [, ], ^, '', ~, ?, :, /, \.

1. With admin privileges, log in
   to NSX Manager.
2. On the homepage, enter a
   search pattern for an object or object type.

   You can also select a recent query or a search query that you saved.

   As
   you enter a search pattern, the search feature provides assistance by showing
   the applicable keywords.

   Search | Search Query || Objects with Logical as the name or property | Logical |
   | Exact logical switch name | display\_name:LSP-301 |
   | Names with special characters such as, ! | Logical\! |

   All the
   related search results are listed and grouped by resource type in different
   tabs.

   You can click the tabs for
   specific search results for a resource type.
3. In the search bar, click
   the save icon to save your refined search criteria.
4. In the search bar, click
   the
   ![Advanced search icon in NSX-T 
   				](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a35906d3-3379-4650-989b-5ff0f87fe4be.original.png) icon to open the advanced search column where you
   can refine your search.
5. Specify one or more
   criteria to refine your search.

   - Name
   - Resource Type
   - Description
   - ID
   - Created by
   - Modified by
   - Tags
   - Creation Date
   - Modified Date

   You can also view your
   recent search results and saved search criteria.
6. Click
   Clear
   All to reset your advanced search criteria.