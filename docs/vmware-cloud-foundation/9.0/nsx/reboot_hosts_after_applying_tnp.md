---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/trigger-auto-deployment-on-target-hosts/reboot-hosts-after-applying-tnp.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Reboot Hosts After Applying TNP
---

# Reboot Hosts After Applying TNP

Only applies to stateless hosts. When a new node is added to the cluster, manually
reboot the node for the ESX and NSX packages to be configured on it.

1. Apply TNP to the stateless
   cluster that is already prepared with host profile. See [Create and Apply TNP on
   Stateless Cluster](https://confluence.eng.vmware.com/display/~jubint/Auto+deploy+stateless+cluster+in+NSX-T#AutodeploystatelessclusterinNSX-T-CreateandApplyTNPonStatelessCluster).
2. Reboot hosts. 

   After applying TNP profile to the stateless cluster, when you reboot any
   new node joining the cluster that node is automatically configured with
   NSX on the
   host.

Ensure that you reboot any new node joining the cluster to automatically deploy and
configure ESX and NSX on the rebooted node.

To troubleshoot issues related to host
profile and transport node profile when configuring auto-deployment, see [Troubleshoot Host Profile and Transport Node Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/troubleshoot-host-profile-and-transport-node-profile.html#GUID-3e36eb9a-892a-44e6-9f12-838605a0333c).