---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster/vsan-build-recommendations-for-vsphere-update-manager.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Build Recommendations for vSphere Lifecycle Manager
---

# vSAN Build Recommendations for vSphere Lifecycle Manager

vSAN generates system baselines and baseline groups that you can use with vSphere Lifecycle Manager.

vSphere Lifecycle Manager in vSphere includes the system baselines that Update Manager provided in earlier vSphere releases. It also includes new image management functionality for hosts running ESX.

vSAN generates automated build recommendations for vSAN clusters. vSAN combines information in the Broadcom Compatibility Guide and vSAN Release Catalog with information about the installed ESX releases. These recommended updates provide the best available release to keep your hardware in a supported state.

System baselines for vSAN can include device driver and firmware updates. These updates support the ESX software recommended for your cluster.

For vSAN, you can choose to provide build recommendations for the current ESX release only, or for the latest supported ESX release. A build recommendation for the current release includes all patches and driver updates for the release.

In vSAN, vSAN build recommendations include patch updates and applicable driver updates. To update firmware on vSAN clusters, you must use an image through vSphere Lifecycle Manager.

## vSAN System Baselines

vSAN build recommendations are provided through vSAN system baselines for vSphere Lifecycle Manager. These system baselines are managed by vSAN. They are read-only and cannot be customized.

vSAN generates one baseline group for each vSAN cluster. vSAN system baselines are listed in the Baselines pane of the Baselines and Groups tab. You can continue to create and remediate your own baselines.

vSAN system baselines can include custom ISO images provided by certified vendors. If hosts in your vSAN cluster have OEM-specific custom ISOs, then vSAN recommended system baselines can include custom ISOs from the same vendor. vSphere Lifecycle Manager cannot generate a recommendation for custom ISOs not supported by vSAN. If you are running a customized software image that overrides the vendor name in the host's image profile, vSphere Lifecycle Manager cannot recommend a system baseline.

vSphere Lifecycle Manager automatically scans each vSAN cluster to check compliance against the baseline group. To upgrade your cluster, you must manually remediate the system baseline through vSphere Lifecycle Manager. You can remediate vSAN system baseline on a single host or on the entire cluster.

## vSAN Release Catalog

The vSAN release catalog maintains information about available releases, preference order for releases, and critical patches needed for each release. The vSAN release catalog is hosted on the VMware Cloud.

vSAN requires Internet connectivity to access the release catalog. You do not need to be enrolled in the Customer Experience Improvement Program (CEIP) for vSAN to access the release catalog.

If you do not have an Internet connection, you can upload the vSAN release catalog directly to the vCenter. In the vSphere Client, click Configure > vSAN > Update, and click Upload from file in the Release Catalog section. You can download the latest vSAN Release Catalog.

vSphere Lifecycle Manager enables you to import storage controller drivers recommended for your vSAN cluster. Some storage controller vendors provide a software management tool that vSAN can use to update controller drivers. If the management tool is not present on ESX hosts, you can download the tool.

## Working with vSAN Build Recommendations

vSphere Lifecycle Manager checks the installed ESX releases against information in the Hardware Compatibility List (HCL) in the Broadcom Compatibility Guide. It determines the correct upgrade path for each vSAN cluster, based on the current vSAN Release Catalog. vSAN also includes the necessary drivers and patch updates for the recommended release in its system baseline.

vSAN build recommendations ensure that each vSAN cluster remains at the current hardware compatibility status or better. If hardware in the vSAN cluster is not included on the HCL, vSAN can recommend an upgrade to the latest release, since it is no worse than the current state.

vSphere Lifecycle Manager uses the vSAN health service when performing remediation precheck for hosts in a vSAN cluster. vSAN health service is not available on hosts running ESX. When vSphere Lifecycle Manager upgrades hosts running ESX, the upgrade of the last host in the vSAN cluster might fail. If remediation failed because of vSAN health issues, you can still complete the upgrade. Use the vSAN health service to resolve health issues on the host, then take that host out of maintenance mode to complete the upgrade workflow.

The following examples describe the logic behind vSAN build recommendations.

Example 1
:   A vSAN cluster is running, and its hardware is included on HCL. The HCL lists the hardware supported. vSAN recommends an upgrade, including the necessary critical patches for the release.

Example 2
:   A vSAN cluster is running, and its hardware is included on HCL. The hardware is also supported on the HCL. vSAN recommends an upgrade.

Example 3
:   A vSAN cluster is running, and its hardware is not on the HCL for that release. vSAN recommends an upgrade, even though the hardware is not on the HCL. vSAN recommends the upgrade because the new state is no worse than the current state.

Example 4
:   A vSAN cluster is running, and its hardware is included on HCL. The hardware is also supported on the HCL and selected baseline preference is patch-only. vSAN recommends an upgrade, including the necessary critical patches for the release.

The recommendation engine runs periodically (once each day), or when the following events occur.

- Cluster membership changes. For example, when you add or remove a host.
- The vSAN management service restarts.
- A user logs in to [Broadcom Support Portal](https://support.broadcom.com/) using a web browser.
- An update is made to the Broadcom Compatibility Guide or the vSAN Release Catalog.

The vSAN Build Recommendation health check displays the current build that is recommended for the vSAN cluster. It also can warn you about any issues with the feature.

## System Requirements

vSphere Lifecycle Manager is an extension service in vCenter 9.0 and later.

vSAN requires Internet access to update release metadata, to check the Broadcom Compatibility Guide, and to download ISO images from Broadcom Support Portal. vSAN requires valid credentials to download ISO images for upgrades from [Broadcom Support Portal](https://support.broadcom.com/).