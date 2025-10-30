---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-multisite.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Multisite
---

# NSX Multisite

NSX supports multisite deployments where you can manage all the sites from one NSX Manager cluster.

Two types of multisite deployments are supported:

- Disaster recovery
- Active-active

The following diagram illustrates a disaster recovery deployment.

![Shows a multisite disaster recovery deployment with a primary site with a secondary site with SRM-replicated VMs](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/15bdbae6-df97-4f0d-b6c7-f921b0d86ca6.original.png)

In a disaster recovery deployment, NSX at the primary site handles networking for the enterprise. The secondary site stands by to take over if a catastrophic failure occurs at the primary site.

The following diagram illustrates an active-active deployment.

![Shows two active sites with L2 stretched across both primary and secondary sites communicating to primary and secondary T0 gateways](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8cbe4ca7-5219-4315-9f09-395f137af6fa.original.png)

You can deploy two sites for automatic or manual/scripted recovery of the management plane and the data plane.

## Automatic Recovery of the Management Plane

Requirements:

- A stretched vCenter cluster with HA across sites configured.
- A stretched management VLAN.

The NSX Manager cluster is deployed on the management VLAN and is physically in the primary site. If there is a primary site failure, vSphere HA will restart the NSX Managers in the secondary site. All the transport nodes will reconnect to the restarted NSX Managers automatically. This process takes about 10 minutes. During this time, the management plane is not available but the data plane is not impacted.

The following diagrams illustrate automatic recovery of the management plane.

Before the disaster:

![Shows the secondary site nodes reconnected to the NSX ManagerNSX Manager in the primary site after automatic recovery of the management plane](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/788d3406-28d1-43b5-a3a1-ea1c79b1dc25.original.png)

After disaster recovery:

![Shows secondary site with NSX ManagerNSX Manager moved from the primary site with transport node connections reconnected after disaster recovery.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0029d38b-b28b-4c8f-8fdd-a474726740fc.original.png)

## Automatic Recovery of the Data Plane

You can configure failure domains for Edge nodes to achieve automatic recovery of the data plane. You can group Edge nodes within an Edge cluster in different failure domains. NSX Manager will automatically place any new active tier-1 gateway in the preferred failure domain, and the standby tier-1 gateway in the other domain. Note that a T1 deployed prior to the failure domain creations will keep their original Edge Node placement and might not be running where you want. If you want to fix their placement, edit the T1 and manually select the Edge Nodes for T1-Active and T1-Standby.

Requirements:

- The maximum latency between Edge nodes is 10 ms.
- If asymmetric north-south routing is not achievable, for example a physical firewall is used northbound to the NSX Edge node, then the HA mode for the tier-0 gateway must be active-standby, and the failover mode must be preemptive.
- If asymmetric north-south routing is possible, for example the two locations are two buildings without any physical firewall between them, then the HA mode for the tier-0 gateway can be active-active.

The failover mode of the tier-1 gateway can be preemptive or non-preemptive, but preemptive is recommended to guarantee that the tier-0 and tier-1 gateways are in the same location.

Configuration steps:

- Using the API, create failure domains for the two sites, for example, FD1A-Preferred\_Site1 and FD2A-Preferred\_Site1.

  If you want all your tier-1 with the T1-Active in the Edge nodes and the T1-Standby in other Edge nodes to be part of the same failure domain (FD1A-Preferred\_Site1 and FD2A-Preferred\_Site1); then you must first create your tier-1 with the option preemptive and then create your failure domain primary (FD1A-Preferred\_Site1) set to preferred\_active\_edge\_services = true. For example,

  ```
  POST /api/v1/failure-domains
  {
  "display_name": "FD1A-Preferred_Site1",
  "preferred_active_edge_services": "true"
  }

  POST /api/v1/failure-domains
  {
  "display_name": "FD2A-Preferred_Site1",
  "preferred_active_edge_services": "false"
  }
  ```
- Using the API, configure an Edge cluster spanning the two sites. For example, the cluster has Edge nodes EdgeNode1A and EdgeNode1B in the primary site, and Edge nodes EdgeNode2A and EdgeNode2B in the secondary site. The active tier-0 and tier-1 gateways will run on EdgeNode1A and EdgeNode1B. The standby tier-0 and tier-1 gateways will run on EdgeNode2A and EdgeNode2B.
- Using the API, associate each Edge node with the failure domain for the site. First call the GET /api/v1/transport-nodes/<transport-node-id> API to get the data about the Edge node. Use the result of the GET API as the input for the PUT /api/v1/transport-nodes/<transport-node-id> API, with the additional property, failure\_domain\_id, set appropriately. For example,

  ```
  GET /api/v1/transport-nodes/<transport-node-id>
  Response:
  {
      "resource_type": "TransportNode",  
      "_revision": 15"
      "description": "Updated NSX configured Test Transport Node",
      "id": "77816de2-39c3-436c-b891-54d31f580961",
      ...
  }

  PUT /api/v1/transport-nodes/<transport-node-id>
  {
      "resource_type": "TransportNode",
      "_revision": 15"
      "description": "Updated NSX configured Test Transport Node",
      "id": "77816de2-39c3-436c-b891-54d31f580961",
      ...
      "failure_domain_id": "<UUID>",
  }
  ```
