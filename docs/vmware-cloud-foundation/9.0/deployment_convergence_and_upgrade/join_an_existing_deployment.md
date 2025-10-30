---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/vcf-operations-for-logs-for-vvf-clients/join-an-existing-deployment.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Join an Existing Deployment
---

# Join an Existing Deployment

After you deploy and set up a standalone VCF Operations for logs node, you can deploy a new VCF Operations for logs instance and add it to the existing node to form a VCF Operations for logs cluster.

- In the vSphere Client, note the IP address of the worker VCF Operations for logs virtual appliance.
- Verify that you have the IP address or host name of the primary VCF Operations for logs virtual appliance.
- Verify that you have a user account on the primary VCF Operations for logs virtual appliance with the Super Admin role, a role that has the relevant permissions.
- Verify that the versions of the VCF Operations for logs primary and worker nodes are in sync. Do not add an older version VCF Operations for logs worker to a newer version VCF Operations for logs primary node.
- Login to the web user interface of the VCF Operations for logs primary node and generate a secure token on the ManagementCluster page.

VCF Operations for logs can scale out by using multiple virtual appliance instances in clusters. Clusters enable linear scaling of ingestion throughput, increase query performance, and allow high-availability ingestion. In cluster mode, VCF Operations for logs provides primary and worker nodes. Both primary and worker nodes are responsible for a subset of data. Primary nodes can query all subsets of data and aggregate the results. You might require more nodes to support site needs. You can use from three to 18 nodes in a cluster. This means that a fully functional cluster must have a minimum of three healthy nodes. Most nodes in a larger cluster must be healthy. For example, if three nodes of a six-node cluster fail, none of the nodes functions fully until the failing nodes are removed.

1. Use a supported browser to navigate to the web user interface of the VCF Operations for logs worker. 

   The URL format is https://operations\_for\_logs-host/, where operations\_for\_logs is the IP address or host name of the VCF Operations for logs worker virtual appliance.

   The initial configuration wizard opens.
2. Click Join Existing Deployment.
3. Enter the following details and click Go.

   1. IP address or host name of the VCF Operations for logs primary node.
   2. The secure token generated on the ManagementCluster page.

   If the primary node provides an untrusted SSL certificate, a dialog box appears with the details of the certificate. Click Accept to send a request to the VCF Operations for logs primary node to join the existing deployment.

   If you click Cancel, the join request is not sent to the primary node. You must accept the certificate to ensure that the worker node joins the existing deployment.

   The worker node joins the existing deployment and VCF Operations for logs begins to operate in a cluster.

- Add more worker nodes as needed. The cluster must have a minimum of three nodes.