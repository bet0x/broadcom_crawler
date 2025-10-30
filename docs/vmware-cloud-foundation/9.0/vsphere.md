---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-in-vcf.html
product: vmware-cloud-foundation
version: 9.0
section: vSphere
breadcrumb: vSphere
---

# vSphere

Use **vSphere** as a VI administrator to virtualize physical infrastructure into managed CPU, storage, and networking resources.

The two core components of VMware vSphere are ESX and vCenter. ESX is the virtualization platform where you create and run virtual machines and virtual appliances, Kubernetes workloads, and AI/ML workloads. vCenter is the service through which you manage multiple hosts connected in a network and pool host resources.

vSphere manages large collections of infrastructure, such as CPUs, storage, networking, GPUs, and DPUs as a seamless and dynamic operating environment, and also manages the complexity of a data center.

| vSphere Functional Area | Capabilities |
| --- | --- |
| Lifecycle management of vSphere | - Lifecycle management via pre-staging ESX images, remediating hosts in parallel, and by applying updates in parallel across clusters. - vSphere can manage infrastructure images to patch, update, or upgrade clusters using a desired state model. - vSphere can reduce maintenance windows via reduced downtime upgrades for vCenter as well as live patching for ESX for near zero downtime for security patches. |
| Workload performance | - With its GPU support, vSphere improves workload performance for modern AI workloads - vSphere on DPUs (VMware vSphere® Distributed Services EngineTM) helps accelerate infrastructure network functions on the Data Processing Unit (DPU) by utilizing available CPU cycles achieve higher workload consolidation per host. - Distributed Resource Scheduler (vSphere DRS) enables automatic load balancing of resources allocated to workloads in a vSphere cluster. Storage DRS optimizes VM data placement as the VM is created and used over time. |
| Business continuity | - High Availability with vSphere automatically restarts your VMs following physical machine failure. - Fault Tolerance provides continuous availability of any application in the event of a hardware failure with no data loss or downtime. - vMotion enables live migration of virtual machines with no disruption to users or loss of service, eliminating the need to schedule application downtime for planned server maintenance. Storage vMotion avoids downtime for planned storage maintenance. |
| Built-in security | - Identity federation with Microsoft Entra ID (formerly Azure AD), ADFS and Okta: Secure access and account management. - Virtual Machine Encryption: Data-at-rest encryption for virtual machine data and disks. - vSphere Trust Authority: Remote attestation for sensitive workloads. |

## vSphere Documentation

For information about the built-in vSphere capabilities, see the [vSphere documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0.html).

## Using the VCF Capabilities for vSphere

VCF fully automates vCenter deployment and management in all infrastructure management including deploying VCF, licensing, and adding workload domains, vSphere clusters and hosts to your environment. See the following documentation for information on these management and operational capabilities..

| Learn More About | Documentation |
| --- | --- |
| Deploying a new VCF platform or using existing vSphere infrastructure to deploy a new VCF platform or VCF instance | [Deployment, Convergence, and Upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment.html) |
| Adding workload domains, clusters and ESX hosts | [Building Cloud Infrastructure](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure.html) |
| Managing licenses | [Licensing](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing.html) |
| Integrating cloud infrastructure in VCF Automation if you are a provider administrator | [Provider Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/provider-management.html) |
| Performing operational and monitoring tasks on cloud infrastructure | - [Fleet Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management.html) - [Infrastructure Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations.html) |