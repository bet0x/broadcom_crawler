---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/hierarchical-api-for-nsx-projects.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Hierarchical API for NSX Projects
---

# Hierarchical API for NSX Projects

NSX
Hierarchical API provides users a way to create an entire or a
part of an intent by invoking a single API call. The input to the API is expressed in a tree
format. Each node in tree can have multiple children of different types.

Hierarchical API is supported for projects.
Project users can invoke the Patch API calls, as described in this documentation, to
create, update, or delete an entire intent hierarchy, or a part of an intent
hierarchy.

## Patch API

The API calls in this section are
organized in terms of user roles.

Enterprise Admin
:   Enterprise Admin can run any
    of these Patch API calls:

    ```
    PATCH https://<nsx-mgr>/policy/api/v1/org-root
    ```

    ```
    PATCH https://<nsx-mgr>/policy/api/v1/orgs/default/projects/<project-id>/infra
    ```

    Example Request Body:

    ```
    PATCH https://<nsx-mgr>/policy/api/v1/org-root
    {
    	"resource_type": "OrgRoot",
    	"children": [{
    		"resource_type": "ChildResourceReference",
    		"id": "default",
    		"target_type": "Org",
    		"children": [{
    			"resource_type": "ChildProject",
    			"Project": {
    				"id": "project-1",
    				"resource_type": "Project",
    				"display_name": "Test HAPI Project",
    				"site_infos": [{
    					"edge_cluster_paths": [
    						"/infra/sites/default/enforcement-points/default/edge-clusters/ec1"
    					],
    					"site_path": "/infra/sites/default"
    				}],
    				"tier_0s": [
    					"/infra/tier-0s/vmware"
    				]
    			}
    		}]
    	}]
    }
    ```

    Role based access control is
    applied to the response payload of this Patch API.

    For a detailed information
    about the org-root schema, see the NSX API Guide.

Project Admin
:   Project Admin can run the
    following Patch API call and use ChildResourceReference
    to specify the children for any node:

    ```
    PATCH https://<nsx-mgr>/policy/api/v1/org-root
    ```

    Alternatively, they can run
    the following Patch API call:

    ```
    PATCH https://<nsx-mgr>/policy/api/v1/orgs/default/projects/<project-id>/infra
    ```

    For a detailed information
    about these APIs, see the NSX API Guide.

Other Project Users
:   They can run the following
    Patch API
    call:

    ```
    PATCH https://<nsx-mgr>/policy/api/v1/orgs/default/projects/<project-id>/infra
    ```

    However, these users can run
    the Patch API against this URI only for objects that they are allowed to
    modify.

## Get API

The APIs calls in this section are
organized in terms of user roles.

Enterprise Admin
:   Only an Enterprise Admin can
    run the Get API call to read the org-root
    properties.

    ```
    GET https://<nsx-mgr>/policy/api/v1/org-root
    ```

    An Enterprise Admin can also
    run the following GET API calls:

    ```
    GET https://<nsx-mgr>/policy/api/v1/org-root?base_path=/orgs/default
    ```

    ```
    GET https://<nsx-mgr>/policy/api/v1/orgs/default/projects/<project-id>/infra?filter=Type-
    ```

    For more information about
    these APIs, see the NSX API Guide.

Project Admin
:   Project Admin can run the
    following Get API call:

    ```
    GET https://<nsx-mgr>/policy/api/v1/orgs/default/projects/<project-id>/infra?filter=Type-
    ```

Other Project Users
:   Hierarchical Get API call is
    not allowed.