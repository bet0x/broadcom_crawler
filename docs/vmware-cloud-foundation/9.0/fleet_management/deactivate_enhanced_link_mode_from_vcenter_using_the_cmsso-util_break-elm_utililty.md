---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Deactivate Enhanced Link Mode from vCenter Using the cmsso-util break-elm Utililty
---

# Deactivate Enhanced Link Mode from vCenter Using the cmsso-util break-elm Utililty

VCF Single Sign-On is not compatible with the vCenter Enhanced Linked Mode (ELM). Before you configure VCF Single Sign-On, you must deactivate ELM on all participating vCenter Instances. As an administrator, if you want to deactivate ELM in vCenter Instances, you can do so without causing any loss to existing customer configurations such as global permissions. This procedure applies to existing customers.

The utility will only deactivate ELM and related features (for example, Single Pane of Glass (SPOG)/replication, and so on). Any shared configurations, like tags, roles, permissions and so on that are in ELM, will remain local to individual vCenter Instances after you deactivate ELM.

The new **cmsso-util break-elm** utility works only if all vCenter Instances in the ELM topology are up and running and vCenter Instances are upgraded 9.0. It is recommended that admins take offline snapshots of all vCenter instances before you deactivate the ELM. The only proper way to back up vCenter instances in ELM is to take offline snapshots of them which results in environment downtime.

If you upgraded from VMware Cloud Foundation 5.x to 9.0, see [Deactivate Enhanced Link Mode (ELM) Using the SDDC Manager API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/deactivate-enhanced-link-mode--elm--for-upgraded-vmware-cloud-foundation-vcenters.html) and [Resolve Enhanced Linked Mode (ELM) Drift for Upgraded vCenter Instances](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime/resolve-enhanced-linked-mode--elm--drift-for-upgraded-vmware-cloud-foundation-vcenters.html).

1. Take an offline backup of the ELM topology (only recommended way to revert back to ELM).

   This is a preparatory step and requires downtime.
2. SSH to any vCenter in ELM.
3. Run configuration pre-checks and fix any issues.
   1. Run cmsso-util break-elm --mode pre-check --password <default administrator user\_password>.
   2. Fix any issues reported by the pre-check.

      Output of break-elm precheck when successful:

      ```
      Command:cmsso-util break-elm --mode pre-check --password 'ZSIY+eDe-14dukrW'
      Output: Mode: pre-check This operation might take a few minutes to complete.
      [Pre-check] Invoking Break ELM topology workflow...
      [Pre-check] Fetch the peer nodes details...
      [Pre-check] Executing break ELM on local node...    
      [Pre-check] Executing break ELM on all peer nodes...    
      Break ELM pre-checks completed successfully.
      ```
4. Deactivate Enhanced Link Mode.
   1. Run cmsso-util break-elm --mode execute --password <administrator\_password>.
   2. Log out from the vSphere Client and log in again for the changes to take effect.
   3. In case of a failure, fix the cause of the failure and rerun cmsso-util break-elm on all nodes where the failure was reported.

You must resolve ELM drift. For more information, see [Resolve Enhanced Linked Mode (ELM) Drift for Upgraded vCenter Instances](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is/points-to-consider-while-setting-up-vmware-cloud-foundation-sso/how-to-deactivate-enhanced-link-mode-in-vcenter-without-downtime/resolve-enhanced-linked-mode--elm--drift-for-upgraded-vmware-cloud-foundation-vcenters.html#GUID-234903af-6a32-41a7-935a-025c44437a55-en_id-da8acaa0-009d-4b7f-cc08-ab38f1b8767a).