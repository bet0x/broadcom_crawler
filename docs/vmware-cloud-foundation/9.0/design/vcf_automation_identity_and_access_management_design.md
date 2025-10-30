---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/vcf-automation-identity-management.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > VCF Automation Identity and Access Management Design
---

# VCF Automation Identity and Access Management Design

As part of the VCF Automation, you configure authentication to grant user access and provide granular control of resources.

VCF Automation contains two persona levels. The provider persona manages the core infrastructure and the tenant / line-of-business (LOB) persona manages the individual tenants within that infrastructure. Each of these personas have different authentication options.

| VCF Automation Personas | Capabilities |
| --- | --- |
| Provider | - Installs and manages core VCF Automation infrastructure - Provider / Enterprise level administrative functions - Manages shared content libraries published to organizations - Creates organizations, assigns resource quotas, regional networking and first tenant user |
| Tenant / LOB | - Manages organizations - Creates and manages projects - Creates and manages vSphere Namespaces - Configures Content Hub - Creates blueprints - Provides organization level user management |

## Provider Persona Attributes

The provider level supports three primary identity providers along with the default local admin account.

| Attribute | Details |
| --- | --- |
| VCF SSO | - Embedded or appliance VCF Identity Broker - Provides consistent SSO across the VMware Cloud Foundation platform - VCF Identity Broker supports multiple different simultaneous LDAP and / or Active Directory connections |
| LDAP | - Allows for the configuration of a single Active Directory or OpenLDAP connection |
| SAML | - Assumes upstream SAML identity provider |
| Default Local Admin Account | - Local admin account created during initial install of VCF Automation - Full admin rights - Only one local admin account allowed |

VCF Automation Provider Authentication Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-PROV-001 | Configure an identity provider for the VCF Automation Provider. | - Allows provider to leverage an enterprise directory. - Enables named access control to Infrastructure level constructs. - Required to provision administrative access to the Provider Administrator Portal for any account other than the default local admin account. | If not configured, the only access to the Provider Administrator Portal will be through the default local admin account created during installation. |
| VCF-AUTO-REQD-PROV-002 | Leverage the VCF Identity Broker identity provider. | - Provides Single Sign-On with the rest of the VMware Cloud Foundation components. - Leverages the authentication direction for VMware allowing support for future enhancements. | None. |

## Tenant Persona Attributes

The tenant level accepts three primary identity providers along with the default local admin account.

| Attribute | Details |
| --- | --- |
| OpenID Connect (OIDC) | - Allows for configuration of a OIDC identity provider |
| LDAP | - Allows for the configuration of a single Active Directory or OpenLDAP connection |
| SAML | - Assumes upstream SAML identity provider |
| First user | - Created during initial deployment of a tenant - Organizational administrator role - Is a local account |

VCF Automation Tenant Authentication Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-AUTO-REQD-TEN-001 | Configure an identity provider for VCF Automation Tenants. | - Allows tenant to leverage enterprise directory. - Enables named access control to tenant level constructs. - Required to provision administrative or user access to the Organization portal for any account other than the first user account established during Organization creation. | If not configured, the only access to the Organization Portal will be through the first user account established during Organization creation. |