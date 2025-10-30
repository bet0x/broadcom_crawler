---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/verify-the-host-profile-association-with-stateless-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Verify the Host Profile Association with Stateless Cluster
---

# Verify the Host Profile Association with Stateless Cluster

To prepare the target stateless cluster with ESX and NSX configuration, associate the host profile extracted from the reference host to the target stateless cluster.

Without the host profile associated to the stateless cluster, new nodes joining the cluster cannot be auto deployed with ESX and NSX VIBs.

1. Attach or Detach Host Profile to Stateless Cluster. See the topic Attach or Detach Entities from a Host Profile in the vSphere product documentation.
2. In the Deployed Hosts tab, verify that the existing stateless host is associated with the correct image and associated with the host profile.
3. If the host profile association is missing, select the target host and click Remediate Host Associations to force update the image and host profile to the target host.

   ![Select a host for remediation to force update the image and host profile to the target host.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ee19c2b2-a193-4721-9188-9dbeb192928b.original.png)

Update Host Customization. See [Update Host Customization](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/update-host-customization.html#GUID-79515e0d-cd50-48f7-b887-201679f4f290).