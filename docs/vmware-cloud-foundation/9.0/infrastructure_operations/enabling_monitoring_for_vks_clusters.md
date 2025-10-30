---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/steps-to-monitor-vsphere-supervisor-clusters-and-resources/prerequisites-for-vsphere-supervisor-monitoring.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Enabling Monitoring for VKS Clusters
---

# Enabling Monitoring for VKS Clusters

Install Supervisor Management Proxy using the vSphere UI and Telegraf and Prometheus in VKS clusters using VCF CLI as a prerequisite to monitor the VKS Clusters. Enable pod and container monitoring of VKS Clusters using VCF Operations.

## Install Supervisor Management Proxy and Telegraf in VKS Clusters

To setup monitoring for VKS Clusters, the following components must be installed in each VKS Clusters:

- Supervisor Management Proxy - This is the supervisor service on Supervisor which is installed in Supervisor.
- Telegraf and Prometheus must be installed and configured by DevOps engineers on each VKS Cluster before metrics and object details are sent to Cloud Proxy. Refer to the steps in this topic for more information, [Install Telegraf.](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/using-tkg-service-with-vsphere-supervisor/installing-standard-packages-on-tkg-service-clusters/installing-standard-packages-on-tkg-cluster-using-tkr-for-vsphere-8-x/install-telegraf.html)

- Supervisor must be of versions that that includes Telegraf support.
- DevOps engineers must use the following values.yaml when installing Telegraf:

  ```
  isMetricProxyConfigured: true
  domainName: cluster.local <-- points to service domain of the cluster
  ```

## Verify Authentication and Security

Supervisor generates the certificates for each Telegraf instance in a VKS Cluster. These certificates are rotated by the cert-manager running on the Supervisor and automatically updated in the VKS Cluster. Supervisor Managment Proxy terminates the TLS connection from the VKS Cluster, thus securing the communication between the Supervisor and VKS Clusters. Supervisor Management Proxy uses the certificates provided by Cloud Proxy for communication between Supervisor Management Proxy and Cloud Proxy. Cloud Proxy terminates the TLS Connection thereby securing communication between the Supervisor and Cloud Proxy.

## Enable Pod and Container Monitoring for VKS Clusters

1. Go to the Inventory Management tile in the InventoryConfigurations.
2. In the search tab, enter the name of the VKS Cluster for which you want to enable pod and container monitoring. This is a quick way to find the object. Alternately, you can browse through the list of objects and locate the VKS Cluster.
3. Click the edit icon to edit the object. The Edit Object dialog box opens.
4. Enter True for the Pod and Container Monitoring Enabled setting under the Advanced Settings. The default value is False.
5. Click OK.