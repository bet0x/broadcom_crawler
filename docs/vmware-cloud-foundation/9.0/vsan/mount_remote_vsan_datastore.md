---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh/mount-remote-vsan-datastore.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Mount Remote vSAN Datastore
---

# Mount Remote vSAN Datastore

You can mount one or more datastores to a local vSAN HCI cluster, compute cluster, or the stretched compute cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Datastore Management.
4. Click Mount Remote Datastore to open the wizard.
5. (Optional) Select a remote vCenter as the datastore source.
6. Select a datastore.
7. (Optional) If the server cluster is a vSAN stretched cluster, configure Site Coupling to choose the optimal data path between the server and the client cluster.

   A vSAN stretched cluster might have an asymmetrical network, where links within each availability zone have higher bandwidth and lower latency than links between availability zones. A symmetrical network has similar links within each availability zone and across availability zones.
8. Check the datastore compatibility, and click Finish.

The remote datastore is mounted to the local vSAN cluster.

When you provision a virtual machine, you can select the remote datastore as the storage resource. Assign a storage policy that is supported by the remote datastore.