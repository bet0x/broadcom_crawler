---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-edge(1)/other-options-with-vcf-edge/2.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Edge Option 3: vSAN Witness Placement for Distributed Edge
---

# VCF Edge Option 3: vSAN Witness Placement for Distributed Edge

Strategically locating the vSAN Witness component outside the primary data-bearing edge sites (e.g., in a central data center or in an independent site) to ensure quorum and data availability in 2-node vSAN edge deployments during site failures.

VCF Edge Option 3: vSAN Witness Placement for Distributed Edge

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6dcf279c-5388-423f-b4f1-7f7fe8ffb49a.original.png)

| Design Requirement | Justification |
| --- | --- |
| Centralized Management | VCF Operation and vCenter are located in a Central DC or Regional DC or a Co-location Facility, managing the edge sites remotely. |
| 2 Node vSAN at Edge Sites | Each edge site has its own vSAN storage.  Provides the local storage capacity and performance required for the VMs and container to run at each edge location. |
| vSAN Witness VM placement | **Option 1: vSAN Witness VM in the Central DC/Regional DC/Co-location Facility.**  This location offers maximum isolation from the potential failure domains of both edge sites, providing the highest level of resilience.  **Option 2: If a Central DC/Regional DC/Co-location Facility is unavailable, implement a cross-site Witness VM configuration.**  Hosting Site A's Witness VM on Site B and vice versa provides a degree of resilience against a single site failure when a dedicated third location is not feasible. However, be mindful of potential network latency between the sites.  **Option 3: Embedded Witness Host - If using embedded hardware specifically designed for a vSAN Witness, consider local hosting at the Edge.**  Embedded Witness appliances are often lightweight and designed for remote locations. However, carefully consider the management and potential single point of failure if the entire physical host housing the embedded Witness fails. This option should be evaluated based on specific hardware capabilities and risk tolerance. |
| Deployment and Licensing | VCF Operation is the mandatory requirement along with vCenter to support this design.  Please deploy VCF Operation and vCenter manually or Using VCF installer with VVF option and then entitle VCF Edge license with VCF Operation. |
| VSAN Witness Licensing | To license vSAN Witness:1) Attach your vSAN Witness Host or Appliance to the vCenter2) Assign your vSAN license to the vCenter3) The Witness host or appliance will be automatically licensed. vSAN Witness host cores do NOT consume capacity from your license capacity. |
| Network Connectivity | Latency and Bandwidth: 100 ms / 10Mbps required for connection between vCenter to the ESXi hosts. |