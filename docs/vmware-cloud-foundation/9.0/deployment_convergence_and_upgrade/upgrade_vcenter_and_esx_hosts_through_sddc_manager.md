---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade vCenter and ESX Hosts Through SDDC Manager
---

# Upgrade vCenter and ESX Hosts Through SDDC Manager

After upgrading all the edge clusters, you can use SDDC Manager to upgrade vCenter and the ESX hosts.

[Upgrade all the edge transport nodes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/upgrade-nsx-edge-cluster-nsxt.html). You cannot proceed with ESX host upgrades in SDDC Manager until all the edge nodes have finished upgrading.

The upgrade tool in SDDC Manager guides you through the process of upgrading vCenter and the ESX hosts. For detailed instructions, see the following:

- [Upgrade to vCenter 9.0 for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vcenter-server-for-vmware-cloud-foundation-5-2.html)
- [Upgrade to ESX 9.0 for VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-esxi-for-vmware-cloud-foundation-5-2-1.html)

Starting with VMware Cloud Foundation 9.0, the NSX VIBs are packaged as part of the ESX image by default. Therefore, the upgrade of these VIBs occurs as part of the ESX host upgrade process performed through SDDC Manager.

The upgrade coordinator in NSX Manager reflects the status of the host upgrade performed through SDDC Manager.