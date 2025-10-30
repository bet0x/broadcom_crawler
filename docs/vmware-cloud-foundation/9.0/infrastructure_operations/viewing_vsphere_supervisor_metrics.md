---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/steps-to-monitor-vsphere-supervisor-clusters-and-resources/vsphere-supervisor-metrics.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Viewing vSphere Supervisor Metrics
---

# Viewing vSphere Supervisor Metrics

This table lists the metrics which the vSphere Supervisor management pack collects. Go to the Metrics tab in the vSphere Supervisor object page by navigating to AdministrationIntegrationsRepository to view their details.

## vSphere Supervisor Metrics

A list of the vSphere Supervisor metrics available in VCF Operations is in the following table:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Object** | **Element** | **Metric** | **Type** | **Unit** |
| Container | CPU | Usage | Metric | Millicores |
| Container | CPU | Throttled | Metric | % |
| Container | CPU | Usage | Metric | % |
| Container | CPU | Requests | Property | Millicores |
| Container | CPU | Limits | Property | Millicores |
| Container | Memory | Usage | Metric | MB |
| Container | Memory | Usage | Metric | % |
| Container | Memory | Limits | Property | MB |
| Container | Memory | Fail Count | Metric |  |
| Container | Memory | Requests | Property | MB |
| Container | Summary | Restart Count | Property | Count |
| Container | Performance | Overall Performance | Metric |  |
| Pod | CPU | Usage | Metric | Millicores |
| Pod | CPU | Worst Throttled Container | Metric | % |
| Pod | CPU | Requests | Property | Millicores |
| Pod | CPU | Limits | Property | Millicores |
| Pod | Memory | Usage | Metric | MB |
| Pod | Memory | Limits | Property | MB |
| Pod | Memory | Requests | Property | MB |
| Pod | Memory | Total Out of Memory Events | Metric | Count |
| Pod | Network | Receive Packets Dropped | Metric | % |
| Pod | Network | Transmit Packets Dropped | Metric | % |
| Pod | Network | Receive Errors Total | Metric | % |
| Pod | Network | Transmit Errors Total | Metric | % |
| Pod | Summary | Status | Property |  |
| Deployment | CPU | Usage | Metric | Millicores |
| Deployment | CPU | Top 95% CPU Throttling Workload's | Metric | % |
| Deployment | CPU | Requests | Property | Millicores |
| Deployment | CPU | Limits | Property | Millicores |
| Deployment | Memory | Usage | Metric | MB |
| Deployment | Memory | Limits | Property | MB |
| Deployment | Memory | Requests | Property | MB |
| Deployment | Memory | Top 95% Out Of Memory Events | Metric | Count |
| Deployment | Network | Top 95% Network Receive Packets Drop | Metric | % |
| Deployment | Network | Top 95% Network Transmit Packets Drop | Metric | % |
| Deployment | Network | Top 95% Network Receive Errors Total | Metric | % |
| Deployment | Network | Top 95% Network Transmit Errors Total | Metric | % |
| Deployment | Status | Replicas | Metric |  |
| Deployment | Summary | No of Containers | Metric |  |
| Deployment | Summary | No of Pods | Metric |  |
| Deployment | Summary | Pods Not Running | Metric |  |
| Deployment | Summary | Status | Metric |  |
| Deployment | Status | Ready Replica's | Metric |  |
| Deployment | Performance | Overall Performance | Metric | % |
| Deployment | Performance | Network Override | Metric | % |
| Node | CPU | Usage | Metric | Millicores |
| Node | CPU | Top 95% CPU Throttling Workload's | Metric | % |
| Node | CPU | Requests | Property | Millicores |
| Node | CPU | Limits | Property | Millicores |
| Node | Memory | Usage | Metric | MB |
| Node | Memory | Limits | Property | MB |
| Node | Memory | Requests | Property | MB |
| Node | Network | Top 95% Network Receive Packets Drop | Metric | % |
| Node | Network | Top 95% Network Transmit Packets Drop | Metric | % |
| Node | Network | Top 95% Network Receive Errors Total | Metric | % |
| Node | Network | Top 95% Network Transmit Errors Total | Metric | % |
| Node | API Server Metrics | Request Rate | Metric |  |
| Node | API Server Metrics | Request Error Rate | Metric |  |
| Node | Controller Manager Metrics | Work Queue Depth | Metric |  |
| Node | ETCD Metrics | Is Leader | Metric |  |
| Node | ETCD Metrics | Leader changes | Metric |  |
| Node | ETCD Metrics | Proposals Applied | Metric |  |
| Node | ETCD Metrics | Proposals Committed | Metric |  |
| Node | ETCD Metrics | Proposals Pending | Metric |  |
| Node | ETCD Metrics | Server Size | Metric | bytes |
| Node | ETCD Metrics | Server Used | Metric | bytes |
| Namespace | CPU | Usage | Metric | Millicores |
| Namespace | CPU | Top 95% CPU Throttling Workload's | Metric | % |
| Namespace | CPU | Requests | Property | Millicores |
| Namespace | CPU | Limits | Property | Millicores |
| Namespace | Memory | Usage | Metric | MB |
| Namespace | Memory | Limits | Property | MB |
| Namespace | Memory | Requests | Property | MB |
| Namespace | Memory | Top 95% Out Of Memory Events | Metric | Count |
| Namespace | Network | Top 95% Network Receive Packets Drop | Metric | % |
| Namespace | Network | Top 95% Network Transmit Packets Drop | Metric | % |
| Namespace | Network | Top 95% Network Receive Errors Total | Metric | % |
| Namespace | Network | Top 95% Network Transmit Errors Total | Metric | % |
| Namespace | Summary | No of Pods | Metric | Count |
| Namespace | Summary | No of Containers | Metric | Count |
| Namespace | Summary | No of Namespaces | Metric | Count |
| Namespace | Summary | No of Deployments | Metric | Count |
| Namespace | Summary | No of Statefulsets | Metric | Count |
| Namespace | Summary | No of Daemonsets | Metric | Count |
| Namespace | Summary | Number of Pods Not running | Metric |  |
| Cluster | Summary | Number of Pods Not running | Metric |  |
| Cluster | CPU | Usage | Metric | Cores |
| Cluster | CPU | Top 95% CPU Throttling Workload's | Metric | % |
| Cluster | CPU | Requests | Metric | Cores |
| Cluster | CPU | Limits | Metric | Cores |
| Cluster | Memory | Usage | Metric | MB |
| Cluster | Memory | Limits | Property | GB |
| Cluster | Memory | Requests | Property | GB |
| Cluster | Memory | Top 95% Out Of Memory Events | Metric | Count |
| Cluster | Network | Top 95% Network Receive Packets Drop | Metric | % |
| Cluster | Network | Top 95% Network Transmit Packets Drop | Metric | % |
| Cluster | Network | Top 95% Network Receive Errors Total | Metric | % |
| Cluster | Network | Top 95% Network Transmit Errors Total | Metric | % |
| Cluster | Summary | No of Nodes | Metric | Count |
| Cluster | Summary | No of Pods | Metric | Count |
| Cluster | Summary | No of Containers | Metric | Count |
| Cluster | Summary | No of Namespaces | Metric | Count |
| Cluster | Summary | No of Deployments | Metric | Count |
| Cluster | Summary | No of Statefulsets | Metric | Count |
| Cluster | Summary | No of Daemonsets | Metric | Count |
| Cluster | Summary | No of Pods not Running | Metric | Count |