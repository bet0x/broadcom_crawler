---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/vcf-operations-for-networks-deployment-models/high-availability-vcf-operations-for-logs-model(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > High Availability VCF Operations for Networks Model
---

# High Availability VCF Operations for Networks Model

The High Availability VCF Operations for Networks model consists of a three-node deployment. This model provides increased performance and scalability. Availability is provided by the native vSphere HA functionality within the vSphere cluster.

**High Availability VCF Operations for Network Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6a5fff11-567f-43a1-94d1-fe195f82c6d1.original.svg)

## High Availability VCF Operations for Networks Model Attributes

A High Availability VCF Operations for Networks Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Availability | Relies on vSphere HA to restart the nodes in the event of an ESX host failure. |
| Scalability | Supports scale-up and scale-out. |
| Recoverability | Restore through a backup. |

## High Availability VCF Operations for Networks Model Options

A High Availability VCF Operations for Networks Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Appliance Size | - Large - Extra Large |

## High Availability VCF Operations for Networks Model Design Requirements

High Availability VCF Operations for Networks Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-REQD-HA-001 | Deploy threeVCF Operations for networksplatform nodes in a cluster. | - Highly Performant. - Highly scalable, can scale up to 15 Extra Large nodes. | - Cluster does not provide high availability. It is for performance. - Requires higher CPU and memory reservations to support additional nodes. |
| VCF-NET-REQD-HA-002 | Deploy a single VCF Operations for networks collector node in the default management vSphere cluster. | A minimum of one VCF Operations for networks collector node is required to provide the VCF Operations for networks platform node with network monitoring data. | A 100% reservation for CPU and RAM for the deployed VCF Operations for networks collector node will be applied. |

## High Availability VCF Operations for Networks Model Design Recommendations

High Availability VCF Operations for Networks Model Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-NET-RCMD-HA-001 | Deploy appropriately sized VCF Operations for networksplatform nodes for your needs. | Ensures resource availability and usage efficiency. | None. |
| VCF-NET-RCMD-HA-002 | Protect all VCF Operations for networks nodes by using vSphere High Availability. | Supports the availability objective for VCF Operations for networks without requiring manual intervention during an ESX host failure event. | You must ensure sufficient spare capacity for vSphere High Availability failover operations. |
| VCF-NET-RCMD-HA-003 | In an environment with multiple VCF Instances, deploy the VCF Operations for networkscollector node(s) in the default management vSphere cluster in each VCF Instance by using VCF Operations fleet management. | - Ensures a consistent deployment in each VCF Instances regarding network data collection. - It is assumed that each VCF Instances introduces a sufficiently high number of virtual machines, so that the deployment of dedicated VCF Operations for networks collector nodes is justified. | Each VCF Operations for networks collector node must be registered with a VCF Operations for networks platform node. |
| VCF-NET-RCMD-HA-004 | For each vCenter data source, enable NetFlow on each vSphere Distributed Switch within the workload domain. | Provides the collection of network flows via the IPFIX protocol. | For the VCF domains, VCF Operations for networks will automatically update the NetFlow settings for each cluster's vSphere Distributed Switch. |
| VCF-NET-RCMD-HA-005 | For each NSX data source, enable IPFIX for the distributed firewall. | Provides the collection of network flows via the IPFIX protocol. | The distributed firewall service must be enabled on the NSX Local Manager for the VCF workload domain. |
| VCF-NET-RCMD-HA-006 | For each NSX Manager data source, enable latency metric collection. | Provides the collection of latency metrics from NSX Transport Nodes. | Any firewall rule sets from all ESX hosts to the VCF Operations for networks collector must allow traffic on TCP 1991. |
| VCF-NET-RCMD-HA-007 | Use the default retention period of one month for the VCF Operations for networks platform node. | Keeping the default value for retention minimizes required storage resources administrative efforts. | None. |
| VCF-NET-RCMD-HA-008 | Use a CA-Signed certificate containing the fully qualified domain names (FQDNs) of each VCF Operations for networks platform and collector node in the SAN attributes, when deploying VCF Operations for networks. | Configuring a CA-Signed certificate ensures that the communication to the externally facing Web UI and API VCF Operations for networks for is encrypted. | - Using CA-signed certificates from a certificate authority might increase the deployment preparation time as certificate requests are generated and delivered. - Each time a node is added the certificate must be replaced to include the fully qualified domain name of the additional node. |
| VCF-NET-RCMD-HA-009 | Use a SHA-2 or higher algorithm when signing certificates. | The SHA-1 algorithm is considered less secure and has been deprecated. | Not all certificate authorities support SHA-2. |