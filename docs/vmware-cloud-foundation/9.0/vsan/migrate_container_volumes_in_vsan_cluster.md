---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/migrate-container-volumes-in-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Migrate Container Volumes in vSAN Cluster
---

# Migrate Container Volumes in vSAN Cluster

You can migrate container volumes to a destination datastore in the vSAN cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under Cloud Native Storage, select Container Volumes to view the container volumes in the vSAN cluster.
4. Click Migrate to migrate a container to a different datastore.
5. In the Migrate volume dialog box, you can view the volume storage policy and actual size of the volume.
6. Filter and select the destination datastore.
7. Select I acknowledge that check box as volume migration is an advanced operation.
8. Click Migrate.