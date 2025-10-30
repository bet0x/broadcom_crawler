---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/managing-public-cloud-endpoints-with-vrealize-automation-8-x-integration.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Managing Public Cloud Endpoints with VCF Automation for VM Apps Organization Tenant Integration
---

# Managing Public Cloud Endpoints with VCF Automation for VM Apps Organization Tenant Integration

With the VCF Operations management pack, you can monitor deployments made to public cloud endpoints such as Amazon Web Services (AWS), Google Cloud Platform (GPC), and Microsoft Azure. You can monitor the performance, health, utilization, and availability attributes of deployments made to public cloud endpoints.

This integration supports the VCF Operations management packs for public clouds – MP for AWS, GCP, and Azure. Hence, the public cloud management packs are a prerequisite for this enhancement.

VCF Operations will display the VCF Automation for VM Apps Organization tenant deployed by public cloud resources as long as the same resources are also monitored by VCF Operations for the respective public cloud management packs.

This enhancement also shows all the cloud accounts and cloud zones that are part of public cloud end points.

To monitor the VCF Automation for VM Apps Organization tenant resources deployed to AWS, GCP, and Azure, you must ensure that the cloud accounts are configured in both VCF Automation for VM Apps Organization tenant and VCF Operations.

## Import Account Functionality

Users may import AWS, Azure, and vCenter accounts automatically through the Import Account option. However, for the GCP account you should manually add the cloud account through Add Account option. The credential used to configure the adapter must match the one used in VCF Automation for VM Apps Organization tenant. The traversal specification of VCF Automation for VM Apps Organization tenant has been enhanced to include details about AWS, Azure, and GCP accounts.