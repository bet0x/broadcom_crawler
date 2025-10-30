---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking/deploy-vcf-management-components-on-an-nsx-vlan-segment.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy VCF Management Components on an NSX VLAN Segment
---

# Deploy VCF Management Components on an NSX VLAN Segment

Use the SDDC Manager API to deploy the VCF management components on an NSX VLAN segment. The VCF Operations collector appliances are deployed to the VM management network.

- Review Design Guide. See [Fleet Level Components on NSX VLAN Segment Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/fleet-level-components-on-nsx-segment-using-vlan-model.html).
- Download binaries for the VCF management components to SDDC Manager.
- Create a VLAN transport zone in the management domain NSX Manager. See [Create Transport Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html).
- In NSX Manager, create a segment on the newly created VLAN transport zone. See [Create an NSX Segment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-segment.html) .
  - For the Transport Zone, select the VLAN transport zone.
- In NSX Manager, attach the VLAN transport zone to transport node profile for the management domain primary cluster.

Use this procedure to configure all VCF management components (VCF Operations, VCF Operations fleet management, and VCF Automation) to use an NSX VLAN segment. The VCF Operations collector appliances are deployed to the VM management network.

See the [SDDC Manager API Reference Guide](https://developer.broadcom.com/xapis/sddc-manager-api/latest/vcf-management-components/) for more information.

1. Create a JSON file with information about the VCF management components to use for deployment.

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
               "10.11.99.51",
               "10.11.99.52",
               "10.11.99.53",
               "10.11.99.54"
           ],
           "nodePrefix": "flt-auto",
           "hostname": "flt-auto01.rainpole.io",
           "internalClusterCidr": "198.18.0.0/15",
           "adminUserPassword": "<password>"
       },
       "vcfMangementComponentsInfrastructureSpec": {
           "localRegionNetwork": {
               "networkName": "<VM-Management-port-group-name>",
               "subnetMask": "255.255.255.0",
               "gateway": "10.11.10.1"
           },
           "xRegionNetwork": {
               "networkName": "<vlan-segment-name>",
               "subnetMask": "255.255.255.0",
               "gateway": "10.11.99.1"
           }
       }
   }
   ```

   Replace <vlan-segment-name> with the name of the VLAN segment.

   You can use the same segment for both localRegionNetwork and xRegionNetwork.
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