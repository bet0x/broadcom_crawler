---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/vcf-management-appliances.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Components Nodes in VCF and vSphere Foundation
---

# Components Nodes in VCF and vSphere Foundation

The functionality of VCF and vSphere Foundation is implemented by a set of components nodes. For VCF, these nodes are deployed in the management domain of the VCF Instances. For vSphere Foundation, you can run the nodes on a management vCenter.

Example VCF Nodes Configuration in a VCF Fleet

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c99bb603-c1e2-495b-96ca-47c4d55c33ee.original.png)

| Component Node | Platform Type | Description |
| --- | --- | --- |
| VCF Operations | - VCF - vSphere Foundation | See [VCF Operations Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vcf-operations-overview.html). |
| VCF Operations collector (also known as VCF Operations cloud proxy) | - VCF | A part of VCF Operations.  Collects and monitors data locally in the VCF Instance. |
| VCF Operations for logs | - VCF - vSphere Foundation | A part of VCF Operations.  Adds intelligent logging and log analysis to VCF Operations. |
| VCF Operations for networks | VCF | Adds intelligent network analytics to VCF Operations. |
| VCF Operations for networks collector | VCF | A part of VCF Operations.  Collects and monitors network data locally in the VCF Instance. |
| VCF Operations fleet management | VCF | A part of VCF Operations.  Provides support for deployment, lifecycle management, and configuration for the VCF Operations, VCF Automation, and VCF Identity Broker. |
| VCF Identity Broker | VCF | Connects an identity provider (IdP) to the components of the VCF fleet for single sign-on. |
| VCF Operations HCX | VCF | A part of VCF Operations.  Supports workload migration between vCenter instances or between clusters. |
| VCF Automation | VCF | See [VCF Automation Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vcf-automation-overview.html). |
| SDDC Manager | VCF | A part of VCF Operations.  Provides support for the following functionality in VCF Operations:   - Lifecycle management for ESX, vCenter, and NSX - Deployment of workload domains - Import of vCenter instances as workload domains - Configuration of vSAN stretched clusters - Automated certificate replacement and password management |
| NSX Manager | VCF | See [NSX Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/nsx-overview.html). |
| NSX Edge | VCF | Provides north-south traffic connectivity between the physical data center networks and the NSX SDN networks, and east-west traffic flow between virtualized workloads. It provides stateful services such as load balancing and DHCP. |
| vCenter | - VCF  - vSphere Foundation | See [vSphere Overview](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vsphere.html). |

For information about the architecture of these nodes, see [VCF Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design.html).

## Component Comparison Between VCF 5.x and VCF 9.0

For users familiar with VCF 5.x, the following table maps components of VCF 5.x to their equivalents in 9.0.

| VCF 5.x Component | VCF 9.0 Component |
| --- | --- |
| VMware Cloud Builder | VCF Installer |
| SDDC Manager | SDDC Manager |
| VMware Aria Operations | VCF Operations |
| VMware Aria Operations for logs | VCF Operations for logs |
| VMware Aria Operations for networks | VCF Operations for networks |
| VMware Aria Lifecycle | VCF Operations fleet management |
| Workspace ONE Access | - |
| - | VCF Identity Broker |
| VMware HCX | VCF Operations HCX |
| VMware Aria Automation | VCF Automation |
| VMware Aria Automation Orchestrator | VCF Operations orchestrator |
| VMware Cloud Director | VCF Automation |
| VMware vSphere with Tanzu/VMware IaaS Control Plane | vSphere Supervisor |