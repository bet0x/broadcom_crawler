---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/cluster-network-deployment-models.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Distributed Switch Models
---

# Distributed Switch Models

VMware Cloud Foundation supports multiple Distributed Switch Models that provide different levels of network availability, performance, resilience, and scale.

## Distributed Switch Models

VMware Cloud Foundation uses vSphere Distributed Switches to provide many network services, infrastructure networks, virtual networking, etc. A vSphere Distributed Switch acts as a single switch across all associated ESX hosts in a vSphere cluster to provide centralized provisioning, administration, and monitoring of networks.

vSphere Distributed Switches provide several services to ESX hosts and virtual machines. You can enable two types of network services in ESX:

- Connecting virtual machines to the physical network and to each other.
- Connecting VMkernel services (such as management, vMotion, vSAN and NSX host TEP) to the physical network.

When you design vSphere cluster networking, consider the configuration of the vSphere Distributed Switches, distributed port groups, and VMkernel adapters in the VMware Cloud Foundation platform. VMware Cloud Foundation provides a flexible approach to vSphere Distributed Switch deployment options, the Distributed Switch Models will be chosen based on the design qualities, availability, manageability, performance, recoverability and security. The following table shows some of the most common Distributed Switch Models, each with its benefits and implications listed.

Distributed Switch Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Single Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) | Option for minimal deployment. | - Easier to manage with least number of vSphere Distributed Switches. - Can be deployed with least number of ESX host physical NICs (one ESX host physical NIC using API). - Lowest physical switch port density required. | Does not provide network traffic separation to another physical network fabric. |
| [Storage Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-separation-network-model.html) | Option for larger scale deployments where bandwidth and quality of service is a concern, especially storage traffic bandwidth requirement. | - Separates Storage traffic onto dedicated physical ESX host NICs and provides the option to isolate the storage traffic to a different network fabric. - In secure environments, you can provide physical air-gapped separation of network traffic. - Can provide maximum bandwidth and performance for storage traffic with no contention from other traffic. | - Additional vSphere Distributed Switches required increasing management overhead. - Can be a more complex network configuration. - Higher number of ESX host physical NICs required than using single vSphere Distributed Switch with two physical NICs. - Higher physical switch port density required. |
| [Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) | Option for larger scale deployments where bandwidth and quality of service is a concern, especially for workload traffic. | - Separates virtual networking traffic onto different physical ESX host NICs and provides the option to isolate the workload traffic to a different network fabric. - In secure environments, you can provide physical air-gapped separation of network traffic. - Can provide maximum bandwidth and performance for workload traffic with no contention from other traffic on the ESX hosts physical NICs. | - Additional vSphere Distributed Switches required increasing management overhead. - Can be a more complex network configuration. - Higher number of ESX host physical NICs required than using single vSphere Distributed Switch with two physical NICs - Higher physical switch port density required. |
| [Storage and Workload Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) | Option for larger scale deployments where isolation to different fabrics is a requirement, also offers quality of service benefits. | - Separates Virtual Networking and storage traffic onto different physical ESX host NICs and provides the option to isolate the storage and virtual networking traffic to different network fabrics. - In secure environments, you can provide physical air-gapped separation of network traffic - Can provide maximum bandwidth and performance for virtual networking traffic and Storage traffic with no contention from other traffic on the ESX hosts physcial NICs. | - Additional vSphere Distributed Switches required increasing management overhead. - Most complex network configuration. - Highest number of ESX host physical NICs required, minimum of six (6) with redundancy. - Highest switch port density required. |
| [Dedicated vSphere Cluster for NSX Edge Node Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/dedicated-vsphere-cluster-for-edges-network-model.html) | Option for the deployment of NSX edge nodes to vSphere clusters dedicated to only host edges, this design can achieve maximum bandwidth and performance for the edge VMs. | - Provides maximum bandwidth for NSX edge node traffic. - NSX edge utilizes all physical NICs. - Built on workload traffic separation model for simpler deployment. | - Network I/O control on both vSphere Distributed Switches must be disabled manually post deployment for best performance. - Additional vSphere Distributed Switches required increasing management overhead. |
| [vSAN Storage Cluster Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-cluster-client-traffic-separation.html) | Option for Storage clusters where vSAN traffic for the cluster is separated from client vSAN traffic flowing to the compute clusters. | - Provides maximum bandwidth for vSAN storage cluster server traffic. - Isolates client and server traffic onto two different network fabrics if required. | - Two (2) vSphere Distributed Switches required increasing management overhead   - Higher physical switch port density required. |

Distributed Switch Models in VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/50eadc71-6d37-4996-aded-66d5ef711d70.original.svg)