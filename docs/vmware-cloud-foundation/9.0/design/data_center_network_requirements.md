---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking/datacenter-network-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Data Center Network Requirements
---

# Data Center Network Requirements

This section describes the options, requirements and recommendations for the data center network requirements.

Due to the large number hardware specifics between data centers, no one-size-fits-all approach to data center network design exists. The specifics of bandwidth requirements depend heavily on the dynamism of the workloads. Environments with high VM churn, high VM storage I/O, or high inter-VM communication need more network resources than computationally intensive workloads. Moreover, very latency-sensitive applications will require special consideration even at low bandwidth.

The terms "performant" and "adequate" describe a network sized and configured to meet the requirements for VCF components, considering the expected workloads and traffic flows in the production environment. Network paths must be reliable and stable, as even low levels of packet loss and retransmits will result in a substantial decrease in performance and throughput.

## Sites, Availability Zones, and Rack Fault Tolerance

Underneath the virtual infrastructure is the physical. Servers, storage, and network switches are all physical objects which reside in physical locations. VMware Cloud Foundation utilizes compute, storage, and network virtualization to abstract consumption from the physical underpinnings.

A key design aspect of a highly available deployment is to ensure components are distributed into different physical locations to avoid faults from a common source. It is up to each customer to evaluate their own risk tolerance and fault isolation requirements.

The following are typical levels of physical fault tolerance found within an enterprise.

**Sites:** A separate site is typically a considerable geographic distance apart. In some instances, connectivity between this site may have higher latency (over 10ms RTT) or lower bandwidth, so synchronous data replication technologies are impractical.

**Availability Zones:** These are separate sites that are geographically close with low latency (under 10ms RTT) and high-bandwidth connectivity. These may be physically separate buildings or parts of an existing data center that meet the customer's goals for physical fault tolerance. There may be a common or separate network fabric between the AZs - however the network must be able to provide a stretch L2 network between these sites to support mobility of management appliances. AZs should have independent network paths such that the failure of one AZ does not impact another.

With some fabrics, the network vendor does not support BGP peering over the Layer 2 networks stretched between sites.

**Witness Site:** Clustered technologies require a 3rd tie-breaker site to enable automated fast recovery. These witness sites may be a separate AZ or separate Site. Network paths to other sites should be independent of each other. Inter-site connections may have higher latency and lower bandwidth connections.

**Racks:** A rack is a physical location within a site or availability zone that contains physical servers or storage components. Each rack typically has dedicated network switches to which all rack components connect. Typically, connectivity within a rack provides the best network performance to other components within the rack with minimal or no over-subscription. For this design, all servers connected to the same physical network switch are considered part of the same 'rack' regardless of where they are physically located within the data center.