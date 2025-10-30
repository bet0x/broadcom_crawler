---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/overview-of-deploy--converge--and-upgrade.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Overview of Deploy, Converge, and Upgrade
---

# Overview of Deploy, Converge, and Upgrade

There are multiple paths to get to vSphere Foundation and VCF 9.0.x. Depending on your starting state, you follow one of the paths.

## Paths to building an environment with version 9.0.x

Depending on the starting state of your environment, you can deploy, converge, or upgrade the environment to VMware Cloud Foundation 9.0.x. The scope of the deploy, converge, and upgrade guidance is management domain only as this is the minimum required logical block to form a VCF Instance.

## Deploying a new VCF Instance with version 9.0.x

To install a new VCF fleet or VCF Instance without converging or upgrading any existing components, see [Deploying a New VMware Cloud Foundation or VMware vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-.html).

For visual guides to the sequence of installation operations, see the following journey maps.

- [Build Journey - Install a New vSphere Foundation Deployment](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vvf-deploy-journey.pdf)
- [Build Journey - Install a New VMware Cloud Foundation Deployment](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vcf-deploy-journey.pdf)

Starting with VCF 9.0 and later, the deployment process changes and you now install most of the components by using VCF Installer and VCF Operations workflows. Deployment of standalone components by deploying an OVA is typically not supported, apart from specific scenarios where you are explicitly instructed to do so.

- For information about the scope of components for installation by VCF Installer, see [What is the VMware Cloud Foundation Installer?](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/what-is-the-vcf-installer-.html).
- For information about the scope of components for installation after the VCF Installer workflow, see [Completing the Deployment of Your Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform.html).

## Paths to building workload domains with version 9.0.x

After you create your management domain, you can proceed with the analogous, workload domain-specific guidance.

- To create a workload domain, see [Create a New Workload Domain Using VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/deploy-a-vi-workload-domain-using-the-sddc-manager-ui.html).
- To import existing infrastructure as a workload domain in a VCF Instance, see [Import an Existing vCenter to Create a Workload Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/import-an-existing-vcenter-to-create-a-workload-domain.html).
- To upgrade your workload domain components, see [Upgrading VMware Cloud Foundation 5.x Workload Domains to 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2.html).

## Converging your existing components to vSphere Foundation or VCF with version 9.0.x

## Before converging

Before deciding which convergence path to follow, you can independently upgrade your existing pre-version 9.0 standalone components, that are not yet part of a VCF Instance, to version 9.0.x. For example, you can upgrade your vCenter, ESX, and Aria Operations to version 9.0. This component configuration is the minimum requirement to evaluate the capabilities of version 9.0.x, for up to 90 days, before you license the products from VCF Operations.

- [Upgrading vCenter to version 9.0](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered)
- [Upgrading ESX to version 9.0](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-0&language=&format=rendered)
- [Upgrading Aria Operations to version 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore.html)

Starting with VCF and vSphere Foundation 9.0, you manage your licenses through VCF Operations across your entire fleet and can manage licenses for multiple VCF Operations instances from the VCF Business Services console ([vcf.broadcom.com](http://vcf.broadcom.com/)), a part of the Broadcom Support Portal. For more information, see [Licensing Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered).

## Convergence prerequisites

After you chose a convergence path, based on your existing pre-version 9.0.x or independently upgraded version 9.0.x standalone components, you must proceed with creating your management domain by converging the components to a supported vSphere Foundation or VCF deployment model. For either path, first verify that you meet the minimum version requirements and supported configurations. See [Converging Existing Virtual Infrastructure to a VCF or a vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-.html).

## Converging to vSphere Foundation 9.0.x

If you decided to converge your standalone components to vSphere Foundation 9.0.x, you must follow a specific convergence order. See [Converge a vCenter Instance and ESX Hosts to vSphere Foundation Platform](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/use-existing-vsphere-infrastructure-to-create-a-vmware-vsphere-foundation-environment-using-the-deployment-wizard.html).

For a visual guide to the sequence of convergence operations, see the [Build Journey - Converge Existing vSphere to vSphere Foundation 9 with a New VCF Operations Instance](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vvf-converge-from-vsphere-journey.pdf) journey map.

## Converging to VCF 9.0.x

If you decided to converge your virtual infrastructure to a VCF fleet or VCF Instance, again, you must follow a specific convergence order for VCF product components. Depending on your existing components, proceed with one of the converging scenarios. See [Supported Scenarios to Converge to VCF](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/converging-your-existing-vsphere-infrastructure-to-a-vcf-or-vvf-platform-/supported-scenarios-to-converge-to-vcf.html).

For a visual guide to the sequence of convergence operations, see the [Build Journey - Converge Your Infrastructure to VMware Cloud Foundation from Existing vSphere and VMware Aria Operations](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-vcf-converge-from-vsphere-aria-operations-journey.pdf) journey map.

The table bellow lists all VCF components and each table row includes a link to a dedicated upgrade procedure. You must upgrade the management planes first, followed by core SDDC components in a distinct upgrade order.

| # | VCF Component | Converging existing standalone components to VCF 9.0.x |
| --- | --- | --- |
| 1 | Aria Suite Lifecycle | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/apply-a-patch-to-vmware-aria-suite-lifecycle.html)\* |
| 2 | Aria Operations / VCF Operations | Yes, [automated](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/upgrade-to-vcf-operations.html) or [manual](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore.html) |
| 3 | Aria Automation / VCF Automation | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html) |
| 4 | Aria Automation Orchestrator / VCF Operations orchestrator | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-a-standalone-or-clustered-vrealize-orchestrator-8-0-1-deployment-with-iso-image.html) |
| 5 | Aria Operations for Networks / VCF Operations for networks | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-4-upgrade-additional-management-components-in-vcf-9.html) |
| 6 | Aria Operations for Logs / VCF Operations for logs | [No](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-logs.html)\*\* |
| 7 | SDDC Manager | N/A |
| 8 | HCX / VCF Operations HCX | [Yes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/workload-mobility/vmware-hcx-user-guide-vcf-9-0/updating-vmware-hcx.html) |
| 9 | NSX | - VCF 9.0.0 - No - VCF 9.0.1 - Yes\*\*\* |
| 10 | vCenter | [Yes](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_006&appid=vsphere-9-0&language=&format=rendered) |
| 11 | ESX | [Yes](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-0&language=&format=rendered) |
| 12 | vSAN | [Yes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/upgrading-the-vsan-cluster.html) |

