---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security/prepare-clusters-for-networking-and-security.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Prepare ESX cluster Hosts for Networking and Security
---

# Prepare ESX cluster Hosts for Networking and Security

Use the Quick Start wizard to prepare ESX clusters for networking and security using NSX recommended host configurations.

- Register vCenter as a compute manager in NSX.
- Configure ESX cluster hosts member of VDS in vCenter with correct uplinks.
- (Optional) If you are using VLAN for VTEP pool, configue IP Pool for Host VTEP assignment and Uplink Profile using the TEP VLAN.

The Quick Start wizard helps you finish installation with minimum user input, thus, simplifying the installation process. By default, VLAN networking is the default selection in the wizard.

Based on the type of host, the quick start wizard considers the following default configurations:

- ESX hosts running 7.0 and later are prepared on the VDS switch. Configure the desired number of uplinks on the VDS switch in vCenter and set the MTU to 1700.

Each host switch is assigned an auto-created transport zone, uplink profile, and transport node profile.

After preparing ESX clusters for networking and security, you can activate NSX on them. For more information about activating NSX, see [Activate NSX on Distributed Switch](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security/activate-distributed-security-for-vds.html#GUID-bfdb4909-b7a5-471b-b047-6f6e63d6932e-en_GUID-BBEABA82-10D8-4A9E-9AC9-797DC233A3C1).

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Navigate to .
3. On the Prepare Clusters for Networking and Security
   card, click Get Started.
4. Select the clusters you want to prepare for NSX networking.
5. Click Install
   NSX and then select Networking and
   Security.
6. Depending on your requirement, you can prepare the same cluster for both VLAN
   and Overlay networking or for one type of networking. With Overlay networking,
   each host switch is added with a TEP IP address, which is required for overlay
   networking.

   ![Prepare cluster for VLAN and Overlay networking](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/99cd848b-6db4-4e61-869a-c3d039633fd5.original.png)
7. View the NSX recommended Host Switch
   configuration.

   However, you can customize the settings for the cluster, even though it is an
   optional step.

   A dotted line
   originating from a switch to a physical NIC indicates that it is an
   existing configuration on the host switch, which will be replaced by a
   firm line going to the same physical NIC.
8. Even
   though NSX provides
   recommendations, you can still customize the configuration. To customize the
   host switch, select the switch and change the recommended configuration.
   1. IP
      Assignment: Is applicable if overlay is selected for the
      host switch. Choose IP assignment type to be DHCP or a pre-created IP
      Pool for the overlay VTEP Pool.
   2. VDS: Select the VDS switch as the host
      switch.
   3. Transport
      Zone: Select a different transport zone that you want
      the host to be associated with.
   4. Uplink
      Profile: If needed, select a different uplink profile in
      place of the recommended uplink profile.

      If you configure
      two VDS switches with the same configuration, the wizard recommends
      the same uplink profile for both the switches.
   5. Uplink to
      Physical NIC mapping: On a VDS switch, all uplinks
      configured on the VDS switch are mapped to the uplinks in NSX.

      A change to host switch type or uplink to vmnic mapping is
      reflected in the Host Switch Configuration network
      representation.
9. Click
   Install.

   View the progress of installation
   on the Prepare Clusters for Networking and Security
   card. If installation on any of the host fails, retry installation by
   resolving the error.
10. To view successfully prepared
    hosts, go to .

The transport nodes are ready for VLAN and Overlay networking.