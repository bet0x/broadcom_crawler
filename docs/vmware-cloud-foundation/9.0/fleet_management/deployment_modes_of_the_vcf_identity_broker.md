---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/deployment-models-for-sso.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Deployment Modes of the VCF Identity Broker
---

# Deployment Modes of the VCF Identity Broker

When you configure VCF Single Sign-On you can either implement it in embedded mode within the management domain vCenter or deploy it in appliance mode.

## Embedded Deployment Mode

Use the embedded deployment mode if you want to use VCF Identity Broker that is embedded in the management domain vCenter and do not want to deploy a VCF Identity Broker appliance for VCF Single Sign-On configuration. You use the embedded deployment mode typically within a single VCF Instance.

In the embedded deployment mode, the VCF Identity Broker is configured in the management domain vCenter of the VCF Instance.

Embedded Deployment Mode

The following diagram shows the embedded deployment mode where the VCF Identity Broker is configured in the management domain vCenter.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6477d8a0-36b7-4d36-976e-ee10b8ba605a.original.svg)

## Appliance Deployment Mode

VCF Identity Broker is deployed as a stand-alone appliance using VCF Operations fleet management within the management domain of the chosen VCF Instance. VCF Identity Broker appliance is a three-node cluster. Your environment must meet the minimum requirements of the VCF Identity Broker appliance deployed through VCF Operations fleet management.For more details about the minimum requirements, see [Prerequisites for Configuring Single Sign-On using the Appliance Deployment Mode.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso.html#GUID-ec2c7e12-e532-46bf-b08f-6de789b83e3c-en_id-c5679e42-ce64-49da-d98b-5f639ab51213)

Appliance Deployment Mode

The following diagram shows the appliance deployment mode where the VCF Identity Broker is a stand-alone instance deployed as an appliance using VCF Operations fleet management.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/688f6d25-0cd5-4399-9e2f-b095fdc4a37f.original.png)

## Distinguishing Features of the Deployment Modes

The following table provides information that distinguishes the two deployment modes: VCF Identity Broker (embedded) and VCF Identity Broker (appliance).



| Distinguishing Areas | VCF Identity Broker (embedded) | VCF Identity Broker (appliance) |
| --- | --- | --- |
| Deployment location | Deployed in the management domain vCenter of a VCF Instance. | Stand-alone appliance deployed using VCF Operations fleet management in a management domain. |
| Recommendation | Connect one VCF Identity Broker per VCF Instance. | A maximum of five VCF Instances can be connected to one VCF Identity Broker instance. |
| Prerequisites | For more information, see [Prerequisites for Setting Up Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso.html#GUID-ec2c7e12-e532-46bf-b08f-6de789b83e3c-en_id-e44c9d9e-30b8-4c5b-e82f-1c8f628eabe8). | For more information, see [Prerequisites for Setting Up Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso.html#GUID-ec2c7e12-e532-46bf-b08f-6de789b83e3c-en_id-e44c9d9e-30b8-4c5b-e82f-1c8f628eabe8). |
| Cluster size | Embedded vCenter Service | Three-node cluster |
| Reasons to choose a specific deployment mode | Choose the embedded deployment mode if you want to use VCF Identity Broker that is embedded in vCenter.  This can be a single point of failure should the management domain vCenter go down. | - Can handle single node failure. - If you need to connect more than one VCF Instance to the VCF Identity Broker, it is recommended that you use the appliance deployment mode. - If the management domain vCenter is not accessible by some VCF components, choose the appliance deployment mode. |