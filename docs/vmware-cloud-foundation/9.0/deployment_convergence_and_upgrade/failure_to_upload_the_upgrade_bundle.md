---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/failure-to-upload-the-upgrade-bundle.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Failure to Upload the Upgrade Bundle
---

# Failure to Upload the Upgrade Bundle

The upgrade bundle fails to upload because of insufficient disk space.

1. In the NSX Manager CLI, delete the unused files located at /image/vmware/nsx/file-store/\* and /image/core/\*.

   Ensure that you do not delete the /image/upgrade-coordinator-tomcat folder or other folders located at /image.
2. From your browser, log in as a local admin user to an NSX Manager at https://nsx-manager-ip-address/login.jsp?local=true.
3. Select SystemSupport Bundle and delete any unused support bundles.
4. Delete TAR files that contain PCAP files.
5. Reupload the upgrade bundle and continue with the upgrade process.