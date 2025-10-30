---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/chargeback-and-billing.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Chargeback and Billing
---

# Chargeback and Billing

Chargeback is a cost management solution designed to help service providers accurately track and distribute expenses within a private cloud environment. It enables both providers and tenants to gain insights into resource usage and ensures fair cost allocation based on consumption. As a plug-in for tenants, Chargeback provides a metering and billing interface that simplifies usage tracking, measurement, and invoicing for services delivered through VCF Automation and VCF Operation.

Chargeback is an essential component of cloud services, particularly for service providers using VMware Cloud Foundation. It involves assigning the costs of cloud resources and services to the users or departments that actually use them. This practice is critical for both service providers and tenants, as it creates a transparent and clear method for billing and payment.

In older versions of VCF, service providers used VMware Cloud Director (VCD) to handle things like pricing, billing, and dashboards. But in VCF 9.0, these tasks will be managed directly through VCF Automation. This change likely aims to streamline operations, reduce dependencies on external systems, and provide a more integrated experience for providers within the VCF platform.

Figure below describes a high level overview how Chargeback and Billing is integrated part of VCF Operation. VCF Operations acts as the central management hub. It's the starting point for data collection and integration.

**Management Packs (MPs):**

VCF Operations utilizes Management Packs (MPs) to collect data from specific components. These MPs are like plugins or modules that enable integration. Management pack shown here are i) VCF Automation MP, vCenter MP and NSX MP. It shows a one-to-one relationship between each Management Pack and its corresponding component. This suggests a direct integration between each MP and its respective data source.

Chargeback Integration with VCF Operation

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/283b0047-28f7-4495-a673-45f54ee88f73.original.svg)

| Key Use Cases: |
| --- |
| **Flexible Pricing (Rate Cards):**   - Service providers need the ability to set their own prices for different resources (like storage, compute, network) based on regions or quotas. This allows them to offer tailored pricing plans to their customers.   **Accurate Billing (Bills):**   - Providers must be able to generate and provide detailed bills to their customers, showing usage and charges for organizations or specific resource allocations (quotas) in different regions.   **Usage Monitoring (Dashboards):**   - Providers need ready-to-use dashboards that give them a clear view of how their resources are being used by customers.   **Customized Provider Interface (Control Panel and Launchpad):**   - Providers need a customized interface (control panel and launchpad) that allows them to manage and configure their services and resources in a way that suits their specific needs. |

| High-level Steps to Initiate Billing |
| --- |
| **1. VCF Fleet is deployed - VCF Operations and VCF Automation are integrated by default**   - Both VCF Operations and VCF Automation are deployed as part of the VCF Fleet - VCF Automation has a one-to-one integration with VCF Operations, meaning that you can only connect one VCF Automation instance to one VCF Operations instance - VCF Operations automatically collects data from VCF Automation as well as being able to manage functions such as billing (this can be verified in VCF Operations under Administrator > Integrations, then confirm that the VCF Automation for All Apps Organization is collecting data   **2. Create and configure an All Apps Organization**   - Complete initial Organization creation in the VCF Automation Provider Administrator Portal - Complete customization of the Organization as well as deploy any VM or container resources in the VCF Automation Organization Administrator Portal   **3. Create Organization Bill in VCF Operations**   - In the VCF Operations UI, navigate to Capacity > Cost > Bills tab - In the Bills tab,    - Generate a one-time bill   - Schedule a recurring   - Note: The bill can be tied to either the Organization or a Region Qutoa   **4. View Organization Bill in VCF Automation**   - Log in to the VCF Automation Organization Administrator Portal with Organization Admin or Organization Auditor rights, then navigate to Administer > Bills to view any bills associate with the Organization - Note: Organization Users do not have access to billing |