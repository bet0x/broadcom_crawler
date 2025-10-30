---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > VCF SDKs, APIs, and CLIs
---

# VCF SDKs, APIs, and CLIs

This document contains the following sections

- [VCF APIs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html#GUID-c00a841e-a379-4f6b-a642-b0e9dc1af083-en_id-61382d0a-9abb-497d-91f7-7fe921246a8e)
- [VMware Cloud Foundation Java SDK](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html#GUID-c00a841e-a379-4f6b-a642-b0e9dc1af083-en_id-bab608f6-6f06-42d8-8a4c-6340dd12f4fe)
- [VMware Cloud Foundation Python SDK](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html#GUID-c00a841e-a379-4f6b-a642-b0e9dc1af083-en_id-62916cb5-6e67-4301-b8e3-7f92676d60fd)
- [VMware Cloud Foundation PowerCLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html#GUID-c00a841e-a379-4f6b-a642-b0e9dc1af083-en_id-beb86683-5848-4b6b-97fd-aab950d3098d)
- [VCF Consumption CLI](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html#GUID-c00a841e-a379-4f6b-a642-b0e9dc1af083-en_id-a13be24a-8d13-45a7-a73a-0651b6113e06)

## VCF APIs

**OpenAPI 3.0**

vCenter 9.0 adds OpenAPI 3.0 to support all vCenter and vSAN APIs, along with the existing VI JSON and vCenter REST APIs, aligning vCenter APIs with the industry standard for API specifications.

**Support for vCenter authorization management by REST APIs**

vCenter 9.0 adds the com.vmware.vcenter.authorization package that enables you to use modern REST APIs to configure all aspects of authorization in a vCenter system, including privileges, roles, global and inventory permissions, and facilitates the development of better automation solutions. For more information, see the [documentation](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=api-sdk_1&appid=vcf-9-0&language=&format=rendered) on management APIs for authorization.

**API to check customization options of virtual machines**

vCenter 9.0 adds new API that enables you to check if you can customize a virtual machine before customizing it.

**vSphere Automation APIs to customize the guest OS while running**

With vCenter 9.0, you can call Guest OS customization vAPIs for all GOSC operations and supported scenarios.

## VMware Cloud Foundation Java SDK

**Introduction**

|  |
| --- |
| VMware Cloud Foundation Java SDK 9.0 | 17 JUNE 2025 | Build 24798170  Check for additions and updates to these release notes. |

VMware Cloud Foundation (VCF) Java SDK is your gateway to seamless cloud infrastructure management and automation. It consists of API client bindings, sample code, utility code, and documentation for the VCF components.

The SDK consists of the following VMware Cloud Foundation components:

| **Component** | **Description** |
| --- | --- |
| **VMware vCenter** | The vCenter module of the VCF SDK exposes operations related to content libraries and resource deployment, tagging, and managing internal and external security certificates. |
| **Virtual Infrastructure Management (VIM)** | The Virtual Infrastructure Management (VIM) module of the VCF SDK exposes operations related to the management of compute, networking, and storage resources. These resources include virtual machines, ESX hosts, clusters, datastores, networks, and system abstractions such as events, alarms, authorization, and plug-in extensions. |
| **SSOCLIENT** | The Single Sign-On module of the VCF SDK interfaces the Security Token Service (STS) to issue SAML tokens for authentication of vCenter API operations. |
| **VMware vSAN Data Protection (vSAN DP)** | Using native snapshots stored locally on the vSAN cluster, vSAN data protection can quickly recover VMs from operational failure or ransom-ware attacks. The vSAN Data Protection API manages protection groups and discovers VM snapshots. |
| **Virtual Storage Lifecycle Management (VSLM)** | The Virtual Storage Lifecycle Management (VSLM) module of the VCF SDK exposes operations related to First Class Disks (FCD), i.e, virtual disks not associated with a virtual machine. |
| **Storage Monitoring Service (SMS)** | The Storage Monitoring Service (SMS) module of the VCF SDK provides methods to retrieve information about available storage topology, capabilities, and state. The vSphere API for Storage Awareness (VASA) permits storage arrays to integrate with vCenter for management functionality. VASA providers expose features of the physical storage devices, such as storage health status, configuration info, and storage capacity. SMS establishes and maintains connections with VASA providers. SMS retrieves information about storage availability from the providers. |
| **Storage Policy Based Management (SPBM)** | The Storage Policy Based Management (SPBM) module of the VCF SDK exposes operations related to storage policies. They describe storage requirements for virtual machines and storage capabilities of storage providers. |
| **ESX Agent Manager (EAM)** | The ESX Agent Manager (EAM) in VMware vSphere allows developers to extend the functionality of vSphere environments by registering custom software applications as vCenter Server extensions. EAM acts as an intermediary between vCenter and these solutions, managing the provisioning and monitoring of agent virtual machines and vSphere Installation Bundle (VIB) modules |
| **SDDC Manager** | The SDDC Manager module of the VCF SDK exposes operations to manage and monitor the physical and virtual infrastructure deployed as part of a VMware Cloud Foundation deployment. |
| **VMware Cloud Foundation (VCF) Installer** | The VCF Installer module of the VCF SDK exposes operations to validate, deploy, convert, and monitor VCF and VVF installations using new or existing components. |

**Overview**

**Distribution Channels**

**Developer Portal**

The VCF SDK Java is available on the  [Developer Brioadcom Portal](https://developer.broadcom.com/sdks/vcf-java-sdk/latest/) for download.  You could extract the contents of the ZIP archive *vcf-java-sdk-9.0.0.0-24781669.zip* to explore the SDK libraries, utilities and samples. The SDK bindings *.jar*, utility *.jar* and the SDK BOM files are available in the  *../maven/com/vmware/\** folder.

**Maven Central**

The VCF SDK artifacts are available in Maven Central under the groupId: **com.vmware.sdk**. The table below captures the VCF SDK  artifact details for the 9.0.0.0.

| **VCF SDK artifact ID** | **Version** |
| --- | --- |
| wsdl-utils | 9.0.0.0 |
| vsphere-utils | 9.0.0.0 |
| vslm | 9.0.0.0 |
| vSAN-data-protection | 9.0.0.0 |
| vmware-sdk-common | 9.0.0.0 |
| vim25 | 9.0.0.0 |
| vcf-installer-utils | 9.0.0.0 |
| vcf-installer | 9.0.0.0 |
| vcenter | 9.0.0.0 |
| vapi-samltoken | 2.61.2 |
| vapi-runtime | 2.61.2 |
| vapi-authentication | 2.61.2 |
| sso-client-utils | 9.0.0.0 |
| sso-client | 9.0.0.0 |
| sms | 9.0.0.0 |
| sddc-manager | 9.0.0.0 |
| pbm | 9.0.0.0 |
| eam | 9.0.0.0 |

**Github**

The VCF SDK can also be obtained from the [VMware GitHub repository](https://github.com/vmware/vcf-sdk-java/).

**What's New**

The VCF SDK 9.0.0.0 release have new component SDKs i. SDDC Manager and ii. VCF Installer. The vSphere  Management (Web Services) SDK and vSphere Automation SDK Java is unified as a single deliverable in the VCF SDK 9.0.0.0 release. In accordance, the existing vSphere SDK samples and utilities are reorganized. The detailed migration guide for the vSphere SDK users migrating from existing application is available in the vSphere SDK developer portal deliverables and in [Github](https://github.com/vmware/vcf-sdk-java/).

The vSAN Management SDK for Java is integrated with VCF SDK.

For the new APIs introduced in the component SDKs, please refer  the VCF 9.0.0.0 changelog. The VCF component SDK bindings are available for the newly introduced APIs.

All the existing and new VCF artifacts are published in Maven Central.

## VMware Cloud Foundation Python SDK

**Introduction**

|  |
| --- |
| VMware Cloud Foundation Python SDK 9.0 | 17 JUNE 2025 | Build 24798170  Check for additions and updates to these release notes. |

VCF Python SDK is your gateway to seamless cloud infrastructure management and automation. It consists of API Client Bindings (wheel files available in PyPI), sample code, utility code, and documentation. Several existing  SDKs and new SDKs are part of VCF SDK 9.0.

The details of the component SDKs are as below:

| Component | Description |
| --- | --- |
| **pyVmomi** | pyVmomi is the Python SDK for the VMware vSphere Management API that allows you to rapidly build solutions integrated with VMware ESX, vCenter and VSAN. |
| **vCenter** | VMware vCenter library contains client bindings for VMware vCenter Server Automation APIs. |
| **VMware vSAN Data Protection** | Using native snapshots stored locally on the vSAN cluster, vSAN data protection can quickly recover VMs from operational failure or ransomware attacks. vSAN Data Protection API manages protection groups and discovers VM snapshots. |
| **Software-Defined Data Center (SDDC) Manager** | The VMware SDDC Manager library contains client bindings for VMware SDDC Manager Automation APIs for managing software-defined data center (SDDC) infrastructure components. |
| **VMware Cloud Foundation (VCF) Installer** | The VCF Installer module of the VCF SDK exposes operations to validate, deploy, convert, and monitor VCF and VVF installations using new or existing components. |

**Overview**

**Distribution Channels**

The VCF Python SDK is available in the following locations:

**Developer Portal**

The VCF SDK Python is available on [Developer Broadcom Portal](https://developer.broadcom.com/sdks/vcf-python-sdk/latest/) for download. You could extract the contents of the ZIP archive *vcf-python-sdk-9.0.0.0-24781669.zip* to explore the SDK libraries, utilities and samples. However, the third-party dependency packages are not bundled, they are listed in *requirements-third-party.txt*, present in the VCF Python SDK in [Developer Broadcom Portal](https://developer.broadcom.com/sdks/vcf-python-sdk/latest/). The *.whl* files for the VCF SDK components are present in the *../pypi/\** folders and the code samples for the VCF components are available in the */<component\_name>-samples/* directory.

**PyPI**

This is the recommended way to install the SDK. The installation gets the SDK libraries and dependencies from [PyPI](https://pypi.org/project/vcf-sdk/9.0.0.0/).

Following modules are published in  PyPI for VCF SDK 9.0.0.0.

| **PyPi Module Name** | **Version** |
| --- | --- |
| *vmware-vsan-data-protection* | 9.0.0.0 |
| *vmware-vcenter* | 9.0.0.0 |
| *vmware-vapi-runtime* | 2.61.2 |
| *vmware-vapi-common-client* | 2.61.2 |
| *vmware-sddc-manager* | 9.0.0.0 |
| *vcf-sdk* | 9.0.0.0 |
| *vcf-installer* | 9.0.0.0 |
| *pyvmomi* | 9.0.0.0 |

**Github**

The VCF SDK can also be obtained from the [VMware GitHub repository](https://github.com/vmware/vcf-sdk-python/).

**What's New**

The VCF SDK 9.0.0.0 release have new component SDKs : SDDC Manager and VCF Installer.

For the new APIs introduced in the VCF component SDKs, please refer the [VCF 9.0.0.0 API changelog](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk/vcf-changelog.html). The VCF component SDK bindings are available for the newly introduced APIs.

## VMware Cloud Foundation PowerCLI

**Introduction**

|  |
| --- |
| VMware Cloud Foundation PowerCLI 9.0 | 17 JUNE 2025  VCF PowerCLI 9.0 Build 24798382  Check for additions and updates to these release notes. |

**Improved Cmdlet Loading Performance in VCF PowerCLI**

The loading time of VCF PowerCLI cmdlets is improved. For users on PowerShell 5.1, loading is over 50% faster. For users on PowerShell 7.x, loading is improved by up to 70%.

**Recommendation**

In VCF 9.0 PowerCLI gets a name refresh - the main module is now called VCF.PowerCLI. We recommend that you use this new module in your scripts from now on. You can still continue to import VMware.PowerCLI after installing VCF.PowerCLI 9.0 if necessary.

**Upgrading from VMware.PowerCLI to VCF.PowerCLI 9.0**

Upgrading from an existing installation of VMware.PowerCLI is discouraged and we recommend a clean installation.

If you already have VMware.PowerCLI 13.3 or earlier installed on your system you may encounter the following error when attempting to install VCF.PowerCLI 9.0.

```
PackageManagement\Install-Package : The following commands are already available on this system:'
 
...
 
Initialize-X509Certificate,Initialize-X509Crl,Initialize-X509CrlEntry'. This module 'VMware.Sdk.Nsx.Policy.Initialize' may override the existing commands. If you still want to install this module 'VMware.Sdk.
Nsx.Policy.Initialize', use -AllowClobber parameter.
At C:\Program Files\WindowsPowerShell\Modules\PowerShellGet\1.0.0.1\PSModule.psm1:1809 char:21
+ ...          $null = PackageManagement\Install-Package @PSBoundParameters
+                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (Microsoft.Power....InstallPackage:InstallPackage) [Install-Package], Exception
    + FullyQualifiedErrorId : CommandAlreadyAvailable,Validate-ModuleCommandAlreadyAvailable,Microsoft.PowerShell.PackageManagement.Cmdlets.InstallPackage
```

This happens because some of the cmdlets which are part of the PowerCLI SDK have been moved to other modules. To resolve the conflict you need to add the AllowClobber parameter to Install-Module.

You may also encounter certificate errors for some modules when upgrading. This can be caused by the fact that PowerCLI is now signed with a Broadcom certificate and not a VMware one. You can work around this problem by providing the SkipPublisherCheck parameter.

**VCF.PowerCLI Installation Guide**

VCF.PowerCLI is a continuation of VMware.PowerCLI as part of our ongoing commitment to align more closely with VMware Cloud Foundation (VCF) and to better reflect the focus of our automation tooling, VMware PowerCLI has been renamed to VCF PowerCLI. This change reinforces our direction to deliver a more tailored and streamlined automation experience specifically for VCF environments. While the name has changed, the functionality and powerful capabilities you rely on remain intact. All existing cmdlets, modules, and automation scripts continue to work as expected.

**Installation**

- **Step 1 - Uninstall VMware.PowerCLI**

  We recommend a clean installation. To minimize the risk of disruption we also recommend that you update any imports of VMware.PowerCLI in existing scripts to VCF.PowerCLI. Follow the official guide for uninstalling VMware.PowerCLI from your system at [Uninstall VCF PowerCLI](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/administration-sdks-cli-and-tools/introduction-to-vmware-vsphere-powercli/installing-vmware-vsphere-powercli/uninstall-powercli.html).
- **Step 2 - Install VCF.PowerCLI**

  Follow the official guide for installing VCF.PowerCLI - [PowerCLI Installation Guide](https://developer.broadcom.com/powercli/installation-guide). Make sure that you are installing VCF.PowerCLI and not VMware.PowerCLI

**Importing VMware.PowerCLI in PowerShell 5.1**

If you have upgraded VMware.PowerCLI  to the latest version available alongside VCF.PowerCLI  you will no longer be able to import the old module in PowerShell  5.1. The only workaround to this problem is to upgrade to PowerShell 6 or later.

```
Import-Module : The required module 'VMware.Vim' is not loaded. The module 'VMware.Vim' has a requiredModule 'VMware.VimAutomation.Common' in its module manifest 'C:\Users\stoyo\OneDrive\Documents\WindowsPowe
rShell\Modules\VMware.Vim\9.0.0.24771640\VMware.Vim.psd1' that points to a cyclic dependency.
At line:1 char:1
+ Import-Module VMware.PowerCLI
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (C:\Users\stoyo\...e.PowerCLI.psd1:String) [Import-Module], MissingMemberException
    + FullyQualifiedErrorId : Modules_InvalidManifest,Microsoft.PowerShell.Commands.ImportModuleCommand
```

**Overview**

**VMware PowerCLI is now VCF PowerCLI**

As part of our ongoing commitment to align more closely with VMware Cloud Foundation (VCF) and to better reflect the focus of our automation tooling, **VMware PowerCLI has been renamed to VCF PowerCLI**. This change reinforces our direction to deliver a more tailored and streamlined automation experience specifically for VCF environments.While the name has changed, the functionality and powerful capabilities you rely on remain intact. All existing cmdlets, modules, and automation scripts continue to work as expected.

To explore the full list of updates in VCF PowerCLI, please see the detailed [VCF PowerCLI 9.0 changelog](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=api-sdk_6&appid=vcf-9-0&language=&format=rendered).

**Installation, Upgrade, and Removal of VCF PowerCLI**

Management of the VCF PowerCLI modules is provided by the PowerShell Gallery and by using the PowerShell default cmdlets for working with modules in the PowerShell Gallery. For detailed information on how to install, upgrade, or remove VCF PowerCLI, refer to the VMware Cloud Foundation PowerCLI User's Guide.

**Supported Platforms**

VMware Cloud Foundation (VCF) PowerCLI is a suite of PowerShell modules to manage VMware products and services. VCF PowerCLI includes over 7000 cmdlets to easily manage your infrastructure on a global scale. For a list of VCF PowerCLI 9.0 supported operating systems and PowerShell versions, see

Compatibility Matrix for VCF PowerCLI. For a list of VMware products with which VCF PowerCLI 9.0 is compatible, see [Broadcom Product Interoperability Matrixes](https://interopmatrix.broadcom.com/Interoperability).

**What's New**

VCF PowerCLI 9.0 introduces the following new features, changes, and improvements:

- VMware.VimAutomation.Storage

  - Supports to show new properties for global deduplication (ESAGlobalDedupRatio, SharedDataByESADedupGB, OverheadByESADedupGB) Space reporting output enhancement for Get-VsanSpaceUsage.
  - Support to create new vSAN iSCSI VIP configuration, and set and get from vSAN cluster configuration.
  - Supports to show the health score of vSAN cluster health.

- VMware.VimAutomation.Core

  - The newly supported types can be specified as a target type with the New-CustomAttributecmdlet. Get-Annotationand and Set-Annotation now support entities of the newly added types.
  - Added the capability to view the supported sector size(s) on a datastore and to select a sector size when creating a Virtual Machine or Virtual HardDisk.
  - Added the capability to list the available global host images on a vCenter and to assign pre-configured global images to hosts and clusters. (new cmdlet-Get-LcmSoftwareSpecification)
  - VMware.PowerCLI.VCenter is preserved for backwards compatibility and all cmdlets are now available with the VMware.VimAutomation.Core module. (new cmdlets -Add-VITrustedCertificate, Get-VIMachineCertificate, Get-VITrustedCertificate, Remove-VITrustedCertificate, New-VIMachineCertificateSigningRequest, Get-VIApplianceService, Set-VIMachineCertificate, Start-VIApplianceService, Restart-VIApplianceService, and Stop-VIApplianceService).
  - Added the capability to create permissions for users and groups with the new New-VIPermission cmdlet.
  - Several cmdlets are modified to allow VPC support-

    - Get-VM - Allows retrieving VMs that have network adapters, attached to specific Virtual Private clouds or VPC projects.
    - New-NetworkAdapter -

      Subnet parameter - Allows creating network adapters connected to specific VPC subnet.

      AutoAssignExternalIp parameter -  Allows specifying that an external IP address from the VPC subnet is allocated automatically and is assigned to the network adapter.
    - Set-NetworkAdapter -

      Subnet parameter - Allows specifying a VPC subnet to which you want to connect the network adapter.

      AutoAssignExternalIp parameter - Allows an external IP address from the VPC subnet to be allocated automatically and assigned to the network adapter.

      UnassignExternalIp parameter - Allows assigned external IP addresses from VPC subnet must be removed from the network adapter.
- VMware.DeployAutomation - Added two new cmdlets (Set-ClusterNetworkBootMode and Reset-ClusterNetworkBootMode) that configure the network boot mode of a vSphere Lifecycle Manager cluster.

  Currently this allows customers to use network booting and provision stateless hosts in a vSphere Lifecycle Manager cluster and to restore the default stateful behaviour, respectively.

  A cluster configured with those cmdlets can contain either stateful-only or stateless-only hosts.
- VMware.VimAutomation.Vpc - Support for Virtual Private Cloud in vCenter.

  - Get-VpcIpBlock- Supports to retrieve Virtual Private Clouds Ip Address Block.
  - Get-VpcProject- Supports to retrieve Virtual Private Clouds Projects.
  - Get-VpcConnectivityProfile- Supports to retrieve Virtual Private Cloud Connectivity Profiles.
  - Get-VpcServiceProfile- Supports to retrieve Virtual Private Cloud Service Profiles.
  - New-Vpc- Supports to create a Virtual Private Cloud.
  - Get-Vpc- Supports to retrieve Virtual Private Clouds.
  - Set-Vpc- Supports to modify the configuration of the Virtual Private Clouds.
  - Remove-Vpc- Supports to remove Virtual Private Clouds.
  - Get-VpcStatistics- Supports to retrieve Virtual Private Clouds statistics.
  - New-VpcDhcpGenericOption- Supports to create Dynamic Host Configuration Protocol generic option.
  - New-VpcDhcpClasslessStaticRoute- Supports to create Dynamic Host Configuration Protocol classless static route option.
  - New-VpcSubnet- Supports to create Virtual Private Cloud (VPC) subnet.
  - Get-VpcSubnet- Supports to retrieve Virtual Private Cloud Subnet.
  - Set-VpcSubnet- Supports to modify the configuration of Virtual Private Cloud (VPC) subnet.
  - Remove-VpcSubnet- Supports to remove Virtual Private Clouds Subnet.
  - Get-VpcSubnetStatus- Supports to retrieve Virtual Private Cloud Subnet status.
  - Get-VpcSubnetStatistics- Supports to retrieve Virtual Private Cloud Subnet statistics.
  - Get-VpcSubnetDhcpServerStatus- Supports to retrieve Virtual Private Clouds Subnet dhcp server status.
  - Get-VpcSubnetDhcpServerStatistics- Supports to retrieve Virtual Private Clouds Subnet dhcp server statistics.
  - New-VpcDhcpStaticBinding- Supports to create the DHCP static binding for Virtual Private Cloud Subnet.
  - Get-VpcDhcpStaticBinding- Supports to retrieve the DHCP static bindings for Virtual Private Cloud Subnet.
  - Set-VpcDhcpStaticBinding- Supports to modify the DHCP static binding configurations for the Virtual Private Cloud Subnet.
  - Remove-VpcDhcpStaticBinding- Supports to remove the DHCP static bindings for VPC Subnet
- VMware.Sdk.vSphere

  - Invoke-EsxSettingsInventoryUpdateVumCapabilityTask- Temporarily unrestrict VUM for heterogeneous clusters.
  - Invoke-EsxSettingsInventoryReportsTransitionSummaryClustersGet- Gets the transition summary of clusters.
  - Invoke-EsxSettingsInventoryExtractInstalledImageTask- Extracts the information about currently installed images on the host.
  - Invoke-EsxSettingsInventoryTransitionTask- Transitions the specified entities from managed with baselines to managed with images.
  - Invoke-EsxSettingsInventoryReportsTransitionSummaryHostsGet- Gets the transition summary of stand alone hosts.
  - Get-vSphereOperation- Get VCF PowerCLI SDK cmdlets filtered by API path or method.
  - Invoke-VcenterAuthorizationPrivilegesGet- Returns the detailed information about a specific authorization privilege in the vCenter instance.
  - Invoke-VcenterAuthorizationPrivilegesList- Queries the authorization privileges in the vCenter instance matching given criteria.
  - Invoke-VcenterAuthorizationRolesCreate- Creates a new authorization role in vCenter.
  - Invoke-VcenterAuthorizationRolesDelete- Deletes an authorization role from the vCenter instance.
  - Invoke-VcenterAuthorizationRolesUpdate- Updates an existing authorization role in the vCenter instance.
  - Invoke-VcenterAuthorizationRolesGet- Returns the detailed information about a specific authorization role in the vCenter instance.
  - Invoke-VcenterAuthorizationRolesList- Queries the authorization roles in the vCenter instance matching given criteria.
  - Invoke-VcenterAuthorizationPermissionsCreate- Creates a new authorization permission in vCenter.
  - Invoke-VcenterAuthorizationPermissionsDelete- Deletes an authorization permission from vCenter.
  - Invoke-VcenterAuthorizationPermissionsUpdate- Updates an existing authorization permission in the vCenter instance.
  - Invoke-VcenterAuthorizationPermissionsGet- Returns the detailed information about a specific authorization permission in the vCenter instance.
  - Invoke-VcenterAuthorizationPermissionsList- Queries the authorization permissions in the vCenter instance matching given criteria.
- VMware.Vcf.SddcManager

  - Get-SddcCluster- Retrieves information about one or more Cluster objects from SDDC Manager Server.
  - Get-SddcDomain- Retrieves information about one or more Domain objects from SDDC Manager Server.
  - Get-SddcHost- Retrieves information about one or more Host objects from SDDC Manager Server.
  - Get-SddcVcenter- Retrieves information about one or more vCenter objects from SDDC Manager Server.

For more information on changes made in VCF PowerCLI 9.0, including improvements, security enhancements, and deprecated features, see the [VCF PowerCLI Change Log](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=api-sdk_6&appid=vcf-9-0&language=&format=rendered). For more information on specific product features, see the [VMware Cloud Foundation PowerCLI User's Guide](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=api-sdk_5&appid=vcf-9-0&language=&format=rendered). For more information on specific cmdlets, see the [VCF PowerCLI Cmdlet Reference](https://developer.broadcom.com/powercli#ReferencesbyProduct). For the full list of VCF PowerCLI documentation, visit the [VCF PowerCLI 9.0 Home Page](https://developer.broadcom.com/powercli).

## VCF Consumption CLI

**Introducing VCF Consumption CLI - Simplify Your VCF Management**

VCF CLI is a powerful command-line interface designed to streamline your interaction with VMware Cloud Foundation (VCF) environments. This first release focuses on simplifying context management, plugin integration, and resource management, making it easier than ever to work with your VCF infrastructure.

**What's New**

**Key Features:**

**Context Management:**

- **CREATE context:** VCF CLI introduces the concept of "context," which stores client authentication information and server details, providing a unified view of your VCF environment.
- **Kubeconfig Mapping:** VCF CLI contexts map directly to Kubectl contexts in your **kubeconfig** file, ensuring consistency between tools.
- **VCFA and vSphere Supervisor Support:** Create contexts for both VCFA (VMware Cloud Foundation Automation) and vSphere Supervisor endpoints.

**Context-Scoped Plugins:**

- **Auto Discovery and Installation:** VCF CLI automatically discovers and installs context-scoped plugins (VM, Cluster, etc.) for VCFA and vSphere Supervisor endpoints, providing tailored functionality for each environment.
- **Resource Management:** Once logged in (context created), manage VCFA and vSphere Supervisor resources using context-scoped plugins like the VM plugin.

**Non-Context Scoped Plugins:**

- **Install and Use:** Install and manage non-context scoped plugins, plugin groups, and perform operations like those offered by ImgPkg.

**Airgapped Environments:**

- **Offline Operations:** VCF CLI supports airgapped environments with dedicated sub-commands and plugins, allowing you to work with VCF even without internet connectivity.

**Installation Flexibility:**

- **Multiple Methods:** VCF CLI is available for installation through various package managers (Homebrew, apt, yum, choco) as well as binary downloads, offering a convenient and adaptable approach.

**Getting Started:**

- **Download:** Download the latest version from [Download Location].
- **Installation Guide:**Refer to our detailed installation guide at [Link to Documentation].