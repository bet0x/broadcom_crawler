---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api/deploy-a-l3-multi-rack-vsan-vi-workload-domain/create-and-assign-a-new-default-vsan-storage-policy.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create and Assign a New Default Storage Policy for vSAN ESA Cluster
---

# Create and Assign a New Default Storage Policy for vSAN ESA Cluster

By default, the vSAN ESA default storage policy is based on the number of hosts in the cluster during creation. To provide for fault domains that allow rack resiliency in a multi-rack cluster, you must create a default storage policy that is compatible with the number of racks.

1. In the vSphere Client for the workload domain vCenter Server, from the vSphere Client menu, select Policies and Profiles.
2. On the VM Storage Policies page, click Create.
3. On the Name and description page, select the vCenter Server instance that manages the multi-rack cluster.
4. Type a name and a description for the storage policy and click Next.
5. On the Policy structure page, select Enable rules for "vSAN" storage, and click Next.
6. On the Availability tab of the vSAN page, set Failures to tolerate according to the configuration of your environment. 

   You use RAID 5 or RAID 6 (erasure coding) for vSAN ESA.
7. On the Storage Rules tab, select All flash and click Next.
8. On the Storage compatibility page, verify that the datastore is compatible and click Next.
9. On the Review and finish page, review the policy settings and click Finish.
10. In the Storage inventory of the vSphere Client, navigate to the vSAN datastore.
11. On the Configure tab, click General and next to the Default Storage Policy pane, click Edit.
12. Select the storage policy that you want to assign as default to the vSAN datastore and click OK.