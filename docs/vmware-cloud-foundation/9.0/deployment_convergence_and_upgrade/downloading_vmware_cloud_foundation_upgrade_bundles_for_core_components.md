---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Downloading VMware Cloud Foundation Upgrade Bundles for Core Components
---

# Downloading VMware Cloud Foundation Upgrade Bundles for Core Components

Before you can upgrade to VMware Cloud Foundation 9.0, you must download the upgrade bundles for each VMware Cloud Foundation core component that requires an upgrade.

Downloading upgrade bundles requires an internet connection. The method you use to download bundles depends on how you access the internet in your environment.

- Online depot: SDDC Manager can connect to the internet, either directly or through a proxy.
- Offline depot: SDDC Manager cannot connect to the internet, but can connect to a computer with internet access.
- No depot: SDDC Manager cannot connect to the internet or to a computer with internet access.

## Online Depot

When you connect to an online depot, you can download upgrade bundles directly to SDDC Manager.

Downloading upgrade bundles using an online depot happens in two stages. Initially, only the SDDC Manager upgrade bundle is available. After you upgrade SDDC Manager to 9.0, you can download the remaining 9.0 upgrade bundles.

See [Connect SDDC Manager to a Depot for Accessing Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html).

## Offline Depot

When you connect to an offline depot, you must use the VCF Download Tool to download upgrade bundles to the computer that is hosting the offline depot. Once the bundles are downloaded to the offline depot, SDDC Manager can use them for upgrades.

See [Connect SDDC Manager to a Depot for Accessing Bundles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles.html) and [Download VMware Cloud Foundation 9.0 Upgrade Bundles to an Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-to-an-offline-depot.html).

## No Depot

If SDDC Manager cannot connect to an online or offline depot, you must install the VCF Download Tool on a computer with internet access, download the upgrade bundles, and upload the bundles to SDDC Manager.

See [Download VMware Cloud Foundation 9.0 Upgrade Bundles Without an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/offline-download-of-vmware-cloud-foundation-5-2-upgrade-bundles.html).