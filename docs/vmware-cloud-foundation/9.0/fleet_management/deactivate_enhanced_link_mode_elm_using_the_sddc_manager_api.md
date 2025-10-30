---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/deactivate-enhanced-link-mode--elm--for-upgraded-vmware-cloud-foundation-vcenters.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Deactivate Enhanced Link Mode (ELM) Using the SDDC Manager API
---

# Deactivate Enhanced Link Mode (ELM) Using the SDDC Manager API

If you upgraded from VMware Cloud Foundation 5.x to 9.0, you must use the SDDC Manager API to deactivate Enhanced Link Mode (ELM) for upgraded vCenter instances before you can use certain 9.0 features.

Minimum required version of the VCF components.

- SDDC Manager 9.0
- vCenter upgraded to 9.0

When you created a workload domain in VMware Cloud Foundation 5.x, you chose whether to join its vCenter to the management domain's vCenter Single Sign-On domain or to create a new vCenter Single Sign-On domain. If you joined it to the management domain's vCenter Single Sign-On domain, the workload domain vCenter was joined to the management domain vCenter in Enhanced Linked Mode (ELM).

ELM is deprecated in VMware Cloud Foundation 9.0. Before you can use new features in 9.0, such as VCF Single Sign-On and vCenter linking, you must deactivate ELM for all vCenter instances in your VCF instance.

You can use the SDDC Manager API to remove all the vCenter instances in a VCF instance from Enhanced Linked Mode (ELM), creating isolated workload domains.

This procedure deactivates ELM for all vCenter instances in your VCF instance. You cannot select a subset of instances.

If you already used the cmsso-util break-elm utility to remove some or all of you VCF-managed vCenter instances from ELM, see [Resolve Enhanced Linked Mode (ELM) Drift for Upgraded vCenter Instances](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime/resolve-enhanced-linked-mode--elm--drift-for-upgraded-vmware-cloud-foundation-vcenters.html).

1. Use the SDDC Manager API to retrieve the management domain ID.

   | API | Description |
   | --- | --- |
   | GET /v1/domains | Find the management domain ID in the Response. |
2. Validate the break ELM spec.

   | API | Description |
   | --- | --- |
   | POST /v1/domains/{id}/validations | Replace {id} with the management domain ID.  In the body parameter enter:  ``` {   "breakElmSpec": {       "isReconcileWorkflow": false   } } ```  Find the validation ID in the Response. |
3. Get the validation response.

   Make sure that validation is successful.

   | API | Description |
   | --- | --- |
   | GET /v1/domains/{id}/validations/{validation\_id} | Replace {id} with the management domain ID.  Replace {validation\_id} with the validation ID. |
4. Break ELM across all joined domains.

   | API | Description |
   | --- | --- |
   | PATCH /v1/domains/{id} | Replace {id} with the management domain ID.  In the body parameter enter:  ``` {  "breakElmSpec": {      "isReconcileWorkflow": false  } } ```  Find the task ID in the Response. |
5. Monitor the task.

   | API | Description |
   | --- | --- |
   | GET /v1/tasks/{id} | Replace {id} with the task ID. |