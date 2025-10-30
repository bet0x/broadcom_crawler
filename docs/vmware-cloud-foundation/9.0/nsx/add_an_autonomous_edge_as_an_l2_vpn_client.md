---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-an-autonomous-edge-as-an-l2-vpn-client.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an Autonomous Edge as an L2 VPN Client
---

# Add an Autonomous Edge as an L2 VPN Client

You can use L2 VPN to extend your Layer 2 networks to a site that is not managed by
NSX. An autonomous
NSX Edge, also referred to as
NSX Edge for VMware ESX, can be deployed on the site,
as an L2 VPN client. The autonomous for VMware NSX Edge is simple to deploy, easily programmable, and provides
high-performance VPN. The autonomous NSX Edge
is deployed using an OVF file on a host that is not managed by NSX. You can also enable high
availability (HA) for VPN redundancy by deploying primary and secondary autonomous Edge L2
VPN clients.

- Create a port group and bind it to
  the vSwitch on your host. Ensure that this port group accepts promiscuous mode
  and forged transmits from the port group's security settings. For instructions,
  see [Configure an NSX Edge Uplink Port in ESX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/configure-an-edge-uplink-port-in-esxi.html).
- Create a port group for your
  internal L2 extension port.
- Obtain the IP addresses for the
  local IP and remote IP to use with the L2 VPN client session you are adding.
- Obtain the peer code that was
  generated during the L2 VPN server configuration.

1. Using vSphere Client, log in to
   the vCenter that
   manages the non-NSX environment.
2. Select Hosts and Clusters and expand clusters to show
   the available hosts.
3. Right-click the host where you
   want to install the autonomous NSX Edge and select Deploy OVF Template.
4. Enter the URL to download, <https://support.broadcom.com/group/ecx/downloads>, select
   the version, and click Download Now to install the NSX Edge for VMware ESX OVA file from the Internet or click
   Browse to locate the folder on your computer that
   contains the autonomous NSX Edge
   for VMware ESX file and click
   Next. 

   This appliance can be used for
   both autonomous and managed Edges.
5. On the Select name
   and folder page, enter a name for the autonomous NSX Edge and select the folder or data
   center where you want to deploy. Then click Next.
6. On the Select a
   compute resource page, select the destination of the compute
   resource.
7. On the OVF Template Details
   page, review the template details and click Next.
8. On the Configuration page, select a deployment
   configuration option.
9. On the Select storage page, select the location to store
   the files for the configuration and disk files.
10. On the Select
    networks page, configure the networks that the deployed template
    must use. Select the port group you created for the uplink interface, the port
    group that you created for the L2 extension port, and enter an HA interface.
    Click Next.
11. On the Customize
    Template page, enter the following values and click
    Next.

    1. Type and retype the CLI
       admin password.
    2. Type and retype the CLI
       enable password.
    3. Type and retype the CLI
       root password.
    4. Enter the IPv4 address for
       the Management Network.
    5. Enable the option to deploy
       an autonomous Edge.
    6. Enter the
       External Port details for VLAN ID, exit
       interface, IP address, and IP prefix length such that the exit interface
       maps to the Network with the port group of your uplink interface.

       If the exit interface is
       connected to a trunk port group, specify a VLAN ID. For example,
       20,eth2,192.168.5.1,24. You can also
       configure your port group with a VLAN ID and use VLAN 0 for the
       External Port.
    7. To
       configure High Availability, enter the HA Port
       details where the exit interface maps to the appropriate HA
       Network.
    8. When
       deploying an autonomous NSX Edge as a secondary node for HA, select
       Deploy this autonomous-edge as a secondary
       node.

       Use
       the same OVF file as the primary node and enter the primary node's
       IP address, user name, password, and thumbprint.

       To retrieve the
       thumbprint of the primary node, log in to the primary node and run
       the following
       command:

       ```
        get certificate api thumbprint
       ```

       Ensure that the VTEP IP
       addresses of the primary and secondary nodes are in the same subnet
       and that they connect to the same port group. When you complete the
       deployment and start the secondary-edge, it connects to the primary
       node to form an edge-cluster .
12. On the Ready to
    complete page, review the autonomous Edge settings and click
    Finish. 

    If there are errors during
    the deployment, a message of the day is displayed on the CLI. You can also
    use an API call to check for errors:

    ```
    GET https://<nsx-mgr>/api/v1/node/status
    ```

    The
    errors are categorized as soft errors and hard errors. Use API calls to
    resolve the soft errors as required. You can clear the message of day using
    an API
    call:

    ```
    POST /api/v1/node/status?action=clear_bootup_error
    ```
13. Power on the autonomous
    NSX Edge appliance using the
    vSphere Client. Open the console of the NSX Edge node to track the boot process
    using Launch Remote Console.
14. After the NSX Edge starts, log in to the Edge node
    using the console or SSH (provided SSH is enabled at the time of install) with
    admin credentials. 

    After the NSX Edge node starts, if you do not
    log in with admin credentials for the first time, the data plane service
    does not automatically start on the NSX Edge node.
15. Select L2VPNAdd Session and enter the following values:

    1. Enter a session name.
    2. Enter the local IP address
       and the remote IP address.
    3. Enter the peer code from
       the L2VPN server. See [Download the Remote Side L2 VPN Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/download-the-remote-side-l2-vpn-configuration.html) for details on
       obtaining the peer code.
16. Click Save.
17. Select PortAdd Port to create an L2 extension port.
18. Enter a name, a VLAN, and select
    an exit interface.
19. Click Save.
20. Select L2VPNAttach Port and enter the following values:

    1. Select the L2 VPN session
       that you created.
    2. Select the L2 extension
       port that you created.
    3. Enter a tunnel ID.
21. Click Attach.

    You can create additional L2 extension ports and attach them to the session if
    you need to extend multiple L2 networks.
22. Use the browser to log in to the
    autonomous NSX Edge or use API
    calls to view the status of the L2VPN session.

    If the L2VPN server
    configuration changes, ensure that you download the peer code again and
    update the session with the new peer code.