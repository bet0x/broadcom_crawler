---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/join-nsx-edges-with-the-management-plane.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Join NSX Edge with the Management Plane
---

# Join NSX Edge with the Management Plane

To establish communication between NSX Edges and NSX Manager or NSX Manager cluster, join NSX Edges with NSX Manager. You only need to register NSX Edges with one NSX Manager to ensure communication with the management plane.

Verify that you have admin privileges to log
in to the NSX Edges and
NSX Manager
appliance.

1. Open an SSH session or console session to one of the
   NSX Manager appliances.
2. Open an SSH session or console
   session to the NSX Edge node VM.
3. To retrieve the thumbprint of the
   NSX Manager appliance, at
   the NSX Manager appliance console, run the
   get certificate api
   thumbprint command.

   The command output is a string of
   alphanumeric numbers that is unique to this NSX Manager.

   For example:

   ```
   NSX-Manager1> get certificate api thumbprint
   659442c1435350edbbc0e87ed5a6980d892b9118f851c17a13ec76a8b985f57
   ```
4. Alternatively, to retrieve the thumbprint of the cluster, at the NSX Manager appliance console, run
   get certificate cluster thumbprint. 

   The output is a string of alphanumeric numbers that is unique to the
   cluster.
5. To join the NSX Edge node (VM or Bare Metal) to the NSX Manager appliance, run the
   join
   management-plane command.

   Provide the following information:
   - Hostname or IP address of the
     NSX Manager with an optional
     port number
   - User name of the NSX Manager
   - Certificate thumbprint of the
     NSX Manager
   - Password of the NSX Manager

   ```
   NSX-Edge1> join management-plane <Manager-IP> thumbprint <Manager-thumbprint> username admin
   ```

   Repeat this command on each
   NSX Edge node VM.
6. If cluster VIP is configured for
   the NSX Manager, then join
   NSX Edge Node using the
   cluster thumbprint. Run the join management-plane
   command.

   Provide the following information:
   - Virtual IP address of the
     NSX Manager
     cluster with an optional port number
   - User name of the
     NSX Manager
   - Certificate thumbprint of
     the NSX Manager
     cluster
   - Password of the
     NSX Manager

   ```
   NSX-Edge1> join  management-plane <Cluster-VIP> username <Manager-username> password <Manager-password> thumbprint <Cluster-tumbprint>
   ```
7. Verify the result by running the
   get
   managers command on your NSX Edge node VMs. 

   ```
   nsx-edge-1> get managers
   - 10.173.161.17  Connected (NSX-RPC)
   - 10.173.161.140 Connected (NSX-RPC)
   - 10.173.160.204 Connected (NSX-RPC)
   ```
8. In the NSX Manager UI, navigate to .

   On the NSX Edge Transport
   Node page:
   - The Configuration
     State column displays Configure
     NSX. Click Configure NSX
     to begin configuration on the node. If the NSX
     Version column does not display the version number
     installed on the node, try refreshing the browser window.
   - Before you configure NSX on
     the NSX Edge node, the
     Node Status and Tunnel
     Status columns display state Not
     Available. The Transport Zones
     and N-VDS switches columns display value
     0, indicating there are no transport
     zones attached or N-VDS switches configured on the NSX Edge node.

When installing NSX Edge using NSX Manager see [Create an NSX Edge Transport Node](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-transport-node.html#GUID-ab8c1484-ad70-489a-b0df-32974dc418d8).

When installing NSX Edge manually, see [Edit Transport Node Configuration](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/manually-deploying-nsx-edge-node-outside-of-nsx/edit-nsx-edge-transport-node-configuration.html).