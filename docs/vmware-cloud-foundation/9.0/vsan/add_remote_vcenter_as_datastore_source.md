---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh/add-remote-vcenter-as-datastore-source.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Add Remote vCenter as Datastore Source
---

# Add Remote vCenter as Datastore Source

You can add a remote vCenter as a remote datastore source for client clusters on the local vCenter.

1. In the vSphere Client, navigate to the cluster.
2. Select Configure.
3. Under vSAN, click Datastore Management.
4. On the Datastore Sources tab, click Add Remote Datastore Source to open the wizard.
5. Enter information to specify the remote vCenter.
6. Check the compatibility, review the configuration, and click Finish.

The remote vCenter is added as a datastore source. vSAN clusters on the local vCenter can mount remote datastores that reside on the remote vCenter.