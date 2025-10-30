---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/extract-and-verify-the-host-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Extract and Verify the Host Profile
---

# Extract and Verify the Host Profile

After you extract the host profile from the reference host, verify the NSX configuration extracted in the host profile. It consists of ESX and NSX configuration that is applied to target hosts.

1. To extract the host profile, see the topic Extract and Configure Host Profile from the Reference Host.
2. In the extracted host profile verify NSX configuration.

   ![Verify NSX configuration.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/98ef40c8-6b63-4046-84d5-8f33040872b7.original.png)

   ![Verify NSX configuration.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c4cd24bc-ae54-4f6e-9f59-385072fc485f.original.png)
3. To verify DVS switch is enabled on NSX, select Policies and ProfilesHost ProfilesConfigurevSphere Distributed Switch.

   ![Verify whether DVS switch is enabled.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ef6beebd-d887-437d-ab46-608fdae8f82e.original.png)
4. Select the DVS switch and determine whether NSX is enabled on DVS.

Verify the host profile association with stateless cluster. See [Verify the Host Profile Association with Stateless Cluster](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/verify-the-host-profile-association-with-stateless-cluster.html#GUID-809fffdf-6153-43c1-a4c7-082bdf0cd535).