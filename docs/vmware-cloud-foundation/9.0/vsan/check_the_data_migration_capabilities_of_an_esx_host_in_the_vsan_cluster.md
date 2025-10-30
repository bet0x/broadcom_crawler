---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/working-with-members-of-vsan-cluster-in-maintenance-mode/check-the-data-migration-capabilities-of-a-host-in-the-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Check the Data Migration Capabilities of an ESX Host in the vSAN Cluster
---

# Check the Data Migration Capabilities of an ESX Host in the vSAN Cluster

Use data migration pre-check to identify the impact of migration options when placing an ESX host into maintenance mode or removing it from the cluster.

Before you place an ESX host into maintenance mode, run the data migration pre-check. The test results provide information to help you determine the impact to cluster capacity, predicted health checks, and any objects that will go out of compliance. If the operation will not succeed, pre-check provides information about what resources are needed.

1. In the vSphere Client, navigate to the cluster.
2. Click the Monitor tab.
3. Under vSAN, click Data Migration Pre-check.
4. Select an ESX host, a vSAN data migration option, and click Pre-check.

   vSAN runs the data migration precheck tests.
5. View the test results. 

   The pre-check results show whether the ESX host can safely enter maintenance mode.

   - The Object state tab displays objects that might have issues after the data migration.
   - The Cluster Capacity tab displays the impact of data migration on the vSAN cluster before and after you perform the operation.
   - The Predicted Health tab displays the health checks that might be affected by the data migration.

If the pre-check indicates that you can place the ESX host into maintenance mode, you can click Enter Maintenance Mode to migrate the data and place the ESX host into maintenance mode.