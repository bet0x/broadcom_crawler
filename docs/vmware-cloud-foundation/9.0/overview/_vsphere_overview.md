---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation/vsphere.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview >   vSphere Overview
---

# vSphere Overview

Virtualize physical infrastructure into managed CPU, storage, and networking resources.

The two core components of VMware vSphere® are VMware® ESX and VMware® vCenter®. ESX is the virtualization platform where you create and run virtual machines and virtual appliances, Kubernetes workloads, and AI/ML workloads. vCenter is the service through which you manage multiple hosts connected in a network pool host resources.

vSphere manages large collections of infrastructure, such as CPUs, storage, networking, GPUs, and DPUs as a seamless and dynamic operating environment, and also manages the complexity of a data center.

## Lifecycle Management of vSphere

- Lifecycle management via pre-staging ESX images, remediating hosts in parallel, and by applying updates in parallel across clusters.
- vSphere can manage infrastructure images to patch, update, or upgrade clusters using a desired state model.
- vSphere can reduce maintenance windows via reduced downtime upgrades for vCenter as well as live patching for ESX for near zero downtime for security patches.

## Workload Performance

- With its GPU support, vSphere improves workload performance for modern AI workloads
- vSphere on DPUs (VMware vSphere® Distributed Services EngineTM) helps accelerate infrastructure network functions on the Data Processing Unit (DPU) by utilizing available CPU cycles achieve higher workload consolidation per host.
- Distributed Resource Scheduler (vSphere DRS) enables automatic load balancing of resources allocated to workloads in a vSphere cluster. Storage DRS optimizes VM data placement as the VM is created and used over time.

## Business Continuity

- High Availability with vSphere automatically restarts your VMs following physical machine failure.
- Fault Tolerance provides continuous availability of any application in the event of a hardware failure with no data loss or downtime.
- vMotion enables live migration of virtual machines with no disruption to users or loss of service, eliminating the need to schedule application downtime for planned server maintenance. Storage vMotion avoids downtime for planned storage maintenance.

## Built-in Security

- Identity federation with Microsoft Entra ID (formerly Azure AD), ADFS and Okta: Secure access and account management.
- Virtual Machine Encryption: Data-at-rest encryption for virtual machine data and disks.
- vSphere Trust Authority: Remote attestation for sensitive workloads.

## vSphere Documentation

For information about the built-in vSphere capabilities, see the [vSphere documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0.html).