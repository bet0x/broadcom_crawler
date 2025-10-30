---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/what-is-the-vcf-installer-.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > What is the VMware Cloud Foundation Installer?
---

# What is the VMware Cloud Foundation Installer?

The VMware Cloud Foundation Installer is a single virtual appliance that deploys and configures all the required VMware Cloud Foundation and VMware vSphere Foundation components.

Use the VCF Installer to:

- Download and manage the binaries required to deploy VCF or VMware vSphere Foundation.
- Deploy and configure a new VCF or VMware vSphere Foundation platform. The installation process automates the deployment and configuration of the components in each solution. You can use existing VMware Cloud Foundation Operations and VMware Cloud Foundation Automation instances or deploy new ones.
- Use existing vSphere infrastructure to create a VCF or VMware vSphere Foundation platform.

VCF Installer works with major, minor, and maintenance releases, but does not support express patch releases. After the VCF Installer workflows complete, you can apply express patch releases manually.

Depending on where you deploy it, the same VCF Installer appliance is able to deploy multiple VCF platforms. If you deploy the appliance inside the management infrastructure (on one of the hosts that will form the management domain), then the appliance switches into SDDC Manager mode and can no longer be used in installer mode.

VCF Installer Deployment Scope per Platform



| Component | Component Appliances | VMware Cloud Foundation | | vSphere Foundation |
| --- | --- | --- | --- | --- |
| Simple | High Availability |
| VMware vCenter | vCenter | Yes | Yes | Yes |
| VCF Operations | operations (primary node) | Yes | Yes | Yes |
| operations (replica node) | No | Yes | No |
| operations (data node) | No | Yes | No |
| operations-collector (cloud proxy) | Yes | Yes | No |
| fleet management | Yes | Yes | No |
| VMware NSX | NSX (node 1) | Yes | Yes | No |
| NSX (node 2) | No | Yes | No |
| NSX (node 3) | No | Yes | No |
| VCF Automation | automation | Yes | Yes | No |
| automation | No | Yes | No |
| automation | No | Yes | No |
| SDDC Manager | SDDC Manager | Yes | Yes | No |

The VCF Installer can either deploy the required components or use existing components to create your VCF or VMware vSphere Foundation platform. For scenarios with existing components, see [Converging Existing Virtual Infrastructure to a VCF or a vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-.html).

See [What Is VMware Cloud Foundation?](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation.html) for more information about VCF.

For information about deploying optional components for VCF and vSphere Foundation, see [Completing the Deployment of Your Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html).