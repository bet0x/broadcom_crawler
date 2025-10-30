---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Operations for Networks Detailed Design
---

# VCF Operations for Networks Detailed Design

A VCF fleet can include one of the supported VCF Operations for Networks Models. This section describes the options, requirements and recommendations for each VCF Operations for Networks Model.

- [Simple VCF Operations for Networks Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models/simple-vcf-operations-for-networks-model.html)
- [High Availability VCF Operations for Networks Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models/high-availability-vcf-operations-for-logs-model(1).html)

## VCF Operations for Networks - Logical Design

VCF Operations for networks can be deployed as a cluster or a single node. This cluster processes the collected data and presents it using a dashboard. VCF Operations for Networks also uses collector nodes to collect data from the data sources, such as vCenter server and NSX Manager which then sends the data to the platform cluster for processing.

The platform cluster capacity is based on the deployment size of each node and the number of nodes composing the cluster. For more information about how to decide the platform brick (node) size and number of platform bricks (nodes), see the VCF Operations for Networks documentation.

The collector capacity is based on the deployment size. The amount of data sources that you can add to a specific collector is based on the documented capacity of the collector size (accounting for the number of VMs and the number of flows).

## VCF Operations for Networks - Scaling

VCF Operations for networks scales in two dimensions: the platform and the collectors. The platform can only be clustered if using appliances of at least a large size. Medium deployments cannot be scaled into a cluster without first scaling up to large.

The scaling of a platform to a cluster model does not provide additional availability to the platform. Scaling must be used when maximums for a single node exceed.

The overall dimensioning for collector scaling is based on various factors including:

- Number of vCenter instances
- Number of VMs
- Number of flows to track

To determine when to scale the platform and collector nodes, see the VCF Operations for networks sizing below.. When collecting over 10,000 VMs and 4 million active flows, the platform must be upgraded from a single node to a clustered deployment. Similar scale-up and scale-out requirements exist for the Collectors.

| Design Recommendations IDs | Design Recommendation | Justifications | Implications |
| --- | --- | --- | --- |
| VCF-NECE-RCMD-01 | Single Platform Node  Size based upon sizing document and best practices. | - Smallest footprint. - Can be scaled-out to a platform cluster. - Supports 10,000 virtual machines or objects. | - Requires a CPU and RAM reservation of 100% of the CPU and RAM assigned. - No, high availability - Requires the single node be deployed as an Extra Large size |
| VCF-NECE-RCMD-02 | Platform Cluster   - Three node clusters. Consisting of 3 platform instances. Can scale up to 15 XL nodes. - Cluster node sizing starts at a Large Platform Node Size and go up to Extra Large. | - Highly Performant. - Highly scalable. | - Cluster does not provide high availability. It is for performance. - Requires higher CPU and memory reservations to support additional nodes. |
| VCF-NECE-RCMD-03 | Collector  Single VM used to monitor remote VCF deployments and to send data back to the primary cluster. | - Highly Performant. - Highly scalable. | - Limitation of total flows is based on the capacity of the platform. - Requires understanding the amount of VMs, Flows, and Edges will be sending data to the collector. |

## Understanding how to size VCF Operations for Networks

VCF Operations for Networks provides network visibility across virtual and physical devices. The key considerations are:

- Number of VMs monitored
- Flows Per Day
- Total Flows
- Flowing Planning
- Number of Edges

To understand how to properly size the environment see the Capacity for Non-Cluster and Clustered environments below.

- The reservation for the CPU speed and RAM for each node must be 100% of the value specified above.
- If the disk in any of the platform nodes exceeds 95% of the capacity, VCF Operations for Networks UI will not be accessible.

To match your setup to all the specifications, you might have to add the resources (RAM, Disk, CPU). See <https://kb.vmware.com/s/article/53550>and [Increase the Brick Size of Your Setup](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations-for-networks/6-14/vrealize-network-insight-installation-6-14/planning-to-scale-up-your-deployment/scaling-up.html#GUID-E3D77266-E72E-49AF-B4A6-1810DD10C00F-en)

## Non-Cluster Sizing

Single Node Sizing



| Brick Size | Cores required  for 2.1 GHz CPU | Cores required  for 2.3 GHz CPU | Cores required  for 2.6 GHz CPU | RAM | Disk |
| --- | --- | --- | --- | --- | --- |
| Medium | 10 | 9 | 8 | 32 GB | 1 TB |
| Large | 15 | 14 | 12 | 48 GB | 1 TB |
| Extra Large | 20 | 18 | 16 | 64 GB | 2 TB |

Flow and Network Rule Sizing



| Brick Size | Number of VMs  (K = Thousand) | Flows per Day  (M = Million) | Total Flows  (M = Million) | Flow Planning  (M = Million) | Number of Network Rules for Network Map and Intents  (K = Thousand) | Number of Edges for VeloCloud  (K = Thousand) | Number of VMs for Flow Based Application Discovery | Number of UI Entities in the Network Map Topology |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Medium | 4K | 1M | 4M | 2M | Not Applicable | 2K | Not Supported | Not Supported |
| Large | 6K | 2M | 8M | 4M | Not Applicable | 2K | Not Supported | Not Supported |
| Extra Large | 10K | 2M | 8M | 4M | 170K | 4K | 3K | 5K |

## Cluster Sizing

| Brick Size | Cluster Size | Number of VMs  (K = Thousand) | Flows per Day  (M = Million) | Total Flows  (M = Million) | Flow Planning  (M = Million) | Number of Network Rules for Network Map and Intents  (K = Thousand) | Number of Edges for VeloCloud  (K = Thousand) | Number of VMs for Flow Based Application Discovery | Number of UI Entities in the Network Map Topology |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Large | 3 | 10K | 2M | 8M | 4M | Not Applicable | 4K | Not Supported | 5K |
| Extra Large | 3 | 18K | 6M | 24M | 6M | 170K | 6K | 3K | 5K |
| Extra Large | 5 | 30K | 10M | 40M | 10M | 170K | 10K | 3K | 5K |
| Extra Large | 7 | 58K | 12M | 48M | 10M | 170K | 10K | 3K | 5K |
| Extra Large | 10 | 100K | 15M | 60M | 10M | 170K | 10K | 3K | 5K |
| Extra Large | 15 | 150K | 20M | 80M | 10M | 170K | 10K | 3K | 5K |

## Recommendation for the Collector Deployment

| Collector Size | Number of VMs  (K = Thousand) | Flows per Day  (M = Million) | Flow count in 4 days  (M = Million) | Number of Edges for VeloCloud  (K = Thousand) |
| --- | --- | --- | --- | --- |
| Medium | 4K | 2.5M | 3.25M | 4K |
| Large | 10K | 5M | 6.5M | 6K |
| Extra Large | 35K | 10M | 13M | 10K |
| 2X Large | 45K | 17M | 22M | 10K |