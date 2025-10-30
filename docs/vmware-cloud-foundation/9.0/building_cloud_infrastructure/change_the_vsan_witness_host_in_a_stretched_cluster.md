---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/change-a-vsan-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Change the vSAN Witness Host in a Stretched Cluster
---

# Change the vSAN Witness Host in a Stretched Cluster

You can replace or change the vSAN witness host for a stretched cluster using the vSphere Client without affecting lifecycle operations.

Verify that the vSAN witness host is not in use by another cluster, has a VMkernel configured for vSAN traffic, and has no vSAN partitions on its disks.

1. In a web browser, log in to vCenter at https://vcenter\_fqdn/ui.
2. Select MenuHosts and Clusters.
3. In the inventory panel, expand vCenterDatacenter.
4. Select the stretched cluster and click Configure.
5. Under vSAN, click Fault Domains.

   ![The vSAN menu options showing Fault Domains.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f98683ab-29a7-49bf-8a86-42201f8fe072.original.png)
6. Click the Change button.
7. Select a new host to use as the vSAN witness host and click Next.
8. Claim disks on the new witness host and click Next.
9. Review the configuration and click Finish.