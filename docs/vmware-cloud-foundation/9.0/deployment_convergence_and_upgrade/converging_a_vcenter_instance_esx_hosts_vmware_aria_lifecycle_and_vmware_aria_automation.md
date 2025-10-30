---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/supported-scenarios-to-converge-to-vcf/converge-your-existing-vcenter-instance-esx-hosts-vrealize-suite-lifecycle-manager-and-vmware-aria-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Converging a vCenter Instance, ESX Hosts, VMware Aria Lifecycle, and VMware Aria Automation
---

# Converging a vCenter Instance, ESX Hosts, VMware Aria Lifecycle, and VMware Aria Automation

To successfully converge your existing vCenter instance, ESX hosts, VMware Aria Lifecycle, and VMware Aria Automation, you must ensure that you comply with the prerequisites, follow the procedure, and perform the next steps.

- Verify that your existing configuration is supported and you satisfy the minimum component versions. See Supported Configurations in [Converging Existing Virtual Infrastructure to a VCF or a vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-.html).
- Verify that you activated SSH. See [Activate or deactivate SSH on VMware Aria Suite Lifecycle](https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-suite-lifecycle/8-18/vmware-aria-suite-lifecycle-installation-upgrade-and-management-8-18/configuring-vmware-aria-suite-lifecycle/configure-settings/configure-your-system/enable-or-disable-ssh-on-vrealize-lifecycle-manager.html).

| Item | VCF 9.0.0 Requirements | VCF 9.0.1 Requirements |
| --- | --- | --- |
| Minimum component versions prior to running the VCF Installer workflow | - VMware Aria Automation 8.18 - VMware vCenter 9.0 - VMware ESX 9.0 | - VMware Aria Automation 8.18 - VMware vCenter 8.0 Update 1a - VMware ESX 8.0 Update 1a - VMware NSX 4.1.0.2 |

To ensure a successful convergence process, you must follow this high-level converge procedure in the provided step order. Each step includes a dedicated and detailed procedure, that you must complete, before proceeding with the next one.

VMware Aria Lifecycle is not upgraded to version 9.0.x. After the VCF Operations fleet management appliance is deployed, you must manually import the existing connection with VMware Аria Automation to the new appliance.

If your environment has multiple VMware Aria Automation instances, only the first instance can be managed by your VCF Operations fleet management appliance. Any subsequent VMware Aria Automation instances must be managed by other dedicated VCF Operations fleet management appliances.

1. Ensure your vCenter instance is running the supported version for your convergence scenario.
   - If you are converging to VCF 9.0.0, your vCenter instance must be version 9.0 or later. See [Upgrading the vCenter Appliance](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered).
   - If you are converging to VCF 9.0.1 and your vCenter instance is without an existing NSX registration, upgrade your vCenter instance to version 9.0 or later. See [Upgrading the vCenter Appliance](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered).
   - If you are converging to VCF 9.0.1 and your vCenter instance is version 8.0 Update 1a or later and has an existing NSX registration with version 4.1.0.2 or later, proceed without upgrading.
2. Ensure your ESX hosts are running the supported version for your convergence scenario.
   - If you are converging to VCF 9.0.0, your ESX hosts must be version 9.0 or later. See [Overview of the ESX Host Upgrade Process](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-0&language=&format=rendered).
   - If you are converging to VCF 9.0.1 and your ESX hosts are version 8.0 Update 1a or later, proceed without upgrading.
3. Deploy the VCF Installer appliance.

   See [Deploy the VMware Cloud Foundation Installer Appliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/deploy-the-vmware-cloud-foundation-installer-appliance.html).
4. Download binaries to the VCF Installer appliance.

   See [Downloading Binaries to the VCF Installer Appliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/downloading-binaries-to-the-vcf-installer-appliance.html).
5. Deploy VCF 9.0.x by using your existing components as starting building blocks.

   See [Deploy Components by Using VCF Installer to Complete the Converging to VCF Process](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-new-vcf-fleet-or-a-new-vcf-instance-using-the-deployment-wizard.html).
6. Manually deploy remaining components.

   See [Manual Deployment of Components to Complete Your VCF Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html).
7. Import your VMware Aria Automation in VCF Operations and upgrade to VCF Automation version 9.0.x.

   See [Import and Upgrade VMware Aria Automation in VCF Operations 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html) and [Upgrade to VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9/upgrade-to-vcf-automation.html).

To ensure your VCF environment is fully operational, after completing the required steps in the main convergence procedure, perform the following additional tasks.

- License your VCF environment. See [Licensing Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered).
- If you have VMware Aria components that are not subject to upgrade to version 9.0, import configurations from the old appliances to the new ones. See [Deploying the VCF Operations for Logs Appliance for VCF](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-logs.html) and [Import and Upgrade from 6.13 to VCF Operations for Networks.](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-4-upgrade-additional-management-components-in-vcf-9.html)
- If your VMware Aria Suite Lifecycle appliance no longer manages any deployments, you can delete the appliance.
- Import your existing infrastructure as a workload domain. See [Import an Existing vCenter to Create a Workload Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/import-an-existing-vcenter-to-create-a-workload-domain.html).
- Upgrade your workload domains. See [Upgrading Workload Domains to VMware Cloud Foundation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2.html).
- Integrate your workload domains in VCF Automation. See [Add Workload Domains to Your Cloud Organization Structure](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/getting-started-with-vcf.html#GUID-2159c021-6177-415b-9932-65f78073b983-en_id-727d80e3-f770-4f8f-e604-dd9eef449070).