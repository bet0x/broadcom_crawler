---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/trigger-auto-deployment-on-target-hosts/reboot-hosts-before-applying-tnp.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Reboot Hosts Before Applying TNP
---

# Reboot Hosts Before Applying TNP

Only applies to stateless hosts. In this scenario, the transport node profile is not
applied to the stateless cluster, which means that NSX is not installed and configured on the target host.

1. Reboot hosts.

   The target host starts with the ESX image. After starting, the target host remains in
   maintenance mode until the TNP profile is applied to the target host and
   NSX installation is
   complete. Profiles are applied on hosts in the following order:

   Profiles are applied on hosts in
   the following order.
   - Image profile is
     applied to the host.
   - Host profile
     configuration is applied to the host.
   - NSX configuration is applied
     to the host.

   ESX VIBs are
   applied to all the rebooted hosts. A temporary NSX switch in an ESX host. When TNP is applied to the
   hosts, the temporary switch is replaced by the actual NSX switch.

Apply TNP to the stateless cluster. See [Apply TNP on Stateless Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/trigger-auto-deployment-on-target-hosts/apply-tnp-on-stateless-cluster.html#GUID-34fae82d-b47e-41bc-bb61-5bcdbd2ec3d8).