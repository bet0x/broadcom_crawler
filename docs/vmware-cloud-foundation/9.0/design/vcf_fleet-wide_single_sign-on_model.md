---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/-fleet.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Fleet-Wide Single Sign-On Model
---

# VCF Fleet-Wide Single Sign-On Model

With this topology each VCF fleet contains a single VCF Identity Broker deployment. A user can log in once and gain VCF Single Sign-On capabilities for all components across all VCF instances in the same VCF fleet.

For each of these VCF Single Sign-On Models, both VCF Identity Broker Models are supported (embedded and appliance), however it is recommended to use the [Appliance VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html) for multi-VCF Instance Single Sign-On deployments due to availability and scale.

VCF Fleet-Wide Single Sign-On Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/97134a1a-9b5c-45cc-8eb7-d98b000ee9e2.original.svg)

VCF Fleet-Wide Single Sign-On Model Attributes



| Attribute | Detail |
| --- | --- |
| Scale | **Low Scale -** A single VCF Identity Broker services all VCF Instances in your VCF fleet. |
| Resources requirements | **Low Resource Footprint** - A single VCF Identity Broker deployment is required for one VCF fleet. |
| Operational Overhead | **Low Operational Overhead** - A VCF Identity Broker per VCF fleet will need to be managed separately for operational tasks such as backup / restore. |
| Availability | **Low Availability per Private Cloud** - A single VCF Identity Broker servicing all VCF Instances in your VCF fleet. |
| Blast Radius | **Large Blast Radius** - An outage of one VCF Identity Broker appliance will impact logins for a single VCF fleet. |
| Single Sign-On scope | **Large SSO Scope** - Users will not need to re-authenticate when moving between different VCF instances within the same VCF fleet.. |

VCF Fleet-Wide Single Sign-On Design Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-VFL-001 | Deploy VCF Identity Broker in the management domain of the first VCF Instance. | - Provides an authentication service for the first VCF Instance. - Provides VCF Single Sign-On capabilities to the first VCF Instance. | Workload domains will use the same authentication source as management domain |
| VCF-SSO-REQD-VFL-002 | Configure additional VCF Instances in the VCF fleet to consume the same VCF Identity Broker configured in the first VCF Instance. | - Provides an authentication source for all components in the VCF fleet. - Provides VCF Single Sign-On capabilities to all components in the VCF fleet. | An impact to the VCF Identity Broker service will impact the VCF fleet. |