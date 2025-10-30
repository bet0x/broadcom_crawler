---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere-supervisor-monitoring/steps-to-monitor-vsphere-supervisor-clusters-and-resources/disabling-monitoring-for-vks-and-vsphere-supervisor-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Disabling Monitoring for VKS and vSphere Supervisor Clusters
---

# Disabling Monitoring for VKS and vSphere Supervisor Clusters

You can disable monitoring for VKS and vSphere Supervisor clusters from VCF Operations. After you disable monitoring, the objects are not displayed in the Object Relationship chart in the Inventory when you browse to the vSphere Supervisor object. The endpoint is removed from the Telegraf configuration of the vSphere Supervisor cluster.

1. Go to the Inventory Management tile in the InventoryConfigurations.
2. In the search tab, enter the name of the VKS Cluster or the vSphere Supervisor Cluster for which you want to disable monitoring. This is a quick way to find the object. Alternately, you can browse the list of objects and locate the objects.
3. Click the edit icon to edit the object. The Edit Object dialog box opens.
4. From the drop-down, select No for the Enable Monitoring setting under the Advanced Settings. The default value is Yes.
5. Click OK.

A devops engineer must use the vcf-cli to uninstall the Telegraf and Prometheus packages in the VKS cluster.