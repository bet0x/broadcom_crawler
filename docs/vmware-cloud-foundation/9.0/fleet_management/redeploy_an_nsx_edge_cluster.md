---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-edge-cluster/redeploy-nsx-edge-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Redeploy an NSX Edge Cluster
---

# Redeploy an NSX Edge Cluster

To recover an NSX edge cluster, use the NSX API to redeploy the edge nodes.

## Procedure

1. Verify that the NSX Edge node is disconnected from NSX Manager by running the following API call in Postman.

   ```
   GET /<NSX-Manager-IPaddress>/api/v1/transport-nodes/<edgenode_id>/state

    "node_deployment_state":          {"state": MPA_Disconnected"}
   ```
2. Retrieve the edge node configuration by running the following API call and copy the output payload of this API.

   ```
   GET /<NSX-Manager-IPaddress>/api/v1/transport-nodes/<edgenode_id>
   ```

   ```
   "resource_type": "EdgeNode",
   	        "id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
   	        "display_name": "Edge_TN2",
   	        "description": "EN",
   	        "external_id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
   	        "ip_addresses": [
   	            "10.170.94.240"
   	        ],
   	        "_create_user": "admin",
   	        "_create_time": 1600106319056,
   	        "_last_modified_user": "admin",
   	        "_last_modified_time": 1600106907312,
   	        "_system_owned": false,
   	        "_protection": "NOT_PROTECTED",
   	        "_revision": 2
   	    },
   	    "is_overridden": false,
   	    "failure_domain_id": "4fc1e3b0-1cd4-4339-86c8-f76baddbaafb",
   	    "resource_type": "TransportNode",
   	    "id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
   	    "display_name": "Edge_TN2",
   	    "_create_user": "admin",
   	    "_create_time": 1600106319399,
   	    "_last_modified_user": "admin",
   	    "_last_modified_time": 1600106907401,
   	    "_system_owned": false,
   	    "_protection": "NOT_PROTECTED",
   	    "_revision": 1
   	}
   ```
3. Redeploy the edge node using the following API call, passing the JSON data retrieved in Step 2 as the body.

   You do not need to pass any passwords in the JSON file.

   ```
   POST /<NSX-Manager-IPaddress>/api/v1/transport-nodes/<edgenode_id>?action=redeploy
   ```
4. Repeat steps 1-3 for the remaining edge cluster nodes.
5. In NSX Manager, monitor the Configuration Status of the new NSX Edge nodes, until they show Success.

   If you encounter an error Edge redeploy is blocked as an active alarm is found for Edge VM present in NSX Inventory but missing in vCenter, navigate to the Alarms section in the relevant NSX Manager UI, select all relevant alarms whose Event Type is Edge VM Present In NSX Inventory Not Present In vCenter and from the vertical ellipsis menu, select Resolve. Then, retry the redeploy operation.