---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/prerequisites-for-transitioning-to-vsphere-lifecycle-manager-images.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Prerequisites for Transitioning to vSphere Lifecycle Manager Images
---

# Prerequisites for Transitioning to vSphere Lifecycle Manager Images

Before you can transition a vSphere cluster from vSphere Lifecycle Manager baselines to vSphere Lifecycle Manager images, you must meet certain prerequisites.

## vSphere Lifecycle Manager Method Transition Prerequisites

| Category | Prerequisite |
| --- | --- |
| SDDC Manager version | 9.0 or later |
| Network access for SDDC Manager and vCenter | HTTPS (TCP 443) |
| SDDC Manager access privileges | Administrator |
| ESX hosts | Ensure that all the ESX hosts in the vSphere clusters you wish to transition are healthy before beginning the workflow. |
| vSphere Lifecycle Manager image | Both PowerShell and the SDDC Manager API require one more or existing vSphere Lifecycle Manager images. These images are originally authored in vCenter. In vCenter 8.0.3 and below, vLCM images should be authored in the form of empty vLCM-managed clusters. In vCenter 9.0 and above, they should be authored as images in vCenter Image Library.  For information about creating a temporary cluster with a vLCM image in vCenter 8.0.3 and below, see see [Creating and Managing vSphere Lifecycle Manager Clusters](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle-8-0/cluster-operations-and-vsphere-lifecycle-manager.html#GUID-26DBC7B1-F304-4473-AE42-318FB701A081-en).  Only use the "Create a Cluster That Uses a Single Image by Importing an Image from a Host" workflow if your vCenter uses runs version 8.0.3 to due to an NSX limitation. This advise overrides the limited documentation advise. For vCenter versions 8.0.0 through 8.0.2, please use "Create a Cluster That Uses a Single Image by Composing a New Image.  For information about creating a Image Library vLCM image in vCenter 9, see [Create an Image in Image Library Manually.](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/working-with-image-library.html#GUID-321c2bc9-ec98-413a-8195-7d0190949a27-en)  The ESX version of the image must match the current version of the ESX hosts in the cluster you are transitioning.  Use a descriptive name for the images that you create. This will make it easier to know which images to import later. |
| PowerShell version | 7.2 or later  See [Installing Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell). |
| PowerShell script | Download the script from [KB 385617](https://knowledge.broadcom.com/external/article/385617). |
| VCF PowerCLI | Ensure that VCF.PowerCLI is installed. Should VMware.PowerCLI is already installed, you must remove it first, otherwise the two modules will conflict.  [Uninstall VMware.PowerCLI](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/power-cli/latest/powercli/installing-vmware-vsphere-powercli/uninstall-powercli.html).  [Installing VCF.PowerCLI](https://developer.broadcom.com/powercli/installation-guide). |

The processes for transitioning to vSphere Lifecycle Manager images support the following topologies.

## VMware Cloud Foundation Architecture Support

|  |  |
| --- | --- |
| **Topology** | **Minimum Workload Domain Version** |
| Standard architecture | 5.0 |
| Consolidated architecture | 5.1 |
| vSAN Stretched Cluster | 5.1 |
| DR Protected | 5.1 |
| vSphere Supervisor (Workload Management) enabled | Split BOM 9.0 \* |
| Heterogeneous Hardware Clusters | 9.0 \*\* |

\* The workload domain vCenter must first be upgraded to vCenter 9.0 or later, while ESX must remain on version 8.0 Update 1a or earlier.

\* \* If an vSphere cluster contains heterogeneous hardware (different vendors and/or different models requiring different add-ons and/or components) it must first be upgraded to ESX 9.0 or later before it can be transitioned to vSphere Lifecycle Manager images.

## Important Considerations

- You cannot combine the process of transitioning to vSphere Lifecycle manager images with the process of upgrading ESX. vSphere clusters that use vSphere Lifecycle Manager baselines must be transitioned to use images before they can be upgraded to ESX 9.0.
- During the transition process, you cannot perform any other operations on the cluster until the transition is complete.