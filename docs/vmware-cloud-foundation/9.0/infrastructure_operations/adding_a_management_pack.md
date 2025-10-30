---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/the-repository-tab/add-solutions-wizard.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Adding a Management Pack
---

# Adding a Management Pack

Management packs are delivered as PAK files that you upload, license, and install.

## How Management Packs Work

When you add a management pack, you configure adapters that manage the communication and integration between VCF Operations and other products, applications, and functionality.

## Where You Add Solutions

From the left menu, click AdministrationIntegrationsRepository and then click Add to install other management packs. Click the vertical ellipsis of a management pack, and then click Upgrade to upgrade the management pack to the latest version.

## Add Solutions Wizard Options

The wizard includes three pages where you locate and upload a PAK file, accept the EULA and install, and review the installation.

Before you install the PAK file, or upgrade your VCF Operations instance, clone any customized content to preserve it. Customized content can include alert definitions, symptom definitions, recommendations, and views. While upgrading to the latest version, you can select the Install the PAK file even if it is already installed and the Reset Default Content options.

Wizard Options



| Option | Description |
| --- | --- |
| Page 1 | |
| Select a Management pack to install | Navigate to your copy of a management pack PAK file. |
| Download Management Pack | When you click Get in the Repository page, the management pack is automatically downloaded. You can view the Name, Description, and Version of the management pack that is installed. |
| Upload | To prepare for installation, copy the PAK file to VCF Operations. |
| Install the PAK file even if it is already installed | If the PAK file was already uploaded, reload the PAK file using the current file, but leave user customization in place. Do not overwrite or update the solution alerts, symptoms, recommendations, and policies. |
| Reset Default Content | If the PAK file was already uploaded, reload the PAK file using the current file, and overwrite the solution default alerts, symptoms, recommendations, and policies with newer versions provided with the current PAK file. A reset overwrites customized content. If you are upgrading VCF Operations, the best practice is to clone your customized content before you upgrade. |
| The PAK file is unsigned | A warning appears if the PAK file is not signed with a digital signature that VMware provides. The digital signature indicates the original developer or publisher and provides the authenticity of the management pack. If installing a PAK file from an untrusted source is a concern, check with the management pack distributor before proceeding with the installation. |
| Page 2 | |
| I accept the terms of the agreement | Read and agree to the end-user license agreement. Click Next to install the management pack. The installation starts only if all the VCF Operations cluster's nodes are accessible. |
| Page 3 | |
| Installation Details | Review the installation progress, including the VCF Operations nodes where the adapter was installed. |