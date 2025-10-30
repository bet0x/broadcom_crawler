---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/using-the-configuration-management-dashboard/viewing-drifts-for-clusters.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Viewing Drifts for Clusters
---

# Viewing Drifts for Clusters

You can view the drift status of your vSphere clusters in VCF Operations. The drift status is visible only for vSphere clusters that have vSphere Configuration Profiles enabled.

- Verify that you have vCenter version 9.0 or later.
- Verify that you have registered your vCenter with a cloud proxy.
- Clusters are managed with vSphere Configuration Profiles in individual vCenter instances. Enable vSphere Configuration Profiles for clusters in vSphere. For more information, see [Using vSphere Configuration Profiles](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle-8-0/using-vsphere-config-profiles-to-manage-host-configuration-at-a-cluster-level.html).

  There may be a delay of up to 8 hours for updates made on the cluster in vCenter instances to be reflected on the Configuration Drifts page.

1. To view the cluster drift status, from the left menu, click Fleet ManagementConfiguration Drifts.
2. Expand VCF Instances, select any VCF instance, and click on the Drifts tab.
3. Click the Clusters tile.

   You can also view the number of vSphere Configuration Profiles enabled clusters. The drift status of all enabled clusters associated with the VCF instance is displayed.
4. You can click on a cluster to view the cluster drift in vSphere Client (vSphere Client > Inventory > DataCenters > Cluster Name > Configure > Desired State > Configuration > Compliance)