---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool/deploy-nsx-manager-nodes-to-form-a-cluster-using-cli.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Form an NSX Manager Cluster Using the CLI
---

# Form an NSX Manager Cluster Using the CLI

Forming an NSX Manager or Global Manager cluster provides high availability and reliability. If all or atleast one of the three NSX Manager appliances is deployed as an OVA/OVF using vCenter, use the join command to join the NSX Manager nodes and create a cluster.

- To create an NSX Manager cluster, deploy three NSX Manager nodes from the OVF tool CLI or vCenter UI.
- To create a Global Manager cluster, deploy three nodes to create the cluster. However, if your Global Manager has NSX 3.0.0 installed, deploy only one node, and do not form a cluster. See [Install the Active and Standby Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/install-global-manager-appliances.html#GUID-58099280-5447-4d17-8fab-caf2d3ce134c).

1. Open an SSH or console session to the first deployed NSX Manager or Global Manager node and log in with the administrator credentials.
2. On the first deployed node, run the following commands. 
   1. Run the get certificate api thumbprint command. 

      The command output is a string that is unique to this node.
   2. Run the get cluster config command to get the cluster ID of the first deployed node. 

      ```
      mgr-first> get cluster config
      Cluster Id: 7b50abb9-0402-4ed5-afec-363587c3c705
      Cluster Configuration Version: 0
      Number of nodes in the cluster: 1

      ...
      ```
3. Open an SSH or console session to the new node and log in with the administrator credentials.
4. On the new node that is joining the cluster, run the join command.

   Provide the following information about the first deployed node in the join command:

   - IP address
   - Cluster ID
   - User name
   - Password
   - Certificate thumbprint

   ```
   mgr-new> join <Manager-IP> cluster-id <cluster-id> username <Manager-username> password <Manager-password> thumbprint <Manager-thumbprint>
   ```

   The joining and cluster stabilizing process might take from 10 to 15 minutes. Run get cluster status to view the status. Verify that the status for every cluster service group is UP before making any other cluster changes.
5. Add the third node to the cluster. 

   Repeat step 4 on the third node.
6. Verify the cluster status on the web interface.
   - On NSX Manager, log in to the NSX Manager web interface and select SystemAppliances.
   - On Global Manager, log in to the Global Manager web interface and select SystemGlobal Manager Appliances.

Create a transport zone. See [Create Transport Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html#GUID-9bb1c8c1-9063-4d0d-900c-5d94d009140a).