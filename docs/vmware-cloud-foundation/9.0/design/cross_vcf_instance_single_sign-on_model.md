---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/one-sso-deployment-per-vcf-estate.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Cross VCF Instance Single Sign-On Model
---

# Cross VCF Instance Single Sign-On Model

The Cross VCF Instance Single Sign-On Model, includes multiple VCF Identity Broker instances. Each VCF Identity Broker instance serves a defined set of VCF instances in the same VCF fleet. VCF management components, such as VCF Operations and VCF Automation, can connect to only one of VCF Identity Broker instances for Single Sign-On.

Cross VCF Instance Single Sign-On Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6fc84bdf-6e70-49fc-b308-a0d37c746cb1.original.svg)

Cross VCF Instance Single Sign-On Model Attributes



| Attribute | Detail |
| --- | --- |
| Scale | **Balanced Scale -** A single VCF Identity Broker services a set of VCF Instances in your VCF fleet. |
| Resources requirements | **Balanced Resource Footprint** - Additional VCF Identity Broker deployment will require additional compute / memory / storage. |
| Operational Overhead | **Balanced Operational Overhead** - Additional VCF Identity Broker will need to managed separately for operational tasks such as backup / restore. |
| Availability | **Balanced Availability per Private Cloud** - A single VCF Identity Broker servicing a set of VCF Instances in the VCF fleet. |
| Blast Radius | **Balanced Blast Radius** - An outage of your VCF Identity Broker deployment will impact authentication across a set of VCF Instances connected to this VCF Identity Broker. |
| Single Sign-On scope | **Balanced SSO Scope** - With one VCF Identity Broker deployment for a set of VCF Instances, users authentication will carry across instances in the same fleet requiring no additional re-authentication. |

Cross VCF Instance Single Sign-On Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-VCI-001 | Deploy VCF Identity Broker in the management domain of a VCF Instance. | - Provides an authentication source for the VCF Instance. - Provides VCF Single Sign-On capabilities to the VCF Instance. | All VMware Cloud Foundation platform components will use the same authentication source. |
| VCF-SSO-REQD-VCI-002 | Configure additional VCF Instances in the same VCF fleet to consume the same VCF Identity Broker configured in the first VCF Instance. | - Provides an authentication source for all components in the configured VCF Instances. - Provides VCF Single Sign-On capabilities to all components in the configured VCF Instances. | Any impact to the VCF Identity Broker service will impact all VCF Instances configured to use it. |