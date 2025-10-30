---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/add-hosts-to-a-stretched-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Expand a Stretched Cluster in VMware Cloud Foundation
---

# Expand a Stretched Cluster in VMware Cloud Foundation

You can expand a stretched cluster by adding ESX hosts. It is recommended that you add the same number of hosts to both availability zones for symmetry and cluster balance.

1. Commission the additional hosts to the global inventory. 

   See [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html).

   Make sure to select the correct network pool for the availability zone to which you are adding each host.
2. Get the UIDs of the hosts you commissioned.
   1. In the navigation pane, click Developer CenterAPI Explorer.
   2. Under APIs for managing hosts, click GET /v1/hosts.
   3. Click Execute.
   4. Click Download to download the JSON file.
   5. Open the JSON file and copy the the UIDs of the hosts.
3. Get the ID of the cluster you are expanding.
   1. In the API Explorer, navigate to APIs for managing clusters and click GET /v1/clusters.
   2. Click Execute.
   3. Click Download to download the JSON file.
   4. Open the JSON file and copy the the cluster ID for the cluster you are expanding.
4. Get the primary and secondary availability zone names from vCenter.
   1. In a web browser, log in to the vCenter at https://vcenter\_fqdn/ui.
   2. Select MenuHosts and Clusters.
   3. In the inventory panel, expand vCenterDatacenter.
   4. Select the cluster and then click the Configure tab.
   5. Under vSAN, select Fault Domains.
   6. Note the primary and secondary availability zone names.
5. Prepare the JSON request body.
   1. Click Patch /v1/clusters/id.
   2. Under ClusterUpdateSpec field, click Cluster Update Data ClusterUpdateSpec{ ... }.
   3. Click Download to download the JSON file.
   4. Edit the downloaded JSON file so that it contains only the expand section similar to the example below. In the azName field, type the primary and secondary names you had retrieved in step 4.

      The ESXi hosts that you are adding must use the same vmnic to vSphere Distributed Switch mapping as the existing hosts in the stretched cluster. For example: If existing hosts map vmnic0 and vmnic1 to vSphere Dstributed Switch 1 and vmnic2 and vmnic3 to vSphere Distributed Switch 2, then the hosts you are adding must map the same vmincs to the same vSphere Distributed Switches.

      ```
      {
        "clusterExpansionSpec": {
           "hostSpecs": [ {
              "id": "ESX host 1 ID",
              "deployWithoutLicenseKeys": "true",
              "azName":"primary/secondary",
              "hostNetworkSpec": {
               "vmNics": [{
                "id": "vmnic0",
                "vdsName": "<vSphere Distributed Switch 1>"
               },
               {
                "id": "vmnic1",
                "vdsName": "<vSphere Distributed Switch 2>"
               }
              ]
             }
            }, {
              "id": "ESX host 2 ID",
              "deployWithoutLicenseKeys": "true",
              "azName":"primary/secondary",
              "hostNetworkSpec": {
               "vmNics": [{
                "id": "vmnic0",
                "vdsName": "<vSphere Distributed Switch 1>"
               },
               {
                "id": "vmnic1",
                "vdsName": "<vSphere Distributed Switch 2>"
               }
              ]
             }
           }, {
              "id": "ESX host 3 ID",
              "deployWithoutLicenseKeys": "true",
              "azName":"primary/secondary",
              "hostNetworkSpec": {
               "vmNics": [{
                "id": "vmnic0",
                "vdsName": "<vSphere Distributed Switch 1>"
               },
               {
                "id": "vmnic1",
                "vdsName": "<vSphere Distributed Switch 2>"
               }
              ]
             }
           }, {
              "id": "ESX host 4 ID",
              "deployWithoutLicenseKeys": "true",
              "azName":"primary/secondary",
              "hostNetworkSpec": {
               "vmNics": [{
                "id": "vmnic0",
                "vdsName": "<vSphere Distributed Switch 1>"
               },
               {
                "id": "vmnic1",
                "vdsName": "<vSphere Distributed Switch 2>"
               }
              ]
             }
           } ]
        }
      }
      ```
6. Run the expand cluster API.
   1. For the ClusterUpdateSpec field, update the cluster ID (you retrieved this in step 3) and JSON file with the payload you prepared in step 5.
   2. Click Execute.
   3. Monitor the task until it is completed.
7. If required, SSH in to each newly added host and add a static route to the vSAN network of the witness host. Also add static routes in the witness if it could not reach the vSAN network of the newly added hosts.
8. Update the value of Host failure cluster tolerates to the number of hosts in AZ1 after cluster expansion.
   1. Log in to the management vCenter instance.
   2. Select Cluster and click the Configure tab.
   3. Under Services, click vSphere Availability and then click Edit.
   4. On the Admission Control page of the Edit Cluster Settings dialog box, set host failures cluster tolerates to the number of hosts in availability zone 1 and click OK.