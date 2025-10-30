---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/replacing-a-host-in-a-stretched-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Replace a Failed Host in a Stretched Cluster
---

# Replace a Failed Host in a Stretched Cluster

If an ESX host or ESX host component in a stretched cluster fails, it is recommended that you replace the host with a new host.

- Image the replacement host with the same ESX version as the other hosts in the cluster.
- Check the health of the cluster.

1. Get the IDs of the hosts to be removed.
   1. In the VCF Operations console, clickDeveloper CenterAPIs & SDKs.
   2. Click the API Explorer link for the SDDC Manager API.
   3. Under APIs for managing hosts, click GET /v1/hosts.
   4. Click Execute.
   5. Click Download to download the JSON file.
   6. Open the JSON file and copy the the ID of the host to be removed.
2. Get the ID of the cluster from where the host is to be removed.
   1. In the API Explorer, navigate to APIs for managing clusters and click GET /v1/clusters.
   2. Click Execute.
   3. Click Download to download the JSON file.
   4. Open the JSON file and copy the the cluster ID.
3. Prepare the JSON request body.
   1. Click Patch /v1/clusters/id.
   2. Under ClusterUpdateSpec, click Cluster Update Data ClusterUpdateSpec{ ... }.
   3. Click Download to download the JSON file.
   4. Edit the JSON file so that it contains only the compact section similar to the example below.

      ```
      {
        "clusterCompactionSpec": {
           "hosts": [ {
              "id": "ESX host 1 ID"
           }, {
              "id": "ESX host 2 ID"
           }, {
              "id": "ESX host 3 ID"
           } ]
        }
      }
      ```
4. Run the compact cluster API.
   1. In the id field, replace the values with the host IDs you retrieved in step 1.
   2. Click Execute.
   3. Monitor the task till it is completed.
5. Decommission the host to be removed. 

   See [Decommission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/decommission-hosts.html#GUID-5eff3df4-8366-4ea4-82f4-5b2c80ae577d-en).
6. Commission the replacement host to the same network pool as the removed host. 

   See [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html#GUID-2fcdd4bd-0a02-4121-a6ac-b13498b1406d-en).
7. Expand the cluster to add the commissioned host to the cluster. See [Expand a Stretched Cluster in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/add-hosts-to-a-stretched-cluster.html#GUID-55b0645c-79ff-4be8-b348-95e68e82ea6b-en).
8. If required, SSH in to each newly added host and add a static route to the vSAN network of the witness host.