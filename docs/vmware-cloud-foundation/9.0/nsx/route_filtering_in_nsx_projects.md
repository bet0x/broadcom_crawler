---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/route-filtering-in-nsx-projects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Route Filtering in NSX Projects
---

# Route Filtering in NSX Projects

In an NSX environment, multiple projects can be configured with the same tier-0 or a tier-0 VRF gateway. This implies that tier-1 gateways and NSX VPCs in the projects are connected to the same tier-0 or a tier-0 VRF gateway.

To avoid IP address conflicts between the projects, you can filter routes that are advertised out of the specified projects by all the tier-1 gateways or NSX. For instance, prefixes allow you to ensure that only the IP addresses from the external IP blocks are advertised out of the specified projects.

An Enterprise Admin can configure route filtering and it cannot be overwritten at the project level.

First, you need to create the prefix lists that you want to use. Then, in the project route filter, you can define the mapping of the projects to the prefix lists.

Project route filter is supported only using NSX APIs. The UI does not support this feature.

Example
:   The following diagram shows two projects, Project 1 and Project 2, which are connected to the same tier-0 gateway. Project 1 contains two tier-1 gateways, and Project 2 contains a single tier-1 gateway. For Project 1, the allowed prefix is 10.0.0.0/24, and for Project 2, the allowed prefix is 192.168.0.0/24.

    ![This diagram is explained in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/653b04b5-37c8-4718-b271-9eea5e68fb07.original.png)

## Workflow for Creating a Project Route Filter Using APIs

1. Create a prefix list.

   For example, run the following NSX API:

   ```
   PATCH https://<nsx-mgr>/policy/api/v1/infra/routing-config/prefix-lists/<prefix-list-id>
   {
     "prefixes": [
         {
             "network":"172.20.0.0/16",
             "action":"PERMIT"
         },
         
     ]
   }
   ```

   For more information about this API, see the NSX API Guide.
2. Read the prefix lists and verify the details.

   For example, run the following NSX APIs:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/routing-config/prefix-lists
   ```

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/routing-config/prefix-lists/<prefix-list-id>
   ```
3. Create a project route filter.

   For example, run the following NSX API:

   ```
   PATCH https://<nsx-mgr>/policy/api/v1/infra/routing-config/project-route-filters/<route-filter-id>
   {
     "projects_list": ["/orgs/default/projects/project-1"],
     "match_prefix_list" : ["/infra/routing-config/prefix-lists/list-1", "/infra/routing-config/prefix-lists/list-2"]
   }
   ```

   This API creates a mapping of projects to prefix lists. Prefix lists are applied to all tier-1 gateways in the specified projects.

   For more information about this API, see the NSX API Guide.
4. Read the project route filter and verify the details.

   For example, run the following NSX API:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/routing-config/project-route-filters/<route-filter-id>
   ```
5. Optional: Retrieve a list of all project route filters.

   For example, run the following NSX API:

   ```
   GET https://<nsx-mgr>/policy/api/v1/infra/routing-config/project-route-filters
   ```
6. Optional: Delete a prefix list and a project route filter.

   For example, run the following NSX APIs:

   ```
   DELETE https://<nsx-mgr>/policy/api/v1/infra/routing-config/project-route-filters/<route-filter-id>
   ```

   ```
   DELETE https://<nsx-mgr>/policy/api/v1/infra/routing-config/prefix-lists/<prefix-list-id>
   ```