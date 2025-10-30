---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/apply-a-patch-to-vmware-aria-suite-lifecycle.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Download Patch and Upgrade Binaries and Patch VMware Aria Suite Lifecycle
---

# Download Patch and Upgrade Binaries and Patch VMware Aria Suite Lifecycle

Before starting the upgrade process, download VMware Aria Suite Lifecycle 8.18 Patch 2 or later. You also need the binaries that VMware Aria Suite Lifecycle uses to upgrade VMware Aria Operations to VCF Operations version 9, and to deploy the VCF Operations fleet management appliance.

To upgrade to VCF Operations using VMware Aria Suite Lifecycle, you must apply the latest patch to your existing VMware Aria Suite Lifecycle 8.18 installation.

Perform the following steps to download the binaries that you need and apply the latest VMware Aria Suite Lifecycle 8.18 patch.

Before starting the procedure, review the [VMware Aria Suite Lifecycle 8.18 Release Notes](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-suite-lifecycle/8-18/release-notes.html) for current information about the latest patch.

1. Download binaries.
2. Log in to the [Broadcom Support Portal](https://support.broadcom.com).
3. Download VMware Aria Suite Lifecycle 8.18 Patch 2 or later.
   1. On My Downloads, search for the VMware Aria Suite product name and click Show Results.
   2. Select VMware Aria Suite.
   3. Click the Solutions tab, select VMware Aria Suite - Enterprise, and choose the 2019 release.
   4. Select the vrslcm-8.18.0-PATCH solution with the latest patch number and download the .patch file.
4. Download the binaries for the upgrade to VCF Operations.
   1. On My Downloads search for the VMware Cloud Foundation product name and click Show Results.
   2. Select VMware Cloud Foundation.
   3. Click the Product tab and select VMware Cloud Foundation 9. Choose the 9.0.0.0 release.
   4. On the Primary Downloads tab, next to VMware Cloud Foundation Operations, click View Group.
   5. Download the Operations-Upgrade-9.0.0.X.XXXXXXXX.pak PAK file for the VCF Cloud Foundation Operations upgrade.
5. Download the binaries for the deployment of the VCF Operations fleet management appliance.
   1. On My Downloads search for the VMware Cloud Foundation product name and click Show Results.
   2. Select VMware Cloud Foundation.
   3. Click the Product tab and select VMware Cloud Foundation 9. Choose the 9.0.0.0 release.
   4. On the Primary Downloads tab, next to VMware Cloud Foundation Operations fleet management, click View Group.
   5. Download the VCF-OPS-Lifecycle-Manager-Appliance-9.0.0.X.XXXXXXX.ova OVA file for the VCF Cloud Foundation Operations fleet management deployment.
6. Use WinSCP or a similar file transfer utility to log in to your VMware Aria Suite Lifecycle virtual appliance.
7. Copy the downloaded binaries to the /data partition.
8. Apply the VMware Aria Suite Lifecycle 8.18 patch.
9. Log in to VMware Aria Suite Lifecycle.
10. From the Lifecycle Operations dashboard, navigate to SettingsBinary Mapping and click Patch Binaries. If any binaries from a previous installation are listed, delete them.
11. To map the binary, click Add Binaries.

    - In Source Location**,** enter the path to the patch binary or /data and click Discover.
    - When the patch binary appears, click Add.

    The binary mapping request begins.
12. After binary mapping completes, navigate to SettingsSystem Patches and click Create Snapshot.

    Creating a snapshot is mandatory before patching.
13. To install the patch, click New Patch.
    1. Select the VMware Aria Suite Lifecycle 8.18 2 or later and click Next.
    2. Review the installation summary and click Install.

    The installation request moves through patch installation and services restart.

The VMware Aria Suite Lifecycle 8.18 patch has been applied. To verify that the latest patch has been applied:

- Click SettingsSystem Details and verify the Patch Version shows Patch 2 or later.
- Click SettingsSystem Patches and verify the Product Patch Level shows Patch 2 or later.