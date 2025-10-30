---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/scaling-up-and-scaling-out-management-nodes-in-vcf/scale-out-vrealize-suite-products.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Vertical scale up for VCF Operations and VCF Operations for logs
---

# Vertical scale up for VCF Operations and VCF Operations for logs

To scale up resource allocations such as vCPUs, RAM, and disk capacity in cluster nodes, you can use VCF Operations fleet management. The Vertical Scale Up option is supported for VCF Operations and VCF Operations for logs.

1. Under Fleet ManagementLifecycleComponents, select the integrated component that you want to update.
2. On the component details screen that appears, click the ellipses (...) and select Vertical Scale Up.
3. The Proceed to Vertical Scale Up pop-up window appears. Acknowledge the downtime warning and click Trigger Inventory Sync to synchronize the VCF Operationsfleet management appliance with the latest data from the cluster.
   1. When the inventory sync completes successfully, click Proceed.
4. Select the nodes to be scaled up.

   - For VCF Operations , you scale up the operations primary nodes.
   - For VCF Operations for logs, you scale up the operations-log primary nodes.
5. For vertical scale up details, the current cluster size appears. To scale up, provide the following information.

   - Scale up Size: Select a larger size such as Medium, Large, or Extra large.
   - Additional disk size: Provide the additional size in GB.
   - Advanced settings: Select the datastore for nodes and provide an additional disk size in GB.
6. Click Next.
7. Click RUN PRECHECK.

   If the data validation is not successful, perform the recommended actions and run the precheck again.
8. After a successful precheck run, review the summary of your vertical scale up request and click Submit.

Vertical scale up begins. During the process, the VCF Operations nodes are restarted. During the downtime, VCF Operations is not available.