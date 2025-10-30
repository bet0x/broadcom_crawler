---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/preparing-esxi-hosts-as-transport-nodes/verify-the-transport-node-status.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Verify the Transport Node Status
---

# Verify the Transport Node Status

Verify the transport node is created and VDS configured successfully.

1. Log in to the NSX Manager UI.
2. Navigate to SystemFabricHosts page.
3. To view the host and VDS status, navigate to Host DetailsOverview tab.
4. Verify host controller connectivity and manager connectivity is UP.
5. Navigate to the Transport Node page and view the VDS status.
6. To view active manager node for this transport node, run nsxcli -c get managers \*.
7. To view the master controller with 'connected' status and session state up for this transport node, run nsxcli -c get controllers.
8. Alternatively, view the VDS on ESX with the esxcli network ip interface list command. 

   On ESX, verify correct number of vmk interfaces are configured with a VDS name that matches the name you used when you configured the transport zone and the transport node.

   ```
   # esxcli network ip interface list
   ...

   vmk10
      Name: vmk10
      MAC Address: 00:50:56:64:63:4c
      Enabled: true
      Portset: DvsPortset-1
      Portgroup: N/A
      Netstack Instance: vxlan
      VDS Name: overlay-hostswitch
      VDS UUID: 18 ae 54 04 2c 6f 46 21-b8 ae ef ff 01 0c aa c2
      VDS Port: 10
      VDS Connection: 10
      Opaque Network ID: N/A
      Opaque Network Type: N/A
      External ID: N/A
      MTU: 1700
      TSO MSS: 65535
      Port ID: 67108895

    ...
   ```

   If you are using the vSphere Client, you can view the installed VDS in the UI by selecting host ConfigurationNetwork Adapters.
9. Check the transport node's assigned tunnel endpoint address.

   The vmk10 interface receives an IP address from the NSX IP pool or DHCP, as shown here:

   ```
   # esxcli network ip interface ipv4 get
   Name   IPv4 Address    IPv4 Netmask   IPv4 Broadcast   Address Type  DHCP DNS
   -----  --------------  -------------  ---------------  ------------  --------
   vmk0   192.168.210.53  255.255.255.0  192.168.210.255  STATIC           false
   vmk1   10.20.20.53     255.255.255.0  10.20.20.255     STATIC           false
   vmk10  192.168.250.3   255.255.255.0  192.168.250.255  STATIC           false
   ```
10. Check the API for transport node state information.

    Call the (deprecated API) GET https://<nsx-mgr>/api/v1/transport-nodes/<transport-node-id>/state API call.

    Or call the GET /policy/api/v1/infra/sites/<site-id>/enforcement-points/<enforcement-point-id>/transport-node-status-report, where the default value for <site-id> and <enforcement-point-id> is default.

    For example:

    ```
    { "transport_node_id": "55120a1a-51c6-4c20-b4a3-6f59662c9f6a", "host_switch_states": 
     [ { "host_switch_id": "50 21 0c 52 94 22 aa 20-b7 f0 0b da 1c 7c 29 ea", "host_switch_name": "dvs1", 
     "endpoints": [ { "device_name": "vmk10", "ip": "172.16.223.175", "default_gateway": "", "subnet_mask": "255.255.224.0", "label": 53249 } ],
     "transport_zone_ids": [ "1b3a2f36-bfd1-443e-a0f6-4de01abc963e" ], "host_switch_type": "VDS" } ],
     "maintenance_mode_state": "DISABLED", 
     "node_deployment_state": { "state": "success", "details": [] }, "deployment_progress_state": { "progress": 100, "current_step_title": "Configuration complete" }, 
     "state": "success",
     "details": [ { "sub_system_id": "55120a1a-51c6-4c20-b4a3-6f59662c9f6a",
     "sub_system_type": "HostConfig", "state": "success" }, 
     { "sub_system_id": "55120a1a-51c6-4c20-b4a3-6f59662c9f6a", "sub_system_type": "AppInit", "state": "success" },
     { "sub_system_id": "55120a1a-51c6-4c20-b4a3-6f59662c9f6a", "sub_system_type": "LogicalSwitchFullSync", 
     "state": "success" } ] }
    ```