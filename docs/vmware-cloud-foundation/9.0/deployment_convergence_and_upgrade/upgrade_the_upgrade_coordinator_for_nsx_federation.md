---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/upgrade-nsx-in-a-federated-environment/upgrade-the-upgrade-coordinator-for-nsx-federation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade the Upgrade Coordinator for NSX Federation
---

# Upgrade the Upgrade Coordinator for NSX Federation

The upgrade coordinator runs in the NSX Manager. It is a self-contained web application that orchestrates the upgrade process of hosts, NSX Edge cluster, NSX Controller cluster, and the management plane.

The upgrade coordinator guides you through the upgrade sequence. You can track the upgrade process and, if necessary, you can pause and resume the upgrade process from the UI.

1. In a web browser, log in to the NSX Global Manager for the domain at https://nsx\_gm\_vip\_fqdn/).
2. Select SystemUpgrade from the navigation panel.
3. Click Proceed to Upgrade.
4. Navigate to the upgrade bundle .mub file you downloaded or paste the download URL link.

   - Click Browse to navigate to the location you downloaded the upgrade bundle file.
   - Paste the VMware download portal URL where the upgrade bundle .mub file is located.
5. Click Upload.

   When the file is uploaded, the Begin Upgrade button appears.
6. Click Begin Upgrade to upgrade the upgrade coordinator.

   Upgrade one upgrade coordinator at a time.
7. Read and accept the EULA terms and accept the notification to upgrade the upgrade coordinator..
8. Click Run Pre-Checks to verify that all NSX components are ready for upgrade.

   The pre-check checks for component connectivity, version compatibility, and component status.
9. Resolve any warning notifications to avoid problems during the upgrade.