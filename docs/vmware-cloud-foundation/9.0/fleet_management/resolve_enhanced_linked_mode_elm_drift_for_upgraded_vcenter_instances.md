---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime/resolve-enhanced-linked-mode--elm--drift-for-upgraded-vmware-cloud-foundation-vcenters.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Resolve Enhanced Linked Mode (ELM) Drift for Upgraded vCenter Instances
---

# Resolve Enhanced Linked Mode (ELM) Drift for Upgraded vCenter Instances

If you remove vCenter instances from ELM outside of SDDC Manager, some workflows will be blocked until you reconcile the ELM drift using the SDDC Manager API.

Remove all the vCenter Instances in your VCF instance from ELM using the cmsso-util break-elm utility. See [Deactivate Enhanced Link Mode from vCenter Using the cmsso-util break-elm Utililty](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime.html).

Until you resolve ELM drift, you may see error messages when running certain workflows. For example: Functionality CREATE\_DOMAIN is not allowed because there is an ELM Drift. Ensure the ELM is completely broken, then run the reconcile workflow..

1. Use the SDDC Manager API to retrieve the management domain ID.

   | API | Description |
   | --- | --- |
   | GET /v1/domains | Find the management domain ID in the Response. |
2. Validate the break ELM reconcile workflow.

   | API | Description |
   | --- | --- |
   | POST /v1/domains/{id}/validations | Replace {id} with the management domain ID.  In the body parameter enter:  ``` {  "breakElmSpec": {      "isReconcileWorkflow": true  } } ```  Find the validation ID in the Response. |
3. Get the validation response.

   Make sure that validation is successful.

   | API | Description |
   | --- | --- |
   | GET /v1/domains/{id}/validations/{validation\_id} | Replace {id} with the management domain ID.  Replace {validation\_id} with the validation ID. |
4. Resolve ELM drift across all joined domains.

   | API | Description |
   | --- | --- |
   | PATCH /v1/domains/{id} | Replace {id} with the management domain ID.  In the body parameter enter:  ``` { "breakElmSpec": {     "isReconcileWorkflow": true } } ```  Find the task ID in the Response. |
5. Monitor the task.

   | API | Description |
   | --- | --- |
   | GET /v1/tasks/{id} | Replace {id} with the task ID. |