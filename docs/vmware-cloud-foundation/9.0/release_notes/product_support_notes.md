---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > Product Support Notes
---

# Product Support Notes

Following are the key product support notes for VMware Cloud Foundation 9.0:

## Deprecation Notes

**Deprecation of vCenter Enhanced Linked Mode (ELM):**

With vCenter 9.0, ELM, which allows unified view and administration of multiple vCenter instances, is deprecated and will be removed in a future release. ELM is supported in vCenter 9.0 to allow smooth upgrade of existing infrastructure to VCF, but the recommended alternative is the grouping capability under VCF Operations. Group admins can enable alternatives for each ELM capability, such as VMware Single Sign-On, consolidated licensing, vCenter roles and privileges sync, vCenter tags replication, and vCenter single API endpoint.

**Deprecation of vSphere Host Profiles:**

The vSphere Host Profiles capability is deprecated in vCenter 9.0 and will be removed in a future release. Instead of Host Profiles, you can use vSphere Configuration Profiles to manage configurations at a cluster level. For more details, see this [blog](https://blogs.vmware.com/cloud-foundation/2024/07/12/using-vsphere-configuration-profiles-in-vmware-vsphere-8-update-3-with-baseline-managed-clusters/).

**SDDC Manager UI**

SDDC Manager UI is now deprecated, to be removed in a future major release.

**SDDC Manager APIs for Identity Configuration**

SDDC Manager APIs for identity configuration are deprecated and will be removed in a future major release. The functionality is now replaced by VCF Operations.

**VMware Aria Operations for Logs**

VMware Aria Operations for Logs is now deprecated, with version 8.18 being the final release, and will remain supported until its designated end-of-life date. However, VCF Operations 9.0 does not support integration with VMware Aria Operations for Logs 8.18. Existing VMware Aria Operations for Logs 8.18 instances can still forward logs to VCF Operations 9.0.

## End of Support Notes

**Cloud Builder Appliance**

The VCF Installer appliance now replaces the Cloud Builder appliance.

**Removal of Integrated Windows Authentication (IWA):**

vCenter 9.0 discontinues support for Integrated Windows Authentication. To ensure continued secure access, migrate from IWA to Active Directory over LDAPS or to Identity Federation with Multi-Factor Authentication.

**Removal of vSphere Lifecycle Manager baselines:**

Managing clusters with vSphere Lifecycle Manager baselines and baseline groups (legacy vSphere Update Manager (VUM) workflows) is no longer supported in vCenter 9.0. Instead of using baselines and baseline groups, you can use vSphere Lifecycle Manager images to perform tasks at a cluster level, for example, you can install a desired ESX version on all hosts in a cluster, install and update third-party software, update, and upgrade ESX or firmware, generate recommendations, and use a recommended image for your cluster.

**Deployment Parameter Worksheet**

The VCF Installer appliance UI and JSON input functionality now replace the Deployment Parameter Worksheet.

**SDDC Manager UI to Deploy Application Virtual Network**

SDDC Manager UI to deploy Application Virtual Network is removed and replaced by API functionality to deploy VCF Operations and VCF Automation on NSX Segments.

**SDDC manager UI and API to Deploy VMware Aria Suite**

VCF Installer and VCF Operations now replace SDDC manager UI and API to deploy VMware Aria Suite components.

**SDDC Manager Life Cycle Management Capabilities**

SDDC Manager no longer provides life cycle management API (/v1/system/precheck). SDDC Manager's life cycle management capabilities are now moved to VCF Operations.

**SDDC Manager Bring-Up APIs**

The VCF Installer appliance updates or replaces previous bring-up APIs.

## Other Notes

**VMware Update Manager Download Service (UMDS) becomes part of the VMware Cloud Foundation Download Tool:**

With vCenter 9.0, the VMware Update Manager Download Service (UMDS) becomes part of the VMware Cloud Foundation Download Tool, formerly known as Offline Bundle Transfer Utility (OBTU). With the combined functionality of UMDS and OBTU, you can download all binaries of VMware Cloud Foundation components. The standalone UMDS tool is deprecated and will be removed in a future vCenter release.

**Product Support Notes for VMware Cloud Foundation 9.0 by Component:**

See key product support notes for VMware Cloud Foundation 9.0 listed within each component:

- [vSphere](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/product-support-notes-vsphere.html)
- [vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/product-support-notes-vsan.html)
- [NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/product-support-notes-nsx.html)
- [VCF Installer](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/product-support-notes-installer.html)
- [VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/product-support-notes-vcf-ops.html)
- [VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/product-support-notes-vcf-automation.html)
- [VCF SDKs, APIs, and CLIs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-product-support-notes/vcf-sdks-apis-and-clis-product-support-notes.html)