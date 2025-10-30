---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/git/syncing-config-templates-with-git-integration.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Syncing Configuration Templates with Source Control
---

# Syncing Configuration Templates with Source Control

After you configure the source control solution in VCF Operations, sync the configuration templates with the source control repository. This topic outlines the different workflows you can follow to manage the configuration templates and integrate them with the repository.

## Review, Sync, and Merge Templates from VCF Operations

**Review Process Enabled**

When you create, edit, or delete a template in VCF Operations, a merge request is created in source control and is visible in the Config Template list view. You must review and approve the request in your source control solution. After the request is approved, the template status changes to OUT\_OF\_SYNC. Sync the template using the Sync option in VCF Operations. The template status changes to IN\_SYNC after the sync is complete.

The edited or deleted content is reflected only after the merge request is approved and the content is synced.

**Review Process Disabled**

When you edit a template, the template is directly edited in the source control repository without a request. If you delete a template from VCF Operations, the template is marked OUT\_OF\_SYNC and is directly deleted from the source control during the next sync.

## Sync Existing Templates in VCF Operations

**Code Review Process Enabled**

When source control integration is enabled, merge requests are created for syncing all existing templates from VCF Operations to the source control repository. After the request is approved, the template status changes to OUT\_OF\_SYNC. Use the Pull from GitHub option to sync content from the repository. The status of the template changes to IN\_SYNC after the sync is successful.

**Code Review Process Disabled**

The status of all existing templates reflects as OUT\_OF\_SYNC: No request is raised. You must use the Sync option to sync content from source control. The status changes to IN\_SYNC after the sync is complete.

## Sync Remote Templates to VCF Operations

If you edit or delete existing templates in the source control repository, the status of the corresponding templates reflects as OUT\_OF\_SYNC in VCF Operations.

When you edit a template in the source control repository, you must Pull from GitHub, and after the sync is successful, the updated template content gets reflected in VCF Operations and the status changes to IN\_SYNC.

When you delete a template in the source control repository, the template is removed from VCF Operations.

When you configure a source control in VCF Operations, existing templates without any content in the source control repository will be created in VCF Operations as placeholders and reflect the OUT\_OF\_SYNC status. You must sync the content to populate the templates. The status changes to IN\_SYNC after the sync is complete.

## Additional Information

**Merge Request Discarded**

A merge request can be discarded if the changes proposed in the merge request are no longer valid or required. If a merge request is discarded or closed by the user, a warning message is displayed informing the user that the changes made to the corresponding template in VCF Operations are not merged and the current template may not reflect the desired state in source control

You can edit the template to make the necessary updates and address the issues that caused the merge request to be discarded. After you make the update a new request is raised. This ensures that the latest template changes are submitted for review.

**Drift Detection**

Drift detection is skipped if the template does not exist in the source control repository. This may occur in scenarios where the template has not been synced with the source control.

## Updating Source Control Configurations

**Editing or Updating Branch or Repositories**

You can update the branch or repository or switch to a new branch or repository. Once done, the templates from the previous source control repository displays the OUT\_OF\_SYNC status. The existing templates in VCF Operations will sync to the new branch or repository. For more information, see Sync Existing Templates in VCF Operations section.

If you delete a source control configuration, the templates stored locally in VCF Operations remain unchanged, however the status changes to OUT\_OF\_SYNC.

If you want to update your source control type, you must first delete the existing configuration.