---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/sso-architecture.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management >   VCF Single Sign-On Architecture
---

# VCF Single Sign-On Architecture

VCF allows organizations to configure VCF Single Sign-On across a fleet of VCF Instances based on your preference for manageability and availability.

You can deploy one or more VCF Identity Brokers across VCF Instances. There are two potential designs for VCF Single Sign-On configuration which depend on the deployment of VCF Identity Brokers across VCF Instances. The VCF Single Sign-On configuration options are as follows:

1. **VCF Single Sign-On configuration across components within a single VCF Instance**

   The components of a single VCF Instance are connected to one VCF Identity Broker.
2. **VCF Single Sign-On configuration across a set or entire fleet of VCF Instances**

   The components across multiple VCF Instances are connected to one VCF Identity Broker.

The deployment mode you choose does not affect the design of VCF Single Sign-On configuration. VCF Single Sign-On configuration strategies can vary from one organization to another. You can either:

- Connect one VCF Identity Broker (embedded) per VCF Instance, and/or,
- Connect one VCF Identity Broker (appliance) to a maximum of five VCF Instances.

## **VCF Single Sign-On Configuration Across Components Within a Single VCF Instance**

VCF Single Sign-On Configuration Across Components Within a Single VCF Instance

The following diagram illustrates a configuration where a VCF Identity Broker is configured for each VCF Instance, activating VCF Single Sign-On across components for the specific VCF Instance.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/25865d5c-78fc-4594-9fc8-1ed4424fc444.original.svg)

## **VCF Single Sign-On Configuration Across a Set or Entire Fleet of VCF Instances**

VCF Single Sign-On Configuration Across a Set or Entire Fleet of VCF Instances

The following diagram illustrates a VCF Single Sign-On configuration where a single VCF Identity Broker is connected to more than one VCF Instance.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/767746d7-a933-49db-b964-b129a4cf7c99.original.svg)