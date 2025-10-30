---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-vlcm-baseline-clusters-to-vlcm-image-clusters-using-powercli(1)/transition-to-vsphere-lifecycle-manager-images-using-the-powershell-script-command-line-interface.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Transition to vSphere Lifecycle Manager Images Using the PowerShell Script Command-Line Interface
---

# Transition to vSphere Lifecycle Manager Images Using the PowerShell Script Command-Line Interface

The PowerShell script command-line interface is useful for larger environments and can be used to transition a single cluster at a time or, multiple vSphere clusters using JSON files.

See [PowerShell Script CLI Options for Transitioning to vSphere Lifecycle Manager Images](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-vlcm-baseline-clusters-to-vlcm-image-clusters-using-powercli(1)/powershell-script-cli-options-for-transitioning-to-vsphere-lifecycle-manager-images.html) for information about all the CLI options, .

For bulk operations utilizing a JSON file, use a JSON validator to ensure your file is properly formed prior to using it as an input.

Appending -Silent to any command suppresses screen output and any progress indicators. Pertinent data is still sent to the log file and status queried through the relevant check commands. This can be useful in scripting operations.

1. Run the script with -Version and compare it to the version listed on [KB 385617](https://knowledge.broadcom.com/external/article?articleNumber=385617) to determine if you are running the latest copy of the script.

   ```
   PS C:\Users\Admin>.\VcfBaselineClusterTransition.ps1 -Version
   ```
2. Connect to SDDC Manager and its vCenter instances.

   You can provide your SDDC Manager credentials interactively or by including the path to a JSON with the credentials.

   Command | Description || ``` .\VcfBaselineClusterTransition.ps1 -Connect ``` | Enter the following information for SDDC Manager: - FQDN - ADMIN user name - ADMIN passwordOptionally, you can choose to save these credentials in a JSON file. |
   | ``` .\VcfBaselineClusterTransition.ps1 -Connect -JsonInputpath_to_file ``` | For the path\_to\_file.json, enter the location of the file containing the SDDC Manager credentials. For example:  ``` C:\Users\Admin\SddcManagerCredentials.json ``` |

   The script connects to SDDC Manager and all vCenter instances that it manages.

   If you see the message Failed to connect to vCenter, verify that you can access the vCenter from PowerShell and that it returns a 200 status code.

   ```
   Invoke-WebRequest -Method HEAD -SkipCertificateCheck -Uri https://vCenter_FQDN|Select-Object StatusCode
   ```

   If it does not, verify you can login to that vCenter from a browser. If you cannot, contact Broadcom Support.
3. Identify vSphere clusters across all workload domains that are managed using vSphere Lifecycle Manager baselines.

   Command | Description || ``` .\VcfBaselineClusterTransition.ps1 -ShowBaselineClusters ``` | Displays a list of baseline clusters. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ShowBaselineClusters -JsonOutput path_to_file ``` | Displays a list of baseline managed vSphere clusters and saves the output to a file. |

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bbc94bc2-6726-4d87-bd6a-0a015d4cc4cd.original.png)
4. Display and/or save all the vSphere Lifecycle Manager images in connected vCenter(s). 

   Command | Description || ``` .\VcfBaselineClusterTransition.ps1 -ShowImagesInVcenter ``` | Displays vCenter images on screen. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ShowImagesInVcenter -JsonOutputpath_to_file ``` | Displays vCenter images on screen and saves the output to a file. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ShowImagesInVcenter -JsonOutputpath_to_file -Silent ``` | Only saves vCenter image output to a file. |

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/becd3335-49ca-4b80-a4b3-1ea3ec4bff81.original.png)
5. Import vSphere Lifecycle Manager images into SDDC Manager from connected vCenter instances.

   Command | Description || ``` .\VcfBaselineClusterTransition.ps1 -ImportImagesFromVcenter -VcenterImageNameimage_name-VcenterNamevc_FQDN ``` | Import a single image from vCenter and display progress on screen. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ImportImagesFromVcenter -VcenterImageNameimage_name-VcenterNamevc_FQDN-Silent ``` | Import a single image from vCenter and do not display progress on screen. |
   | ``` \VcfBaselineClusterTransition.ps1 -ImportImagesFromVcenter -JsonInputpath_to_file -VcenterNamevc_FQDN ``` | Import multiple images from vCenter through JSON input file serially and display progress on screen.  Example JSON file for bulk import:  ``` [  {    "VcenterImageName": "image_name",  "VcenterName": "vCenter_FQDN" },   { "VcenterImageName": "another_image_name", "VcenterName": "vCenter_FQDN" } ] ``` |
   | ``` .\VcfBaselineClusterTransition.ps1 -ImportImagesFromVcenter -JsonInputpath_to_file -VcenterNamevc_FQDN-Parallel ``` | Import multiple images from vCenter via JSON input file in parallel. |

   If the script is called without the flag -Parallel, it attempts to delete empty vSphere clusters after a successful import. It does not delete vSphere clusters with hosts or images from the vCenter image catalog.

   To check the task status, run the following command:

   ```
   .\VcfBaselineClusterTransition.ps1 -CheckTaskStatus -TaskType SddcManagerImageUpload
   ```

   If the import task fails with the error message An image named <image-name> already exists in the SDDC Manager., you can rename the source image in vCenter or delete the conflicting image from SDDC Manager before retrying. To delete the conflicting image in SDDC Manager, run the following command:

   ```
   .\VcfBaselineClusterTransition.ps1 -DeleteImageFromSddcManager -SddcManagerImageNameimage_name
   ```
6. Review the images available in SDDC Manager.

   Command | Description || ``` ./VcfBaselineClusterTransition.ps1 -ShowImagesInSddcManager ``` | Displays a list of and summary information for all vSphere Lifecycle Manager images in SDDC Manager. |
   | ``` Get-Content logs/image_name.json ``` | Displays detailed information about a specific vSphere Lifecycle Manager image. |

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6a5c6569-db26-43da-ac13-0cd541494b52.original.png)
7. Check vSphere Lifecycle Manager baseline managed vSphere clusters for compliance with a vSphere Lifecycle Manager image.

   You can run compliance checks in parallel, but there is a concurrent task limit of 25 compliance and transition tasks. If you exceed this limit, the task will be rejected, rather than queued.

   You can safely ignore the following compliance check findings:
   - Components NSX LCP Bundle are removed in the image. They will be removed from the host during remediation.
   - The following VIBs on the host are missing from the image and will be removed from the host during remediation.

   This component and VIBs are managed by VMware solutions, NSX and vCenter HA, respectively, and not part of the vSphere Lifecycle manager image. When the hosts are rebooted, the appropriate packages are re-added.

   Command | Description || ``` .\VcfBaselineClusterTransition.ps1 -ComplianceCheck -ClusterNamecluster_Name-WorkloadDomainNameworkload_domain_name-SddcManagerImageNameimage_name ``` | Performs a compliance check of single vSphere cluster against a vSphere Lifecycle Manager image and displays the results after check is complete. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ComplianceCheck -JsonInput path_to_file ``` | Performs a compliance check of multiple vSphere clusters sequentially against vSphere Lifecycle Manager images using a JSON input file and displays results after the check is complete.  Example JSON input file:  ``` [  {    "ClusterName": "vSphere_cluster_name",  "WorkloadDomainName": "workload_domain_name", "SddcManagerImageName" :image_name},   { "ClusterName": "vSphere_cluster_name",  "WorkloadDomainName": "workload_domain_name", "SddcManagerImageName" :image_name} ] ``` |
   | ``` .\VcfBaselineClusterTransition.ps1 -ComplianceCheck -JsonInput path_to_file -Parallel ``` | Performs a compliance check of multiple vSphere clusters in parallel against vSphere Lifecycle Manager images using a JSON input file. Does not display results after the check is complete.  For compliance checks performed with the parallel or silent flag, the success or failure of the check can be verified by running the following command.  ``` .\VcfBaselineClusterTransition.ps1 -CheckTaskStatus -TaskType ComplianceCheck ``` |

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/96828add-5358-4263-ac9e-c2385b7be1d1.original.png)
8. For compliance checks performed in parallel or with the silent flag, review the compliance results after the compliance check is complete.

   Command | Description || ``` .\VcfBaselineClusterTransition.ps1 -ReviewComplianceResults -ShowAllClusters ``` | Displays a summary of the compliance findings for all vSphere clusters. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ReviewComplianceResults -ShowAllClusters-ShowExtendedResults ``` | Displays a summary and detailed compliance findings for all vSphere clusters. |
   | ``` \VcfBaselineClusterTransition.ps1 -ReviewComplianceResults -ClusterNamecluster_name-WorkloadDomainNameworkload_domain_name ``` | Displays a summary of the compliance findings for a specific vSphere cluster. |
   | ``` .\VcfBaselineClusterTransition.ps1 -ReviewComplianceResults -ClusterNamecluster_name-WorkloadDomainNameworkload_domain_name-ShowExtendedResults ``` | Displays a summary and detailed compliance findings for a specific vSphere cluster. |
