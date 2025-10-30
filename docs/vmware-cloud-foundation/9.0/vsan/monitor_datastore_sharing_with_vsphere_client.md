---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/sharing-remote-vsan-datastores-with-hci-mesh/monitoring-hci-mesh-using-vsphere-client.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor Datastore Sharing with vSphere Client
---

# Monitor Datastore Sharing with vSphere Client

You can use the vSphere Client to monitor the status of vSAN datastore sharing operations.

vSAN capacity monitor notifies you when remote datastores are mounted to the cluster. You can select the remote datastore to view its capacity information (Monitor > vSAN > Capacity). vSAN displays a banner informing you in case there are existing clusters mounting the vSAN datastore from this cluster.

- The Virtual Objects view (Monitor > > vSAN > Virtual Objects) shows the virtual objects used by the remote cluster VMs .
- The Physical disk placement view (VM > Monitor > Physical disk placement) for a VM located on a remote datastore shows information about its remote location.

vSAN health (Monitor > vSAN > Skyline Health > Health Findings > All > Filter by Category) checks report on the status of HCI functions.

- Data > vSAN Object health check shows accessibility information of remote objects.
- Network > Server cluster partition check reports about network partitions between hosts in the client cluster and the server cluster.
- Network > Latency checks the latency between hosts in the client cluster and the server cluster.

vSAN cluster performance views include virtual machine performance charts that display the virtual machine level performance of the client cluster from the perspective of the remote cluster. You can select a remote datastore to view the performance.

You can run pro-active tests on remote datastores to verify virtual machine creation and network performance. The virtual machine creation test creates a virtual machine on the remote datastore. The Network performance test checks the network performance between all hosts in the client cluster and all hosts the server clusters. For more information, see [Proactive Tests on vSAN Cluster.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/proactive-tests-on-vsan-cluster.html)