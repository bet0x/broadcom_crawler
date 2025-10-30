---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/design-library-workload-networking.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Workload Networking Detailed Designs
---

# Workload Networking Detailed Designs

This section outlines various workload network models for virtualized data center environments.

## Overview

The section covers several key topology models including:

- VPC with Full Services Model: Offering full centralized services with Active/Standby gateways. It's the only model supported by VMware Kubenetes Engine (VKS) and VCF Automation all Apps Orgs.
- VPC Scalable Model: Providing scalable North-South throughput with Active/Active gateways
- VPC Getting-Started Model: A simplified deployment without NSX Edge Nodes
- Scalable NSX Segment Network Virtualization: Supporting NSX federation and VM mobility across VCF Instances
- Large-Scale Composite Topologies Model: Designed for service providers managing multi-tenant environments. It can be based on VPC or NSX Segment consumtion models, or both.

Each workload networking model presents different tradeoffs between simplicity, performance, service availability, and scalability. The corresponding design library elements explain the architecture overview, key benefits, limitations, and specific deployment considerations for each model.