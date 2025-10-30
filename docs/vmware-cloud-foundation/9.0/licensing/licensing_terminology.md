---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/licensing-terminology.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Licensing Terminology
---

# Licensing Terminology

As part of the licensing workflows, specific terminology is used to refer to different licensing-related objects and actions.

|  |  |  |
| --- | --- | --- |
| **Term** | **Related actions** | **Description** |
| Subscription |  | You purchase a subscription for a specific product. You decide what capacity to purchase for the subscription. Subscriptions are term based. |
| Assets |  | Any object in your environment that requires licensing. Assets are vCenter instances, ESX hosts, VCF Operations instances, NSX, and others. Starting with 9.0, you assign a license to a vCenter instance, and all other assets, which are connected to that vCenter instance, are licensed automatically. |
| License |  | An object that entitles you to use the products that you purchased subscriptions for. A license can span multiple subscriptions or, when you split the default license, a license can be a portion of a subscription. |
|  | Create/Split | Performed in the VCF Business Services console. The process of generating a new license. You allocate to it a portion from the capacity of a default license. For more information, see [Split Default Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/split-licenses.html) |
|  | Add (to VCF Operations) | Performed in the VCF Business Services console. The process of associating the license with a VCF Operations instance. Then you can assign that license to vCenter instances from the VCF Operations instance. For more information, see [Add a License to VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/add-a-license-to-vcf-operations.html). |
|  | Remove (from VCF Operations) | Performed in theVCF Business Services console. When you remove a license from aVCF Operationsinstance, the license is no longer available in that VCF Operations instance, and you can add it to a different VCF Operations instance. For more information, see [Remove a License from VCF Operations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/remove-a-license-from-vcf-operations.html) |
|  | Delete | Performed in the VCF Business Services console. After you delete a license, the license is no longer available and the allocated capacity from this license is automatically merged into the capacity of the corresponding default license. For more information, see [Delete a License.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/delete-a-license.html) |
|  | Assign | Performed in VCF Operations. The action of entitling a vCenter instance, the cores or TiBs on assets within the vCenter instance, including hosts or vSAN clusters, and any connected component, for example NSX. For more information, see [Assign a Primary License to a vCenter Instance or a VCF Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-a-licenses-to-a-vcenter-instance.html) and [Assign an Add-on License to a vCenter Instance.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/assign-an-addon-license-to-an-asset.html) |
| Default license |  | The initial license that is automatically created in the VCF Business Services console after you purchase a subscription. The default license is a pool of capacity from all active subscriptions of the same product in the same site. |
| Split License |  | A license that you create manually. You allocate to it a portion from the capacity of a default license. For more information, see [Split Default Licenses.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/split-licenses.html) |
| Primary license |  | VCF and vSphere Foundation licenses. |
| Add-on license |  | You purchase them separately from the primary license, or, in the case of vSAN, you also receive capacity for the add-on license with your primary product purchase. You can assign add-on licenses to vCenter instances only after you assign a primary license. For example, in VCF 9.0 and vSphere Foundation 9.0, two of the supported add-on licenses are VMware vSAN (TiB) and VMware Private AI Foundation with NVIDIA (cores). |
| License file |  | The license file contains information that proves to VCF Operations that your environment is licensed. A license file can contain multiple licenses. |
| License Unit |  | The unit of measure for capacity, for example cores and TiBs. |
| Capacity |  | The number of cores or vSAN storage TiBs. |
|  | Allocate | The process of adding cores quantity or vSAN storage capacity to a license through splitting or merging. |
| Allocated capacity |  | A portion of the default license capacity that you added to a new license. Allocated capacity can be measured in cores or TiBs. |
|  | Increase | The capacity allocated to a license can be increased up to the available capacity in the default license. For more information, see [Change License Capacity.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/edit-license-capacity.html) |
|  | Decrease | The capacity allocated to a license can be decreased. For more information, see [Change License Capacity.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/manage-licenses-in-the-vcf-business-services-console/edit-license-capacity.html) |
| Total capacity |  | The total capacity of a product equals the combined capacity of the default license and all other licenses split from that default license. |
| Used capacity |  | Per license, the actual capacity consumed by the assets in your environment. |
| Unused capacity |  | Per license, the part of the allocated capacity that is not yet consumed by assets in the vCenter instances to which the license is assigned. |
| Over use |  | When a license has more used capacity than its currently allocated capacity. |
| Pooling |  | Combining the total capacity of subscriptions for the same product in one license. |