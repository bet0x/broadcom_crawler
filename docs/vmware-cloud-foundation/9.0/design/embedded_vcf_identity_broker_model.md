---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/embedded-vidb.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Embedded VCF Identity Broker Model
---

# Embedded VCF Identity Broker Model

The Embedded VCF Identity Broker Model is the simplest form of configuring VCF Single Sign-On for VMware Cloud Foundation. The deployment fits new VMware Cloud Foundation platforms, or deployments that have lower requirements for availability.

**Embedded VCF Identity Broker Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5a7d23af-32df-486b-827d-f14ebfbcf9d0.original.svg)

## Embedded VCF Identity Broker Attributes

The Embedded VCF Identity Broker Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Service Location | VCF Identity Broker runs as a service within the management domain vCenter. |
| Deployment mechanism | As an embedded service running on vCenter, no additional deployment is required. |
| Number of Nodes | 1 (As part of vCenter) |
| Deployment Timing | As an embedded service running on vCenter, no additional deployment is required. |
| Scale considerations | One VCF Identity Broker per VCF instance. |
| Supported services | For support directories and IdPs, see [Identity Providers and Protocols Supported for Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/protocols-suported-for--sso.html). |
| Backup and restore | As part of the vCenter Backup/Restore. |
| High Availability | High Availability is provided by vSphere HA as this service runs as part of the vCenter appliance. |
| Operational Impacts | As this services run as part of vCenter, maintenance tasks performed on the vCenter instance also impact your ability to authenticate to the VMware Cloud Foundation components. |
| Migration path | To migrate from embedded to the appliance it requires a reset of the VCF Single Sign-On configuration. Users must be re-added to components. |

## Embedded VCF Identity Broker Model Design Requirements

Embedded VCF Identity Broker Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-EMB-001 | Leverage the embedded VCF Identity Broker in the first management domain vCenter. | - Simplifies the authentication configuration for the VMware Cloud Foundation platform. - Simplifies the operational overhead. | - Limits the Scale supported by the embedded model. - Limits the availability of the authentication service in a VMware Cloud Foundation platform. |
| VCF-SSO-REQD-EMB-002 | Connect the embedded VCF Identity Broker to your corporate IdP. | Provides directory service (users and group) and user authentication service to the VCF Identity Broker service. | None. |