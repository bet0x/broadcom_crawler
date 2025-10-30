---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/add-a-location.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Location 
---

# Add a Location

After you add a location to Global Manager, you can create objects from Global Manager that span that location.

- Verify that the NSX environment you are adding has the latest version of NSX installed.

  This new NSX location can be a new NSX environment or an NSX environment with an existing Network and Security configuration.
- The NSX environment in the new location must have three NSX Manager nodes deployed and a cluster VIP configured. See [Configure a Virtual IP Address for a Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/configure-a-virtual-ip-address-for-a-cluster.html)
- .

  For a proof-of-concept environment, you can add a location that has only one NSX Manager node, but you must still configure a cluster VIP.
- Verify that the latency between the Global Manager and the location is 500 ms or less for non-stretched networks or 150 ms or less for stretched networks.

You can find the number of supported locations in the [VMware Configuration Maximums tool](https://configmax.vmware.com/home). Select the appropriate version of NSX, select the NSX Federation category, and click View Limits.

Only use the admin account credentials to register the Local Manager with the Global Manager.

After you add a location to the Global Manager, the NSX Manager is called a Local Manager (LM).

1. Log in to the Global Manager at https://global-manager-ip-or-fqdn/.
2. Select SystemLocation Manager and click Add On-Prem Location.
3. In the Add New Location dialog box, enter the Location details.

   Option | Description || Location Name | Provide a name for the location. |
   | FQDN/IP | Enter the FQDN or IP address of the NSX Manager cluster VIP. Do not enter an individual NSX Manager FQDN or IP. |
   | Username and Password | Provide the admin user's credentials for the NSX Manager at the location. Do not use any other account to register the Local Manager with the Global Manager. |
   | SHA-256 Thumbprint | Log in to any NSX Manager node in the cluster and run this command: ``` get certificate cluster thumbprint ```  The result is the cluster VIP certificate:  bfae1a0a... |
   | Check Compatibility | Click Check Compatibility to ensure that the location can be added. This checks that the NSX version is compatible. |

If you want to create gateways and segments that span more than one location, you must configure a remote tunnel endpoint (RTEP) on Edge nodes in each location to handle the cross-location traffic. See [Configure Edge Nodes for Stretched Networking](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/add-a-location/configure-edge-nodes-for-stretched-networking.html#GUID-360c7f37-f1ae-42ab-b10c-aecab56fd116-en). After you add a location to your Global Manager, you can import your configurations from that location's Local Manager appliance into the Global Manager. See [Importing Configurations from Local Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/add-a-location/importing-lm-configs.html#GUID-1b0e8ac3-f6f3-44c6-9c99-05d0829317c0).