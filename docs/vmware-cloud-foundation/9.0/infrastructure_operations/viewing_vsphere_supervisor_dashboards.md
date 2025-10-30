---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/steps-to-monitor-vsphere-supervisor-clusters-and-resources/vsphere-supervisor-dashhboards.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Viewing vSphere Supervisor Dashboards
---

# Viewing vSphere Supervisor Dashboards

When the vSphere Supervisor management pack is enabled, you can view the metrics and resource information in VCF Operations using the three types of dashboards.

## Where You Find the vSphere Supervisor Dashboards

Go to Infrastructure OperationsDashboards and ReportsInventory. Expand the All folder and look for the vSphere Supervisor dashboards.

## Types of vSphere Supervisor Dashboards

- Kubernetes Inventory

  - Infrastructure details in your vSphere Supervisor, via nodes.
  - Pod and container status via namespace.
  - VKS Clusters lifecycle metrics.
- Kubernetes Performance

  - CPU and memory usage.
  - vSphere Supervisor and VKS Clusters performance.
- vSphere Supervisor

  - Monitor the critical components of the vSphere Supervisor.

## Using the vSphere Supervisor Dashboards

Together, these dashboards offers the following capabilities:

- High-Level Cluster Overview

  - The dashboard offers a summary of cluster health, showing key metrics such as CPU usage, memory consumption, and node availability.
  - You can quickly spot clusters with performance bottlenecks before diving into detailed analysis.
- Drill-Down Approach for Root Cause Analysis

  - If an issue is detected at the cluster level, you can navigate into child objects such as namespaces, nodes, and pods to pinpoint the source.
  - Example: If CPU throttling is detected at the cluster level, users can filter to see which namespaces or pods are consuming excessive CPU.
- Real-Time Monitoring with Push-Based Data Collection

  - Unlike traditional pull-based methods, metrics are pushed to the Cloud Proxy in real time, allowing for faster detection of performance spikes.
  - Users can correlate metrics over time, helping them understand trends that may lead to potential failures.
- Supervisor and Guest Cluster Insights

  - The Supervisor Dashboard monitors critical lifecycle components. If a Supervisor goes down, it may impact all associated VKS Clusters.
  - You can see which clusters are affected and take corrective action immediately.
- Debugging Pods and Containers

  - The dashboard provides alerts on failed pods, frequent container restarts, and out-of-memory (OOM) errors.
  - You can filter by node or namespace to isolate problematic workloads.