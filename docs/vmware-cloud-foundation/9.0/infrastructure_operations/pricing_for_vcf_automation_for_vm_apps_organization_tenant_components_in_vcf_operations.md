---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vrealize-automation-8-x/pricing-for-vrealize-automation-8-x-components-in-vrealize-operations-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Pricing for VCF Automation for VM Apps Organization tenant Components in VCF Operations
---

# Pricing for VCF Automation for VM Apps Organization tenant Components in VCF Operations

After you integrate VCF Automation for VM Apps Organization tenant private cloud adapter instances with VCF Operations you can calculate the cost of deployments, projects, and virtual machines of the selected cloud adapter. Pricing provides an overview of the costs related to the cloud environment, cloud resources, and the costs associated with the project.

## How the Pricing Works in VCF Automation for VM Apps Organization Tenant

- VCF Operations understands the constructs defined in VCF Automation for VM Apps Organization tenant and calculates the CPU, RAM, Storage and Additional prices for Projects, Deployments, and virtual machines.
- A single project can have multiple deployments and a single deployment can have multiple virtual machines associated with the deployment.
- Pricing for multiple virtual machines associated with the deployment is the sum of all the resources associated with individual virtual machines.
- If a single project has multiple deployments, then the project pricing is equal to the sum of individual deployments. The deployment can have multiple virtual machines and resources associated with it.
- On day one, the pricing is equal to the cost of resources defined in VCF Operations.
- On day two, the price is calculated using the following formula.
  - Cost of resources for the present day – Cost of resources for the previous day.
- If in case the pricing does not happen as per the definition, then the partial price is set to true, and the pricing is calculated based on the previous days price.
- In VCF Operations, the following new dashboards are included to view the pricing details for the VCF Automation for VM Apps Organization tenant instances.

  - Cloud Automation Environment Overview
  - Cloud Automation Project Cost Overview
  - Cloud Automation Resource Consumption Overview
  - Cloud Automation Top-N Dashboard

## Data Collection Enhancements in VCF Automation for VM Apps Organization Tenant for Pricing in VCF Operations

The following enhancements have been made for the data collection process from VCF Automation for VM Apps Organization tenant for pricing purposes.

- Collect cloud zones with relation to clusters and resources pools from VCF Automation for VM Apps Organization tenant to VCF Operations.
- Collect Projects from VCF Automation for VM Apps Organization tenant with relation to deployments.
- Include project, cloud zone, and blueprint as properties in virtual machines that are deployed in VCF Automation for VM Apps Organization tenant.

## Upfront Price Support for VCF Automation for VM Apps Organization Tenant Private Cloud Components

VCF Operations supports upfront pricing for VCF Automation for VM Apps Organization in the following ways:

- VCF Operations uses rate cards to provide upfront cost estimates of catalog items just before deployment.
- VCF Automation for VM Apps Organization tenant retrieves the deployment cost and estimated cost from VCF Operations.
- VCF Automation for VM Apps Organization tenant user interface allows you to customize the pricing policies and assign them to the projects or cloud zones.
- If VCF Automation for VM Apps Organization tenant does not specify the pricing policy, then the price is calculated using the VCF Operations cost calculation policy.
- If a custom pricing policy is set for a price calculation, then the deployment and upfront catalog price computation is done as per the custom policy.

## Upfront Price Support for VMware Cloud on AWS Resources

VCF Operations supports upfront pricing for VMware Cloud on AWS resources in the following ways:

- VCF Operations supports upfront pricing for VMware Cloud on AWS only if rate-based pricing is configured in VCF Automation for VM Apps Organization tenant for VMware Cloud on AWS resources.
- VCF Operations does not support cost-based computation for VMware Cloud on AWS resources.