---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-and-configuration-of-components-for-advanced-architectures/deploying-vcf-management-components-with-custom-networking/deploy-vcf-management-components-on-an-nsx-overlay-segment.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy VCF Management Components on an NSX Overlay Segment
---

# Deploy VCF Management Components on an NSX Overlay Segment

Use the SDDC Manager API to deploy the VCF management components on an NSX overlay segment.

- Review Design Guide. See [Fleet Level Components on NSX Overlay Segment Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/fleet-level-components-networking-detailed-design/logical-application-virtual-network-design-for-vmware-cloud-foundation.html).
- Download binaries for the VCF management components to SDDC Manager.
- Using the vSphere Client, create an NSX Edge cluster with a centralized transit gateway in the management domain. See [Configure Centralized Network Connectivity with Edge Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/managing-centralized-network-connectivity-with-edge-clusters.html).
  - You can choose Active Active or Active Standby for the high-availability mode.
  - VPC external IP blocks are not required.
- In NSX Manager, create a tier-1 gateway. See [Add an NSX Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html).
  - Set the HA mode to Active Standby.
  - Linked to the tier-0 gateway.
  - Select the Edge cluster you created.
  - Under Route Advertisement, select All Connected Segments and Service Ports.
- In NSX Manager, create a segment on the management domain overlay transport zone. See [Create an NSX Segment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-segment.html) .
  - For the Connected Gateway, select the tier-1 gateway.
  - For the Transport Zone, select the overlay transport zone.
  - For the

Use this procedure to configure all VCF management components (VCF Operations, VCF Operations fleet management, and VCF Automation) to use an NSX overlay segment. The VCF Operations collector appliances are deployed to the VM management network.

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
               "192.168.11.51",
               "192.168.11.52",
               "192.168.11.53",
               "192.168.11.54"
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
               "networkName": "<overlay-segment-name>",
               "subnetMask": "255.255.255.0",
               "gateway": "192.168.11.1"
           }
       }
   }
   ```

   Replace <overlay-segment-name> with the name of the overlay segment.

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