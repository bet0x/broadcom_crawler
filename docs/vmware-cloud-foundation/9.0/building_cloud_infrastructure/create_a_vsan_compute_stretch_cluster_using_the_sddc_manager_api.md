---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/create-a-vsan-compute-stretch-cluster-using-the-vmware-cloud-foundation-api.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a vSAN Compute Stretch Cluster Using the SDDC Manager API
---

# Create a vSAN Compute Stretch Cluster Using the SDDC Manager API

You can create a vSAN compute stretch cluster using the POST /v1/clusters API.

- See [vSAN Stretched Compute Cluster Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-compute-cluster.html) for design requirements and recommendations.
- A minimum of four ESX hosts commissioned with the vSAN type vSAN Compute Cluster. See [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html).
- ESX, vCenter, and SDDC Manager must all be version 9.0 or later.
- An existing remote datastore. It can be a vSAN ESA, vSAN OSA, or vSAN storage datastore.
- The server cluster providing the remote datastore must be stretched. See [Stretch a vSAN Storage Cluster Using the SDDC Manager API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/stretch-a-vsan-storage-cluster-using-the-vmware-cloud-foundation-api.html).

No vSAN witness host is required for a stretched vSAN compute cluster.

If you want to stretch a vSAN compute cluster that you already created, see [Stretch a vSAN Compute Cluster Using the SDDC Manager API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/stretch-a-vsan-compute-cluster-using-the-vmware-cloud-foundation-api.html).

This procedure provides two different sample JSON specification files for the different topologies:

| Topology | Description |
| --- | --- |
| Symmetric | This reflects a topology that has multiple routes to and from the server cluster, with **all routes** having the same bandwidth and latency characteristics. This is not typical in stretched cluster deployments but may arise if the vSAN compute cluster is deployed at different sites unrelated to where the stretched vSAN storage cluster resides. |
| Asymmetric | This typically reflects a topology that has multiple routes to and from the server cluster, with **one route** having optimal bandwidth and latency characteristics. This is typical in stretched cluster deployments where a client stretched cluster needs to access storage on a server stretched cluster would ideally access the object data in the same site, known as **inter-site-connectivity**. In this case you specify the site affinity between server and client sites in the JSON specification file.  For example, if your environment looks like this:  - AZ1 (Server): East Coast - AZ2 (Server): West Coast - AZ1 (Client): East Coast - AZ2 (Client): West Coast  Then you would use an asymmetric topology with the following site affinity:  - AZ1 (Client) → AZ1 (Server) - AZ2 (Client) → AZ2 (Server) |

