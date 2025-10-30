---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/scaling-up-and-scaling-out-management-nodes-in-vcf/scale-up-vrealize-suite-products.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Add Nodes to VCF Operations
---

# Add Nodes to VCF Operations

You can add nodes to your VCF Operations, VCF Operations for logs, and VCF Operations for networks.

1. On the Components tab under Fleet ManagementLifecycle, select the integrated component that you want to update.
2. On the component details screen that appears, click Add Nodes.
3. The Proceed to Add Nodes pop-up window appears. Read the downtime warning and click Trigger Inventory Sync to synchronize the VCF Operations fleet management appliance with the latest data from the cluster. Click Submit to start the inventory sync.
   1. Click Submit to start the inventory sync.
   2. When the inventory sync completes successfully, click Proceed.
4. On the Infrastructure pane, review the existing infrastructure and click Next.

   If the Cluster, Network, and Datastore are not selected, you must make selections before clicking Next.
5. On the Network pane, review the existing network information and click Next.
6. On the Components pane, click the down arrow for Component Properties to display the existing nodes. Click the plus sign to add a node.

   - For VCF Operations , select from the following node types and complete the FQDN and IP Address fields for each:

     - Operations replica node. Adding a replica node requires a certificate change on the cluster.
     - Operations data node. Adding a data node requires a certificate change on the cluster. See [Managing Certificates in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0.html).
     - Cloud Proxy. Adding a cloud proxy node also requires a Deployment type.
     - Collector groups. Adding a collector group automatically adds a new cloud proxy node to the group. The new cloud proxy node also requires a Deployment type.
   - For VCF Operations for logs, each added node requires a minimum of two operations-logs worker nodes. Complete the FQDN and IP Address fields for the two nodes.
7. Click RUN PRECHECK.

   If the data validation is not successful, perform the recommended actions and run the precheck again.
8. After a successful precheck run, review the summary of your add nodes request and click Submit.