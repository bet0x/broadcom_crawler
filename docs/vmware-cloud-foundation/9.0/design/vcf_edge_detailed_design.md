---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1).html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Detailed Design
---

# VCF Edge Detailed Design

VMware Cloud Foundation Edge extends the centralized management capabilities of the platform to geographically dispersed edge locations.

This section describes different design options for deploying VCF Edge, covering various needs and complexities.

| Feature | 1-Node cluster in a VCF Instance | 2-Node with external storage (minimum) in a workload domain | 3-Node vSAN cluster (minimum) in a workload domain | 4-Node VCF Fleet with single domain and one or multiple clusters. |
| --- | --- | --- | --- | --- |
| **Prime Use Case** | Remote / Branch Offices, Edge locations | Remote / Branch Offices, Edge locations | Small to medium-sized deployments | Large-scale, distributed environments or locally managed edge environments |
| **Storage** | Local or external NFS or FC | External NFS or FC (No vSAN) | vSAN or External Storage | vSAN or External Storage |
| **Networking** | - NSX supported - vSphere Distributed Switch supported | - NSX supported - vSphere Distributed Switch supported | - NSX supported - vSphere Distributed Switch supported | - NSX supported - vSphere Distributed Switch supported |
| **Max Hosts per Cluster** | 64 | 64 | 64 | 64 |
| **Max Workload Domains** | Not supported | 24 | 24 | 24 |
| **Life cycle Management** | Central or local life cycle management with vCenter | Central or local life cycle management with VCF Operation | Central or local life cycle management with VCF Operation | Central or local life cycle management with VCF Operation |
| **Latency & Bandwidth Requirements** | 100ms latency, 10 Mbps bandwidth | 100ms latency, 10 Mbps bandwidth | 100ms latency, 10 Mbps bandwidth | 100ms latency, 10 Mbps bandwidth |
| **VKS Support** | Yes | Yes | Yes | Yes |
| **Key Advantage** | Lower cost for edge deployments | Lower cost for edge deployments | Simplified management for smaller environments | Highly scalable, resilient architecture, can fit any deployment models such as centrally managed, locally managed and Isolated Edge. |