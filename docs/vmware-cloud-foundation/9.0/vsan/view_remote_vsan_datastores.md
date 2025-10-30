---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh/view-remote-vsan-datastores.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View Remote vSAN Datastores
---

# View Remote vSAN Datastores

Use the Datastore Management page to view remote datastores mounted to the local vSAN cluster, and client clusters sharing the local datastore.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Datastore Management.

This view lists information about each datastore mounted to the local cluster.

- Server cluster that hosts the datastore
- vCenter of the server cluster (if applicable)
- Capacity usage of the datastore
- Free capacity available
- Number of virtual machines using the datastore (number of virtual machines using the compute resources of the local cluster, but the storage resources of the server cluster)
- Client clusters that have mounted the datastore

You can mount or unmount remote datastores from this page.