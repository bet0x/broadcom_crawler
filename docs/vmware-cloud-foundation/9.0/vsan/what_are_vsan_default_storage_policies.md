---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-vsan-policies/about-the-vsan-default-storage-policy.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > What are vSAN Default Storage Policies
---

# What are vSAN Default Storage Policies

vSAN requires that the virtual machines deployed on the vSAN datastores are assigned at least one storage policy.

When provisioning a virtual machine, if you do not explicitly assign a storage policy, vSAN assigns a default storage policy to the virtual machine. Each default policy contains vSAN rule sets and a set of basic storage capabilities, typically used for the placement of virtual machines deployed on vSAN datastores. If vSAN does not assign a storage policy to the virtual machine, vSAN health check prompts a warning to reapply the VM storage policy. For more information, see Broadcom knowledge base article [326534](https://knowledge.broadcom.com/external/article/326534/vsan-health-service-vsan-storage-policy.html).

If you use a vSAN ESA cluster, depending on your cluster size, you can use one of the vSAN ESA policies listed here.

The objects in a vSAN ESA cluster with RAID 0 or RAID 1 configuration have 3 disk stripes, though the default storage policy defines only 1 disk stripe.

vSAN ESA Default Storage Policy Specifications - RAID-5



| Specification | Setting |
| --- | --- |
| Failures to tolerate | 1 |
| Number of disk stripes per object | 1 |
| Flash read cache reservation, or flash capacity used for the read cache | 0 |
| Object space reservation | Thin provisioning |
| Force provisioning | No |

RAID-5 in vSAN ESA supports three ESX host clusters. If you enable auto-policy management, the cluster must have four ESX hosts to use RAID-5.

vSAN ESA Default Storage Policy Specifications - RAID-6



| Specification | Setting |
| --- | --- |
| Failures to tolerate | 2 |
| Number of disk stripes per object | 1 |
| Flash read cache reservation, or flash capacity used for the read cache | 0 |
| Object space reservation | Thin provisioning |
| Force provisioning | No |

To use RAID-6, you must have at least six ESX hosts in the vSphere cluster.

vSAN Default Storage Policy Specifications



| Specification | Setting |
| --- | --- |
| Failures to tolerate | 1 |
| Number of disk stripes per object  In some cases, vSAN also applies a stripe. | 1 |
| Flash read cache reservation, or flash capacity used for the read cache | 0 |
| Object space reservation | 0  Setting the Object space reservation to zero means that the virtual disk is thin provisioned, by default. |
| Force provisioning | No |

You can review the configuration settings for the default virtual machine storage policy when you navigate to the VM Storage Policies > name of the default storage policy > Rule-Set 1: VSAN.

For best results, consider creating and using your own virtual machine storage policies, even if the requirements of the policy are same as those defined in the default storage policy.

When you assign a user-defined storage policy to a datastore, vSAN applies the settings for the user-defined policy on the specified datastore. Only one storage policy can be the default policy for the vSAN datastore.

## Auto-Policy Management

Clusters with vSAN ESA can use auto-policy management to generate an optimal default storage policy, based on the cluster type (standard or stretched) and the number of ESX hosts. vSAN configures the Site disaster tolerance and Failures to tolerate to optimal settings for the cluster.

The name of the auto-generated policy is based on the cluster name, as follows: ClusterName - Optimal Default Datastore Policy

When you enable auto-policy management, vSAN assigns a new optimal policy to the vSAN datastore, and that policy becomes the datastore default policy for the cluster.

To enable auto-policy management, use the slide control on vSAN> Services > Storage > Edit.

## vSAN Default Storage Policy Characteristics

The following characteristics apply to the vSAN datastore default storage policies.

- The vSAN Default Storage Policy is assigned to all virtual machine objects if you do not assign any other vSAN policy when you provision a virtual machine. The VM Storage Policy text box is set to Datastore default on the Select Storage page. For more information about using storage policies, see the [vSphere Storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/vsphere-storage.html) guide.

  Virtual machine swap and virtual machine memory objects receive a vSAN default storage policy with Force provisioning set to Yes.
- A vSAN default policy only applies to vSAN datastores. You cannot apply a default storage policy to non- vSAN datastores, such as NFS or a VMFS datastore.
- Objects in a vSAN ESA cluster with RAID 0 or RAID 1 configuration will have 3 disk stripes, even if the default policy defines only 1 disk stripe.
- Because the **vSAN Default Storage Policy** is compatible with any vSAN datastore in the vCenter, you can move your virtual machine objects provisioned with the default policy to any vSAN datastore in the vCenter.
- You can clone the vSAN Default Storage Policy and use it as a template to create a user-defined storage policy.
- You can edit the vSAN Default Storage Policy, if you have the StorageProfile.View privilege. You must have at least one vSAN-enabled cluster that contains at least one ESX host. Typically you do not edit the settings of the vSAN Default Storage Policy.
- You cannot edit the name and description of the vSAN Default Storage Policy, or the vSAN storage provider specification. All other parameters including the policy rules are editable.
- You cannot delete the vSAN Default Storage Policy.
- A default storage policy is assigned when the policy that you assign during virtual machine provisioning does not include rules specific to vSAN.