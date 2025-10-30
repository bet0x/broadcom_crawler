---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/deploy-nsx-manager-nodes-to-form-a-cluster-using-ui.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Deploy NSX Manager Nodes to Form a Cluster from the UI
---

# Deploy NSX Manager Nodes to Form a Cluster from the UI

Forming an NSX Manager or Global Manager cluster provides high availability and reliability. Deploying nodes using the UI is supported only on ESX hosts managed by vCenter that is added as a compute manager.

- Verify that an NSX Manager or Global Manager node is installed. See [Install NSX Manager and Available Appliances](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances.html).
- Verify that compute manager is configured. See [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en).

- Verify that the system requirements are met. See [Planning and Preparation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/planning-and-preparation.html).
- Verify that the required ports are open. Refer to [VMware Ports and Protocols](https://ports.broadcom.com/) for more details.

For deploying additional NSX Manager nodes on a vCenter that is not added as a compute manager, see [Install NSX Manager on ESX Using the Command-Line OVF Tool](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool.html) and [Deploy NSX Manager Nodes to Form a Cluster from the UI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/deploy-nsx-manager-nodes-to-form-a-cluster-using-ui.html).

When you deploy a new node from the UI, the node connects to the first deployed node to form a cluster. All the repository details and the password of the first deployed node are synchronized with the newly deployed node. The first node is known as the orchestrator node because it contains the original copy of the VIBs and installation files required to prepare hosts of the cluster. The orchestrator node also help identify the node on which the Upgrade-Coordinator is running. When new nodes are added to the cluster, NSX uses the repository IP to synchronize the repository of VIBs and installation files on the new nodes of the cluster.

To create an NSX Manager cluster, deploy two additional nodes to form a cluster of three nodes total.

Data is replicated to all the active NSX Manager nodes of the cluster. So, when the NSX Manager cluster is stable, every NSX Manager node contains the same data.

To create a Global Manager cluster, deploy two additional nodes to form a cluster of three nodes total. However, if your Global Manager has NSX 3.0.0 installed, deploy only one node, and do not form a cluster. See [install-global-manager-appliances.html#GUID-58099280-5447-4d17-8fab-caf2d3ce134c\_GUID-58099280-5447-4d17-8fab-caf2d3ce134c-en](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/install-global-manager-appliances.html#GUID-58099280-5447-4d17-8fab-caf2d3ce134c_GUID-58099280-5447-4d17-8fab-caf2d3ce134c-en).

1. From a browser, log in with admin privileges to the NSX Manager or Global Manager at https://<manager-ip-address>.
2. Deploy an appliance.
   - From NSX Manager, select .
   - From Global Manager, select .
3. Enter the appliance information details.

   Option | Description || Host Name or FQDN | Enter a name for the node. If you plan to deploy NSX Manager in dual stack mode (IPv4 and IPv6) and if you plan to configure NSX Manager with CA signed certificates, you must set a FQDN with valid domain name. |
   | IP Type | Select the IP type. The appliance can have IPv4 address only, dual stack address (both IPv4 and IPv6), or IPv6 address only. Note that if you have deployed the first appliance node with IPv4 address only or dual stack address (both IPv4 and IPv6), you cannot deploy additional appliance nodes with IPv6 address only. |
   | Management IPv4/Netmask | Enter an IPv4 address to be assigned to the node. This field is not displayed if you have selected IP Type as IPv6. |
   | Management Gateway IPv4 | Enter a gateway IPv4 address to be used by the node. This field is not displayed if you have selected IP Type as IPv6. |
   | Management IPv6/Netmask | Enter an IPv6 address to be assigned to the node. This option appears when IP Type is set to Both IPv4 and IPv6 or IPv6. |
   | Management Gateway IPv6 | Enter a gateway IPv6 address to be used by the node. This option appears when IP Type is set to Both IPv4 and IPv6 or IPv6. |
   | DNS Servers | Enter DNS server IP addresses to be used by the node. |
   | NTP Server | Enter an NTP server IP address to be used by the node. |
   | Node Size | Select the form factor to deploy the node from the following options: - Small (4 vCPU, 16 GB RAM, 300 GB storage) - Medium (6 vCPU, 24 GB RAM, 300 GB storage) - Large (12 vCPU, 48 GB RAM, 300 GB storage) - Extra Large (24 vCPU, 96 GB RAM, 400 GB storage) For Global Manager select size: - Medium GM appliance for deployments up to four locations and 128 hypervisors across all locations - Large or Extra Large GM appliance for deployments with higher scaleDo not use Small GM appliance for scale deployment. For details see the [VMware Configuration Maximums tool.](https://configmax.esp.vmware.com/guest?vmwareproduct=VMware%20NSX&release=NSX%204.2.0&categories=74-65,74-87,74-88,74-89,74-90,74-91,74-92,74-113) |
4. Enter the configuration details.

   Option | Description || Compute Manager | Select the vCenter to provision compute resources for deploying the node. |
   | Compute Cluster | Select the cluster the node is going to join. |
   | (Optional) Resource Pool | Select a resource pool for the node from the drop-down menu. |
   | (Optional) Host | Select a host for the node from the drop-down menu. |
   | Datastore | Select a datastore for the node files from the drop-down menu. |
   | Virtual Disk Format | - For NFS datastores, select a virtual disk format from the available provisioned policies on the underlying datastore.   - With hardware acceleration, Thin Provision, Thick Provision Lazy Zeroed, and Thick Provision Eager Zeroed formats are supported.   - Without hardware acceleration, only Thin Provision format is supported. - For VMFS datastores, Thin Provision, Thick Provision Lazy Zeroed, and Thick Provision Eager Zeroed formats are supported. - For vSAN datastores, you cannot select a virtual disk format because the VM storage policy defines the format.   - The vSAN storage policies determine the disk format. The default virtual disk format for vSAN is Thin Provision. You can change the vSAN storage policies to set a percentage of the virtual disk that must be thick-provisioned. By default, the virtual disk for an NSX Manager or Global Manager node is prepared in the Thin Provision format.  You can provision each node with a different disk format based on which policies are provisioned on the datastore. |
   | Network | Click Select Network to select the management network for the node. |
5. Enter the access and credentials details.

   Option | Description || Enable SSH | Toggle the button to allow an SSH login to the new node. |
   | Enable Root Access | Toggle the button to allow root access to the new node. |
   | System Root Credentials | Set the root password and confirm the password for the new node.  Your password must comply with the password strength restrictions. - At least 12 characters - At least one lower-case letter - At least one upper-case letter - At least one digit - At least one special character - At least five different characters - Default password complexity rules are enforced by the following Linux PAM module arguments:   - retry=3: The maximum number of times a new password can be entered, for this argument at the most 3 times, before returning with an error.   - minlen=12: The minimum acceptable size for the new password. In addition to the number of characters in the new password, credit (of +1 in length) is given for each different kind of character (other, upper, lower and digit).   - difok=0: The minimum number of bytes that must be different in the new password. Indicates similarity between the old and new password. With a value 0 assigned to difok, there is no requirement for any byte of the old and new password to be different. An exact match is allowed.   - lcredit=1: The maximum credit for having lower case letters in the new password. If you have less than or 1 lower case letter, each letter will count +1 towards meeting the current minlen value.   - ucredit=1: The maximum credit for having upper case letters in the new password. If you have less than or 1 upper case letter each letter will count +1 towards meeting the current minlen value.   - dcredit=1: The maximum credit for having digits in the new password. If you have less than or 1 digit, each digit will count +1 towards meeting the current minlen value.   - ocredit=1: The maximum credit for having other characters in the new password. If you have less than or 1 other characters, each character will count +1 towards meeting the current minlen value.   - enforce\_for\_root: The password is set for the root user. For more details on Linux PAM module to check the password against dictionary words, refer to the man page. For example, avoid simple and systematic passwords such as VMware123!123 or VMware12345. Passwords that meet complexity standards are not simple and systematic but are a combination of letters, alphabets, special characters, and numbers, such as VMware123!45, VMware 1!2345 or VMware@1az23x. |
   | Admin CLI Credentials and Audit CLI Credentials | Select the Same as root password check box to use the same password that you configured for root, or deselect the check box and set a different password. |
6. Click Install Appliance.

   The new node is deployed. You can track the deployment process in the page for NSX Manager, the for Global Manager, or the vCenter for either. Do not add additional nodes until the installation is finished and the cluster is stable.
7. Wait for the deployment, cluster formation, and repository synchronization to finish. 

   The joining and cluster stabilizing process might take from 10 to 15 minutes. After the node boots (as part of appliance bringup) and is back up, log in to the first deployed NSX Manager CLI as an admin. Run get cluster status to view the status. Verify that the first node and second node are members of the cluster and the status for every cluster service group is UP and cluster status STABLE before making any other cluster changes.

   - If you reboot the first deployed NSX Manager node, when the deployment of a new node is in progress, the new node might fail to register with the cluster. It displays the Failed to Register message on the new node's thumbnail. To redeploy the node manually on the cluster, delete and redeploy the failed node again.
   - If a node deployment fails, you cannot reuse the same IP address to deploy another node until the failed node is deleted.
   - NSX Manager nodes that are removed from the cluster should be powered off or deleted. Do not reuse it in your deployments.
8. After the VM node boots a second time, log in to the CLI as admin and run the get interface eth0 command to verify that the IP address was applied as expected.
9. Verify that your NSX Manager,or Global Manager node has the required connectivity. 

   Perform the following tasks:
   - Ping your node from another machine.
   - The node can ping its default gateway.
   - The node can ping the hypervisor hosts that are in the same network using the management interface.
   - The node can ping its DNS server and its NTP Server or FQDN.
   - If you enabled SSH, make sure that you can SSH to your node.

   If connectivity is not established, make sure that the network adapter of the virtual appliance is in the proper network or VLAN.
10. If your cluster has only two nodes, add another appliance.
    - From NSX Manager, select and repeat the configuration steps.
    - From Global Manager, select and repeat the configuration steps.

    If the orchestrator node (first NSX Manager node deployed) goes down or becomes unreachable while additional nodes in the cluster have not finished replicating with first node fully, further operations on the cluster will fail. To avoid this, bring up the first node up successfully and then delete and redeploy the additional nodes that had failed to finish replication of data with the first node.

    NSX Manager nodes that are removed from the cluster should be powered off or deleted. Do not reuse it in your deployments.
11. Before adding or removing an existing node from the cluster, place all Security Intelligence and NDR SaaS agents in maintenance mode.

    PUT https://nsx-manager-ip/policy/api/v1/infra/sites/agents/intelligence/maintenance

    ```
    {
    "enable": true
    }
    ```
12. After adding or removing nodes from the cluster, take all the Security Intelligence and NDR SaaS agents out of maintenance mode.

    PUT https://nsx-manager-ip/policy/api/v1/infra/sites/agents/intelligence/maintenance

    ```
    {
    "enable": false
    }
    ```

Configure NSX Edge. See [Install an NSX Edge on ESX Using the vSphere GUI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/install-an-nsx-edge-on-esxi-using-a-gui.html#GUID-a98b0a06-775e-4a72-b4e4-3b2b423d5a81).