---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/upgrade-to-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade VMware Aria Operations to VCF Operations 9.0
---

# Upgrade VMware Aria Operations to VCF Operations 9.0

The upgrade to VCF Operations 9.0 upgrades your VMware Aria Operations instance to VCF Operations 9, installs the VCF Operations fleet management appliance, and transfers the existing VMware Aria Operations and VMware Aria Automation integrations from the VMware Aria Suite Lifecycle appliance to the newly deployed fleet management appliance. You later use that VCF Operations instance to upgrade other management components.

- Verify that your environment includes VMware Aria Operations version 8.14 or later.
- Verify that you have downloaded the following binary files to the /data partition on your VMware Aria Suite Lifecycle appliance.

  - OVA file: VCF-OPS-Lifecycle-Manager-Appliance-9.0.0.X.XXXXXXX.ova
  - PAK file: Operations-Upgrade-9.0.0.X.XXXXXXXX.pak
- Verify that you have an FQDN for the fleet management appliance. The FQDN must resolve both ways.
- Verify that you have a 15 character or longer password to use for both the root and admin@local users of the VCF Operations fleet management appliance.
- To deploy the VCF Operations fleet management appliance, verify that the following hardware requirements are satisfied:

  - 4 vCPU
  - 12 GB RAM
  - 200 GB Disk

Perform the following steps to upgrade to VCF Operations using the patched version of VMware Aria Suite Lifecycle.

1. Log in to VMware Aria Suite Lifecycle.
2. From the Lifecycle Operations dashboard, navigate to SettingsBinary Mapping and click Product Binaries.
3. To map the binaries, click Add Binaries.

   - In Base Location**,** enter the directory to the binaries or /data and click Discover.
   - Select the VCF-OPS-Lifecycle-Manager-Appliance-9.0.0.X.XXXXXXX.ova and Operations-Upgrade-9.0.0.X.XXXXXXXX.pak files and click Add.

   The binary mapping request begins and takes a few seconds to complete.
4. From the Lifecycle Operations dashboard, click Environments. On the Aria Operations environment, click View Details and select Upgrade.

   The upgrade starts with an inventory sync process that ensures the VMware Aria Suite Lifecycle and the Aria Operations environments are in sync.

   When the Proceed to Upgrade advisory appears, read the recommendation.

   - The recommended action is to click Trigger Inventory Sync and click Submit. After the inventory sync completes, click Upgrade again and click Proceed.
   - If your product inventory is already synced, click Proceed.

   The upgrade proceeds through several stages.
5. The Product Version and Repository URL fields are populated for version 9.0. Click Next.
6. Choose the VCF license type then click Next.

   - VMware Cloud Foundation: Provides the license to install the VCF Operations fleet management appliance with the VMware Aria Operations upgrade to VCF Operations.
   - VMware vSphere Foundation: Provides the license for the VMware Aria Operations upgrade to VCF Operations.
7. Click Run Assessment.

   This starts the upgrade assessment tool for VMware Aria Operations. After the assessment completes, click Next.
8. Click Take product snapshot. Retaining the product snapshot is optional.
9. Enter the Infrastructure properties needed to deploy the VCF Operations fleet management appliance.

   - Select vCenter server: Enter a value to place the appliance.
   - Select Cluster: Enter a value to place the appliance.
   - Folder: Enter a value to place the appliance.
   - Resource pool: Enter a value to place the appliance.
   - Select Network
   - Select Datastore
   - Select Disk Mode
   - VM Name: Enter a name for the new appliance that is being deployed.
   - FQDN: Enter the FQDN of the appliance.
   - IP Address: Enter the IP address of the appliance.
   - Admin Password: Enter the password that admin@local uses to log in to the VCF Operations fleet management native UI.
   - Root Password: Must be a 15-character password, or Precheck will fail
10. Enter the Network details.

    - Domain Name: Top-level domain, such as broadcom.com.
    - Domain Search Path: Top-level domain, such as broadcom.com.
    - DNS Servers: To select the DNS server that you want to configure VCF Operations with, click Edit Server Selection. If the DNS server that you want is not available, click Add New Server to add and select it.
    - NTP: To select the NTP server that you want to VCF Operations with, click Edit Server Selection. If the NTP server that you want is not available, click Add New Server to add and select it.
    - IPv4 Details:

      - IPv4 gateway: Default gateway of the network for VCF Operations to join.
      - IPv4 netmask: Netmask of the network for VCF Operations to join.
11. Click Run Precheck.
12. After reviewing the summary, click Submit.

    The request moves through several task steps.

    After the upgrade, the Aria Operations environment is removed from VMware Aria Suite Lifecycle.

Upgrading to VCF Operations installs the fleet management appliance node. VCF Operations is listed as a new deployment on the Overview tab under Fleet ManagementLifecycle.