---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/finalize-upgrade.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Finalize Upgrade Through NSX Manager
---

# Finalize Upgrade Through NSX Manager

As the last step in the manual upgrade process, you must finalize the upgrade.

Verify that you have upgraded all of the following components:

- [Management Plane](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-management-plane-from-nsx-3-2-1-x-and-later.html)
- All [edge nodes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-nsx-edge-cluster-nsxt.html)
- All host transport nodes, either by upgrading [both the NSX VIBs and ESX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts.html) through SDDC Manager or by upgrading [only the NSX VIBs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts-nsxt.html) through NSX Manager.

After the upgrades of the Management Plane, edge transport nodes, and hosts are complete, the upgrade coordinator in NSX Manager finalizes the upgrade by unpinning the NSX API and NSX Manager UI from the source version. This operation enables your access to the target version of the NSX API and NSX Manager UI.

The upgrade coordinator also validates that any vSphere Supervisor cluster running on the NSX instance is compatible with the target VCF version. If the validation fails, the Finalize Upgrade step pauses until you have upgraded vSphere Supervisor to a compatible version (for example, vSphere Supervisor 9.0.0.0 is compatible with VCF 9.0.0.0). This validation applies only to vSphere Supervisor, not to any other type of Kubernetes cluster running on the NSX instance.

1. In the upgrade coordinator in NSX Manager, click Finalize Upgrade.

   The upgraded NSX functionality does not become available until after the Finalize Upgrade step succeeds.

- Check the cluster status and verify that the services have started from the NSX Manager user interface.
- [Verify the upgrade](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/verify-the-upgrade-nsxt.html) or [troubleshoot upgrade failures](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt.html), depending on the upgrade status.