---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9/upgrade-to-vcf-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade VMware Aria Automation to VCF Automation 9.0
---

# Upgrade VMware Aria Automation to VCF Automation 9.0

After importing and integrating the VMware Aria Automation instance into VCF Operations, proceed to upgrade the instance.

If after completing the import process, you realize that your upgrade cannot continue due to specific endpoints, delete Automation from VCF Operations and import VMware Aria Automation back into VMware Aria Suite Lifecycle .

To upgrade to VCF Automation, you must have the following service account permissions:

- ServiceAccount.Administer
- ServiceAccount.ManageAccount
- ServiceAccount.ManagePassword

Upgrading to VCF Automation starts with creating an upgrade plan. This ensures that the correct binary is mapped to the upgrade. After creating the plan, you start the upgrade process.

1. On the Components tab under Fleet ManagementLifecycle, automation appears as an integrated component. Click Plan Upgrade.
2. In the Plan Upgrade window that appears:
   1. Use the drop down menu to select the Target Version, such as 9.0.0.0 for the automation component.

      If the drop down menu is empty, the mapped binaries are incorrect. For example, install binaries might have been mapped instead of upgrade binaries. To display the correct target versions, you must download the correct binary type. See [Downloading VCF management components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).
   2. Click Create Plan.

      On the Components tab, the action for the automation component changes from Manage to Upgrade.
3. Click the Upgrade action button for automation.
4. On the Proceed to Upgrade advisory that appears:
   1. Click the checkbox to acknowledge the warnings about upgrade failures or broken integrations.
   2. Click Trigger Inventory Sync.
   3. After inventory sync complete successfully, click Proceed.

   The upgrade process begins. Most fields are automatically completed with values discovered and imported from the integrated Aria Automation instance, so you can accept default values at each stage or input new values, if needed.
5. Infrastructure includes the following prepopulated settings for your review.

   - Deployment Target: vCenter where VMware Aria Automation is deployed.
   - Select Cluster
   - Select Folder (optional)
   - Select Resource Pool (optional)
   - Select Network
   - Select Datastore
6. Network includes the following pre-populated settings for your review.

   - Domain Name
   - Domain Search Path
   - DNS Servers: If no DNS servers are listed, click to add a new server.
   - Time Sync Mode
   - NTP Servers: If no NTP servers are listed, click to add a new server.
7. Components include the following settings:

   - FQDN: Use the prepopulated VCF Automation FQDN.

     - Certificate: Use the prepopulated certificate.
     - Password: Select the password to be used for the VCF Automation vmware-system-user and admin accounts. If the desired password is not a selection, click ADD PASSWORD at the upper right and enter a 15 character password.
   - Cluster FQDN (for clustered deployments): Use the pre-populated VCF Automation FQDN.
   - Controller type:
   - Node Prefix: Enter a user-defined prefix for naming newly deployed VCF Automation virtual machines. To avoid conflicts and maintain proper node identification within the cluster, ensure that the node prefix is unique.
   - Primary VIP: The IP address of the first node in the VMware Aria Automation instance.
   - Internal Cluster CIDR: Choose a CIDR block that does not conflict with your existing infrastructure.
   - Additional VIPs: The IP addresses of the second and third nodes in the VMware Aria Automation instance.
   - Cluster Node IP Pool: Enter the IP addresses to use for deploying the new virtual machines that will host the VCF Automation components. The number of IP addresses depends on the size of your deployment:

     - For a small deployment, enter two IP addresses.
     - For a medium or large deployment, enter four IP addresses.

     When entering values for the Cluster Node IP Pool, note how an Aria Automation 8.x deployment will be transitioned into VCF Automation 9.0.

     | Automation deployment | 8.x cluster size | 9.0 cluster size |
     | --- | --- | --- |
     | Small, single node | Medium | Small (1-node) |
     |  | Extra large | Large (3-nodes) |
     | Clustered, three nodes | Medium | Medium (3-node) |
     |  | Extra large | Large (3-nodes) |

     VMware Aria Suite Lifecycle 8.
8. Click RUN PRECHECK.

   If the data validation is not successful, perform the recommended actions and run the precheck again.
9. After a successful precheck run, review the upgrade summary and click Submit.

An upgrade takes approximately one hour to complete. If the upgrade does not succeed, perform the following steps to remove the new VCF Automation instance:

1. Power on the existing Aria Automation 8.x
2. Use VMware Aria Suite Lifecycle 8.18 Patch 2 or later to import Aria Automation 8.x and re-register with VMware Identity Manager.
3. [Import and Upgrade VMware Aria Automation in VCF Operations 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html).