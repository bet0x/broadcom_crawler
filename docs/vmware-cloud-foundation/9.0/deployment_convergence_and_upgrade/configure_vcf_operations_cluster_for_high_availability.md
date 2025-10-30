---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/run-the-setup-wizard-to-create-an-ha-node.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure VCF Operations Cluster for High Availability
---

# Configure VCF Operations Cluster for High Availability

VCF Installer supports the manual deployment of VCF Operations in Simple mode for VMware vSphere Foundation. After the initial deployment, the VCF Operations cluster can be converted to a high availability architecture. To activate high availability (HA) for a VCF Operations cluster, specify one of the data nodes to become a replica of the primary node.

- Create and configure the primary node.
- Create and configure a data node with a static IP address.
- Note the fully qualified domain name (FQDN) or IP address of the primary node.

If the cluster is running, activating HA restarts the cluster.

You can add HA to the VCF Operations cluster at installation time or after VCF Operations is up and running. Adding HA at installation is less intrusive because the cluster has not yet started.

1. In a Web browser, navigate to the primary node administration interface. 

   https://primary-node-name-or-ip-address/admin
2. Enter the VCF Operations administrator user name of admin.
3. Enter the VCF Operations administrator password and click Log In.
4. To add a new data node, click Add new Nodes.
   1. In the Add new nodes to cluster wizard, click the Add Nodes icon.
   2. For Node Name, enter a generic name to identify the node.
   3. For Node Address, enter the IP address of the node you want to add.
   4. For Current Cluster Role, select Data, to add a data node to be used as the primary replica node.
   5. Click Save, review and close the thumbprint information, and then click Next.
   6. For Primary Node Password, enter the administrator password used during log in, and then click Finish.

   If the cluster was online, the administration interface displays that the cluster initialization is in progress as the new data node gets added to the VCF Operations cluster. You must wait for the cluster to come Online again before activating HA.
5. Under High Availability, click Activate.
6. In the Activate High Availability wizard, select a data node to serve as the replica for the primary node, and click OK.
7. To activate HA, you must restart your cluster. Review the Confirm Cluster Restart message and click Yes.

   If the cluster was online, the administration interface displays progress as VCF Operations configures, synchronizes, and rebalances the cluster for HA.
8. If the primary node and replica node go offline, and the primary remains offline for any reason while the replica goes online, the replica node does not take over the primary role, take the entire cluster offline, including data nodes and log in to the replica node command-line console as a root.
9. Open $ALIVE\_BASE/persistence/persistence.properties in a text editor.
10. Locate and set the following properties: 

    ```
    db.role=PRIMARY
    db.driver=/data/vcops/xdb/vcops.bootstrap
    ```
11. Save and close persistence.properties.
12. In the administration interface, bring the replica node online, and verify that it becomes the primary node and bring the remaining cluster nodes online.

High Availability is activated on your VCF Operations cluster.

After creating a primary replica node, you have the following options.

- New, unstarted clusters:
  - Create and add data nodes.
  - Click Start VCF Operations to start the cluster, and log in to finish configuring the product.

    The cluster might take from 10 to 30 minutes to start, depending on the size of your cluster and nodes. Do not make changes or perform any actions on cluster nodes while the cluster is starting.
- Established, running clusters:
  - Create and add data nodes.
- To deactivate high availability, click Deactivate HA and follow the steps in the admin UI. The deativation timeline depends on the cluster size and the data retention period. Please wait for the deactivation to complete.