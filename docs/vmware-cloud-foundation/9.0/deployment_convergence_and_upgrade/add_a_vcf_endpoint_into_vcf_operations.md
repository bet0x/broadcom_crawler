---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/preparing-to-upgrade-to-vmware-cloud-foundation/add-a-vcf-endpoint-into-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Add a VCF Endpoint into VCF Operations
---

# Add a VCF Endpoint into VCF Operations

To integrate VMware Cloud Foundation with VCF Operations, add a VCF endpoint into VCF Operations.

Perform the following steps to add a VCF endpoint and enable collection for that endpoint.

1. Log in to VCF Operations.
2. On AdministrationIntegrations, click Add.
3. Under Account Types, select VMware Cloud Foundation and enter the following information:

   - Cloud Account Information

     - Name: Alias of SDDC-Manager
     - Description
     - Physical Datacenter (Optional)
   - VCF Credentials

     - SDDC Manager: FQDN of the SDDC Manager
     - Credential: If not present, click to add one.
     - Collector/Group: Use the Default Collector Group, or select a cloud proxy.

     Click Validate Connection.

   Click Add to save the adapter instance
4. On AdministrationIntegrations, click to open the VMware Cloud Foundation account. The newly added endpoint appears. Click the ellipses for the endpoint and select Enable Collection.

You configure and deploy the remaining VCF Operations components after the SDDC Manager upgrade. You can now proceed to [Upgrade the Management Domain Core Components to VMware Cloud Foundation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2.html).