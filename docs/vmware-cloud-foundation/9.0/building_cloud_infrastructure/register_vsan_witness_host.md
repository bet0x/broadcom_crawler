---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host/register-vsan-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Register vSAN Witness Host
---

# Register vSAN Witness Host

Before you can configure the vSAN witness host, you must register it with vCenter.

1. Use the vSphere Client to log in to the vCenter containing the cluster that you want to stretch.
2. In the vSphere Client, navigate to the datacenter.
3. Right-click the datacenter and select Add Host.

   You must add the vSAN witness host to the datacenter. Do not add it to a folder.
4. On the Name and location page, enter the Fully Qualified Domain Name (FQDN) of the vSAN witness host and click Next.

   Do not use the IP address.
5. On the Connection settings page, enter the root credentials for the witness host and click Next.
6. On the Host summary page, review the summary of the host details and click Next.
7. On the Host lifecycle page, select an option and specify a vSphere Lifecycle Manager image.
8. On the Assign license page, assign an existing license and click Next.

   Do not create a new license.
9. Review the summary and click Finish.