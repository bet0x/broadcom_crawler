---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/using-the-configuration-management-dashboard/viewing-drifts-for-the-vcenter-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Viewing Drifts and Downloading Drift Reports for vCenter Instances
---

# Viewing Drifts and Downloading Drift Reports for vCenter Instances

You can detect configuration drifts for each configuration template you have created for a specific vCenter.

To view vCenter configuration setting values and detect configuration drifts, you must:

- Ensure that you have created at least one configuration template for your vCenter.
- Ensure that the user is configured with the Administrator role in VCF Operations. For more information, see [Privileges Required for Configuring a Adapter Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations/privileges-required-for-configuring-a-vcenter-adapter-instance.html).
- Verify that you have Configuration Drifts privileges to access configuration templates. For more information, see [Managing Users and Access Control in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/managing-user-access-control.html) .

  - Manage Privilege: for creating templates, assigning them to policy, and running drift check.
  - View Privilege: for viewing template content and viewing existing drift.
- Verify that you have the vCenter instance configured and registered with the cloud proxy and that the vCenter instance has one active policy assigned to the configuration template.

1. To view your configuration drift details, Fleet ManagementConfiguration Drifts.
2. Expand VCF Instances, select any VCF instance, and click on the Drifts tab.

   On the Drifts Details page, you can view the number of enabled vCenter instances on the vCenter Instances tile. You can also view the number of vSphere Configuration Profiles enabled clusters on the Clusters tile. For more information, see [Viewing Drifts for Clusters](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/using-the-configuration-management-dashboard/viewing-drifts-for-clusters.html).

   By default, the vCenter instances tile is selected.
3. Select one or more vCenter instances.
4. Click Detect Drift to detect configuration drift.

   This detects drifts across all the configuration templates and displays the result in the Drifts table.
5. To view the drift for each vCenter, click on the vCenter instance.
6. Select a Config Template to view the drift details.

   If a drift is detected, the right pane displays the drifts between the Current vCenter Value and the Config Template Value. If no drift is detected for the selected template, the message No drift found for this Config Template since last configuration drift check status is displayed.

   - Detect Drift: To further detect drift for a particular template in a vCenter instance.
   - View Template: To view the configuration template.
7. Navigate to the Drifts Details page, select one or more vCenter instances, and click Download Drift Status Report to download the historical drift data.

   The Config Drift Report displays the date, resource, template, and drift status for each vCenter instance. By default the report shows data for the last seven days. You can update the duration to up to 30 days from the Global Settings page. For more information, see [List of Global Settings](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/modifying-global-settings/list-of-global-settings.html).