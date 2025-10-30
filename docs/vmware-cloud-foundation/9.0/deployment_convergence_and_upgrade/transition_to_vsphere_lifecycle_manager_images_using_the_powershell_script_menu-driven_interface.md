---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-vlcm-baseline-clusters-to-vlcm-image-clusters-using-powercli(1)/transition-to-vsphere-lifecycle-manager-images-using-the-powershell-script-menu-driven-interface.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Transition to vSphere Lifecycle Manager Images Using the PowerShell Script Menu-Driven Interface
---

# Transition to vSphere Lifecycle Manager Images Using the PowerShell Script Menu-Driven Interface

The PowerShell script menu-driven interface provides a guided experience for managing vSphere Lifecycle Manager images, scanning baseline clusters for image compliance, and transitioning vSphere clusters to vSphere Lifecycle Manager images.

The PowerShell script imports vSphere Lifecycle Manager images from the vCenter Image Catalog in vCenter 9.0 or later and from vSphere clusters in vCenter 8.0.3 and earlier.

If the vLCM image is vSphere cluster-based, rather than from the vCenter Image Catalog, and contains no hosts, the script deletes the vSphere cluster after completing the import and performing necessary safety checks.

SDDC Manager requires images be unique in two regards: name and manifest.

Name example: if you have an image named "esx-803b" in vCenter m01-vc01.example.com and in w01-vc01.example.com and try to import them one after another into SDDC Manager vcf01.example.com, the second image will be rejected.

Manifest example: if you have two images, one called "esx-803b" and another called "esx-803-test", but they both contain the same ESX 8 Update 3b base version and the same vendor add-on, and import one after another, SDDC Manager will reject the second image during its final image validation step. This validation only occurs once the entire image has been uploaded to SDDC Manager.

1. Launch the script.

   ```
        .\VcfBaselineClusterTransition.ps1
   ```
2. Connect to SDDC Manager and select a vCenter that manages the vSphere clusters you want to transition.
   1. Select option 1 Connect to SDDC Manager and select vCenter..

      If this is your first time using the script, or if you have chosen not to save your credential file, you are prompted to enter your SDDC Manager FQDN and administrative credentials. If an SDDC credential file is present, the script uses those credentials to connect to the SDDC Manager referenced in the file.
   2. Select the vCenter(s) to which you want to connect.

      You can connect to all vCenters, a single vCenter, or a comma-delimited list of multiple vCenters.

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/fa706614-fc98-486c-8de2-08ad2a620437.original.png)
3. Import a vSphere Lifecycle Manager image into SDDC Manager from any connected vCenter.
   1. From the main menu of the script, select option 2, Import vLCM images from vCenter(s) into SDDC Manager.
   2. Select the ID of the image to import and wait for the task to complete.

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2b4bb05e-b91e-4187-a47a-75ce4da96a81.original.png)

      If the import task fails with the error message An image named <image-name> already exists in the SDDC Manager., you can rename the source image in vCenter or delete the conflicting image from SDDC Manager before retrying. To delete the conflicting image in SDDC Manager, retrun to the main menu and select option 7, (Optional) Delete SDDC Manager Image.
   3. Repeat these steps for all the images you want to import.
4. Check vSphere Lifecycle Manager baseline clusters for compliance with a vSphere Lifecycle Manager image.

   Although the PowerShell menu-driven interface allows you to queue up compliance checks against multiple vSphere clusters, the checks are performed sequentially. Each check must complete before the next one begins. If you want to run a compliance check against a large number of vSphere clusters, consider running compliance checks using using the command-line interface with the -Parallel option.

   You can safely ignore the following compliance check findings:
   - Components NSX LCP Bundle are removed in the image. They will be removed from the host during remediation.
   - The following VIBs on the host are missing from the image and will be removed from the host during remediation.

   This component and VIBs are managed by VMware solutions, NSX and vCenter HA, respectively, and not part of the vSphere Lifecycle manager image. When the hosts are rebooted, the appropriate packages are re-added.

   1. From the main menu, select option 3, Check existing cluster(s)' vLCM image compliance..
   2. Enter a comma-delimited list of the IDs of the vSphere clusters you want to scan for compliance.
   3. Select the vSphere Lifecycle Manager image to compare these vSphere clusters against.

      The script returns a high-level status and summary and saves a JSON file with the full findings for each vSphere cluster.
   4. Review the summary report to determine if a vSphere cluster is ready to be transitioned.

      Resolve any issues for vSphere clusters with a status of INCOMPATIBLE or UNKNOWN .

      | Status | Description |
      | --- | --- |
      | NON\_COMPLIANT | The vSphere cluster is not currently compliant with the selected vSphere Lifecycle Manager image, but is ready to be transitioned. |
      | INCOMPATIBLE | The vSphere cluster cannot be transitioned to the selected vSphere Lifecycle Manager image without taking additional steps. Review the summary and JSON file and resolve any issues that are blocking the transition. Contact Broadcom Support if you are unable to resolve the issue(s). |
      | UNKNOWN | Compatibility could not be determined. Make sure that all the hosts in the vSphere cluster are available. Contact Broadcom Support if you are unable to resolve the issue. |
      | COMPLIANT | The vSphere cluster has already successfully been transitioned to vSphere Lifecycle Manager image management and no further action is required. |

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/9bdf25a2-88a5-4d48-8aaa-ac1f84bb8ca7.original.png)
5. Transition NON\_COMPLIANT (ready to transition) vSphere clusters to vSphere Lifecycle Manager images.

   Once you start a vSphere cluster transition task you cannot pause it.

   1. From the main menu, select option 4, Transition vLCM baseline (VUM) cluster to vLCM image management.
   2. Enter a comma-delimited list of the IDs of the vSphere clusters you want to transition to vSphere Lifecycle Manager images.
   3. Review the compliance findings from those vSphere clusters, if you haven't already, and enter Y to confirm.

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/12c56d71-4f5b-4a4d-86c6-12ddb6be889f.original.png)
   4. Monitor the status of the transition task.

      If the task fails, try the following steps:
      - Return to the main menu .
      - Select Option 6, (Optional) Retry incomplete transition tasks..
      - Wait some time then select Option 9,(Optional) Show cluster transition status..
      - If the process succeeds, no further action is required, if it fails, contact Broadcom Support.
6. Disconnect from SDDC Manager and vCenter.

   Close the PowerShell window or enter Q to quit.