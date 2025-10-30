---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-the-upgrade-coordinator.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Update the Upgrade Coordinator in NSX Manager
---

# Update the Upgrade Coordinator in NSX Manager

After you finish the prerequisites for a manual upgrade, your first step is to update the NSX Manager upgrade coordinator to initiate the upgrade process.

- Complete all the checklist tasks related to preparing for the upgrade, as described in [Upgrading NSX to 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9.html).
- Download the upgrade pre-check bundle (.pub) and [run the upgrade pre-checks](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/run-the-upgrade-precheck-pub-bundle.html).
- [Download the upgrade bundle](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/download-the-nsxt-upgrade-bundle.html).
- Make necessary adjustments to your system configuration to [manage unsupported features](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/manage-deprecated-nsx-features.html). The pre-check step of the upgrade coordinator will raise an error if it detects an unsupported feature in the source deployment.

The upgrade coordinator runs in NSX Manager. It is a self-contained web application that orchestrates the upgrade process of the Management Plane, NSX edge clusters, and NSX VIBs on the host transport nodes.

The upgrade coordinator guides you through the proper upgrade sequence. You can track the upgrade process and if necessary you can pause and resume the upgrade process from the user interface.

1. From your browser, log in as a local admin user to the NSX Manager at https://nsx-manager-ip-address/login.jsp?local=true. You can log in as a local admin user to any one of the NSX Manager nodes.
2. Select SystemUpgrade from the navigation panel.
3. Click Upgrade.
4. Click Browse to navigate to the location where you [downloaded the upgrade bundle](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/download-the-nsxt-upgrade-bundle.html).mub file.
5. Click Upload. 

   Upgrading the upgrade coordinator might take 10–20 minutes, depending on your network speed. If the network times out, reload the upgrade bundle.

   When the upload process finishes, the Prepare for Upgrade button appears.
6. Click Prepare for Upgrade to upgrade the upgrade coordinator. 

   Do not initiate multiple simultaneous upgrade processes for the upgrade coordinator.

   The EULA appears.
7. Read and accept the EULA terms.
8. Accept the notification to upgrade the upgrade coordinator.
9. If a patch release becomes available after the upgrade coordinator is updated, upload the latest upgrade bundle and upgrade the upgrade coordinator.
10. Click Run Pre-Checks to verify that all the NSX components are ready for upgrade.

    You must run the pre-checks when you change or reset your upgrade plan, or upload a new upgrade bundle.

    This action checks for component connectivity, version compatibility, and component status among other environment readiness checks, for your current upgrade plan.
11. View the list of pre-checks that are performed with the API call GET https://<nsx-manager>/api/v1/upgrade/upgrade-checks-info.
12. Acknowledge the issues as required and refresh your browser if needed.
13. Resolve issues detected from the pre-check.
    1. In the NSX Manager section, click the Pre Check Status issues to see the issue details.
    2. In the Edges section, click the Pre Check Status issues to see the issue details.

       If the allocated CPU cores or memory of the edge node is less than the standard edge node form factor, an alarm is generated to warn you. In this scenario, you must acknowledge this type of alarm to proceed with the edge upgrade which will result in the upgrade coordinator changing the edge CPU cores and memory to match the standard edge node form factor. After the upgrade, these type of alarms are cleared on the next edge transport node refresh action. For more details, see [Edge Node Upgrade Process Through the Upgrade Coordinator](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/nsx-edge-node-upgrade-process-by-the-upgrade-coordinator.html).
    3. In the Hosts section, click the Pre Check Status issues to see the issue details.

       You might have to place some of the hosts in maintenance mode.

    You can click Download Pre-Check Results to download a CSV file with details about pre-check errors for each component and their status.
14. Click View Upgrade History and view information about previous NSX Manager upgrades.

    If new NSX Manager nodes are added after the upgrade coordinator is upgraded, upload the upgrade bundle to the newly added nodes and upgrade the upgrade coordinator again.

Proceed to [Upgrade the Management Plane](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-management-plane-from-nsx-3-2-1-x-and-later.html).