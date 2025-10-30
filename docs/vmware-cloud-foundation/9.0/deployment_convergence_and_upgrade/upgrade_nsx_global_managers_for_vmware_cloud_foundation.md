---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/upgrade-nsx-in-a-federated-environment/upgrade-nsx-global-managers-for-vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrade NSX Global Managers for VMware Cloud Foundation
---

# Upgrade NSX Global Managers for VMware Cloud Foundation

Manually upgrade the NSX Global Managers when NSX Federation is configured between two SDDC Manager instances.

You must upgrade NSX Global Managers before you can upgrade any VMware Cloud Foundation instances in the NSX Federation, including NSX Local Managers.

1. In a web browser, log in to the NSX Global Manager for the domain at https://nsx\_gm\_vip\_fqdn/).
2. Select System > Upgrade from the navigation panel.
3. Click Start to upgrade the management plane and then click Accept.
4. On the Select Upgrade Plan page, select Plan Your Upgrade and click Next.

   The NSX Manager UI, API, and CLI are not accessible until the upgrade finishes and the management plane is restarted.