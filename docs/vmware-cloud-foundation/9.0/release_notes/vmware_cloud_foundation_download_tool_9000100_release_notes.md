---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vmware-download-tool/vcf-dt-9-0-0-0100.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > VMware Cloud Foundation Download Tool 9.0.0.0100 Release Notes
---

# VMware Cloud Foundation Download Tool 9.0.0.0100 Release Notes

This document contains the following sections

- [Introduction](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vmware-download-tool/vcf-dt-9-0-0-0100.html#GUID-74864433-dfd2-4a15-a926-5e62686b6d9f-en_id-4b6c995a-f4ba-4295-9256-c30fb8511286)
- [What's New](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vmware-download-tool/vcf-dt-9-0-0-0100.html#GUID-74864433-dfd2-4a15-a926-5e62686b6d9f-en_id-4e4ce444-1579-40ef-864a-22f3391d4ba2)
- [Resolved Issues](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vmware-download-tool/vcf-dt-9-0-0-0100.html#GUID-74864433-dfd2-4a15-a926-5e62686b6d9f-en_id-41ed7a06-b735-4f4f-87b7-8f3262c169af)
- [Known Issues](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vmware-download-tool/vcf-dt-9-0-0-0100.html#GUID-74864433-dfd2-4a15-a926-5e62686b6d9f-en_id-c8d89c85-81ce-43f5-a72d-52871fd0f000)

## Introduction

|  |
| --- |
| VMware Cloud Foundation Download Tool 9.0.0.0100 | 04 AUG 2025 | Build 24887569  Check for additions and updates to these release notes.  This version is replaced by VMware Cloud Foundation Download Tool 9.0.1.0000 Build 24887569 and is no longer available for download. |

## What's New

- VMware Cloud Foundation Download Tool replaces the Bundle Transfer Utility.

  - The VCF Download Tool package includes both the lcm-bundle-transfer-util and the vcf-download-tool tools.

## Download

1. Log in to the [Broadcom Support Portal](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Cloud%20Foundation&displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN), select the My Downloads tab and locate VMware Cloud Foundation.
2. Select the Drivers & Tools tab and download VCF Download Tool**.**

## Installation

1. Download the tool from the Broadcom Support Portal.
2. Extract the contents of the tar.gz file.
3. Install UMDS by running the vcf-download-tool umds install command.

## Upgrade

To upgrade the VMware Cloud Foundation Download Tool, you must manually uninstall the current UMDS version, extract the tar.gz file and install the latest version of UMDS.

1. To uninstall UMDS, run the the vcf-download-tool umds uninstall command.
2. Download the tool from the Broadcom Support Portal.
3. Extract the contents of the tar.gz file.

   Before installing the VMware Cloud Foundation Download Tool, clear the existing patch store.
4. To install UMDS, run the vcf-download-tool umds install command.

## Resolved Issues

**When starting the Bundle Transfer Utility and the VCF Download Tool on a Windows operating system without Java installed, the tools quits unexpectedly**

Both tools (lcm-bundle-transfer-util and vcf-download-tool) are prepacked with Java 17. The tool launcher searches for an existing Java trust store in the Windows operating system and attempts to dump the trusted certificates installed in the store and then import the certificates in Java trust stores, that are the embedded in the tools. Since Java is not installed on the operating system and the trust store is missing, as a result, the launcher exits silently. This issue is fixed in this release. Download the latest version of the VMware Cloud Foundation Download Tool from the Broadcom Support portal.

**When downloading multiple patch bundles for SDDC Manager with the Bundle Transfer Utility, the tool cannot download all of the patches**

When multiple bundles are available for SDDC Manager, for example Express patches, the Bundle Transfer Utility downloads only two of the patches on a random basis. This issue is fixed in this release. Download the latest version of the VMware Cloud Foundation Download Tool from the Broadcom Support portal and re-try downloading the patch bundles.

**When using the VMware Cloud Foundation Download Tool on a Windows operating system, the tool fails**

An OS dependent file separator is used in both URL assembling and file path, which results in the tool failing downloads with the following error message: Binaries 1 out of 1 failed to download. This issue is fixed in this release. Download the latest version of the VMware Cloud Foundation Download Tool from the Broadcom Support portal.

**When using the VMware Cloud Foundation Download Tool with а proxy to connect to the Internet, the tool fails to execute any operation**

In the VCF Download Tool, when using the command line options to enter the details of the proxy server, the command line pre-validates the proxy settings and the validation fails with the following error message: Unable to connect. This issue is fixed in this release. Download the latest version of the VMware Cloud Foundation Download Tool from the Broadcom Support portal and re-try the operation.

## Known Issues

For the full list of known issues in VMware Cloud Foundation 9.0, see [VMware Cloud Foundation 9.0 Known Issues](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/component-specific.html).

**When trying to connect to an online depot, the Bundle Transfer Utility fails**

During the initial connection to an online depot for credential validation, the Bundle Transfer Utility fails with the following error message: Username or password is invalid for user.

Workaround: Inspect the Bundle Transfer Utility logs for warning or error messages related to the failure. The failure might occur due to incorrect username or password, misconfigured or unreachable proxy server, missing proxy credentials (username/password), or any other connection-related issues.

**While downloading, the Bundle Transfer Utility fails**

When running the lcm-bundle-transfer-util command with the --sddcMgrVersion option and empty --outputDirectory folder, the command fails with the following error message: Unable to fetch index file from the depot, this is needed to fetch the bundles information {}.

Workaround: Create a tmp folder inside the specified --outputDirectory folder and re-run the lcm-bundle-transfer-util command.

**UMDS download fails**

When adding an invalid or empty entitlement token using the umds run -S --add-entitlement-token or ./vmware-umds -S --add-entitlement-token <token\_id> commands, UMDS accepts the token without validation. Later, during the download phase, the download from default URLs fails with an error message. For example:

```
2025-07-22T10:15:21.111-07:00 warning vmware-downloadService[3605451] [Originator@6876 sub=httpDownload][httpDownloadPosix 923] Download https://dl.broadcom.com/abcd/PROD/COMP/ESX_HOST/main/vmw-depot-index.xml failed, retry in 15 seconds.
```

Workaround: To overwrite the previously stored invalid token without manual configuration changes, re-run the commands with a valid entitlement token.