\* VMware Aria Suite Lifecycle has no upgrade path to version 9. A VCF Operations fleet management appliance 9 is deployed and the existing connection with VMware Аria Operations 8.x is imported to the new appliance.

\*\* No upgrade path for VMware Aria Operations for Logs. Redeploy of VCF Operations for logs 9.0 is required.

\*\*\* Starting with VCF 9.0.1, NSX 4.1.0.2 or later deployments that are registered with vCenter appliances that do not use Enchanced Linked Mode, are upgraded to version 9.0.1 as a part of the VCF Installer workflows.

## Upgrading a VCF Instance with version 5.x to version 9.0.x

If you have an existing VCF 5.x environment, see [Upgrading Your VCF Management Domain to VMware Cloud Foundation 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation.html).

For a visual guide to the sequence of upgrade operations, see the [Holistic Journey - Fully Adopt VMware Cloud Foundation from Existing vSphere and VMware Aria Operations](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/assets/vmware-cis/vcf/vcf-9.0-holistic-from-vsphere-aria-operations-end-to-end-journey.pdf) journey map.

The table bellow lists all VCF components and each table row includes a link to a dedicated upgrade procedure. You must upgrade the management planes first, followed by core SDDC components in a distinct upgrade order.

| # | VCF Component | Upgrading to version 9.0.x |
| --- | --- | --- |
| 1 | Aria Suite Lifecycle | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/apply-a-patch-to-vmware-aria-suite-lifecycle.html)\* |
| 2 | Aria Operations / VCF Operations | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrading-management-components/upgrade-to-vcf-operations.html) |
| 3 | Aria Automation / VCF Automation | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-3-import-and-upgrade-aria-automation-8-to-vcf-automation-9.html) |
| 4 | Aria Automation Orchestrator / VCF Operations orchestrator | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-a-standalone-or-clustered-vrealize-orchestrator-8-0-1-deployment-with-iso-image.html) |
| 5 | Aria Operations for Networks / VCF Operations for networks | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/phase-4-upgrade-additional-management-components-in-vcf-9.html) |
| 6 | Aria Operations for Logs / VCF Operations for logs | [No](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-logs.html)\*\* |
| 7 | SDDC Manager | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/apply-cloud-foundation-5-2-update-bundle.html) |
| 8 | HCX / VCF Operations HCX | [Yes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/workload-mobility/vmware-hcx-user-guide-vcf-9-0/updating-vmware-hcx.html) |
| 9 | NSX | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9.html)\*\*\* |
| 10 | vCenter | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vcenter-server-for-vmware-cloud-foundation-5-2.html) |
| 11 | ESX | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-esxi-for-vmware-cloud-foundation-5-2-1.html) |
| 12 | vSAN | [Yes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrade-vsan-on-disk-format-versions.html) |

\* VMware Aria Suite Lifecycle has no upgrade path to version 9. A VCF Operations fleet management appliance 9 is deployed and the existing connection with VMware Аria Operations 8.x is imported to the new appliance.

\*\* No upgrade path for VMware Aria Operations for Logs. Redeploy of VCF Operations for logs 9.0.x is required.

\*\*\* NSX 4.x deployments that are not part of VCF instances can be upgraded to version 9.0.x after they are first imported to existing VCF instances as workload domains. See [Import an Existing vCenter to Create a Workload Domain](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/import-an-existing-vcenter-to-create-a-workload-domain.html) and [Upgrading VMware Cloud Foundation 5.x Workload Domains to 9.0](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/upgrade-workload-domains-to-vcf-5-2.html). Starting with VCF 9.0.1, NSX 4.1.0.2 or later deployments that are not part of VCF instances and are registered with vCenter appliances that do not use Enchanced Linked Mode, can be upgraded to version 9.0.1 as a part of a management domain by using the VCF Installer convergence workflow.