1. Create a JSON specification file in a text editor.

   Symmetric vSAN remote datastore topology:

   ```
   {
     "domainId": "<domain ID>",
     "computeSpec": {
       "clusterSpecs": [
         {
           "name": "sfo-w01-cl02",
           "hostSpecs": [
             {
               "id": "ESX host 1 ID",
               "hostname": "sfo01-w01-r01-esx04.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_primary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo01-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             },
             {
               "id": "ESX host 2 ID",
               "hostname": "sfo01-w01-r01-esx05.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_primary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo01-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             },
             {
               "id": "ESX host 3 ID",
               "hostname": "sfo02-w01-r01-esx04.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_secondary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo02-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             },
             {
               "id": "ESX host 4 ID",
               "hostname": "sfo02-w01-r01-esx05.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_secondary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo02-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             }
           ],
           "datastoreSpec": {
             "vsanRemoteDatastoreClusterSpec": {
               "vsanRemoteDatastoreSpec": [
                 {
                   "datastoreUuid": "<-- ENTER UUID OF REMOTE DATASTORE HERE -->",
                   "networkTopology": "Symmetric"
                 }
               ]
             }
           },
           "networkSpec": {
             "vdsSpecs": [
               {
                 "name": "sfo-w01-cl02-vds01",
                 "mtu": "9000",
                 "portGroupSpecs": [
                   {
                     "name": "sfo-w01-cl02-pg-esxi-mgmt",
                     "transportType": "MANAGEMENT",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl02-pg-vmotion",
                     "transportType": "VMOTION",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl02-pg-vsan",
                     "transportType": "VSAN",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   }
                 ],
                 "nsxtSwitchConfig": {
                   "hostSwitchOperationalMode": "STANDARD",
                   "transportZones": [
                     {
                       "name": "vlan-tz-sfo-w01-nsx01",
                       "transportType": "VLAN"
                     },
                     {
                       "name": "overlay-tz-sfo-w01-nsx01",
                       "transportType": "OVERLAY"
                     }
                   ]
                 }
               }
             ],
             "nsxClusterSpec": {
               "nsxTClusterSpec": {
                 "ipAddressPoolsSpec": [
                   {
                     "name": "sfo01-w01-r01-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.13.14.0/24",
                         "gateway": "10.13.14.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.13.14.101",
                             "end": "10.13.14.132"
                           }
                         ]
                       }
                     ]
                   },
                   {
                     "name": "sfo02-w01-r01-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.14.14.0/24",
                         "gateway": "10.14.14.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.14.14.101",
                             "end": "10.14.14.132"
                           }
                         ]
                       }
                     ]
                   }
                 ],
                 "uplinkProfiles": [
                   {
                     "name": "sfo01-w01-r01-uplink-profile01",
                     "transportVlan": 1314,
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
                   },
                   {
                     "name": "sfo02-w01-r01-uplink-profile01",
                     "transportVlan": 1414,
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
             "networkProfiles": [
               {
                 "isDefault": true,
                 "name": "sfo01-w01-r01-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo01-w01-r01-ip-pool01-host",
                     "uplinkProfileName": "sfo01-w01-r01-uplink-profile01",
                     "vdsName": "sfo-w01-cl02-vds01",
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
               },
               {
                 "isDefault": false,
                 "name": "sfo02-w01-r01-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo02-w01-r01-ip-pool01-host",
                     "uplinkProfileName": "sfo02-w01-r01-uplink-profile01",
                     "vdsName": "sfo-w01-cl02-vds01",
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
             ]
           },
           "clusterImageId": "<personality ID>"
         }
       ]
     },
     "deployWithoutLicenseKeys": "true"
   }
   ```

   Asymmetric vSAN remote datastore topology:

   ```
   {
     "domainId": "<domain ID>",
     "computeSpec": {
       "clusterSpecs": [
         {
           "name": "sfo-w01-cl02",
           "hostSpecs": [
             {
               "id": "ESX host 1 ID",
               "hostname": "sfo01-w01-r01-esx04.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_primary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo01-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             },
             {
               "id": "ESX host 2 ID",
               "hostname": "sfo01-w01-r01-esx05.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_primary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo01-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             },
             {
               "id": "ESX host 3 ID",
               "hostname": "sfo02-w01-r01-esx04.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_secondary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo02-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             },
             {
               "id": "ESX host 4 ID",
               "hostname": "sfo02-w01-r01-esx05.sfo.rainpole.io",
               "azName": "sfo-w01-r01-c01_secondary-az-faultdomain",
               "hostNetworkSpec": {
                 "networkProfileName": "sfo02-w01-r01-network-profile01",
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl02-vds01",
                     "uplink": "uplink2"
                   }
                 ]
               }
             }
           ],
           "datastoreSpec": {
             "vsanRemoteDatastoreClusterSpec": {
               "vsanRemoteDatastoreSpec": [
                 {
                   "datastoreUuid": "<-- ENTER UUID OF REMOTE DATASTORE HERE -->",
                   "networkTopology": "Asymmetric",
                   "siteAffinity": [
                     {
                       "serverSite": "sfo-w01-c01_primary-az-faultdomain",
                       "clientSite": "sfo-w01-c01_primary-az-faultdomain"
                     },
                     {
                       "serverSite": "sfo-w01-c01_secondary-az-faultdomain",
                       "clientSite": "sfo-w01-c01_secondary-az-faultdomain"
                     }
                   ]
                 }
               ]
             }
           },
           "networkSpec": {
             "vdsSpecs": [
               {
                 "name": "sfo-w01-cl02-vds01",
                 "mtu": "9000",
                 "portGroupSpecs": [
                   {
                     "name": "sfo-w01-cl02-pg-esxi-mgmt",
                     "transportType": "MANAGEMENT",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl02-pg-vmotion",
                     "transportType": "VMOTION",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl02-pg-vsan",
                     "transportType": "VSAN",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   }
                 ],
                 "nsxtSwitchConfig": {
                   "hostSwitchOperationalMode": "STANDARD",
                   "transportZones": [
                     {
                       "name": "vlan-tz-sfo-w01-nsx01",
                       "transportType": "VLAN"
                     },
                     {
                       "name": "overlay-tz-sfo-w01-nsx01",
                       "transportType": "OVERLAY"
                     }
                   ]
                 }
               }
             ],
             "nsxClusterSpec": {
               "nsxTClusterSpec": {
                 "ipAddressPoolsSpec": [
                   {
                     "name": "sfo01-w01-r01-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.13.14.0/24",
                         "gateway": "10.13.14.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.13.14.101",
                             "end": "10.13.14.132"
                           }
                         ]
                       }
                     ]
                   },
                   {
                     "name": "sfo02-w01-r01-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.14.14.0/24",
                         "gateway": "10.14.14.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.14.14.101",
                             "end": "10.14.14.132"
                           }
                         ]
                       }
                     ]
                   }
                 ],
                 "uplinkProfiles": [
                   {
                     "name": "sfo01-w01-r01-uplink-profile01",
                     "transportVlan": 1314,
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
                   },
                   {
                     "name": "sfo02-w01-r01-uplink-profile01",
                     "transportVlan": 1414,
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
             "networkProfiles": [
               {
                 "isDefault": true,
                 "name": "sfo01-w01-r01-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo01-w01-r01-ip-pool01-host",
                     "uplinkProfileName": "sfo01-w01-r01-uplink-profile01",
                     "vdsName": "sfo-w01-cl02-vds01",
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
               },
               {
                 "isDefault": false,
                 "name": "sfo02-w01-r01-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo02-w01-r01-ip-pool01-host",
                     "uplinkProfileName": "sfo02-w01-r01-uplink-profile01",
                     "vdsName": "sfo-w01-cl02-vds01",
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
             ]
           },
           "clusterImageId": "<personality ID>"
         }
       ]
     },
     "deployWithoutLicenseKeys": "true"
   }
   ```

   Replace the example values in the JSON file with the correct values for your environment.
