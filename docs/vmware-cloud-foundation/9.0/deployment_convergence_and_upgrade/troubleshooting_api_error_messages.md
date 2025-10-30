---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-to-vsphere-lifecycle-manager-images-using-the-vmware-cloud-foundation-api/troubleshooting-api-error-messages.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Troubleshooting API Error Messages
---

# Troubleshooting API Error Messages

Review the following common error messages that you may see when transitioning vSphere clusters from vSphere Lifecycle Manager baselines to vSphere Lifecycle Manager images. Refer to the remediation information for next steps.

The underlying cause of a failed step may be within an asynchronous task or the original API call.

| Error Message | Possible cause | Remediation |
| --- | --- | --- |
| Personality <Image Name> with same specification already exists | A vSphere Lifecycle Manager image with the exact same parameters already exists in SDDC Manager. You cannot import duplicate images, even if they have different names. | No action required. Use the existing image in SDDC Manager to transition the vSphere cluster(s). |
| Failed to import the image. Personality with the specified name/id already exists. | A vSphere Lifecycle Manager image with the same name already exists in SDDC Manager. | For vCenter 8.0.3 and below, repeat the workflow with a new name.  For vCenter 9.0 and above, rename the source image and repeat the workflow. |
| Highest ESX version <Version> in cluster: <Cluster Name> does not match version: <Version> in cluster image: <Image Name> | The vSphere Lifecycle Manager base image does not match the ESX version running on the hosts in the vSphere cluster. | Update the vSphere Lifecycle Manager image to match the ESX version on the hosts. |