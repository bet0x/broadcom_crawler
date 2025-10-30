---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/define-a-storage-policy-for-virtual-san.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Define a Storage Policy for vSAN Using vSphere Client
---

# Define a Storage Policy for vSAN Using vSphere Client

You can create a storage policy that defines storage requirements for a virtual machine and its virtual disks.

- Verify that the vSAN storage provider is available. Refer to [View vSAN Storage Providers](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/view-vsan-storage-providers.html#GUID-05d09b41-7c47-4945-9f7b-1398fff851da-en).
- Required privileges: Profile-driven storage.Profile-driven storage view and Profile-driven storage.Profile-driven storage update

In this policy, you reference the storage capabilities supported by the vSAN datastore.

1. Navigate to Policies and Profiles, then click VM Storage Policies in the vSphere Client.
2. Click Create.
3. On the Name and description page, select a vCenter.
4. Type a name and a description for the storage policy and click Next.
5. On the Policy structure page, select Enable rules for vSAN storage, and click Next.
6. On the vSAN page, define the policy rule set, and click Next. 
   1. On the Availability tab, define the Site disaster tolerance and Failures to tolerate.

      Availability options define the rules for failures to tolerate, data locality, and failure tolerance method.
      - Site disaster tolerance defines the type of site failure tolerance used for virtual machine objects.
      - Failures to tolerate defines the number of ESX host and device failures that a virtual machine object can tolerate, and the data replication method.For example, if you choose Dual site mirroring and 2 failures - RAID-6 (Erasure Coding), vSAN configures the following policy rules:
      - Failures to tolerate: 1
      - Secondary level of failures to tolerate: 2
      - Data locality: None
      - Failure tolerance method: RAID-5/6 (Erasure Coding) - Capacity
   2. On the Storage Rules tab, define the encryption, space efficiency, and storage tier rules that can be used along with the vSAN HCI Datastore Sharing to distinguish the remote datastores.

      - Encryption services: Defines the encryption rules for virtual machines that you deploy with this policy. You can choose one of the following options:
        - Data-at-rest encryption: Encryption is enabled on the virtual machines.
        - No encryption: Encryption is not enabled on the virtual machines.
        - No preference: Makes the virtual machines compatible with both data-at-rest encryption and No encryption options.
      - Space Efficiency: Defines the space saving rules for the virtual machines that you deploy with this policy. You can choose one of the following options:
        - Deduplication and compression: Enables both deduplication and compression on the virtual machines. Deduplication and compression are available only on all-flash disk groups. For more information, see [Deduplication and Compression Design Considerations in a vSAN Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/increasing-space-efficiency-in-a-vsan-cluster/using-deduplication-and-compression-in-vsan-cluster/duplication-and-compression-design-considerations-in-vsan-cluster.html#GUID-70978532-9adb-49b9-a541-f9d9a9ee958a-en).
        - Compression only: Enables only compression on the virtual machines. Compression is available only on all-flash disk groups. For vSAN ESA compression is defined in the vSAN policy.
        - No space efficiency: Space efficiency features are not enabled on the virtual machines. Choosing this option requires datastores without any space efficiency options to be turned on.
        - No preference: Makes the virtual machines compatible with all the options.
      - Storage tier: Specifies the storage tier for the virtual machines that you deploy with this policy. You can choose one of the following options. Choosing the No preference option makes the virtual machines compatible with both hybrid and all flash environments.
        - All flash
        - Hybrid
        - No preference
   3. On the Advanced Policy Rules tab, define advanced policy rules, such as number of disk stripes per object and IOPS limits.
   4. On the Tags tab, click Add Tag Rule, and define the options for your tag rule.

      Make sure that the values you provide are within the range of values advertised by storage capabilities of the vSAN datastore.
7. On the Storage compatibility page, review the list of datastores under the COMPATIBLE and INCOMPATIBLE tabs and click Next.

   To be eligible, a datastore does not need to satisfy all the rule sets within the policy. The datastore must satisfy at least one rule set and all rules within this set. Verify that the vSAN datastore meets the requirements set in the storage policy and that it appears on the list of compatible datastores.
8. On the Review and finish page, review the policy settings, and click Finish.

The new policy is added to the list.

Assign this policy to a virtual machine and its virtual disks. vSAN places the virtual machine objects according to the requirements specified in the policy. For information about applying the storage policies to virtual machine objects, see the [vSphere Storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-storage.html) guide.