2. Log in to VCF Operations.
3. In the navigation pane, click Developer CenterAPIs & SDKs.
4. Click the API Explorer link on the SDDC Manager API.
5. Click the VCF Instance in which you want to create the stretched cluster.
6. Retrieve the unique IDs for each ESX host that will be part of the stretched cluster and add the IDs to the JSON specification file.
   1. Navigate to HostsGET /v1/hosts.
   2. In the Status text box, enter UNASSIGNED\_USEABLE and click Execute.
   3. In the Response section, click PageOfHost, copy the id element of each host, and replace the respective value in the JSON specification file.

   | ESX Host | Value |
   | --- | --- |
   | ESX Host 1 | ESX host 1 ID |
   | ESX Host 2 | ESX host 2 ID |
   | ESX Host 3 | ESX host 3 ID |
   | ESX Host 4 | ESX host 4 ID |
7. Retrieve the ID of the workload domain in which you want to create the cluster and add the ID to the JSON specification file.
   1. Navigate to DomainsGET /v1/domains.
   2. Click Execute.
   3. In the Response section, click the domain name, copy the id element, and replace the <domain ID> value in the JSON specification file.
8. Retrieve the vSphere Lifecycle Manager image ID to use for the cluster and add the ID to the JSON specification file.
   1. Navigate to PersonalitiesGET /v1/personalities.
   2. Click Execute.
   3. In the Response section, click the personality representing the image you want to use, copy the personalityId element, and replace the <personality ID> value in the JSON specification file.
9. Retrieve the datastore Uuid for the server cluster providing the remote datastore and add it to the JSON specification file.
   1. Navigate to ClustersGET /v1/clusters.
   2. Click Execute.
   3. In the Response section, click PageOfCluster, and copy the id element of the server cluster providing the remote datastore.
   4. Navigate to ClustersGET /v1/clusters{id}/datastores.
   5. In the Value text box, enter the unique ID for the server cluster and click Execute.
   6. In the Response section, click the datastore, copy the id element, and replace the <datastore ID> value in the JSON specification file.
10. Navigate to ClustersPOST /v1/clusters.
11. Paste the content from your JSON specification file in the Value text box for the body parameter and click Execute.
12. On the confirmation dialog box, click Continue.

    You can monitor the stretch cluster creation in Fleet Management Tasks.