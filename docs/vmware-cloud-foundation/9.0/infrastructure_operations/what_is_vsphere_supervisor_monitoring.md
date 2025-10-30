---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/what-is-vsphere-supervisor-monitoring.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > What is vSphere Supervisor Monitoring
---

# What is vSphere Supervisor Monitoring

VMware Cloud Foundation 9.0 introduces an integrated monitoring solution in the form of the vSphere Supervisor management pack to track Kubernetes resource allocation, availability, and performance.

vSphere Supervisor management pack is a native, but internal management pack which is automatically installed when you configure the vCenter integration. This pack enables automated resource detection and monitoring specifically for vSphere Supervisor and vSphere Kubernetes Service (VKS) Clusters. When you enable a setting in the vCenter integration, VCF Operations automatically detects and creates vSphere Supervisor adapter instances for streamlined monitoring.

Previously, the VMware Aria Operations Management Pack for Kubernetes monitored Kubernetes clusters using a pull based model. The vSphere Supervisor management pack monitors vSphere Supervisor and VKS Clusters using push based metric collection. Unlike the traditional pull based approach, the vSphere Supervisor adapter uses Telegraf and the data is pushed directly to a Cloud Proxy. The Cloud Proxy acts as an intermediary to store and forward data, ensuring reliability even if temporary network disruptions occur. To see a list of metrics collected, go to the topic, [vSphere Supervisor Metrics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/steps-to-monitor-vsphere-supervisor-clusters-and-resources/vsphere-supervisor-metrics.html).

## How vSphere Supervisor Monitoring Works

The Application Monitoring adapter is responsible for collecting metrics and organizing the resource inventory. For every Cloud Proxy account which is configured in VCF Operations, an Application Monitoring adapter is automatically created for it.

Telegraf collects metrics from different Kubernetes objects inside the vSphere Supervisor and VKS Clusters and forwards them to the Cloud Proxy. Monitoring of Kubernetes objects such as vSphere Pods and containers is supported. vSphere Pods are only supported with Supervisors that are configured with NSX as the networking stack. For vSphere Supervisor, monitoring of these objects is enabled by default. For VKS Clusters, you must enable it.

During the first collection cycle, certificates are created, and the endpoint details are sent to the vSphere Supervisor. The vSphere Supervisor adapter ensures that metrics are directed to the appropriate Cloud Proxy.

Once the Application Monitoring adapter receives metrics, it organizes and stores the inventory. If needed, you can switch to any other Cloud Proxy, and the vSphere Supervisor adapter will automatically update the endpoint details.