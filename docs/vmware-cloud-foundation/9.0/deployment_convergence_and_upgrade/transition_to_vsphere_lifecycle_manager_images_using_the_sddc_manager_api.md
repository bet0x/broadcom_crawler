---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-to-vsphere-lifecycle-manager-images-using-the-vmware-cloud-foundation-api.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Transition to vSphere Lifecycle Manager Images Using the SDDC Manager API
---

# Transition to vSphere Lifecycle Manager Images Using the SDDC Manager API

If you do not want to use the PowerShell script to transition vSphere clusters to vSphere Lifecycle manager images, you can use the SDDC Manager API instead.

This procedure describes how to use SDDC Manager's Developer Center for single vSphere cluster transitions.

The API workflow does not contain the same guardrails and error handling as the PowerShell script. Using the SDDC Manager API is only recommended if the PowerShell script does not meet your business requirements.

1. Retrieve the names and IDs of vSphere clusters that are managed using vSphere Lifecycle Manager baselines.
   1. Log in to the SDDC Manager UI.
   2. Click Developer CenterAPI Explorer.
   3. Expand Clusters and click GET /v1/clusters.
   4. Enter the value false for the isImageBased parameter and click Execute.
   5. Click Download to save the results.

      You can rename the saved file using a more meaningful name.
   6. Review the file to identify the vSphere cluster ID associated with each vSphere cluster name.

      Example:

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/492b018b-1049-4b7c-89c5-9a7bb14244e5.original.png)
2. Import vSphere Lifecycle Manager images from vCenter into SDDC Manager using the SDDC Manager UI.
   1. In the navigation pane, click Lifecycle ManagementImage Management .
   2. Click Import Image.
   3. Select Import from a vCenter.
   4. From the vCenter drop-down menu, select the vCenter containing your vSphere Lifecycle Manager image.

      Click Refresh to see the current list of images or vSphere clusters.
   5. Select the image (vCenter 9.0 and later) or vSphere cluster (vCenter 8.0.3 and below).

      For vCenter 8.0.3 and below, enter a name for your image.
   6. Click Import.

      You can monitor the status in the Tasks panel.
   7. Repeat the process for each unique image you want to import.
3. Check a vSphere Lifecycle Manager baseline managed vSphere cluster for compliance with a vSphere Lifecycle Manager image.

   You can run a vSphere cluster compliance check multiple times, but only the latest check (and associated image) is used for transitioning the vSphere cluster.

   You can safely ignore the following compliance check findings:
   - Components NSX LCP Bundle are removed in the image. They will be removed from the host during remediation.
   - The following VIBs on the host are missing from the image and will be removed from the host during remediation.

   This component and VIBs are managed by VMware solutions, NSX and vCenter HA, respectively, and not part of the vSphere Lifecycle manager image. When the hosts are rebooted, the appropriate packages are re-added.

   1. Click Lifecycle ManagementImage Management .
   2. Identify the name of the vSphere Lifecycle Manager image you want to use for the compliance check.
   3. Click Developer CenterAPI Explorer.
   4. Expand Personalities and click GET /v1/personalities.
   5. Enter the name of the image for the personalityName parameter and click Execute.
   6. Retrieve the personalityId from the response.
   7. Expand Clusters and click PATCH /v1/clusters/{id}.
   8. Enter the vSphere cluster ID for the id parameter.
   9. Enter the following information for the body parameter.

      Use the personality ID you retrieved for the clusterImageId value.

      ```
      {
      "clusterImageComplianceCheckSpec": { "clusterImageId": "personalityId" }
      }
      ```
   10. Click Execute.
4. Review the compliance findings to determine if a cluster is ready to be transitioned.

   Resolve any issues for clusters with a status of INCOMPATIBLE or UNKNOWN .

   | Status | Description |
   | --- | --- |
   | NON\_COMPLIANT | The vSphere cluster is not currently compliant with the selected vSphere Lifecycle Manager image, but is ready to be transitioned. |
   | INCOMPATIBLE | The vSphere cluster cannot be transitioned to the selected vSphere Lifecycle Manager image without taking additional steps. Review the summary and JSON file and resolve any issues that are blocking the transition. Contact Broadcom Support if you are unable to resolve the issue(s). |
   | UNKNOWN | Compatibility could not be determined. Make sure that all the hosts in the vSphere cluster are available. Contact Broadcom Support if you are unable to resolve the issue. |
   | COMPLIANT | The vSphere cluster has already successfully been transitioned to vSphere Lifecycle Manager image management and no further action is required. |

   1. Expand Clusters and click GET /v1/clusters/{id}/image-compliance
   2. Enter the vSphere cluster ID for the id parameter.
   3. Click Execute.
   4. Click Download to save the results.
   5. Review the results using the tool of your choice.
5. Transition NON\_COMPLIANT (ready to transition) clusters to vSphere Lifecycle Manager images.
   1. Expand Clusters and click PATCH /v1/clusters/{id}.
   2. Enter the vSphere cluster ID for the id parameter.
   3. Enter the following information for the body parameter.

      ```
      { "clusterTransitionSpec": { } }
      ```

      Optionally, you can specify additional options:

      ```
      {   
      "clusterTransitionSpec":
      {
       "remediationOptionsSpec":
       {
        "disableDpm": false,
        "disableHac": false,
         "enableQuickboot": true,
        "evacuateOfflineVms": true,
          "preRemediationPowerAction":      "DO_NOT_CHANGE_VMS_POWER_STATE",       "remediationFailureAction":
      {
      "action": "RETRY",
      "retryCount": 3,
      "retryDelay": 1200
        }
      }
      }
      ```
6. Monitor the task in the Tasks panel.

   If the task completes successfully, you can repeat these steps for additional vSphere clusters you want to transition.

   If the task fails, review the details, remediate any issues, and retry the task.