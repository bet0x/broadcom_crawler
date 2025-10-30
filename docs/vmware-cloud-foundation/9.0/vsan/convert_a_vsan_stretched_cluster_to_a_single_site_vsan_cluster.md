---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/converting-a-vsan-stretched-cluster-into-a-single-site-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Convert a vSAN Stretched Cluster to a Single Site vSAN Cluster
---

# Convert a vSAN Stretched Cluster to a Single Site vSAN Cluster

You can decommission a vSAN stretched cluster and convert it to a single site vSAN cluster.

- Back up all running virtual machines, and verify that all virtual machines are compliant with their current storage policy.
- Ensure that no health issues exist, and that all resync activities are complete.
- Change the associated storage policy to move all VM objects to one site. Use the Data locality rule to restrict virtual machine objects to the selected site.
- Replace the stretched cluster storage policies applied to the VMs with standard vSAN cluster policies or create a new vSAN storage policy that you can apply to a standard vSAN cluster.

When you decommission a vSAN stretched cluster, you must manually delete the fault domain configuration and remove the witness host. Because the witness host is not available, all witness components are missing for your virtual machines. To ensure full availability for your virtual machines, repair the cluster objects immediately.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains.
4. Change the storage policy to the default vSAN storage policy.
5. Disable the vSAN stretched cluster. 
   1. Click Disable. The Remove Witness Host dialog opens.
   2. Click Remove to confirm.
6. Remove the hosts available at the secondary site from the cluster.
7. Remove the fault domain configuration.
   1. Select a fault domain, and choose menu Actions > Delete. Click Yes to confirm.
   2. Select the other fault domain, and choose menu Actions > Delete. Click Yes to confirm.
8. Remove the witness host from inventory.
9. Repair the objects in the cluster. 
   1. Click the Monitor tab.
   2. Under vSAN, click Health and click vSAN object health.
   3. Click Repair object immediately.

   vSAN recreates the witness components within the cluster.