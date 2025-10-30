---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api/deploy-a-l3-multi-rack-vsan-vi-workload-domain/deploy-a-workload-domain-with-a-3-three-multi-rack-vsan-hci-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a Workload Domain with a Layer 3 Multi-Rack vSAN HCI Cluster
---

# Create a Workload Domain with a Layer 3 Multi-Rack vSAN HCI Cluster

Deploying a workload domain with a layer 3 vSAN HCI cluster that spans multiple racks requires routed networks between racks. To deploy such a workload domain, you use the VCF API and continue the setup after the deployment is complete.

1. Create a JSON specification file in a text editor.

   The following example is for an environment with a single vSphere Distributed Switch. If you have multiple vSphere Distributed Switches, see the [SDDC Manager API Reference Guide](https://developer.broadcom.com/xapis/vmware-cloud-foundation-api/latest/clusters/#_usecase_stretchCluster) for details about creating a JSON specification.

   ```
   {
     "domainName": "sfo-w01",
     "vcenterSpec": {
       "name": "sfo-w01-vc01",
       "networkDetailsSpec": {
         "ipAddress": "10.11.10.160",
         "dnsName": "sfo-w01-vc01.sfo.rainpole.io"
       },
       "rootPassword": "VMw@re1!VMw@re1!",
       "datacenterName": "sfo-w01-dc01",
       "vmSize": "Medium"
     },
     "computeSpec": {
       "clusterSpecs": [
         {
           "name": "sfo-w01-cl01",
           "hostSpecs": [
             {
               "id": "<ESX host 1 ID>",
               "hostname": "sfo01-w01-r01-esx01.sfo.rainpole.io",
               "hostNetworkSpec": {
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink2"
                   }
                 ],
                 "networkProfileName": "sfo01-w01-r01-network-profile01"
               }
             },
             {
               "id": "<ESX host 2 ID>",
               "hostname": "sfo01-w01-r02-esx01.sfo.rainpole.io",
               "hostNetworkSpec": {
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink2"
                   }
                 ],
                 "networkProfileName": "sfo01-w01-r02-network-profile01"
               }
             },
             {
               "id": "<ESX host 3 ID>",
               "hostname": "sfo01-w01-r03-esx01.sfo.rainpole.io",
               "hostNetworkSpec": {
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink2"
                   }
                 ],
                 "networkProfileName": "sfo01-w01-r03-network-profile01"
               }
             },
             {
               "id": "<ESX host 4 ID>",
               "hostname": "sfo01-w01-r04-esx01.sfo.rainpole.io",
               "hostNetworkSpec": {
                 "vmNics": [
                   {
                     "id": "vmnic0",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink1"
                   },
                   {
                     "id": "vmnic1",
                     "vdsName": "sfo-w01-cl01-vds01",
                     "uplink": "uplink2"
                   }
                 ],
                 "networkProfileName": "sfo01-w01-r04-network-profile01"
               }
             }
           ],
           "datastoreSpec": {
             "vsanDatastoreSpec": {
               "datastoreName": "sfo-w01-cl01-vsan01",
               "esaConfig": {
                 "enabled": "true"
               }
             }
           },
           "networkSpec": {
             "vdsSpecs": [
               {
                 "name": "sfo-w01-cl01-vds01",
                 "mtu": 9000,
                 "portGroupSpecs": [
                   {
                     "name": "sfo-w01-cl01-vds01-pg-esxi-mgmt",
                     "transportType": "MANAGEMENT",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl01-vds01-pg-vmotion",
                     "transportType": "VMOTION",
                     "standByUplinks": [],
                     "teamingPolicy": "loadbalance_loadbased",
                     "activeUplinks": [
                       "uplink1",
                       "uplink2"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl01-vds01-pg-vsan",
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
             "networkProfiles": [
               {
                 "isDefault": true,
                 "name": "sfo01-w01-r01-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo01-w01-r01-ip-pool01-host",
                     "uplinkProfileName": "sfo01-w01-r01-uplink-profile01",
                     "vdsName": "sfo-w01-cl01-vds01",
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
                 "name": "sfo01-w01-r02-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo01-w01-r02-ip-pool01-host",
                     "uplinkProfileName": "sfo01-w01-r02-uplink-profile01",
                     "vdsName": "sfo-w01-cl01-vds01",
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
                 "name": "sfo01-w01-r03-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo01-w01-r03-ip-pool01-host",
                     "uplinkProfileName": "sfo01-w01-r03-uplink-profile01",
                     "vdsName": "sfo-w01-cl01-vds01",
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
                 "name": "sfo01-w01-r04-network-profile01",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo01-w01-r04-ip-pool01-host",
                     "uplinkProfileName": "sfo01-w01-r04-uplink-profile01",
                     "vdsName": "sfo-w01-cl01-vds01",
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
               "nsxTClusterSpec": {
                 "ipAddressPoolsSpec": [
                   {
                     "name": "sfo01-w01-r01-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.15.14.0/24",
                         "gateway": "10.15.14.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.15.14.101",
                             "end": "10.15.14.132"
                           }
                         ]
                       }
                     ]
                   },
                   {
                     "name": "sfo01-w01-r02-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.15.25.0/24",
                         "gateway": "10.15.25.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.15.25.101",
                             "end": "10.15.25.116"
                           }
                         ]
                       }
                     ]
                   },
                   {
                     "name": "sfo01-w01-r03-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.15.36.0/24",
                         "gateway": "10.15.36.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.15.36.101",
                             "end": "10.15.36.116"
                           }
                         ]
                       }
                     ]
                   },
                   {
                     "name": "sfo01-w01-r04-ip-pool01-host",
                     "subnets": [
                       {
                         "cidr": "10.15.47.0/24",
                         "gateway": "10.15.47.1",
                         "ipAddressPoolRanges": [
                           {
                             "start": "10.15.47.101",
                             "end": "10.15.47.132"
                           }
                         ]
                       }
                     ]
                   }
                 ],
                 "uplinkProfiles": [
                   {
                     "name": "sfo01-w01-r01-uplink-profile01",
                     "transportVlan": 1514,
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
                     "name": "sfo01-w01-r02-uplink-profile01",
                     "transportVlan": 1525,
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
                     "name": "sfo01-w01-r03-uplink-profile01",
                     "transportVlan": 1536,
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
                     "name": "sfo01-w01-r04-uplink-profile01",
                     "transportVlan": 1547,
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
             }
           },
           "clusterImageId": "<personality ID>"
         }
       ]
     },
     "nsxTSpec": {
       "formFactor": "Large",
       "nsxManagerSpecs": [
         {
           "name": "sfo-w01-nsx01a",
           "networkDetailsSpec": {
             "ipAddress": "10.11.10.162",
             "dnsName": "sfo-w01-nsx01a.sfo.rainpole.io"
           }
         }
       ],
       "vip": "10.11.10.161",
       "vipFqdn": "sfo-w01-nsx01.sfo.rainpole.io",
       "nsxManagerAdminPassword": "VMw@re1!VMw@re1!"
     },
     "ssoDomainSpec": {
       "ssoDomainName": "sfo-w01.local",
       "ssoDomainPassword": "VMw@re1!VMw@re1!"
     },
     "deployWithoutLicenseKeys": "true"
   }
   ```
2. In the navigation pane of the VCF Operation UI click Developer CenterAPIs & SDKsAPI Explorer
3. Click the VCF Instance in which you want to create the layer 3 multi-rack vSAN HCI cluster.
4. Retrieve the unique IDs for each ESX host that will be part of the stretched cluster and add the IDs to the JSON specification file.
   1. Navigate to HostsGET /v1/hosts.
   2. In the Status text box, enter UNASSIGNED\_USEABLE and click Execute.
   3. In the Response section, click PageOfHost, copy the id element of each host, and replace the respective value in the JSON specification file.

   | ESX Host | Value |
   | --- | --- |
   | ESX Host 1 | ESX host 1 ID |
   | ESX Host 2 | ESX host 2 ID |
   | ESX Host 3 | ESX host 3 ID |
   | ESX Host 4 | ESX host 4 ID |
5. Retrieve the vSphere Lifecycle Manager image ID to use for the cluster and add the ID to the JSON specification file. Navigate to PersonalitiesGET /v1/personalities. Click Execute. In the Response section, click the personality representing the image you want to use, copy the personalityId element, and replace the <personality ID> value in the JSON specification file.
6. Expand the Domains API category.
7. To validate the JSON specification, paste the JSON specification in the body of the POST /v1/domains/validations API and click Execute.
8. To create the workload domain, paste the JSON specification in the body of the POST /v1/domains/ API and click Execute.
9. Click View Task Status to view the domain creation tasks and sub tasks.