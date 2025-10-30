---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/update-host-customization.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Update Host Customization
---

# Update Host Customization

After the attaching the host profile to the target cluster, additional custom entries
might be required on the host to successfully auto deploy the ESX and NSX packages on it.

1. After attaching the host profile
   to the target cluster, if the hosts are not updated with custom values, the
   system displays the following message.

   ![Hosts were not updated with customizations because attaching the host
                               profile to the target cluster did not complete.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/624e22ea-d158-44b8-80d1-dc882ffe9dc4.original.png)
2. To update host customizations, navigate to the host profile, click
   Actions -> Edit Host
   Customizations.
3. For ESX versions 67ep6, 67ep7,
   67u2, enter the MUX user password.

   ![Enter MUX user password.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/45931676-febd-42f2-a461-441bbeba563c.original.png)
4. Verify that all the required fields are updated with appropriate values.

Trigger Auto Deployment on Target Hosts. See [Trigger Auto Deployment on Target Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/trigger-auto-deployment-on-target-hosts.html#GUID-e893d88a-19a5-4653-974a-05d014c8e6b9).