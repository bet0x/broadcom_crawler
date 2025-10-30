---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking/deploy-vcf-management-components-with-custom-networking.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy VCF Management Components on the Shared Management Network
---

# Deploy VCF Management Components on the Shared Management Network

Use the SDDC Manager API to deploy the VCF management components using the same distributed port group as the VCF core components.

- Review Design Guide. See [Fleet Level Components on Shared Management Network Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-shared-vm-management-network-model.html).
- Download binaries for the VCF management components to SDDC Manager.

Use this procedure to configure all VCF management components (VCF Operations, VCF Operations fleet management, VCF Operations collector, and VCF Automation) to use the same distributed port group as the core components (for example, vCenter).

See the [SDDC Manager API Reference Guide](https://developer.broadcom.com/xapis/sddc-manager-api/latest/vcf-management-components/) for more information.

1. Create a JSON file with information about the VCF management components to use for deployment.

   Do not include the vcfMangementComponentsInfrastructureSpec section in the JSON file. This ensures that the VCF management components use the same distributed port group as the VCF core components.

   For example:

   ```
   {
       "vcfOperationsFleetManagementSpec": {
           "hostname": "flt-fm01.rainpole.io",
           "rootUserPassword": "<password>",
           "adminUserPassword": "<password>",
           "useExistingDeployment": false
       },
       "vcfOperationsSpec": {
           "nodes": [
               {
                   "hostname": "flt-ops01a.rainpole.io",
                   "rootUserPassword": "<password>",
                   "type": "master"
               },
               {
                   "hostname": "flt-ops01b.rainpole.io",
                   "rootUserPassword": "<password>",
                   "type": "replica"
               },
               {
                   "hostname": "flt-ops01c.rainpole.io",
                   "rootUserPassword": "<password>",
                   "type": "data"
               }
           ],
           "useExistingDeployment": false,
           "applianceSize": "medium",
           "adminUserPassword": "<password>"
       },
       "vcfOperationsCollectorSpec": {
           "hostname": "sfo-opsc01.sfo.rainpole.io",
           "rootUserPassword": "<password>",
           "version": "9.0.0.0",
           "applianceSize": "small"
       },
       "vcfAutomationSpec": {
           "ipPool": [
               "10.11.10.51",
               "10.11.10.52",
               "10.11.10.53",
               "10.11.10.54"
           ],
           "nodePrefix": "flt-auto",
           "hostname": "flt-auto01.rainpole.io",
           "internalClusterCidr": "198.18.0.0/15",
           "adminUserPassword": "<password>"
       }
   }
   ```
2. Log in to the SDDC Manager UI and navigate to Developer Center.
3. Validate your JSON file.

   ```
   POST /v1/vcf-management-components/validations
   ```
4. Deploy the VCF management components.

   ```
   POST /v1/vcf-management-components
   ```
5. When the deployment completes, open the VCF Operations UI to apply licensing and perform other post-deployment configuration.