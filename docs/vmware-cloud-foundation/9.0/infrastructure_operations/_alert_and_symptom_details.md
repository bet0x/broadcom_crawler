---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/policy-workspace-override-alert-definitions-and-symptom-definitions.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >  Alert and Symptom Details
---

# Alert and Symptom Details

You can activate or deactivate alert and symptom definitions to have VCF Operations identify problems on objects in your environment and trigger alerts when conditions occur that qualify as problems. You can automate alerts.

## How the Alert and Symptom Definitions Workspace Works

VCF Operations
collects data for objects and compares the collected data to the alert definitions and symptom definitions defined for that object type. Alert definitions include associated symptom definitions, which identify conditions on attributes, properties, metrics, and events.

You can configure your local policy to inherit alert definitions from the base policies that you select, or you can override the alert definitions and symptom definitions for your local policy.

Before you add or override the alert definitions and symptom definitions for a policy, familiarize yourself on the available alerts and symptoms.

- To view the available alert definitions, from the left menu, click Infrastructure OperationsConfigurations, and then click the Alert Definitions tile.
- To view the available symptom definitions, from the left menu, click Infrastructure OperationsConfigurations, and then click the Symptom Definitions tile. Symptom definitions are available for metrics, properties, messages, faults, smart early warnings, and external events.

A summary of the number of problem and symptoms that are activated and deactivated, and the difference in changes of the problem and symptoms as compared to the base policy, appear in the Analysis Settings pane of the policies workspace.

## Where You Override the Alert Definitions and Symptom Definitions

To override the alert definitions and symptom definitions for your policy, from the left menu click Infrastructure OperationsConfigurations, and then click the Policy Definition tile. Click Add to add a policy or select the required policy. In the right pane, click Edit Policy to edit a policy. In the Create or Edit policies workspace, click Alerts and Symptoms. The definitions appear in the workspace.

## Policy Alert Definitions and Symptom Definitions

You can override the alert definitions and symptom definitions for each policy.