---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/check-a-disk-or-disk-group-s-data-migration-capabilities-from-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Check a Disk or Disk Group's Data Migration Capabilities from vSAN Cluster
---

# Check a Disk or Disk Group's Data Migration Capabilities from vSAN Cluster

Use the data migration pre-check to find the impact of migration options when unmounting a disk or disk group, or removing it from the vSAN cluster.

Run the data migration pre-check before you unmount or remove a disk or disk group from the vSAN cluster. The test results provide information to help you determine the impact to cluster capacity, predicted health checks, and any objects that will go out of compliance. If the operation will not succeed, pre-check provides information about what resources are needed.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, click Data Migration Pre-check.
4. Select a disk or disk group, choose a data migration option, and click Pre-check. 

   vSAN runs the data migration precheck tests.
5. View the test results. 

   The pre-check results show whether you can safely unmount or remove the disk or disk group.
   - The Object Compliance and Accessibility tab displays objects that might have issues after the data migration.
   - The Cluster Capacity tab displays the impact of data migration on the vSAN cluster before and after you perform the operation.
   - The Predicted Health tab displays the health checks that might be affected by the data migration.

If the pre-check indicates that you can unmount or remove the device, click the option to continue the operation.