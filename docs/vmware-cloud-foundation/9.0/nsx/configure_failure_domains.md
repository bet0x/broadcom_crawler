---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/stateful-services-on-tier-0-and-tier-1-gateways/configure-failure-domains.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Failure Domains
---

# Configure Failure Domains

A Failure domain is a logical grouping of NSX Edge nodes within an NSX Edge Cluster. Failure domains compliment auto placement algorithm and guarantee service availability in case of a failure affecting multiple NSX Edge nodes.

In a failure domain, Active and Standby instances of a Tier-1 SR or members of a sub-cluster always run in different failure domains. Without a failure domain, a Tier-1 SR could be auto placed on NSX Edge nodes that are in the same rack. So, if rack1 fails, both active and standby instance of this Tier-1 SR fail as well.

Without Failure Domains configured:

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/edecb4fc-572f-4792-9ae9-b86a273f2734.original.png)

- In an Edge cluster comprising of four Edge nodes (EdgeNode1, EdgeNode2, EdgeNode3, EdgeNode4), any new Tier-1 Gateways in A/S mode are automatically placed in any two of those four Edge Nodes.

- However, high-availability cannot be achieved if Tier-1 A/S is deployed in Rack1 and Tier-2 A/S is deployed in Rack2. If Rack1 fails, Tier-1 A/S on EdgeNode1 and EdgeNode2 are lost as they are in the same failure domain.

With Failure Domains configured:

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1f592b8b-da5b-42b8-b8f8-d9b136c68e8c.original.png)

- EdgeNode1 and EdgeNode2 are configured to be a part of failure domain-1, while EdgeNode3 and EdgeNode4 are in failure domain-2. When a new Tier-1 SR is created and if the active instance of that Tier-1 is hosted on EdgeNode1, then the standby Tier-1 SR will be instantiated in failure domain 2 (EdgeNode3 or EdgeNode4).

- After configuring Failure Domains on an Edge cluster, any new Tier-1 Active/Standby SRs are correctly placed in different Failure Domains.

1. Using the API, create failure domains for the each Edge node that you will add to the stateful A-A cluster, for example, in FailureDomain1 include FD1-EdgeNode1 and FD1-EdgeNode2 and in FailureDomain2 include FD2-EdgeNode3 and FD2-EdgeNode4. Set the parameter preferred\_active\_edge\_services to true for Edge nodes in both failure domains. The preferred\_active\_edge\_services is useful only when a Tier-1 gateway is created in preemptive failover mode.

   ```
   POST /api/v1/failure-domains
   {
   "display_name": "FD1-EdgeNode1",
   "preferred_active_edge_services": "true"
   "display_name": "FD1-EdgeNode2",
   "preferred_active_edge_services": "true"
   }

   POST /api/v1/failure-domains
   {
   "display_name": "FD2-EdgeNode3",
   "preferred_active_edge_services": "true"
   "display_name": "FD2-EdgeNode4",
   "preferred_active_edge_services": "true"
   }
   ```
2. Using the API, associate each Edge node with the failure domain for the site. First call the GET /api/v1/transport-nodes/<transport-node-id> API to get the data about the Edge node. Use the result of the GET API as the input for the PUT /api/v1/transport-nodes/<transport-node-id> API, with the additional property, failure\_domain\_id, set appropriately. For example,

   ```
   GET /api/v1/transport-nodes/<transport-node-id>
   Response:
   {
       "resource_type": "TransportNode",
       "description": "Updated NSX configured Test Transport Node",
       "id": "77816de2-39c3-436c-b891-54d31f580961",
       ...
   }
   ```

   ```
   PUT /api/v1/transport-nodes/<transport-node-id>
   {
       "resource_type": "TransportNode",
       "description": "Updated NSX configured Test Transport Node",
       "id": "77816de2-39c3-436c-b891-54d31f580961",
       ...
       "failure_domain_id": "<UUID>",
   }
   ```
3. Using the API, configure the Edge cluster to allocate nodes based on failure domain. First call the GET /api/v1/edge-clusters/<edge-cluster-id> API to get the data about the Edge cluster. Use the result of the GET API as the input for the PUT /api/v1/edge-clusters/<edge-cluster-id> API, with the additional property, allocation\_rules set appropriately. For example,

   ```
   GET /api/v1/edge-clusters/<edge-cluster-id>
   Response:
   {
       "_revision": 0,
       "id": "bf8d4daf-93f6-4c23-af38-63f6d372e14e",
       "resource_type": "EdgeCluster",
       ...
   }
   ```

   ```
   PUT /api/v1/edge-clusters/<edge-cluster-id>
   {
       "_revision": 0,
       "id": "bf8d4daf-93f6-4c23-af38-63f6d372e14e",
       "resource_type": "EdgeCluster",
       ...
       "allocation_rules": [
           {
               "action": 
                   {
                    "enabled": true,
                    "action_type": "AllocationBasedOnFailureDomain"
                   }
           }
       ],
   }
   ```

The NSX Edge nodes are referenced to different failure domains. You can now use them to create a cluster and configure Tier-0 gateway in A-A Stateful HA mode.