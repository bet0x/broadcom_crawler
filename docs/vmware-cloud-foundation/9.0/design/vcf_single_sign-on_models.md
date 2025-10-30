---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/vmware-cloud-foundation-concepts/auth-design-vcf.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Single Sign-On Models
---

# VCF Single Sign-On Models

Authentication in VMware Cloud Foundation provides identity and access management services to VCF fleet components. You build your authentication design by using three main pillars - your external Identity Provider (IdP), VMware Cloud Foundation Identity Broker, and VMware Cloud Foundation Single Sign-On.

Your corporate identity provider is the centralized source of digital identities for your enterprise, which provides authentication and identity assertion. You connect the corporate identity provider to your VCF fleet components by using VCF Identity Broker. VCF Identity Broker enables a VCF Single Sign-On implementation and streamlines authentication across different VCF fleet components, except for the SDDC Manager. The last pillar of this design uses VCF Single Sign-On to provide centralized authentication, identity federation, and user management.

## VCF Identity Broker Models

The VCF Identity Broker service acts as the single broker for VCF Single Sign-On that all components in a VMware Cloud Foundation platform can authenticate to. It connects to your identity provider or directory, maintains Single Sign-On tokens and validates users as they log into VCF fleet components. VCF Identity Broker is consumed as an embedded service, running on vCenter, or deployed as an appliance with a multi-node cluster.

VCF Identity Broker Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| [Embedded VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/embedded-vidb.html) | - Service deployed as part of vCenter. - High Availability is provided through vSphere HA. | No additional appliance required. | Transitioning from an embedded to an external VCF Identity Broker requires a reset of VCF Single Sign-On. |
| [Appliance VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html) | - Service deployed as a three (3) node cluster. - High Availability is provided through a multi-node deployment. | Ensures availability in the event of ESX host failure events. | Additional resource footprint. |

VCF Identity Broker Models for VMware Cloud Foundation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a9030c92-6fbe-4251-a1ed-61494feee0f6.original.svg)

## VCF Single Sign-On Models

To accommodate multiple VCF Instances as your VMware Cloud Foundation platform grows, you make design decisions regarding the placement and size of the VCF Identity Broker service. These decisions impact the scale, availability, blast radius, and span of your VCF Single Sign-On environment.

VCF Single Sign-On Models in VMware Cloud Foundation



| Model | Attributes | Benefits | Implications |
| --- | --- | --- | --- |
| VCF Fleet-Wide Single Sign-On Model | Single VCF Identity Broker instance per VCF fleet. | Provides VCF Single Sign-On capabilities across all components in VCF fleet. | Single point of failure for the authentication service for a VCF fleet. |
| Cross VCF Instance Single Sign-On Model | Single VCF Identity Broker instance for multiple VCF instances in VCF fleet. | Provides VCF Single Sign-On capabilities across multiple VCF instances in VCF fleet. | Single point of failure for the authentication service for multiple VCF instances in VCF fleet. |
| Single VCF Instance Single Sign-On Model | Single VCF Identity Broker instance per VCF Instance. | ProvidesVCF Single Sign-On capabilities across all components in VCF Instance. | Single point of failure for the authentication service for a VCF Instance. |