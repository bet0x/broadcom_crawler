---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/other-options-with-vcf-edge/option-3.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Option 2: Thin Edge with vSphere Supervisor on Two-Node vSAN
---

# VCF Edge Option 2: Thin Edge with vSphere Supervisor on Two-Node vSAN

A resource-constrained edge deployment utilizing a small, two-node vSAN cluster to provide local storage for running both traditional VMs and modern containerized applications orchestrated by vSphere Kubernetes Service (VKS)

VCF Edge Option 2: Thin Edge with vSphere Supervisor on Two-Node vSAN

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bf623e44-4782-4aab-bd46-d9e0b849c77d.original.png)

|  |  |
| --- | --- |
| Design Requirement | Justification |
| Locally Managed or Centrally Managed | VCF Operation, vCenter, and a Witness VM are located in a Central Management Cluster. This cluster can be hosted locally at edge site or it can be hosted in a central or regional data center. |
| vSphere Supervisor | Supervisor is enabled in the vSphere environment at each edge site (within each 2-node cluster). This enables the deployment and management of Kubernetes workloads alongside traditional VMs. |
| vSAN for Local Storage | Each 2-node cluster utilizes vSAN for local shared storage. |
| Control Plane VM at each edge location | Provides the necessary control plane components for managing the Kubernetes environment and potentially other edge-specific services locally at each site.  Recommend to have 1 control plane VMs on 2 node vSAN cluster. With 1 CP VM on a two-node cluster, the Supervisor Cluster will be degraded but functioning if one of the nodes fails. While you've lost redundancy for the CP VM itself, the Kubernetes control plane remains operational on the surviving node, allowing existing workloads to continue running and management operations (though potentially with reduced performance) to still be possible. |
| Network Connectivity | Latency and Bandwidth: Minimum 100ms / 10Mbps required for connection between vCenter to the ESXi hosts. |
| Deployment and Licensing | VCF Operation is the mandatory requirement along with vCenter to support this design.  Please deploy VCF Operation and vCenter manually or Using VCF installer with VVF option and then entitle VCF Edge license with VCF Operation. |

**A key deviation from Pattern 6 is that this design does not incorporate a full VCF stack, but it does leverage vSAN.**