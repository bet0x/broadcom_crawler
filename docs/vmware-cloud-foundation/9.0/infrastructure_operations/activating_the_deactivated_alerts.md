---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-override-alert-definitions-and-symptom-definitions/policy-alert-definitions/activating-the-deactivated-alerts.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Activating the Deactivated Alerts
---

# Activating the Deactivated Alerts

Several out-of-the-box alerts have been deactivated to enhance your alert experience and reduce alert noise in your environment. The alerts that are triggered for these deactivated alerts are auto-cancelled and as a result, you may experience a dip in the number of alerts triggered. However, you can still activate these alerts in specific policies.

The reason for deactivating these alerts is that there could be an overwhelming number of alerts when alerts are turned on for all objects, making it difficult to identify the ones that need immediate attention. It is recommended to exercise caution while activating the deactivated alerts for applicable policies.

Read the KB article, KB 91410 to know the list of deactivated alerts.

Perform the following steps to activate the deactivated alerts:

1. From the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile.
2. Select the required policy and in the right pane, click Edit Policy, and then select the Alerts and Symptoms tile.
3. Go to Filters and enter the name of the deactivated alert, and click Apply. You can refer to the KB article, KB 91410 for the list of deactivated alerts.
4. Select Activated from the State drop-down list or click ActionsStateActivated.
5. Click Save.

   You can also activate all the deactivated alerts at once. To do this, filter the alerts by Deactivated State, click on the Select All option, and from the Actions drop-down list, click StateActivated.

   You can also activate the deactivated alerts by creating a separate policy, adding custom groups in that policy, and activating the alert definitions in the required policy. By doing this, the deactivated alerts are activated in the user-defined policy and will apply to the objects in the custom group. For more details on custom groups, see [Managing Custom Object Groups in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/inventory-management/configuring-objects/object-discovery/managing-custom-object-groups.html#GUID-260ea762-9d8a-4541-8202-c5b94c81329c-en_GUID-FFCA5453-A141-49F7-9533-31F76104F6C6).

The deactivated alerts are now active.