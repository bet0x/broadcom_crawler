---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/associate-the-custom-image.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Associate the Custom Image with the Reference and Target Hosts
---

# Associate the Custom Image with the Reference and Target Hosts

To start the reference host and target hosts with the new custom image containing
ESX and NSX packages, associate the
custom image profile.

At this point in the procedure, the
custom image is only being associated to the reference and target hosts but NSX
installation does not happen.

Perform this custom image association procedure on both
reference and target hosts.

1. On the ESX host, navigate to
   Menu > Auto Deploy >
   Deployed Hosts.
2. To associate the custom image profile with a host, select the custom
   image.
3. Click Edit Image Profile Association.
4. In the Edit Image Profile Association wizard, click
   Browse and select the custom depot and select the
   custom image profile.
5. Enable Skip image profile signature check.
6. Click Ok.

   ![Edit the Image Profile Association for a deployed host and assign it a
                               custom image profile.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f55de651-5e14-4bd2-906f-2d0c7b645be6.original.png)

Set up Network Configuration on the
Reference Host. See [Set Up Network Configuration on the Reference Host](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/set-up-network-configuration-on-the-reference-host.html#GUID-657de35b-88ad-4c3f-a8e4-b9d4a1f6917c).