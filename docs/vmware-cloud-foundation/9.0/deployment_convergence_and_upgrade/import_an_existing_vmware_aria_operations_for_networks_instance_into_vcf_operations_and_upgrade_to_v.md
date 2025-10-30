---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-4-upgrade-additional-management-components-in-vcf-9.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Import an Existing VMware Aria Operations for Networks Instance Into VCF Operations and Upgrade to VCF Operations for Networks
---

# Import an Existing VMware Aria Operations for Networks Instance Into VCF Operations and Upgrade to VCF Operations for Networks

Use VCF Operations to import and upgrade VMware Aria Operations for Networks 6.13.

You can only import and upgrade one instance of VMware Aria Operations for Networks to VCF Operations for networks.

## Add upgrade binaries in VCF Operations

Before upgrading to VCF Operations for networks, you log in to your VCF Operations instance to ensure that your offline depot is active with a path that points to the location where the VCF Operations for networks binaries are stored. See [Lifecycle Management of VCF Management Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab.html).

In VCF Operations, on the Binary Management tab, verify that the VMware Cloud Foundation Operations for networks version 9.0.0.0 is listed and click to download the binary. See [Downloading VCF Management Components into Binary Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/using-the-depot-configuration-tab/using-the-overview-tab.html).

## Import VMware Aria Operations for Networks

On the Overview tab under Fleet ManagementLifecycle, click Add on the tile for VCF Operations for networks. The import moves through the following stages.

You can only deploy or import one VMware Aria Operations for Networks instance into the VCF Operations fleet management appliance

1. Deployment Settings: Select Import from legacy Fleet Management
2. Lifecycle Configuration

   - VMware Aria Suite Lifecycle FQDN
   - Username
   - Admin Password
   - Root Password
3. Select Aria Operations for Networks Platform instance

   Select the instance that you want to deploy. You can only deploy or import one VMware Aria Operations for Networks instance into the VCF Operations fleet management appliance.
4. Review

   - From VMware Aria Suite Lifecycle: FQDN of the Aria Suite Lifecycle legacy environment that the component is being imported from.
   - Component VMware Aria Operations for Networks platform: FQDN of the VMware Aria Operations for Networks instance that is to be imported and integrated.

After reviewing the details of the components and environments that are being integrated, check the box to acknowledge that this integration is irreversible and click Submit.

After the import task completes, the Overview tab reappears with a tile that displays a new deployment of VCF Operations for networks.

- On the tile, click Manage.
- On the Components page that appears, click Plan Upgrade.

The Overview tab reappears with a tile that displays a pending upgrade of VMware Aria Operations for Networks Version 6.13.0 to VCF 9.0.0.0.

## Upgrade to VCF Operations for Networks

The upgrade process automatically completes fields with values discovered and imported from VMware Aria Operations for Networks, so you can accept default values to perform the upgrade.

From the Overview tab, click Upgrade on the VCF Operations for networks tile.

To ensure that VCF Operations fleet management appliance and the imported Aria Operations for Networks environment are in sync, the upgrade triggers an inventory sync.

- Click Trigger Inventory Sync, then click Submit.
- When all stages of the inventory sync are complete, it is safe to start the upgrade.

Return to the Overview tab, click Upgrade, then click Proceed. The upgrade moves through the following stages.

1. Product Version and Repository URL are populated by default.
2. Snapshot: Take product snapshot (default)
3. Precheck: To validate various properties of VCF Operations for networks, click Run Precheck.
4. Upgrade Summary: Shows the details of the upgrade. To start the upgrade, click Submit.

The Tasks tab shows the status of the upgrade.