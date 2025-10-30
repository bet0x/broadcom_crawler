---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-installer.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > VCF Installer
---

# VCF Installer

VMware Cloud Foundation 9.0 ships with VCF Installer, which is a new virtual appliance that provides automated deployment and configuration workflows for the VCF environment. VCF Installer 9.0 replaces the Cloud Builder appliance and Deployment Parameter Worksheet. You can download it from the [Broadcom Support portal](http://support.broadcom.com/).

With the VCF Installer, you can perform the following actions:

- Deploy and configure new VMware Cloud Foundation or vSphere Foundation environments with different deployment models, storage, and networking configuration.
- Converge existing vSphere infrastructure or vSphere Foundation platform to a VMware Cloud Foundation platform.
- Download all necessary install binaries and deploy patched versions of VCF components.
- VCF Installer is now part of the VCF SDK, available with both Python and Java bindings. It is also integrated with PowerCLI and provides a comprehensive OpenAPI 3.0 specification, enabling additional custom automation to the VCF Installer APIs.
- Deploy new VMware Cloud Foundation environment with Link Aggregation Control Protocol (LACP) as teaming policy. This operation can only be performed through the API.

**VCF Converge**

With VCF 9.0, you can converge an existing vSphere infrastructure into a new or existing VMware Cloud Foundation instance.

The converge process supports a broad range of topologies and relaxes many of the constraints from previous releases. You can use the VCF Installer or the VCF Operations to perform this process.

You can now bring in:

- vSphere clusters with shared vSphere Distributed Switches (VDS)
- vSphere clusters with active Link Aggregation Control Protocol (LACP)
- Environments using various external storage options (VMFS and NFS), remote datastores, and vSAN Storage Clusters
- vCenter with NSX environments, including NSX Edge nodes, as Workload Domains
- Two-node remote offices/branch offices (ROBO) vSAN deployments
- vSAN stretched deployments
- Single node vSphere clusters
- Standalone ESX hosts
- ESX hosts with Single PNICs