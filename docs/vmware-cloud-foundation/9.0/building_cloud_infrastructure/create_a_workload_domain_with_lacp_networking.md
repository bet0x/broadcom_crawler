---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api/create-a-workload-domain-with-lacp-networking.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a Workload Domain with LACP Networking
---

# Create a Workload Domain with LACP Networking

You use the VCF Operations API to create a workload domain with LACP networking

The physical network infrastructure in your environment must meet certain requirements for deployment of a workload domain, configured to use LACP on the vSphere Distributed Switch.

For each host on which you want to use LACP, you must create a separate LACP port channel on the physical switches. You must consider the following requirements when configuring LACP on the physical switches:

- The hashing algorithm of the LACP port channel on the physical switches must be the same as the hashing algorithm that is configured for the LAG on the distributed switch.
- All physical NICs that you want to connect to the LACP port channel must be configured with the same speed and duplex.
- Determine the LACP mode on the physical switch, either Active or Passive
- If the Physical switch is set to Passive mode the vDS LAG will need to be set to Active
- If the Physical switch is set Active mode the vDS LAG can be either Active or Passive

Please contact the physical switch vendor for any specific configuration required to implement LACP on the switch.

1. Create a JSON specification file in a text editor.

   The following example is for an environment with a single vSphere Distributed Switch. If you have multiple vSphere Distributed Switches, see the [SDDC Manager API Reference Guide](https://developer.broadcom.com/xapis/sddc-manager-api/latest/data-structures/DomainCreationSpec/) for details about creating a JSON specification.

   ```
   {
     "domainName": "sfo-w01",
     "orgName": "Rainpole",
     "vcenterSpec": {
       "name": "sfo-w01-vc01",
       "networkDetailsSpec": {
         "ipAddress": "10.11.10.160",
         "dnsName": "sfo-w01-vc01.sfo.rainpole.io",
         "gateway": "10.11.10.1",
         "subnetMask": "255.255.255.0"
       },
       "rootPassword": "VMw@re1!VMw@re1!",
       "datacenterName": "sfo-w01-DC",
       "vmSize": "large"
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
                 ]
               }
             },
             {
               "id": "<ESX host 2 ID>",
               "hostname": "sfo01-w01-r01-esx02.sfo.rainpole.io",
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
                 ]
               }
             },
             {
               "id": "<ESX host 3 ID>",
               "hostname": "sfo01-w01-r01-esx03.sfo.rainpole.io",
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
                 ]
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
                 "mtu": 8900,
                 "portGroupSpecs": [
                   {
                     "name": "sfo-w01-cl01-vds01-pg-esxi-mgmt",
                     "transportType": "MANAGEMENT",
                     "standByUplinks": [],
                     "teamingPolicy": "failover_explicit",
                     "activeUplinks": [
                       "lag"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl01-vds01-pg-vmotion",
                     "transportType": "VMOTION",
                     "standByUplinks": [],
                     "teamingPolicy": "failover_explicit",
                     "activeUplinks": [
                       "lag"
                     ]
                   },
                   {
                     "name": "sfo-w01-cl01-vds02-pg-vsan",
                     "transportType": "VSAN",
                     "standByUplinks": [],
                     "teamingPolicy": "failover_explicit",
                     "activeUplinks": [
                       "lag"
                     ]
                   }
                 ],
                 "nsxtSwitchConfig": {
                   "hostSwitchOperationalMode": "STANDARD",
                   "transportZones": [
                     {
                       "name": "nsx-vlan-transportzone",
                       "transportType": "VLAN"
                     },
                     {
                       "name": "overlay-tz-sfo-w01-nsx01",
                       "transportType": "OVERLAY"
                     }
                   ]
                 },
                 "lagSpecs": [
                   {
                     "name": "lag",
                     "uplinksCount": 2,
                     "lacpMode": "ACTIVE",
                     "loadBalancingMode": "SOURCE_AND_DESTINATION_IP_AND_TCP_UDP_PORT_AND_VLAN",
                     "lacpTimeoutMode": "SLOW"
                   }
                 ]
               }
             ],
             "networkProfiles": [
               {
                 "isDefault": true,
                 "name": "sfo-w01-sfo-w01-cl01-r01-network-profile",
                 "nsxtHostSwitchConfigs": [
                   {
                     "ipAddressPoolName": "sfo-w01-r01-ip-pool01-host",
                     "uplinkProfileName": "sfo-w01-r01-uplink-profile01",
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
                     "name": "sfo-w01-r01-ip-pool01-host",
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
                   }
                 ],
                 "uplinkProfiles": [
                   {
                     "name": "sfo-w01-r01-uplink-profile01",
                     "transportVlan": 1314,
                     "teamings": [
                       {
                         "name": "DEFAULT",
                         "policy": "FAILOVER_ORDER",
                         "standByUplinks": [],
                         "activeUplinks": [
                           "lag"
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
       "formFactor": "MEDIUM",
       "nsxManagerSpecs": [
         {
           "name": "sfo-w01-nsx01a",
           "networkDetailsSpec": {
             "ipAddress": "10.11.10.132",
             "dnsName": "sfo-w01-nsx01a.sfo.rainpole.io",
             "gateway": "10.11.10.1",
             "subnetMask": "255.255.255.0"
           }
         },
         {
           "name": "sfo-w01-nsx01b",
           "networkDetailsSpec": {
             "ipAddress": "10.11.10.133",
             "dnsName": "sfo-w01-nsx01b.sfo.rainpole.io",
             "gateway": "10.11.10.1",
             "subnetMask": "255.255.255.0"
           }
         },
         {
           "name": "sfo-w01-nsx01c",
           "networkDetailsSpec": {
             "ipAddress": "10.11.10.134",
             "dnsName": "sfo-w01-nsx01c.sfo.rainpole.io",
             "gateway": "10.11.10.1",
             "subnetMask": "255.255.255.0"
           }
         }
       ],
       "vip": "10.11.10.131",
       "vipFqdn": "sfo-w01-nsx01.sfo.rainpole.io",
       "nsxManagerAdminPassword": "VMw@re1!VMw@re1!"
     },
     "deployWithoutLicenseKeys": "true",
     "ssoDomainSpec": {
       "ssoDomainName": "sfo-w01.local",
       "ssoDomainPassword": "VMw@re1!VMw@re1!"
     }
   }
   ```
2. In the navigation pane of the VCF Operation UI click Developer CenterAPIs & SDKsAPI Explorer
3. Click the VCF Instance in which you want to create the new workload domain,
4. Retrieve the unique IDs for each ESX host that are part of the stretched cluster and add the IDs to the JSON specification file.
   1. Navigate to HostsGET /v1/hosts.
   2. In the Status text box, enter UNASSIGNED\_USEABLE and click Execute.
   3. In the Response section, click PageOfHost, copy the id element of each host, and replace the respective value in the JSON specification file.

   | ESX Host | Value |
   | --- | --- |
   | ESX Host 1 | ESX host 1 ID |
   | ESX Host 2 | ESX host 2 ID |
   | ESX Host 3 | ESX host 3 ID |
5. Retrieve the vSphere Lifecycle Manager image ID to use for the cluster and add the ID to the JSON specification file.
   1. Navigate to PersonalitiesGET /v1/personalities and click Execute.
   2. In the Response section, click the image.
   3. Copy the personalityId element and replace the <personality ID> value in the JSON specification file.
6. Expand the Domains API category.
7. To validate the JSON specification, paste the JSON specification in the body of the POST /v1/domains/validations API and click Execute.
8. To create the workload domain, paste the JSON specification in the body of the POST /v1/domains/ API and click Execute.
9. Click View Task Status to view the domain creation tasks and sub tasks.