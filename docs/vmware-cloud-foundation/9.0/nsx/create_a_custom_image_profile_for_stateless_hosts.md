---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/create-a-custom-image-profile-for-stateless-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create a Custom Image Profile for Stateless Hosts
---

# Create a Custom Image Profile for Stateless Hosts

In your data center, identify a host to be prepared as the reference host.

Ensure that the auto-deploy service and image builder service are enabled. See Using vSphere Auto Deploy to Reprovision Hosts.

The first time the reference host starts up, ESX associates the default rule with the reference host. In this procedure, we are adding a custom image profile (ESX and NSX VIBs) and associate the reference host with the new custom image. An image profile with the NSX image significantly reduces the installation time. The same custom image is associated with the target hosts in the stateless cluster.

Alternatively, you can add only an ESX image profile to the reference and target stateless cluster. The NSX VIBs are downloaded when you apply the transport node profile on the stateless cluster. See Add a Software Depot.

1. To import NSX packages, create a software depot.
2. Download the nsx-lcp packages.

   1. On the [Broadcom Support](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20NSX) portal, search NSX Kernel Modules for a specific VMware ESX version and download the nsx-lcp packages.
   2. Import nsx-lcp packages into the software depot.

   ![Download NSX packages into the software depot.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7b711e0b-1c4a-43b9-8176-1f18c8ad6972.original.png)
3. Create another software depot to import ESX packages.

   The vSphere Web Client displays two depots created on the reference host.
4. Create a custom software depot to clone previously imported ESX image and nsx-lcp packages.

   1. Select the ESX Image profile from the ESX software depot created in the earlier step.
   2. Click Clone.
   3. In the Clone Image Profile wizard, enter a name for the custom image to be created.
   4. Select the custom software depot where the cloned image (ESX) must be available.
   5. In the Select software packages window, select the Acceptance level to VMware Certified. The ESX VIBs are preselected.
   6. Identify and select the NSX packages manually from the list of packages and click Next.
   7. In the Ready to complete screen, verify the details and click Finish to create the cloned image containing ESX and NSX packages into the custom software depot.

   ![Select software packages into the custom software depot.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2da3346e-4230-40ce-885e-221bb3071e63.original.png)

Associate the custom image with the reference and target hosts. See Associate the Custom Image with the Reference and Target Hosts.