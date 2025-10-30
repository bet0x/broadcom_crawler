---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh/unmount-remote-vsan-datastore.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Unmount Remote vSAN Datastore
---

# Unmount Remote vSAN Datastore

You can unmount a remote datastore from a vSAN cluster.

If no virtual machines on the local cluster are using the remote vSAN datastore, you can unmount the datastore from your local vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Datastore Management.
4. Select a remote datastore, and click Unmount.
5. Click Unmount to confirm.

The selected datastore is unmounted from the local cluster.