---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/stretch-a-vsan-storage-cluster-using-the-vmware-cloud-foundation-api.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Stretch a vSAN Storage Cluster Using the SDDC Manager API
---

# Stretch a vSAN Storage Cluster Using the SDDC Manager API

You can stretch an vSAN storage cluster using the PATCH /v1/clusters/{id} API. You must stretch a vSAN storage server cluster before you can stretch any of its vSAN compute client clusters.

- See [vSAN Stretched Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-storage-cluster.html) for design requirements and recommendations.
- Commission a minimum of three ESX hosts with the vSAN type vSAN Storage (formerly known as vSAN Max). See [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html).
- An existing vSAN storage cluster with a minimum of three ESX hosts.
- Deploy and configure a vSAN ESA witness host. See [Deploy and Configure vSAN Witness Host](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host.html).
- Unmount any vSAN compute cluster datastores that are mounted to the vSAN storage cluster.

1. Create a JSON specification file in a text editor.

   The following example is for an environment with two vSphere Distributed Switches. This is typcial in a vSAN storage cluster where vSAN storage traffic separation is configured with a dedicated vDS just for the vSAN storage traffic and all other traffic including the vSAN client traffic is on a separate vDS.

   The ESX hosts that you are adding to availability zone 2 must use the same vmnic to vSphere Distributed Switch mapping as the existing hosts in availability zone 1.

   ```
   {
     "clusterStretchSpec": {
       "hostSpecs": [
         {
           "id": "<ESX host 1 ID>",
           "hostname": "sfo02-w01-r01-esx01.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-w01-r01-network-profile01",
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
               },
               {
                 "id": "vmnic2",
                 "vdsName": "sfo-w01-cl01-vds02",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic3",
                 "vdsName": "sfo-w01-cl01-vds02",
                 "uplink": "uplink2"
               }
             ]
           }
         },
         {
           "id": "<ESX host 2 ID>",
           "hostname": "sfo02-w01-r01-esx02.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-w01-r01-network-profile01",
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
               },
               {
                 "id": "vmnic2",
                 "vdsName": "sfo-w01-cl01-vds02",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic3",
                 "vdsName": "sfo-w01-cl01-vds02",
                 "uplink": "uplink2"
               }
             ]
           }
         },
         {
           "id": "<ESX host 3 ID>",
           "hostname": "sfo02-w01-r01-esx03.sfo.rainpole.io",
           "hostNetworkSpec": {
             "networkProfileName": "sfo02-w01-r01-network-profile01",
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
               },
               {
                 "id": "vmnic2",
                 "vdsName": "sfo-w01-cl01-vds02",
                 "uplink": "uplink1"
               },
               {
                 "id": "vmnic3",
                 "vdsName": "sfo-w01-cl01-vds02",
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
             "name": "sfo-w01-r01-network-profile-01",
             "nsxtHostSwitchConfigs": [
               {
                 "ipAddressPoolName": "sfo02-w01-r01-ip-pool01-host",
                 "uplinkProfileName": "sfo02-w01-r01-uplink-profile01",
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
           "ipAddressPoolsSpec": [
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
               "name": "sfo02-w01-r01-uplink-profile-01",
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
       "isEdgeClusterConfiguredForMultiAZ": false,
       "witnessSpec": {
         "fqdn": "sfo-w01-cl01-vsw01.sfo.rainpole.io",
         "vsanCidr": "10.21.10.0/24",
         "vsanIp": "10.21.10.219"
       },
       "witnessTrafficSharedWithVsanTraffic": false,
       "deployWithoutLicenseKeys": true
     }
   }
   ```

   Replace the example values in the JSON file with the correct values for your environment.
2. Log in to VCF Operations.
3. In the navigation pane, click Developer CenterAPIs & SDKs.
4. Click the API Explorer link on the SDDC Manager API.
5. Click the VCF Instance which contains the cluster you want to stretch.
6. Retrieve the unique IDs for each ESX host that will be part of the stretched cluster and add the IDs to the JSON specification file.
   1. Navigate to HostsGET /v1/hosts.
   2. In the Status text box, enter UNASSIGNED\_USEABLE and click Execute.
   3. In the Response section, click PageOfHost, copy the id element of each host, and replace the respective value in the JSON specification file.

   | ESX Host | Value |
   | --- | --- |
   | ESX Host 1 | ESX host 1 ID |
   | ESX Host 2 | ESX host 2 ID |
   | ESX Host 3 | ESX host 3 ID |
7. Retrieve the unique ID for the cluster you want to stretch.
   1. Navigate to ClustersGET /v1/clusters.
   2. Click Execute.
   3. In the Response section, click PageOfCluster, copy the id element of the cluster.

      You will need the cluster ID for the subsequent step.
8. Stretch the cluster with the JSON specification.
   1. Navigate to ClustersPATCH /v1/clusters/{id}.
   2. Paste the unique ID of the cluster in the Value text-box.
   3. In the clusterUpdateSpec text box, paste the JSON specification.
   4. Click Execute.
   5. On the confirmation dialog box, click Continue.

      You can monitor the stretch cluster creation in Fleet Management Tasks.