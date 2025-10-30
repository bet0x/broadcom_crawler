---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/configure-a-virtual-ip-address-for-a-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure a Virtual IP Address for a Cluster
---

# Configure a Virtual IP Address for a Cluster

To provide fault tolerance and high availability to NSX Manager nodes, assign a virtual IP address (VIP) to the NSX cluster.

NSX Manager nodes of a cluster become part of an HTTPS group to service API and UI requests. The leader node of the cluster assumes ownership of the set VIP of the cluster to service any API and UI request. Any API and UI request coming in from clients is directed to the leader node.

When assigning Virtual IP, all the NSX Manager VMs in the cluster must be configured in the same subnet. But if external load balancer is used to configure cluster VIP, then NSX Managers and VIP can belong to a different subnet.

If the leader node that owns VIP becomes unavailable, NSX elects a new leader. The new leader owns the VIP. It sends out a gratuitous ARP packet advertising the new VIP to MAC address mapping. After a new leader node is elected, new API and UI requests are sent to the new leader node.

Failover of VIP to a new leader node of the cluster might take a few minutes to become functional. If the VIP fails over to a new leader node because the previous leader node became unavailable, reauthenticate the NSX Manager credentials so that API requests are directed to the new leader node.

VIP is not designed to serve as a load-balancer and you cannot use it if you enable the vIDM External Load Balancer Integration from SystemUsersConfiguration. Do not set up a VIP if you want to use the External Load Balancer from vIDM. See [Configure VMware Workspace ONE Access Integration](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/configure-vmware-identity-manager-workspace-one-access-integration.html) in the NSX Administration Guide for more details.

If you reset the cluster VIP, then vIDM configurations that are using the VIP is cleared. You will need to reconfigure vIDM configuration with the new VIP.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Go to System > Appliances.
3. In the Virtual IP field, click Set Virtual IP.
4. Enter the IPv4 and/or IPv6 address to use as VIP for the cluster.

   Ensure that VIP is part of the same subnet as the other management nodes. When you deploy a NSX Manager in a dual stack environment (IPv4 and IPv6), use a valid FQDN address and use the same FQDN address for both IPv4 and IPv6 addresses.
5. Click Save.
6. To verify the cluster status and the API leader of the HTTPS group, enter the NSX Manager CLI command get cluster status verbose in the NSX Manager console or over SSH.

   The following is an example output:

   ```
   Group Type: HTTPS
   Group Status: STABLE

   Members:
    UUID                                       FQDN                  IP               STATUS          
    cdb93642-ccba-fdf4-8819-90bf018cd727       nsx-manager       192.196.197.84        UP              
    51a13642-929b-8dfc-3455-109e6cc2a7ae       nsx-manager       192.196.198.156       UP              
    d0de3642-d03f-c909-9cca-312fd22e486b       nsx-manager       192.196.198.54        UP              

   Leaders:
    SERVICE                                    LEADER                                     LEASE VERSION                  
    api                                        cdb93642-ccba-fdf4-8819-90bf018cd727            8
   ```
7. Verify that the VIP is working correctly. 

   From a browser, log in to the NSX Manager using the virtual IP address assigned to the cluster at https://<VIP-address>.

Any API requests to NSX are redirected to the virtual IP address of the cluster, which is owned by the leader node. The leader node then routes the request forward to the other components of the appliance.

If you deploy NSX Manager in dual stack mode (IPv4, IPv6) and/or if you plan to configure NSX Manager deployment with CA-signed certificates, associate the VIP IP address with DNS name. Also, configure reverse and forward proxy for the VIP IP address on the DNS server. Then access VIP from https://<VIP-dns-name>.