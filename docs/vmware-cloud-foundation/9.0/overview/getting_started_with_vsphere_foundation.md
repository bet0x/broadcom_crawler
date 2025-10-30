---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/getting-started-with-vsphere-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Overview
breadcrumb: Overview > Getting Started with vSphere Foundation
---

# Getting Started with vSphere Foundation

You can start building a vSphere Foundation private cloud by deploying a new platform оr converging your existing virtual infrastructure to vSphere Foundation. After you deploy VCF Operations using a new or existing vCenter instance , you can continue with adding vCenter instances to the cloud.

In this article:

- [Deploy VCF Operations](#GUID-7e31f41c-7373-4220-a12e-45b2824b54fe-en_id-6f7a9559-13aa-4e75-ab6a-3b104e4a481d)
- [Add vCenter Instances to VCF Operations](#GUID-7e31f41c-7373-4220-a12e-45b2824b54fe-en_id-be93f6d9-0612-4d13-8651-ddb3a54b48ef)
- [Complete the Configuration of vSphere Foundation](#GUID-7e31f41c-7373-4220-a12e-45b2824b54fe-en_id-3ca04d18-c07c-4bbb-edd8-4ee22c8c781f)
- [Detailed Journeys](#GUID-7e31f41c-7373-4220-a12e-45b2824b54fe-en_id-c819e954-e704-4c14-dce7-f606a737a2f6)
- [What to Do Next](#GUID-7e31f41c-7373-4220-a12e-45b2824b54fe-en_id-5e06cb55-0d23-4024-a7e2-019e783b85e7)

## Deploy VCF Operations

The first step in building a vSphere Foundation platform is deploying VCF Operations in one of the following ways:

- [Deploy VCF Operations with a new vCenter instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-.html).
- [Deploy VCF Operations on an existing vCenter instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-vmware-vsphere-foundation-environment-using-the-deployment-wizard.html).

If you have an existing VMware Aria Operations and vCenter instance with managed vSphere clusters, upgrade VMware Aria Operations to VCF Operations 9.0, and vCenter and ESX to version 9.0.

## Add vCenter Instances to VCF Operations

After you deploy or upgrade to VCF Operations, you can start adding vCenter instances with infrastructure running consumer workloads. See [vSphere as a data source in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere.html).

## Complete the Configuration of vSphere Foundation

After you deploy VCF Operations or add a vCenter instance to it, complete the platform's configuration by performing the following tasks. Assigning a license must be done right after you complete deployment.

- [Assign a license](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing.html).
- [Configure backup of the management components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation.html).
- [Configure certificate management in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation.html).
- [Configure password management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/passwords-and-certificates-container.html).
- [Deploy and configure vSphere Supervisor](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsphere-supervisor-installation-and-configuration.html).

## Detailed Journeys

For visual guides to the sequences of getting started operations, see the following vSphere Foundation journey maps.

- [Build Journey - Install a New vSphere Foundation Deployment](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vvf-deploy-journey.pdf)
- [Build Journey - Converge Existing vSphere to vSphere Foundation 9 with a New VCF Operations Instance](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vvf-converge-from-vsphere-journey.pdf)
- [Build - Upgrade Existing vSphere and VMware Aria Operations to vSphere Foundation 9](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vvf-converge-from-vsphere-aria-operations-journey.pdf)

## What to Do Next

If you want to run Kubernetes workloads, VMs, or vSphere Pods on vSphere, see [Building Cloud Applications](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-cloud-applications.html).