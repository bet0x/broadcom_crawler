---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-identity-management/vcf-aution/vcf-a-auth-enterprise-model.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Enterprise Authentication Design
---

# VCF Automation Enterprise Authentication Design

The VCF Automation Enterprise Authentication Model configures both the provider and tenant to authenticate to the same identity provider.

VCF Automation Enterprise Authentication Model

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9ff0bbb5-09b7-4c95-ad70-87bfc8ad609a.original.svg)

## VCF Automation Enterprise Authentication Design Attributes

A VCF Automation enterprise authentication model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Provider | - The provider organization connects to the VCF Identity Broker service. - VCF Identity Broker sources the users and groups from the identity provider. - The provider uses the same identity provider as the tenant. |
| Tenant | - The tenant organization connects directly to the identity provider through either OIDC or SAML. - The tenant uses the same identity provider as the provider. |
| Single Sign-On scope | - The provider log-ins have Single Sign-On with the rest of VCF components. - The tenant log-ins do not have Single Sign-On with the rest of VCF components. |

## VCF Automation Enterprise Authentication Model Options

A VCF Automation Enterprise Authentication Model can leverage options from the design areas listed below, depending on objectives.

| Design Area | Options |
| --- | --- |
| VCF Identity Broker models | - [Embedded VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/embedded-vidb.html) - [Appliance VCF Identity Broker Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html) |

VCF Automation Enterprise Authentication Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-IDP-001 | The provider uses the same IdP as the tenant. | - Allows consistent authentication across provider and tenant | None |