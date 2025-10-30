---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/key-features-of-the-vsphere-supervisor-adapter.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Key Features of the vSphere Supervisor Management Pack
---

# Key Features of the vSphere Supervisor Management Pack

The vSphere Supervisor management pack provides enhanced observability and lifecycle management for VKS.

Push-Based Metrics Collection
:   The vSphere Supervisor adapter introduces a push-based model that leverages Telegraf, enabling improved efficiency in metric collection. The metrics are pushed into a Cloud Proxy. This ensures faster and more reliable metric collection.

Seamless Integration
:   Enabling the vSphere Supervisor management pack is simple, and allows for automatic detection and configuration of Kubernetes clusters within vCenter instances.

Support for vSphere Supervisor and VKS Clusters
:   - vSphere Supervisor
      **:** Manages the lifecycle of VKS Clusters and ensure overall system stability.
    - VKS Clusters**:** Hosts application workloads and run user-deployed applications.

    The vSphere Supervisor management pack can monitor both types of clusters, ensuring quick identification of performance issues.

Automated Cluster Discovery
:   When enabled, the vSphere Supervisor adapter identifies all the vSphere Supervisor and VKS Clusters in a vCenter environment and creates the necessary Application Monitoring adapter instances for monitoring.

Enhanced Observability with Dashboards and Metrics
:   The vSphere Supervisor adapter provides details about the vSphere Supervisor and VKS cluster infrastructure, and applications running in the VKS Clusters.