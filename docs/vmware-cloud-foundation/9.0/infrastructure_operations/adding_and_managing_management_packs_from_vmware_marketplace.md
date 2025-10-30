---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/adding-and-managing-content-from-vmware-marketplace.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Adding and Managing Management Packs from VMware Marketplace
---

# Adding and Managing Management Packs from VMware Marketplace

You can add and manage VCF Operations management packs from VMware Marketplace in the Marketplace page.

From the left menu click AdministrationIntegrationsMarketplace. By default, the latest versions of the available management packs from VMware Marketplace are displayed. Use the version selector to view or select a different version the the management pack.

Use the Search option to filter the list of available management packs by name.

To create a management pack that is not published on VMware Marketplace, click Create Management Pack. After you create a management pack, you can install it in VCF Operations. For more information, see [Management Pack Builder](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/extending-monitoring-capabilities/cloud-foundation-operations-configuration-guide-management-pack-builder.html).

## Download, Install, and Uninstall Management Packs from VMware Marketplace

If your VCF Operations instance is online and can successfully sync with VMware Marketplace, you can download any available management pack. By default, the latest published version of the management pack is displayed, use the version selector to view the available versions or to select the version you want to download. To download a management pack in VCF Operations, click Download, accept the EULA Agreement, and then click Download again.

If your VCF Operations instance is offline and unable to connect to VMware Marketplace, no management pack is displayed in the Marketplace page. If no management pack is available, open the [VMware Marketplace](https://vcf.broadcom.com/vsc/) web page and download the management pack manually for VCF Operations. For more information, see [VMware Marketplace Overview](https://techdocs.broadcom.com/us/en/vmware-cis/other/vmware-marketplace/index/vmware-marketplace-overview.html).

Once you have successfully downloaded the management pack zip file, click Upload and Install. To upload the management pack, browse and select the management pack PAK file and enter the Password. The password is the asset key that is used when downloading the management pack PAK file from VMware Marketplace.

All downloaded management packs appears on the Downloaded section of the Marketplace page. After you download a management pack, you have to install it. To install a management pack, locate the management pack you want to install and click Install. Verify the Component Confirmation and click Install. Content will be installed.

After you download and install a management pack, you must add accounts for each management pack from the AdministrationIntegrationsRepository page. For more details, see [The Repository Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-repository-tab.html).

To uninstall a management pack, click Uninstall, confirm that you want to uninstall the management pack, and then click Uninstall again. If you uninstall a management pack, it automatically deletes the associated accounts.

You can view the status of the action you initiate on a management pack in the Fleet ManagementLifecycleTasks page. When you download, install, or uninstall a management pack, click Request Status to view its progress.

## View and Upgrade your Marketplace content

You can view information about the available management packs and the management packs that you have previously downloaded from VMware Marketplace in VCF Operations. To view all the available management packs from  , click AdministrationIntegrationsMarketplace. To view all the downloaded management packs from  , click Downloaded.

On the Downloaded page, click View Details for any management pack to learn more about a the management pack, including the content compatibility. You can view the management pack Overview and then click on Tasks to see the actions that were performed on that management pack.

To sync the management pack inventories on demand, click Sync Installed Content. By default, the management pack inventory in the VCF Operations Repository page is synced with the Marketplace page every 12 hours.

To check for upgrades of any previously downloaded management packs, click Check for Updates. If there is an update available, the Upgrade button becomes active and you can download a newer version of the content. If you are upgrading a VCF Operations management pack with a newer version, the new version content overwrites the old version content.