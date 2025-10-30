---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/configure-an-esxi-host-transport-node-with-link-aggregation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an ESX Host Transport Node with Link Aggregation Group
---

# Configure an ESX Host Transport Node with Link Aggregation Group

This procedure describes how to create an uplink profile that has a link aggregation group configured and how to configure an ESX host transport node to use that uplink profile.

- Familiarize yourself with the steps to create an uplink profile. See [Create an Uplink Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html).
- Familiarize yourself with the steps to create a host transport node.
- For ESX hosts (connecting to VDS), the LAG configuration is only in vCenter, on the VDS. Therefore configure LAG on the VDS switch in vCenter.

1. From a browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricProfilesUplink ProfilesAdd Profile.
3. Enter a name and optionally a description.

   For example, you enter the name uplink-lag1.
4. Under Teamings, select Default Teaming.
5. In the Active Uplinks field, do one of the following:
   1. Enter the name of the LAG that you configured on the VDS switch in vCenter.
6. Enter the VLAN ID for Transport VLAN.
7. Click Add at the bottom of the dialog box.
8. Select SystemFabricHosts.
9. Select the Cluster tab and select an ESX host.
10. Select Configure NSX.
11. In the Host Details  tab, enter IP address, OS name, admin credentials, and SHA-256 thumbprint of the host.
12. During the switch configuration, depending on the VDS switch, select the uplink profile uplink-lag1 that was created in step 3.
13. In the Physical NICs field, the physical NICs and uplinks dropdown list reflects the new NICs and uplink profile. Specifically, the uplink LAG that is configured on the VDS switch is displayed in the uplink profile drop-down list. Select the VDS uplink for LAG.
14. Enter information for the other fields and complete host preparation.

    The ESX host is prepared as a transport node using the LAG profile.

    You can only use LAGs that you define in NSX uplink profile for transport nodes that are prepared using N-VDS. However, for ESX transport nodes prepared using VDS, you can only use LAGs configured on vSphere and it is referred to in the uplink profile.
15. SSH in to ESX host as root and run the following commands:
    1. Run nsxcli.
    2. To verify LACP bond is up and active, run get bonds.