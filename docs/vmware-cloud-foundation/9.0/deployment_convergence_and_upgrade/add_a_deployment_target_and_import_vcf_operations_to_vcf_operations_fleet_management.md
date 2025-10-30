---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/finish-configuring-newly-deployed-vcf-operations-instance-as-part-of-upgrade/add-deployment-targets.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Add a Deployment Target and Import VCF Operations to VCF Operations fleet management
---

# Add a Deployment Target and Import VCF Operations to VCF Operations fleet management

Use VCF Operations to add vCenter deployment targets. Then import the VCF Operations component into fleet management.

- After integrating your VCF instance in VCF Operations, wait at least 15 minutes for the VCF endpoint that you added to VCF Operations to complete a collection cycle.
- Verify that SSH is enabled on the nodes for import.
- Verify that you have upgraded to SDDC Manager 9.0.

The deployment target is the vCenter instance where the VCF Operations instance is deployed. Perform the following steps to add that vCenter to the fleet management appliance inventory and import VCF Operations into VCF Operations fleet management.

1. Log in to VCF Operations.
2. Add the vCenter instance as a deployment target.
   1. Select Fleet ManagementLifecycle, and click the Settings tab.
   2. Under Preferences, select Deployment Targets and click Add Deployment Target.
   3. Add the information for the deployment target.

      - Select the vCenter where VCF Operations is deployed or go to AdministrationIntegrations to add it.

        To add the deployment target, the SDDC and vCenter must be version 9.0 or later.
      - Click Validate.
      - Click Add.

   The vCenter is added to the fleet management appliance inventory.
3. Import VCF Operations in the fleet management appliance.
   1. Select Fleet ManagementLifecycle and click the Overview tab.
   2. On the VCF Operations component tile, Pending Import appears. Click Import.
   3. For configuration, add component properties. Most fields are prepopulated and require no action.

      - VCF Operations FQDN.
      - Admin password of VCF Operations.
      - Root password of VCF Operations. Select the root password that is being used. If the root password is the same as the admin password and the admin password is not listed as an option, click ADD PASSWORD to enter the Operations Admin password.
      - vCenter Server. Check the box next to the name of the vCenter that was added as a deployment target.
      - Accept the certificate.
   4. Review the summary and click Submit.

      If the workflow fails while looking for a new VCF collector, select a new Management vCenter and click Submit.

   After VCF Operations is imported, it becomes a component that you can manage in VCF Operations fleet management. As examples of the types of Day-N operations that you can manage, see [Scaling Up and Scaling Out Management Nodes in VCF](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/scaling-up-and-scaling-out-management-nodes-in-vcf.html).