---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-identity-management/vcf-aution/vcf-a-auth-sp-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Service Provider Authentication Design
---

# VCF Automation Service Provider Authentication Design

The VCF Automation Service Provider Authentication Model configures the provider and tenant to authenticate to different identity providers.

VCF Automation Service Provider Authentication Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/84b79691-08bc-4d1a-b249-f9b76dd20a10.original.svg)

## VCF Automation Service Provider Authentication Design Attributes

| Attribute | Detail |
| --- | --- |
| Provider | - The provider organization connects to the VCF Identity Broker service. - The VCF Identity Broker sources the users and group from the identity provider. - The provider uses a different identity provider than the tenant. |
| Tenant | - The tenant organization connects directly to the identity provider through OIDC or SAML. - The tenant uses a different identity provider than the provider. |
| Single Sign-On scope | - The provider log-ins have Single Sign-On with the rest of VCF components. - The tenant log-ins do not have Single Sign-On with the rest of VCF components. |

## VCF Automation Service Provider Authentication Model Options

A VCF Automation Service Provider Authentication Modelcan leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| VCF Identity Broker models | - [Embedded VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/embedded-vidb.html) - [Appliance VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html) |

## VCF Automation Service Provider Authentication Design Requirements

VCF Automation Service Provider Authentication Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-IDP-002 | The provider uses a different IdP than the tenant. | - Supports separate authentication mechanisms for provider and tenant. | None |