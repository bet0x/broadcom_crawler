---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/redeploy-an-nsx-edge-vm-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Redeploy an NSX Edge Node
---

# Redeploy an NSX Edge Node

You might want to redeploy an NSX Edge node when you experience problems with the node or want to change node configuration settings that are unavailable in edit mode.

**What Happens When You Redeploy an Edge Node**

The redeployment workflow performs the following operations:

1. Places the existing edge node in maintenance mode and then powers off the edge node.
2. Deletes the existing edge node VM.
3. Deploys a new edge node VM with the configuration settings that you specified.

The placement of the existing gateway and services on the node remain unchanged.

If the NSX Edge node is redeployed, the new node is upgraded to a VM hardware version compatible with the ESX host version. After redeploying an edge node, check all the other nodes in that edge cluster to ensure that VM hardware versions are consistent. VM hardware versions compatible with ESX hosts are listed in Knowledge Base article 312100: [ESX hosts and compatible virtual machine hardware versions list](https://knowledge.broadcom.com/external/article?articleNumber=312100).

All logs collected for an existing NSX Edge node are deleted when you redeploy the node. It is recommended that you generate and download the support bundle for the node before starting the redeployment workflow.

**Redeployment Methods**

You can redeploy an edge node using either the NSX Manager UI or the [NSX API](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/). Use the appropriate method:

- To redeploy a VM node that was auto-deployed through NSX Manager, use the NSX Manager UI or the API.
- To redeploy a node that was manually deployed through vSphere Client, use the API.

## Prerequisites

- Ensure that the node shows Success as its Configuration State.
- Ensure connectivity between the NSX Edge node and NSX Manager is down if the existing NSX Edge node was manually deployed through vSphere Client. If connectivity is Up, then NSX does not allow the existing NSX Edge node to be replaced with a new one.
- If possible, collect the support bundle for the node.

## Redeploy an NSX Edge Node Using the NSX Manager UI

This redeployment method is supported for NSX Edge VM nodes that were auto-deployed through NSX Manager.

1. From a browser, log in with admin privileges to NSX Manager.
2. Select System > Fabric > Nodes > Edge Transport Nodes.
3. In the list, select the edge node that you want to redeploy.
4. Select Actions > Redeploy Edge to open the Redeploy Edge Node workflow.

   The Redeploy Edge Node workflow is identical to the Add Edge Node workflow that was originally used to auto-deploy the node. The editable fields in the Redeploy Edge Node workflow are pre-filled with the existing configuration settings of the node. You can modify these settings as needed.
5. Proceed through the workflow steps and either accept the existing settings or modify the settings as needed. See [Create an NSX Edge Transport Node](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-transport-node.html) for detailed information on each configuration setting.

   You must reenter the CLI credentials for the node VM, as the Credentials fields are left blank for security. Also, do not modify the Compute Manager setting unless you intend to change the compute manager for the node. Once you modify the setting, the configuration mappings associated with the original compute manager are cleared and cannot be retrieved, even if you re-select the original compute manager.
6. After finishing the Redeploy Edge Node workflow, allow the node redeployment to proceed and reach completion.
7. Verify the node configuration status and connection status on the Edge Transport Nodes page. Alternatively, you can verify the transport node status by running the Get edge-cluster-status | get managers | get controllers | get host-switch CLI command.
8. Perform the postrequisites described later on this page.

## Redeploy an NSX Edge Node Using the API

Redeployment through the API is recommended in the following scenarios:

- You need to recover an NSX Edge node that has been lost due to storage corruption.
- You need to change the node's form factor by scaling up or down, upgrade the hardware version, or update management connectivity.
- You need to convert a manually deployed edge node to a system-managed node.

1. (NSX Edge node manually deployed through vSphere Client) Open an SSH session and connect to the NSX Edge console.
2. Verify the logical routes configured on the NSX Edge node through the CLI console, get logical-routers.
3. Power off NSX Edge node.
4. Verify that the NSX Edge node is disconnected from NSX Manager by running the API command:

   GET api/v1/transport-nodes/<edgenode>/state

   1. If the node\_deployment\_state value is MPA Disconnected, you can proceed to redeploy the NSX Edge node.
   2. If node\_deployment\_state is Node Ready, NSX Manager displays an error 78006 - Manager connectivity to Edge node must be down. Else replacement/redeployment of hardware is not allowed.
5. Alternatively, view the state of connectivity between NSX Edge node and NSX Manager from the Edge Transport Node page. A disconnected NSX Edge node displays the following system message, Configuration Error, Edge VM MPA Connectivity is down.
6. Retrieve the placement parameters and management network settings for the node.
   1. For an auto-deployed node, run GET /<NSX-Manager-IPaddress>/api/v1/transport-nodes/<edgenode>. Copy the output payload of this API.

      ```
      "resource_type": "EdgeNode",
                 "id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
                 "display_name": "Edge_TN2",
                 "description": "EN",
                 "external_id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
                 "ip_addresses": [
                     "10.170.94.240"
                 ],
                 "_create_user": "admin",
                 "_create_time": 1600106319056,
                 "_last_modified_user": "admin",
                 "_last_modified_time": 1600106907312,
                 "_system_owned": false,
                 "_protection": "NOT_PROTECTED",
                 "_revision": 2
             },
             "is_overridden": false,
             "failure_domain_id": "4fc1e3b0-1cd4-4339-86c8-f76baddbaafb",
             "resource_type": "TransportNode",
             "id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
             "display_name": "Edge_TN2",
             "_create_user": "admin",
             "_create_time": 1600106319399,
             "_last_modified_user": "admin",
             "_last_modified_time": 1600106907401,
             "_system_owned": false,
             "_protection": "NOT_PROTECTED",
             "_revision": 1
         }
      ```
   2. For a manually deployed node, retrieve the placement parameters and management network settings from vCenter.
7. You can choose from one of these redeployment scenarios:

   | Choice | Actions |
   | --- | --- |
   | Redeploy a manually deployed NSX Edge node with a system-managed NSX Edge node (deployed through NSX Manager API) | Perform the following in the API command, /api/v1/transport-nodes/<transport-node-id>?action=redeploy  - Paste the payload in the body of the redeploy API. - Verify the deployment\_config section references the compute manager, datstore, and network details, where you want to redeploy the node. Ensure these values are consistent with the values used in the node\_settings section. - Add login passwords in the deployment\_config section.  NSX Manager redeploys the NSX Edge node based on the details provided in the deployment\_config section. |
   | Change the placement of the existing NSX Edge node | Perform the following in the API command, /api/v1/transport-nodes/<transport-node-id>?action=redeploy  - Paste the payload in the body of the redeploy API. - In the deployment\_config section, reference the new compute manager, datastore, network, CPU, memory, or latency sensitivity details. Confirm the VLAN and MTU configuration on the new cluster and host. |

   An example of the payload for POST https://<manager-ip>/api/v1/transport-nodes/<transport-node-id>?action=redeploy:

   ```
      {
          "node_id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
          "host_switch_spec": {
              "host_switches": [
                  {
                      "host_switch_name": "nsxvswitch_overlay",
                      "host_switch_id": "c0a4a83e-c8b8-4324-a4d7-dbbc07b30b53",
                      "host_switch_type": "NVDS",
                      "host_switch_mode": "STANDARD",
                      "host_switch_profile_ids": [
                          {
                              "key": "UplinkHostSwitchProfile",
                              "value": "f9a2a2fa-b49d-498f-abaf-2fdc81917716"
                          },
                          {
                              "key": "LldpHostSwitchProfile",
                              "value": "9e0b4d2d-d155-4b4b-8947-fbfe5b79f7cb"
                          }
                      ],
                      "pnics": [
                          {
                              "device_name": "fp-eth0",
                              "uplink_name": "uplink1"
                          }
                      ],
                      "is_migrate_pnics": false,
                      "ip_assignment_spec": {
                          "ip_pool_id": "647d9b0d-0143-4903-91f5-930d9ab011e8",
                          "resource_type": "StaticIpPoolSpec"
                      },
                      "cpu_config": [],
                      "transport_zone_endpoints": [
                          {
                              "transport_zone_id": "0b33b078-6438-4d9b-a1ec-33211fd36822",
                              "transport_zone_profile_ids": [
                                  {
                                      "resource_type": "BfdHealthMonitoringProfile",
                                      "profile_id": "52035bb3-ab02-4a08-9884-18631312e50a"
                                  }
                              ]
                          },
                          {
                              "transport_zone_id": "a0133574-48de-4e3a-9407-7db1a68bae41",
                              "transport_zone_profile_ids": [
                                  {
                                      "resource_type": "BfdHealthMonitoringProfile",
                                      "profile_id": "52035bb3-ab02-4a08-9884-18631312e50a"
                                  }
                              ]
                          }
                      ],
                      "vmk_install_migration": [],
                      "pnics_uninstall_migration": [],
                      "vmk_uninstall_migration": [],
                      "not_ready": false
                  }
              ],
              "resource_type": "StandardHostSwitchSpec"
          },
          "transport_zone_endpoints": [],
          "maintenance_mode": "DISABLED",
          "node_deployment_info": {
              "deployment_type": "VIRTUAL_MACHINE",
              "deployment_config": {
                  "vm_deployment_config": {
                      "vc_id": "cc82da39-b119-4869-a7fe-a54621cb4d3d",
                      "compute_id": "domain-c9",
                      "storage_id": "datastore-14",
                      "host_id": "host-12",
                      "compute_folder_id": "group-v5",
                      "management_network_id": "network-16",
                      "hostname": "EdgeSmallFactor",
                      "data_network_ids": [
                          "5638c577-e142-4a50-aed3-a7079dc3b08c",
                          "5638c577-e142-4a50-aed3-a7079dc3b08c",
                          "5638c577-e142-4a50-aed3-a7079dc3b08c"
                      ],
                      "search_domains": [
                          "eng.vmware.com",
                          "vmware.com"
                      ],
                      "enable_ssh": true,
                      "allow_ssh_root_login": true,
                      "reservation_info": {
                          "memory_reservation": {
                              "reservation_percentage": 100
                          },
                          "cpu_reservation": {
                              "reservation_in_shares": "HIGH_PRIORITY",
                              "reservation_in_mhz": 0
                          }
                      },
                      "resource_allocation": {
                          "cpu_count": 4,
                          "memory_allocation_in_mb": 8192
                      },
                      "placement_type": "VsphereDeploymentConfig"
                  },
                  "form_factor": "MEDIUM",
                  "node_user_settings": {
                       "cli_username": "admin",
                          "root_password":"Admin!23Admin",
                          "cli_password":"Admin!23Admin"
                  }
              },
              "node_settings": {
                  "hostname": "EdgeSmallFactor",
                  "search_domains": [
                      "eng.vmware.com",
                      "vmware.com"
                  ],
                  "enable_ssh": true,
                  "allow_ssh_root_login": true
              },
              "resource_type": "EdgeNode",
              "id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
              "display_name": "Edge_TN2",
              "description": "EN",
              "external_id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
              "ip_addresses": [
                  "10.170.94.240"
              ],
              "_create_user": "admin",
              "_create_time": 1600106319056,
              "_last_modified_user": "admin",
              "_last_modified_time": 1600106907312,
              "_system_owned": false,
              "_protection": "NOT_PROTECTED",
              "_revision": 2
          },
          "is_overridden": false,
          "failure_domain_id": "4fc1e3b0-1cd4-4339-86c8-f76baddbaafb",
          "resource_type": "TransportNode",
          "id": "9f34c0ea-4aac-4b7f-a02c-62f306f96649",
          "display_name": "Edge_TN2",
          "_create_user": "admin",
          "_create_time": 1600106319399,
          "_last_modified_user": "admin",
          "_last_modified_time": 1600106907401,
          "_system_owned": false,
          "_protection": "NOT_PROTECTED",
          "_revision": 1
      }
   ```

   If the old node is an NSX Edge node auto-deployed through NSX Manager UI, then you do not need to provide login credentials in the node\_user\_settings section in the API payload. For more information on the payload details, see the [NSX API Guide](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/).
8. In NSX Manager, verify the Configuration Status of the new NSX Edge node.
9. Alternatively, verify the status of the newly prepared NSX Edge node by running the API command, Get api/v1/transport-nodes/<node-id>/state.
10. Verify logical router configurations are migrated to the new NSX Edge node, by running the get logical-routers CLI command.
11. Verify the TEP address remain same on the replaced NSX Edge node.
12. Verify NSX Edge cluster status is Up. API is GET api/v1/edge-clusters/<cluster>. If NSX is configured to use NSX Federation, verify the intersite status us Up.
13. Check NSX Edge node and cluster state API to verify status is Up.
14. Troubleshoot error messages if needed:
    1. (78006) NSX Manager connectivity to Edge node must be down. Else replacement of hardware is not allowed: Ensure NSX Edge node is not connected to NSX Manager.
    2. (16064) Deployment configuration is missing: In the redeploy API, enter details for the deployment\_config section.
    3. (16066) Login password is missing: Provide login credentials.
    4. (15019) Insufficient resources on node to be allocated to load balancer pool: The form factor size of the new NSX Edge node might be smaller than the form factor of the old NSX Edge node. The new form factor might not have enough resources to be allocated to load balancer pool.
15. Perform the postrequisites described in the next section.

## Postrequisites

- If you want to bring up a replaced node VM as part of your network, ensure that the replaced node is disconnected from the network. Then, run del nsx to completely delete NSX VIBs on the node. After you run del nsx on the host, old entries of logical routers, VTEP IP addresses, uplink IP addresses are released.

- Check the redeployed node and all the other nodes in that edge cluster to ensure that their VM hardware versions are consistent.
- After you redeploy a NSX Edge node, several security parameters are set to their default values. Reconfigure these parameters based on your environment.
  - set auth-policy minimum-password-length <password-length-arg>

    Set the minimum number of characters that passwords must have. The smallest value that can be set is 8

    For example, nsx> set auth-policy minimum-password-length 12
  - set user <node-username> password-expiration <password-expiration-arg>

    Set number of days the user's password is valid after a password change.

    Where, <username> is the Username of user,

    <password-expiration> is the number of days password valid after change (1 - 9999)

    For example, nsx> set user audit password-expiration 120
  - set auth-policy cli max-auth-failures <auth-failures-arg>

    Set the number of failed CLI authentication attempts that are allowed before the account is locked. If set to 0, account lockout is disabled.

    Where, <auth-failures> is the number of authentication failures to trigger lockout

    For example, nsx> set auth-policy cli max-auth-failures 5
  - set banner

    Set the security banner or message of the day.

    For example, nsx> set banner

    Enter TEXT message. End with 'Ctrl-D'
  - reset dataplane hugepage

    Reset the hugepage-related boot time option to factory default.

    For example

    nsx-edge-1> reset dataplane hugepage

    ```
    0000:0b:00.0 already bound to driver vfio-pci, skipping
    0000:1b:00.0 already bound to driver vfio-pci, skipping
    0000:13:00.0 already bound to driver vfio-pci, skipping
    INFO: Config was written to: /config/vmware/edge/config.json
    Generating grub configuration file ...
    Found linux image: /vmlinuz-3.14.17-nn4-server
    Found initrd image: //initrd.img-3.14.17-nn4-server
    File descriptor 4 (/tmp/ffinvYglp (deleted)) leaked on lvs invocation. Parent PID 32203: /bin/sh
    done
    INFO: Updated grub. Please reboot to take effect.
    ```