9. Review the compliance findings to determine if a vSphere cluster is ready to be transitioned.

   Resolve any issues for vSphere clusters with a status of INCOMPATIBLE or UNKNOWN .

   | Status | Description |
   | --- | --- |
   | NON\_COMPLIANT | The vSphere cluster is not currently compliant with the selected vSphere Lifecycle Manager image, but is ready to be transitioned. |
   | INCOMPATIBLE | The vSphere cluster cannot be transitioned to the selected vSphere Lifecycle Manager image without taking additional steps. Review the summary and JSON file and resolve any issues that are blocking the transition. Contact Broadcom Support if you are unable to resolve the issue(s). |
   | UNKNOWN | Compatibility could not be determined. Make sure that all the hosts in the vSphere cluster are available. Contact Broadcom Support if you are unable to resolve the issue. |
   | COMPLIANT | The vSphere cluster has already successfully been transitioned to vSphere Lifecycle Manager image management and no further action is required. |
10. Transition NON\_COMPLIANT (ready to transition) clusters to vSphere Lifecycle Manager images.

    Command | Description || ``` ./VcfBaselineClusterTransition.ps1 -TransitionCluster -ClusterNamecluster_name-WorkloadDomainNameworkload_domain_name ``` | Transitions a single vSphere cluster to use a vSphere Lifecycle Manager image and displays progress. |
    | ``` /VcfBaselineClusterTransition.ps1 -TransitionCluster -JsonInput path_to_file ``` | Transitions multiple vSphere clusters sequentially to use a vSphere Lifecycle Manager image and displays progress.  Example JSON input file:  ``` [  {    "ClusterName": "vSphere_cluster_name",  "WorkloadDomainName": "workload_domain_name", },   { "ClusterName": "vSphere_cluster_name",  "WorkloadDomainName": "workload_domain_name", } ] ``` |
    | ``` ./VcfBaselineClusterTransition.ps1 -TransitionCluster -JsonInput path_to_file -Parallel ``` | Transitions multiple vSphere clusters in parallel to use a vSphere Lifecycle Manager image and does not display progress. |

    You can run compliance checks in parallel, but there is a concurrent task limit of 25 compliance and transition tasks. If you exceed this limit, the task will be rejected, rather than queued.

    The system transitions the vSphere cluster using the last image you checked against. If you run the compliance check multiple times against multiple images, run ./VcfBaselineClusterTransition.ps1 -ShowBaselineClusters to review the final association before proceeding.

    Once you start a vSphere cluster transition task you cannot pause it.

    1. Run one of the transition commands listed above.

       ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/153436b8-d492-473f-951e-51fad8245266.original.png)
    2. For parallel and silent operations, check the status of the transition.

       ```
       .\VcfBaselineClusterTransition.ps1 -CheckTransitions
       ```
11. If the transition task fails, try the following steps.
    1. Identify which vSphere cluster has failed to transition.

       ```
       .\VcfBaselineClusterTransition.ps1 -CheckTransitions
       ```
    2. Retrieve instructions on how to retry the transition.

       ```
       .\VcfBaselineClusterTransition.ps1 -CheckTransitions -ClusterNamecluster_name-WorkloadDomainworkload_domain_name
       ```
    3. Resume the failed task using the instructions.

       ```
       .\VcfBaselineClusterTransition.ps1 -RetryTransition -TaskIdtask_id
       ```
    4. Run the check transitions command to see if the vSphere cluster transition is In Progress.

       ```
       .\VcfBaselineClusterTransition.ps1 -CheckTransitions
       ```
    5. Periodically re-run -CheckTransitions to see if the transition completes successfully or fails. If it fails again, contact Broadcom Support.
12. Disconnect from SDDC Manager and all vCenter instances.

    ```
    ./VcfBaselineClusterTransition.ps1 -Disconnect
    ```