---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/single-sign-on-instance-models/external-vidb.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Appliance VCF Identity Broker Model
---

# Appliance VCF Identity Broker Model

To avoid a single point of failure for your authentication services, you can use the Appliance VCF Identity Broker Model, where you deploy a standalone appliance through VCF Operations fleet management prior to performing the VCF Single Sign-On configuration. Use this option if you have critical up-time requirements or a complex multi-instance multi-site VMware Cloud Foundation platform.

**Appliance VCF Identity Broker Model**

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/efd225d0-7475-47f3-8d78-70520c06d23f.original.svg)

## Appliance VCF Identity Broker Model Attributes

The Appliance VCF Identity Broker Model has the following attributes.

| Attribute | Detail |
| --- | --- |
| Service Location | VCF Identity Broker runs as stand alone appliance. |
| Deployment mechanism | Deployed through VCF Operations fleet management prior to VCF Single Sign-On configuration. |
| Number of Nodes | three node cluster. |
| Deployment Timing | Day 2 Operation |
| Scale considerations | It is recommended that one VCF Identity Broker support up to 5 VCF instances. |
| Supported services | For support directories and IdPs, see [Identity Providers and Protocols Supported for Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/protocols-suported-for--sso.html). |
| Backup and restore | Independent Backup/Restore process. |
| High Availability | High Availability is provided by a distributed 3 node deployment running each node on separate vSphere hosts. |
| Operational Impacts | As an isolated, external service, operational tasks performed on vCenter do not impact the authentication stack of the VMware Cloud Foundation components. |
| Migration path | To migrate from the appliance to embedded requires a reset of the VCF Single Sign-On configuration. Users must be re-added to components. |

## Appliance VCF Identity Broker Model Design Requirements

Appliance VCF Identity Broker Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implications |
| --- | --- | --- | --- |
| VCF-SSO-REQD-EXT-001 | Deploy the appliance VCF Identity Broker in the first management domain vCenter. | - Provides high availability to the authentication source for a VCF Instance. - Provides additional scale. | Increases the operational overhead of managing the VCF Identity Broker service. |
| VCF-SSO-REQD-EXT-002 | Connect the appliance VCF Identity Broker to your corporate IdP. | Provides directory services (users and group) and user authentication service to the VCF Identity Broker service. | None. |