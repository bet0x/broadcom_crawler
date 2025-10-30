---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/verify-the-nsxt-environment.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Verify the Current State of NSX
---

# Verify the Current State of NSX

Before you begin the upgrade process, it is important to test the NSX working state. Otherwise, you cannot determine if the upgrade caused post-upgrade problems or if the problem existed before the upgrade.

Do not assume that everything is working before you start to upgrade the NSX infrastructure.

1. Identify and record the administrative user IDs and passwords.
2. Verify that you can log in to the NSX Manager web user interface.
3. Check the Dashboard, system overview, host transport nodes, edge transport nodes, NSX edge cluster, HA status of the edge, and all logical entities to make sure that all the status indicators are green, deployed, and do not show any warnings.
4. Validate North-South connectivity by pinging out from a VM.
5. Validate that there is an East-West connectivity between any two VMs in your environment.
6. Record BGP states on the edge devices.

   - get logical-routers
   - vrf <vrf>
   - get bgp
   - get bgp neighbor