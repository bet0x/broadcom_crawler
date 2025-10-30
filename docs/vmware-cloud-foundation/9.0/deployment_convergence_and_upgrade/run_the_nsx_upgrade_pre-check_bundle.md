---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/run-the-upgrade-precheck-pub-bundle.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Run the NSX Upgrade Pre-check Bundle
---

# Run the NSX Upgrade Pre-check Bundle

The NSX upgrade pre-check bundle .(pub) allows you to run the latest upgrade pre-check operations on your deployment during the planning phase of the upgrade. These operations check for component connectivity, version compatibility, and component status among other environment readiness indicators, for your current upgrade plan.

Run the upgrade pre-checks at least one week in advance of the planned upgrade maintenance window. Running the pre-checks in advance allows you sufficient time to address and resolve issues identified by the pre-checks.

To run the NSX upgrade pre-checks, do the following:

1. Download the .pub upgrade pre-check bundle file.
2. Upload the .pub bundle file to NSX Manager.
3. Run the upgrade pre-checks in NSX Manager.

## Download the Pre-check Bundle

Ensure that you download the pre-check bundle version that corresponds to the target VCF version.

You can also navigate to the pre-check bundle and save the URL. When you upload to NSX Manager, paste the URL so that the pre-check bundle is uploaded from the Broadcom Support portal.

1. Locate the NSX build on the [Broadcom Support portal](https://support.broadcom.com/group/ecx/downloads).
2. Navigate to the pre-check bundle file and click Read More. Verify that the pre-check bundle filename extension ends with .pub.

   The filename will be similar to VMware-NSX-upgrade-bundle-ReleaseNumberNSXBuildNumber.pub.
3. Download the NSX pre-check bundle to the same system you use to access the NSX Manager user interface.

## Upload the Pre-check Bundle to NSX Manager

Uploading the pre-check bundle file upgrades the upgrade coordinator in NSX Manager to the target version so that you can verify that all system components are ready for upgrade.

1. From your browser, log in as a local admin user to the NSX Manager at https://nsx-manager-ip-address/login.jsp?local=true. You can log in as a local admin user to any one of the NSX Manager nodes.
2. Select SystemUpgrade from the navigation panel.
3. Click Upgrade.
4. Click Browse to navigate to the location where you downloaded the pre-check bundle.pub file.
5. Click Upload.

   When the upload process finishes, the Prepare for Upgrade button appears.
6. Click Prepare for Upgrade to upgrade the upgrade coordinator.

   The EULA appears.
7. Read and accept the EULA terms.
8. Accept the notification to upgrade the upgrade coordinator.

   Upgrading the upgrade coordinator might take 10–20 minutes, depending on your network speed. If the network times out, reload the pre-check bundle.

## Run the Upgrade Pre-checks

Run the pre-checks when you start, change, or reset your upgrade plan.

1. In the upgrade coordinator in NSX Manager, click Run Pre-Checks.
2. View the list of pre-checks that are performed with the API call:

   ```
   GET https://<nsx-manager>/api/v1/upgrade/upgrade-checks-info
   ```
3. Acknowledge the issues as required and refresh your browser if needed.
4. Resolve issues detected by the pre-checks.

   1. In the NSX Manager section, click the Pre Check Status issues to see the issue details.
   2. In the Edges section, click the Pre Check Status issues to see the issue details.

      If the allocated CPU cores or memory of the edge node is less than the standard edge node form factor, an alarm is generated to warn you. In this scenario, you must acknowledge this type of alarm to proceed with the edge upgrade which will result in the upgrade coordinator changing the edge CPU cores and memory to match the standard edge node form factor. After the upgrade, these type of alarms are cleared on the next edge transport node refresh action. For more details, see [Edge Node Upgrade Process Through the Upgrade Coordinator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/nsx-edge-node-upgrade-process-by-the-upgrade-coordinator.html).
   3. In the Hosts section, click the Pre Check Status issues to see the issue details.

      You might have to place some of the hosts in maintenance mode.
5. (Optional) Click Download Pre-Check Results to download a CSV file with details about pre-check errors for each component and their status.
6. (Optional) Click View Upgrade History to view information about previous upgrades.