---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-simple-deployment-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Simple VCF Automation Model
---

# Simple VCF Automation Model

The Simple VCF Automation Model consists of a single node deployed in a vSphere cluster. Availability is provided by the native vSphere HA functionality within the vSphere cluster.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0898b90b-6305-4cce-b7c9-4efa41ba1566.original.png)

## Simple VCF Automation Model Attributes

A Simple VCF Automation Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Availability | Relies on vSphere HA to restart the nodes in the event of an ESX host failure. |
| Scalability | Supports scale-up and scale-out to high the availability model.  Scale-up to a larger node size and scale-out to three nodes at the same time. |
| Recoverability | Restore through a backup. |

## Simple VCF Automation Model Options

A Simple VCF Automation Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| Network Placement | Deploy on the default VCF Management DVPG network |
| Deploy on a separate dedicated DVPG network |
| Deploy on a separate NSX overlay network |

## Simple VCF Automation Model Design Requirements

Simple VCF Automation Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-SIM-001 | Deploy VCF Automation as a single node in the default management vSphere cluster. | - Supports the simple deployment objective. - VCF Automation supports scale out and up to a high availability model. | - The simple deployment model defaults to the small appliance size. - Administrators will need to be aware of the scale and performance implications of the small size node to their design. - If deployed VCF Automation through VCF Installer, the installer will deploy the small appliance by default. - If deployed via VCF Operations fleet management, you will have to select the small appliance size to deploy the simple model. |
| VCF-AUTO-REQD-SIM-002 | [Deploy VCF Automation in separate DVPG or NSX Overlay](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking/deploy-vcf-management-components-on-an-nsx-overlay-segment.html) through VCF Operations fleet management Or SDDC Manager API | Supports different network other than default management network for security requirements. | If deployed via VCF Operations fleet management, all the VCF Operations components (to include fleet manager) will need to be fully up and functional prior to starting the VCF Automation deployment. |
| VCF-AUTO-REQD-SIM-003 | Protect the VCF Automation nodes by using vSphere HA. | Ensures availability of VCF Automation without requiring manual intervention during an ESX host failure event. | None. |