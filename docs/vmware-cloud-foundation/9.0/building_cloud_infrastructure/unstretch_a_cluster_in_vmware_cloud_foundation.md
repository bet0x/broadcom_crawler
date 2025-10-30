---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/unstretch-a-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Unstretch a Cluster in VMware Cloud Foundation
---

# Unstretch a Cluster in VMware Cloud Foundation

This procedure describes how to unstretch a vSAN cluster in VMware Cloud Foundation.

- Consolidate or delete all virtual machine snapshots on the vSAN cluster before unstretching the cluster.
- If you are unstretching a vSAN storage cluster (formerly known as vSAN Max), unmount any stretched vSAN compute clusters to which the vSAN storage cluster is providing a remote datastore.

1. Get the ID of the cluster you are unstretching.
   1. In the VCF Operations console, clickDeveloper CenterAPIs & SDKs.
   2. Click the API Explorer link for the SDDC Manager API.
   3. In the API Explorer, navigate to APIs for managing clusters and click GET /v1/clusters.
   4. Click Execute.
   5. Click Download to download the JSON file.
   6. Open the JSON file and copy the the cluster ID for SDDC-Cluster1.
2. Prepare the JSON request body.
   1. Click Patch /v1/clusters/id.
   2. Under ClusterUpdateSpec field, click Cluster Update Data ClusterUpdateSpec{ ... }.
   3. Click Download to download the JSON file.
   4. Edit the downloaded JSON file so that it contains only the unstretch information similar to the example below.

      ```
      { "clusterUnstretchSpec": {} }
      ```
3. Run the unstretch cluster API.
   1. For the ClusterUpdateSpec field, update the cluster UID (you retrieved this in step 1) and unstretch JSON file with the payload you prepared in step 2.
   2. Click Execute.

      The unstretch cluster task is displayed in the SDDC Manager task panel.
   3. Monitor the unstretch cluster task till it is completed.

      All hosts from AZ2 are removed from the unstretched cluster and the cluster is converted to standard vSAN cluster.