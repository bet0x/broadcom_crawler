---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/install-global-manager-appliances.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Install the Active and Standby Global Manager
---

# Install the Active and Standby Global Manager

To use NSX Federation, you must install the Global Manager.

- Verify that your environment meets the requirements for NSX Manager.
- Decide which locations will contain the active and standby Global Manager appliances.

  To consume the latest features of a given NSX version, all Global Manager and Local Manager appliances in an NSX Federation environment must have the same version of NSX installed.

Installing a Global Manager appliance is similar to installing an NSX Manager appliance. The only difference is that when you deploy the appliance, you select NSX Global Manager for the role.

Install a standby Global Manager appliance for high availability and disaster recovery. The standby Global Manager appliance must be installed in a different location with a latency of 500ms or less.

1. To install the first Global Manager appliance on vSphere: [Install NSX Manager and Available Appliances](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances.html#GUID-b8749665-6812-493c-bc81-a4069c4c2467).

   - Select Medium, Large, or Extra Large for the deployment configuration size.
   - Select NSX Federation Global Manager for the Rolename.
2. Log in to the NSX Manager appliance.

   See [Log In to the Newly Installed NSX Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/log-in-to-your-newly-created-nsx-manager.html#GUID-06b390a4-50cc-44bb-b8ee-ef608b1165a6).
3. Configure a compute manager.

   See [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en).

   If you are at this step while installing the standby Global Manager, you must configure a separate compute manager. Do not use the same compute manager that you configured for the active Global Manager.
4. Create a Global Manager cluster. 
   - On vSphere with a compute manager configured: See [Deploy NSX Manager Nodes to Form a Cluster from the UI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-and-available-appliances/deploy-nsx-manager-nodes-to-form-a-cluster-using-ui.html#GUID-9e3d276e-309a-402a-8fc4-da44c47fac4a).
   - On vSphere without a compute manager configured: Repeat the NSX Manager install on vSphere steps to install three appliances, then form the cluster. See [Form an NSX Manager Cluster Using the CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool/deploy-nsx-manager-nodes-to-form-a-cluster-using-cli.html#GUID-3d870057-b9ef-4f40-8ae6-4151181fe0ad).
5. Configure a VIP for the Global Manager cluster.

   See [Configure a Virtual IP Address for a Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/configure-a-virtual-ip-address-for-a-cluster.html).
6. In a different location, install a standby Global Manager appliance and form a cluster by repeating these steps.

Select the designated Global Manager appliance as active and connect it with the standby Global Manager.