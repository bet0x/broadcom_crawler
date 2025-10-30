---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-models/single-single-sign-on-deployment-per-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Single VCF Instance Single Sign-On Model
---

# Single VCF Instance Single Sign-On Model

With this topology each VCF Instance will utilize its own dedicated VCF Identity Broker. The VCF Single Sign-On scope will be limited to the VCF Instance. VCF management components, such as VCF Operations and VCF Automation, can connect to only one of VCF Identity Broker instances for Single Sign-On.

Single VCF Instance Single Sign-On Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1f2ccd85-efa1-4af8-8efa-0d033bf70503.original.svg)

Single VCF Instance Single Sign-On Model Attributes



| Attribute | Detail |
| --- | --- |
| Scale | **High Scale -** A single VCF Identity Broker services each VCF Instance. |
| Resources requirements | **Large Resource Footprint** - Each VCF Identity Broker deployment will require additional compute / memory / storage resources. |
| Operational Overhead | **High Operational Overhead** - Each VCF Identity Broker will need to be managed separately for operational tasks such as backup / restore. |
| Availability | **High Availability per Private Cloud** - A single VCF Identity Broker servicing each VCF Instance. |
| Blast Radius | **Small Blast Radius** - An outage of one VCF Identity Broker instance will only impact logins for the VCF Instance associated with it. |
| Single Sign-On scope | **Small SSO scope** - For each VCF Identity Broker deployment users will have an additional Single Sign-On scope. Moving across instances will require re-entering credentials. |

Single VCF Instance Single Sign-On Design Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-VSI-001 | Deploy VCF Identity Broker in the management domain of the first VCF Instance. | - Provides an authentication service for the first VCF Instance. - Provides VCF Single Sign-On capabilities to the first VCF Instance. | Workload domains will use the same authentication source as management domain. |