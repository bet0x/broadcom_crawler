---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/monitor-container-volumes-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor Container Volumes in vSAN Cluster
---

# Monitor Container Volumes in vSAN Cluster

You can view the status of the container volumes in the vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under Cloud Native Storage, select Container Volumes to view the container volumes in the vSAN cluster. You can view information about the volume name, label, datastore, compliance status, health status, and capacity quota.
4. Click ![CNS Volume Details](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c8fb469c-71c2-4b8d-af1a-c7810121df6f.original.png) to view the following:

   - Click the Basics tab to view the volume details such as volume type, ID, datastore, storage policy, compliance, and health status.
   - Click the Kubernetes objects tab to view Kubernetes related data such as Kubernetes cluster, namespace, pod, persistent volume claim, labels, and so on.
   - Click the Physical Placement tab to view the type, ESX host, cache, and capacity disk of the virtual object components.
   - Click the Performance tab to view the performance of the container volumes.
5. Select the check box for the volumes that have an out-of-date policy status that you can view under Compliance Status column. Click Reapply Policy to reapply the policy on the selected volumes.
6. Select the check box for the container volume you want to delete and click Delete.
7. Click Migrate to migrate a container to a different datastore.
8. Use the Add Filter option to add filters to the container volumes.