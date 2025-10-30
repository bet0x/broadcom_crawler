---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/getting-started-with-vcf.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview > Getting Started with VMware Cloud Foundation
---

# Getting Started with VMware Cloud Foundation

You start building a VCF platform by deploying a new platform, converging your existing virtual infrastructure to VCF, or upgrading existing your VCF platform. After you deploy your VCF Instances and VCF fleet, you can continue with adding workload domains and integrating them in VCF Automation for end-user consumption.

In this article:

- [Deploy a VCF Fleet or a VCF Instance](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-9d016632-d79b-4c8d-b489-d72dc3d9fce9)
- [Add Workload Domains to a VCF Instance](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-f574ab7f-cd7d-4635-e488-c5a84d28e81f)
- [Add a vCenter Instance to the VCF Fleet](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-9773d2e3-8350-4b75-b944-6e54b5b14479)
- [Complete the Configuration of the VCF Fleet, VCF Instances, and Workload Domains](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-b16e1152-fd4f-4189-a631-f4e4e3ef78aa)
- [Add Workload Domains to Your Cloud Organization Structure](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-0b09e119-51e3-4615-c8d7-a88da4056aff)
- [Detailed Journeys](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-256e994e-3670-45f1-d8b4-8a4bfb29817b)
- [Design Blueprints](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-fbab952b-9092-45a5-f7ca-6986e4103066)
- [List of VCF Capabilities](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-23ea50c3-3c62-4a0e-f590-4c5b8c8227c5)
- [What to Do Next](#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-412d3bd5-c814-4aff-fc44-e9642615df1b)

## Deploy a VCF Fleet or a VCF Instance

The first step in building a VCF platform is deploying a VCF fleet or a VCF Instance in a VCF fleet.

| Operation Type | Options |
| --- | --- |
| [Deploying a New VMware Cloud Foundation or vSphere Foundation Private Cloud](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-.html). | - Deploy a new VCF fleet.  You deploy the components of the VCF fleet and of the first VCF Instance with the initial management domain. In addition to the management components of the VCF Instance, the initial management domain hosts the components of the VCF fleet too. - Deploy a new VCF Instance within an existing VCF fleet.  You deploy a VCF Instance with its management domain. |
| [Converging Your Existing Virtual Infrastructure to VMware Cloud FoundationPlatform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/supported-scenarios-to-converge-to-vcf.html). | - Converge to a new VCF fleet.  You can use VMware Aria Operations and other VMware Aria Suite components in your environment as the VCF fleet. The vCenter instance and ESX hosts running VMware Aria Operations become the first VCF Instance with the initial management domain.  If your environment does not have VMware Aria Operations, then you can make a vCenter and its managed hosts the first VCF Instance and deploy VCF Operations and the other required fleet components on it. - Converge to a new VCF Instance within a VCF fleet.  You can add a vCenter and its managed ESX hosts as a VCF Instance with its management domain that is managed by an existing VCF fleet. |
| [Upgrade Your Management Domain to VCF](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation.html). | - Upgrade the existing VMware Aria components and management domain components. Then, deploy the rest of the VCF fleet components that you need. - If VMware Aria Operations is not included in your VCF 5.2 environment, deploy VCF Operations and then VCF Operations fleet management. Then, upgrade the the other VMware Aria components in your environment and the management domain. Deploy the rest of the VCF fleet components that you need. |

## Add Workload Domains to a VCF Instance

After you deploy the VCF fleet and VCF Instances, you can start adding workload domains with infrastructure for consumer workloads to the VCF Instances in one of the following ways:

- [Deploy new workload domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains.html).

  As part of workoad domain deployment, you can enable vSphere Supervisor with NSX VPC on the initial cluster of the workload domain. You can then add the initial infrastructure of the workload domain to VCF Automation.
- [Import vCenter instances, managing consumer workloads, as workload domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/import-an-existing-vcenter-to-create-a-workload-domain.html).

  You can import components that are compatible with VCF 5.x and upgrade to version 9.0 after you import them as a workload domain.

## Add a vCenter Instance to the VCF Fleet

You can add virtual infrastructure under a vSphere Foundation license to a VCF fleet. See [vSphere as a data source in VCF Operations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere.html)

## Complete the Configuration of the VCF Fleet, VCF Instances, and Workload Domains

After you deploy the VCF fleet or VCF Instance or add a workload domain to a VCF Instance, complete its configuration by performing the following tasks. Assigning a license must be done right after you complete deployment.

- [Assign a license to the VCF fleet, VCF Instance or workload domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing.html).
- [Configure depot settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components.html).
- [Deploy VCF Identity Broker](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-identity-broker.html) and [configure identity and access management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html).
- [Configure backup of the management components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation.html).
- [Configure certificate management in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0.html).
- [Configure password management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords.html).
- [Add clusters and individual ESX hosts to your VCF domains](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/expand-a-workload-domain.html).

## Add Workload Domains to Your Cloud Organization Structure

You can add workload domains to an organization in VCF Automation provider management for consumption by end users. You can create two types of organizations in VCF Automation - All Apps Organizations for workload domains with Supervisor clusters that run both containers and VMs, and a VM Apps Organization for workload domains with clusters that run only VMs.

You cannot use the same workload domain in an All Apps Organization and a VM Apps Organization.

1. [Deploy an NSX Edge cluster and set up network connectivity in the workload domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter.html) and [create Virtual Private Cloud (VPCs) in vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter.html).
2. [Deploy a Supervisor with NSX VPC](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration/supervisor-networking-with-virtual-private-clouds/deploy-a-supervisor-with-nsx-vpc.html).
3. [Add an identity provider for your organizations.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/provider-management/managing-identity-providers-in-vcd.html)
4. [Create organizations for all applications for the workload domains with Supervisor instances.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/provider-management/managing-organizations/create-an-organization.html)
5. [Create an organization for VM applications for the workload domains that do not run Supervisor instances.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/provider-management/managing-organizations/create-an-organization-for-vm-apps.html)

## Detailed Journeys

For visual guides to the sequences of getting started operations, see the following VCF journey maps.

- [Build Journey - Install a New VMware Cloud Foundation Deployment](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vcf-deploy-journey.pdf)
- [Build Journey - Converge Your Infrastructure to VMware Cloud Foundation from Existing vSphere and VMware Aria Operations](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vcf-converge-from-vsphere-aria-operations-journey.pdf)
- [Holistic Journey - Fully Adopt VMware Cloud Foundation from Existing vSphere and VMware Aria Operations](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-holistic-from-vsphere-aria-operations-end-to-end-journey.pdf)

## Design Blueprints

You can apply a pre-defined architecture for your specific business and technology requirements. See [Design Blueprints for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/blueprints.html).

## List of VCF Capabilities

For a detailed list of capabilities and links to the documentation for them, see [Capabilities by Job Function](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/vcf-capabilities.html).

## What to Do Next

Share the details of the organizations you created in VCF Automation provider management with the administrators for those organizations. Organization administrators can start distributing the infrastructure and configuring access management to the groups in their organizations by using the organization management functionality in VCF Automation. See [Managing Organizations for All Apps in VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/organization-management/managing-organizations-for-all-apps-in-vcf-automation.html) and [Managing Organizations in VCF Automation for VM Apps](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/organization-management/vcfa-overview.html).