- Using the API, configure the Edge cluster to allocate nodes based on failure domain. First call the GET /api/v1/edge-clusters/<edge-cluster-id> API to get the data about the Edge cluster. Use the result of the GET API as the input for the PUT /api/v1/edge-clusters/<edge-cluster-id> API, with the additional property, allocation\_rules, set appropriately. For example,

  ```
  GET /api/v1/edge-clusters/<edge-cluster-id>
  Response:
  {
      "_revision": 0,
      "id": "bf8d4daf-93f6-4c23-af38-63f6d372e14e",
      "resource_type": "EdgeCluster",
      ...
  }

  PUT /api/v1/edge-clusters/<edge-cluster-id>
  {
      "_revision": 0,
      "id": "bf8d4daf-93f6-4c23-af38-63f6d372e14e",
      "resource_type": "EdgeCluster",
      ...
      "allocation_rules": [
          {
              "action": {
                        "enabled": true,
                        "action_type": "AllocationBasedOnFailureDomain"
                        }
          }
      ],
  }
  ```
- Create tier-0 and tier-1 gateways using the API or NSX Manager UI.

In case of a full primary site failure, the tier-0 standby and tier-1 standby in the secondary site automatically take over and become the new active gateways.

The following diagrams illustrates automatic recovery of the data plane.

Before the disaster:

![Automatic recovery of the data plane before disaster recovery](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5baefc94-9a62-4000-8575-86c7b11621ad.original.png)

After disaster recovery:

![Automatic recovery of the data plane after disaster recovery](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/55e5c84c-cc78-40e1-863f-5bf8f9daf160.original.png)

In case of a failure of one of the Edge nodes in the primary site and not full site failure, it is important to note that the same principle applies. For example, in the diagram, "Before the disaster", assume that Edge node 1B hosts tier-1-blue active and that Edge node 2B hosts the tier-1-blue standby. If Edge node 1B fails, the standby tier-1-blue on Edge node 2B takes over and become the new tier-1-blue active gateway.

## Manual/Scripted Recovery of the Management Plane

Requirements:

- DNS for NSX Manager with a short TTL (for example, 5 minutes).
- Continuous NSX Manager backup.

Neither vSphere HA, nor a stretched management VLAN, is required. NSX Managers must be associated with a DNS name with a short TTL. All transport nodes (Edge nodes and hypervisors) must connect to the NSX Manager using their DNS name. To save time, you can optionally pre-install an NSX Manager cluster in the secondary site.

The recovery steps are:

1. Change the DNS record so that the NSX Manager cluster has different IP addresses.
2. Restore the NSX Manager cluster from a backup.
3. Connect the transport nodes to the new NSX Manager cluster.

The following diagrams illustrate manual/scripted recovery of the management plane.

Before the disaster:

![Shows communication between NSX Manager sites while continuous backups are stored on the secondary site before management plane recovery](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d8f3826c-71ac-44d2-8661-08fa3e7e3489.original.png)

After the disaster:

![Shows an out of service primary site with the secondary site transport nodes communicating to its recovered NSX Manager](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/09a6d882-59de-4791-9bac-6bdc51e709ed.original.png)

## Manual/Scripted Recovery of the Data Plane

Requirement: The maximum latency between Edge nodes is 150 ms.

The tier-0 gateways in each location can be active-standby or active-active. Edge node VMs can be installed in different vCenters. No vSphere HA is required.

The recovery steps are:

- For all tier-1 in primary site (blue), update their Edge Cluster configuration to be the Edge Cluster Site secondary.
- For all tier-1 in primary site (blue), reconnect them to T0 secondary (green).

The following diagrams illustrate manual/scripted recovery of the data plane with both the logical and physical network views.

Before the disaster (logical and physical views):

![Shows a logical view of primary and secondary sites before DR manual data plane recovery.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b598e94a-c8ff-429a-84c6-54bb138a377a.original.png)

![Shows a physical view of primary and secondary sites before DR manual data plane recovery. ](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/776273c7-ee34-4dff-8154-d5b8311551b9.original.png)

After the disaster (logical and physical views):

![Shows the logical view with an inactive primary site after DR manual data plane recovery.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/463a4479-87ea-49df-80e0-e112ada30262.original.png)

![Shows the physical view an inactive primary site after DR manual data plane recovery.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/514ecc22-2cc5-44e9-96de-921cf86a793c.original.png)

## Requirements for Multisite Deployments

Inter-site Communication

- The bandwidth must be at least 1 Gbps and the latency (RTT) must be less than 150 ms.
- MTU must be at least 1700. 9000 is recommended.

NSX Manager

- With automatic recovery of management plane with VLAN management stretched between sites. vSphere HA across sites for NSX Manager VMs.
- With manual/scripted recovery of the management plane with VLAN management stretched between sites. VMware SRM for NSX Manager VMs.
- With manual/scripted recovery of the management plane without VLAN management stretched between sites.
  - Continuous NSX Manager backup.
  - NSX Manager must be set up to use FQDN.

Data Plane

- The same internet provider must be used if public IP addresses are exposed through services such as NAT or load balancer.
- With automatic recovery of management plane
  - Maximum latency between locations is 10 ms.
  - The HA mode for the tier-0 gateway must be active-standby and the failover mode must be preemptive to guarantee no asymmetric routing.
  - The HA mode for the tier-0 gateway can be active-active if asymmetric routing is acceptable (such as different buildings in a metropolitan region).
- With manual/scripted recovery of management plane
  - Maximum latency between locations is 150 ms.

Cloud Management System (CMS)

- The CMS must support an NSX plug-in. In this release, VMware Integrated OpenStack (VIO) and vRealize Automation (vRA) satisfy this requirement.

## Limitations

- No local-egress capabilities. All north-south traffic must occur within one site.
- The compute disaster recovery software must support NSX, for example, VMware SRM 8.1.2 or later.
- When restoring the NSX Manager in a multi-site environment do the following on the secondary/primary site:
  - After the restore process pauses at the AddNodeToCluster step, you must first remove the existing VIP and set the new virtual IP from the SystemAppliances UI page before you add additional manager nodes.
  - Add new nodes to a restored one-node cluster after the VIP is updated.