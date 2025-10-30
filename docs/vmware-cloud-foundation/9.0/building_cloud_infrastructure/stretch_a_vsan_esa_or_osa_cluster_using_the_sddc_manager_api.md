---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/stretch-a-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Stretch a vSAN ESA or OSA Cluster Using the SDDC Manager API
---

# Stretch a vSAN ESA or OSA Cluster Using the SDDC Manager API

You can stretch a vSAN cluster (ESA or OSA) in the management domain or workload domain using a JSON specification and the SDDC Manager API.

- See [vSAN Stretched HCI Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/stretched-vsan-storage-model.html) for design requirements and recommendations.
- Verify that vCenter is operational.
- Verify that you have completed the Planning and Preparation Workbook with the management domain or workload domain deployment option included.
- Verify that your environment meets the requirements listed in the Prerequisite Checklist sheet in the Planning and Preparation Workbook.
- Create a network pool for availability zone 2.
- Commission vSAN ESA or OSA hosts for availability zone 2. See [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html#GUID-2fcdd4bd-0a02-4121-a6ac-b13498b1406d-en).
- Ensure that you have enough hosts such that there is an equal number of hosts on each availability zone. This is to ensure that there are sufficient resources in case an availability zone goes down completely.
- Deploy and configure a vSAN witness host. See [Deploy and Configure vSAN Witness Host](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host.html#GUID-7419ffc7-0d3f-4ddc-975b-92ae4582189e-en).
- If you are stretching a cluster in a workload domain, the default management vSphere cluster must already be stretched.

You cannot stretch a cluster in the following cases:

- The cluster shares a vSAN Storage Policy with any other clusters.
- The cluster includes DPU-backed hosts.
- The cluster includes hosts from different subnets or networks (L3).

When you stretch a cluster, SDDC Manager modifies the site disaster tolerance setting for storage policy associated with datastore of that cluster from None - standard cluster to Site mirroring - stretched cluster. This affects all VMs using default datastore policy in that cluster. If you do not want to change the site disaster tolerance setting for specific VMs, apply a different storage policy to those VMs before stretching the cluster.

1. Create a JSON specification file in a text editor.

   The following example is for an environment with a single vSphere Distributed Switch. If you have multiple vSphere Distributed Switches, see the [SDDC Manager API Reference Guide](https://developer.broadcom.com/xapis/vmware-cloud-foundation-api/latest/clusters/#_usecase_stretchCluster) for details about creating a JSON specification.

   The ESX hosts that you are adding to availability zone 2 must use the same vmnic to vSphere Distributed Switch mapping as the existing hosts in availability zone 1.

   ```
   {
     "clusterStretchSpec": {
       "deployWithoutLicenseKeys": true,
       "hostSpecs": [
         {
           "id": "<ESX host 1 ID>",
           "hostname": "sfo02-m01-r01-esx01.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-m01-r01-network-profile01",
             "vmNics": [
               {
                 "id": "vmnic0",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic1",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink2"
               }
             ]
           }
         },
         {
           "id": "<ESX host 2 ID>",
           "hostname": "sfo02-m01-r01-esx02.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-m01-r01-network-profile01",
             "vmNics": [
               {
                 "id": "vmnic0",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic1",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink2"
               }
             ]
           }
         },
         {
           "id": "<ESX host 3 ID>",
           "hostname": "sfo02-m01-r01-esx03.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-m01-r01-network-profile01",
             "vmNics": [
               {
                 "id": "vmnic0",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic1",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink2"
               }
             ]
           }
         },
         {
           "id": "<ESX host 4 ID>",
           "hostname": "sfo02-m01-r01-esx04.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-m01-r01-network-profile01",
             "vmNics": [
               {
                 "id": "vmnic0",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic1",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "uplink": "uplink2"
               }
             ]
           }
         }
       ],
       "networkSpec": {
         "networkProfiles": [
           {
             "isDefault": true,
             "name": "sfo02-m01-r01-network-profile01",
             "nsxtHostSwitchConfigs": [
               {
                 "ipAddressPoolName": "sfo02-m01-r01-ip-pool01-host",
                 "uplinkProfileName": "sfo02-m01-r01-uplink-profile01",
                 "vdsName": "sfo-m01-cl01-vds01",
                 "vdsUplinkToNsxUplink": [
                   {
                     "nsxUplinkName": "uplink1",
                     "vdsUplinkName": "uplink1"
                   },
                   {
                     "nsxUplinkName": "uplink2",
                     "vdsUplinkName": "uplink2"
                   }
                 ]
               }
             ]
           }
         ],
         "nsxClusterSpec": {
           "ipAddressPoolsSpec": [
             {
               "name": "sfo02-m01-r01-ip-pool01-host",
               "subnets": [
                 {
                   "cidr": "10.12.14.0/24",
                   "gateway": "10.12.14.1",
                   "ipAddressPoolRanges": [
                     {
                       "start": "10.12.14.101",
                       "end": "10.12.14.132"
                     }
                   ]
                 }
               ]
             }
           ],
           "uplinkProfiles": [
             {
               "name": "sfo02-m01-r01-uplink-profile01",
               "transportVlan": 1214,
               "teamings": [
                 {
                   "name": "DEFAULT",
                   "policy": "LOADBALANCE_SRCID",
                   "standByUplinks": [],
                   "activeUplinks": [
                     "uplink1",
                     "uplink2"
                   ]
                 }
               ]
             }
           ]
         }
       },
       "isEdgeClusterConfiguredForMultiAZ": true,
       "witnessSpec": {
         "fqdn": "sfo-m01-cl01-vsw01.sfo.rainpole.io",
         "vsanCidr": "10.21.10.0/24",
         "vsanIp": "10.21.10.218"
       },
       "witnessTrafficSharedWithVsanTraffic": false
     }
   }
   ```

   Replace the example values in the JSON file with the correct values for your environment.

   isEdgeClusterConfiguredForMultiAZ should be set to "true" if the cluster hosts an NSX Edge cluster and "false" if the cluster does not host an NSX Edge cluster.
2. Log in to VCF Operations.
3. In the navigation pane, click Developer CenterAPIs & SDKs.
4. Click the API Explorer link on the SDDC Manager API.
5. Click the VCF Instance which contains the cluster you want to stretch.
6. Retrieve and replace the unique IDs for each ESX host in the JSON specification file.
   1. Navigate to HostsGET /v1/hosts.
   2. In the Status text box, enter UNASSIGNED\_USEABLE and click Execute.
   3. In the Response section, click PageOfHost, copy the id element of each host, and replace the respective value in the JSON specification file.

      | ESX Host | Value |
      | --- | --- |
      | ESX Host 1 | ESX host 1 ID |
      | ESX Host 2 | ESX host 2 ID |
      | ESX Host 3 | ESX host 3 ID |
      | ESX Host 4 | ESX host 4 ID |
7. Retrieve the unique ID for the cluster you want to stretch.
   1. Navigate to ClustersGET /v1/clusters.
   2. Click Execute.
   3. In the Response section, click PageOfCluster, copy the id element of the cluster.

      You will need the cluster ID for subsequent steps.
8. Validate the JSON specification file.
   1. Navigate to ClustersPOST /v1/clusters/{id}/validations .
   2. In the Value text box, enter the unique ID for the cluster that you retrieved in step 5.
   3. In the clusterUpdateSpec text box, type 

      ```
      {
      "clusterUpdateSpec":
      }
      ```
   4. Paste the JSON specification.

      For example:

      ```
      {
      "clusterUpdateSpec": {
      "clusterStretchSpec": {
      "hostSpecs": [
      {
      "hostname": "sfo02-w01-esx01.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 1 ID>"
      },
      {
      "hostname": "sfo02-w01-esx02.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 2 ID>"
      },
      {
      "hostname": "sfo02-w01-esx03.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 3 ID>"
      },
      {
      "hostname": "sfo02-w01-esx04.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 4 ID>"
      }
      ],
      "isEdgeClusterConfiguredForMultiAZ": "true",
      "networkSpec": {
      "networkProfiles": [
      {
      "isDefault": false,
      "name": "sfo-w01-az2-nsx-np01",
      "nsxtHostSwitchConfigs": [
      {
      "ipAddressPoolName": "sfo-w01-az2-host-ip-pool01",
      "uplinkProfileName": "sfo-w01-az2-host-uplink-profile01",
      "vdsName": "sfo-w01-cl01-vds01",
      "vdsUplinkToNsxUplink": [
       {
        "nsxUplinkName": "uplink-1",
        "vdsUplinkName": "uplink1"
       },
       {
        "nsxUplinkName": "uplink-2",
        "vdsUplinkName": "uplink2"
       }
      ]
      }
      ]
      }
      ],
      "nsxClusterSpec": {
      "ipAddressPoolsSpec": [
      {
      "description": "WLD01 AZ2 Host TEP Pool",
      "name": "sfo-w01-az2-host-ip-pool01",
      "subnets": [
      {
       "cidr": "172.16.44.0/24",
       "gateway": "172.16.44.253",
       "ipAddressPoolRanges": [
        {
         "end": "172.16.44.200",
         "start": "172.16.44.10"
        }
       ]
      }
      ]
      }
      ],
      "uplinkProfiles": [
      {
      "name": "sfo-w01-az2-host-uplink-profile01",
      "teamings": [
      {
       "activeUplinks": [
        "uplink-1",
        "uplink-2"
       ],
       "name": "DEFAULT",
       "policy": "LOADBALANCE_SRCID",
       "standByUplinks": []
      }
      ],
      "transportVlan": 1644
      }
      ]
      }
      },
      "witnessSpec": {
      "fqdn": "sfo-w01-cl01-vsw01.sfo.rainpole.io",
      "vsanCidr": "172.17.11.0/24",
      "vsanIp": "172.17.11.219"
      },
      "witnessTrafficSharedWithVsanTraffic": false
      }
      }
      ```

      Replace the example values in the JSON file with the correct values for your environment.

      isEdgeClusterConfiguredForMultiAZ should be set to "true" if the cluster hosts an NSX Edge cluster and "false" if the cluster does not host an NSX Edge cluster.
   5. Click Execute.
   6. In the confirmation dialog box, click Continue.
   7. In the Response section, expand the result section and verify that the response is SUCCEEDED.
9. Stretch the cluster with the JSON specification.
   1. Navigate to ClustersPATCH /v1/clusters/{id}.
   2. Paste the unique ID of the cluster in the Value text-box.
   3. In the clusterUpdateSpec text box, paste the JSON specification.

      For example:

      ```
      {
      "clusterStretchSpec": {
      "deployWithoutLicenseKeys": true,
      "hostSpecs": [
      {
      "hostname": "sfo02-w01-esx01.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 1 ID>"
      },
      {
      "hostname": "sfo02-w01-esx02.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 2 ID>"
      },
      {
      "hostname": "sfo02-w01-esx03.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 3 ID>"
      },
      {
      "hostname": "sfo02-w01-esx04.sfo.rainpole.io",
      "hostNetworkSpec": {
      "networkProfileName": "sfo-w01-az2-nsx-np01",
      "vmNics": [
      {
      "id": "vmnic0",
      "uplink": "uplink1",
      "vdsName": "sfo-w01-cl01-vds01"
      },
      {
      "id": "vmnic1",
      "uplink": "uplink2",
      "vdsName": "sfo-w01-cl01-vds01"
      }
      ]
      },
      "id": "<ESX host 4 ID>"
      }
      ],
      "isEdgeClusterConfiguredForMultiAZ": "true",
      "networkSpec": {
      "networkProfiles": [
      {
      "isDefault": false,
      "name": "sfo-w01-az2-nsx-np01",
      "nsxtHostSwitchConfigs": [
      {
      "ipAddressPoolName": "sfo-w01-az2-host-ip-pool01",
      "uplinkProfileName": "sfo-w01-az2-host-uplink-profile01",
      "vdsName": "sfo-w01-cl01-vds01",
      "vdsUplinkToNsxUplink": [
       {
        "nsxUplinkName": "uplink-1",
        "vdsUplinkName": "uplink1"
       },
       {
        "nsxUplinkName": "uplink-2",
        "vdsUplinkName": "uplink2"
       }
      ]
      }
      ]
      }
      ],
      "nsxClusterSpec": {
      "ipAddressPoolsSpec": [
      {
      "description": "WLD01 AZ2 Host TEP Pool",
      "name": "sfo-w01-az2-host-ip-pool01",
      "subnets": [
      {
       "cidr": "172.16.44.0/24",
       "gateway": "172.16.44.253",
       "ipAddressPoolRanges": [
        {
         "end": "172.16.44.200",
         "start": "172.16.44.10"
        }
       ]
      }
      ]
      }
      ],
      "uplinkProfiles": [
      {
      "name": "sfo-w01-az2-host-uplink-profile01",
      "teamings": [
      {
       "activeUplinks": [
        "uplink-1",
        "uplink-2"
       ],
       "name": "DEFAULT",
       "policy": "LOADBALANCE_SRCID",
       "standByUplinks": []
      }
      ],
      "transportVlan": 1644
      }
      ]
      }
      },
      "witnessSpec": {
      "fqdn": "sfo-w01-cl01-vsw01.sfo.rainpole.io",
      "vsanCidr": "172.17.11.0/24",
      "vsanIp": "172.17.11.219"
      },
      "witnessTrafficSharedWithVsanTraffic": false
      }
      }
      ```

      Replace the example values in the JSON file with the correct values for your environment.

      isEdgeClusterConfiguredForMultiAZ should be set to "true" if the cluster hosts an NSX Edge cluster and "false" if the cluster does not host an NSX Edge cluster.
   4. Click Execute.
   5. On the confirmation dialog box, click Continue.

      You can monitor the stretch cluster creation in Fleet Management Tasks.