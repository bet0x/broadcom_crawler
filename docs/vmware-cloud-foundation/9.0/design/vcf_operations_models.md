---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Operations Models
---

# VCF Operations Models

VMware Cloud Foundation utilizes VCF Operations as the central console for operating your VCF fleet, providing dashboards for monitoring, log analysis, reporting and licensing as well as performing fleet management capabilities such as fleet extension, life cycle, certificate and password management.

## VCF Operations Models

You use the VMware Cloud Foundation Installer to deploy your new VCF fleet, this includes vCenter, NSX, VCF Operations, VCF Automation, and SDDC Manager. At deployment time you must select one of the VCF Operations Models based on your organizational objectives.

By default, vCenter and SDDC Manager are deployed as single node. However, you have the flexibility to choose whether to deploy NSX Manager, VCF Operations, and VCF Automation as single node deployments, or as three node deployments to provide high availability capabilities.

VCF Operations Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Simple VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/simple.html) | - Single node. - Additional appliances deployed:    - VCF Operations fleet management   - VCF Operations collector   - SDDC Manager - Supports scale-up and scale-out. | - Smallest footprint. - Can be scaled-out to be highly available. | - Slower recovery from failure. - Relies on vSphere HA to restart the nodes in the event of an ESX host failure. - Service interruption may occur for:    - monitoring and alerting   - fleet management |
| [High Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/ha.html) | - Three node cluster:    - Primary node   - Replica node   - Data node - Provides greater service availability. - Additional appliances deployed:    - VCF Operations fleet management   - VCF Operations collector   - SDDC Manager - Supports an optional external load balancer. - Supports scale-up for all nodes and scale-out with additional data nodes. | - Highly available cluster with data redundancy. - Rapid recovery of a single node failure in the cluster. | - VCF Operations collector expanded to a collector group manually. - When using an external load balancer:    - Additional IP address and FQDN are required.   - FQDNs for all cluster nodes and the FQDN for the load balancer must be included in the certificate's SAN. |
| [Continuous Availability VCF Operations Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/continuous-availability-vcf-operations-model.html) | - A cluster with a pair of nodes, across two availability zones:    - Primary node <-> Primary replica node   - Data node <-> Data Node - Provides best service availability. - Additional appliance, deployed in the primary availability zone:    - VCF Operations fleet management - Additional appliances, deployed in both availability zones:    - VCF Operations collector   - SDDC Manager - Supports an optional external load balancer. - Supports scale-up for all nodes and scale-out with additional data nodes. | - Highly available cluster with data redundancy across different availability zones. - No service interruption in case of a single availability zone failure. | - Manual operations after the initial installation - Requires a separate VCF Instance in different availability zone. - Maximum network latency between availability zones 10ms. |

VCF Operations Models in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2dfa92b8-e462-4e4d-92a1-67ddbb5934f4.original.svg)

## VCF Operations for Logs Models

VCF Operations for logs can be added to your VCF fleet to extend the capabilities of VCF Operations by providing a centralized log management framework to collect, analyze, and visualize logs from across your VMware Cloud Foundation platform.

You deploy VCF Operations for logs as a Day-2 operation using VCF Operations, see [Deploy VCF Operations for VMware Cloud Foundation 9 Core Components Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/preparing-to-upgrade-to-vmware-cloud-foundation.html). At deployment time you must select one of the VCF Operations for Logs Models based on your organizational objectives.

For the detailed design relating to VCF Operations for Logs Models in the table below see [VCF Operations for Logs Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models.html).

VCF Operations for Logs Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Simple VCF Operations for Logs Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models/simple-vcf-operations-for-logs-model.html) | - Single node. - Additional options on deployment:    - Cluster VIP   - FIPS Compliance Mode - Supports scale-up and scale-out. | - Smallest footprint. - Can be extended to be highly available. | - Slower recovery from failure. - Relies on vSphere HA to restart the nodes in the event of an ESX host failure. - No application high availability. - Deployed through VCF Operations as a Day 2 operation. - VIP IP/FQDN is required during deployment. |
| [High Availability VCF Operations for Logs Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-logs-deployment-models/high-availability-vcf-operations-for-logs-model.html) | - Three node cluster:    - Primary node   - Worker node 1   - Worker node 2 - Application service availability through cluster VIP. - Additional options on deployment:    - Retention notification threshold   - Additional disk node - Supports scale-up and scale-out. | - Highly available cluster with integrated load balancer and data redundancy. - Rapid recovery of single node failure. | - Deployed through VCF Operations as a Day 2 operation. |

VCF Operations for Logs Models in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7b16f92e-5c69-42bb-9e3e-655115c265a3.original.svg)

## VCF Operations for Networks Models

VCF Operations for networks extends the capabilities of VCF Operations providing network visibility and analytics to minimize risk during application migration, optimize network performance, manage and scale your network across the VMware Cloud Foundation platform.

You deploy VCF Operations for networks as a Day-2 operation using VCF Operations, see [Deploying VCF Operations for networks](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-networks.html). At deployment time you must select one of the VCF Operations for Networks Models based on your organizational objectives.

For the detailed design relating to VCF Operations for Networks Models in the table below see [VCF Operations for Networks Detailed Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models.html).

VCF Operations for Networks Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Simple VCF Operations for Networks Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models/simple-vcf-operations-for-networks-model.html) | - Single nodes for    - VCF Operations for networks platform node   - VCF Operations for networks collector node - Supports scale-up and scale-out. | - Smallest footprint - Can be scaled-out to a platform cluster. - Supports 10,000 virtual machines or objects. | - Slower recovery from failure. - Relies on vSphere HA to restart the nodes in the event of an ESX host failure. - No application high availability. - Requires a CPU and RAM reservation of 100% of the CPU and RAM assigned. - Requires the single node be deployed as an Extra Large size. - Deployed through VCF Operations as a Day 2 operation. |
| [High Availability VCF Operations for Networks Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models/high-availability-vcf-operations-for-logs-model(1).html) | - Three node cluster. - Single VCF Operations for networkscollector node. - Provides greater application scale and performance. - Supports scale-up and scale-out. | - Highly performant - Highly scalable | - Cluster does not provide high availability. It is for performance. - Requires higher CPU and memory reservations to support additional nodes. - Deployed through VCF Operations as a Day 2 operation. |

VCF Operations for Networks Models in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4f520596-3ae5-4cba-9310-d7727e95a574.original.svg)