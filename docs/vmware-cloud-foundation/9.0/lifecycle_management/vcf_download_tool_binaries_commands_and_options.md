---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-binaries-commands.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > VCF Download Tool Binaries Commands and Options
---

# VCF Download Tool Binaries Commands and Options

Use the VCF Download Tool binaries commands to list, download, upload, and manage VMware Cloud Foundation installation, upgrade, and patch binaries.

## Binaries Commands

| Command | Description |
| --- | --- |
| download | Downloads binaries and metadata (unified release manifest, product version catalog, vSAN HCL, and compatibility data). The command supports filtering to narrow down the selection. At least one filter is required.  When executed multiple times with the same output directory, the command’s behavior is cumulative, adding to previously downloaded binaries without overwriting them.  The download command does not include UMDS binaries. |
| upload | Uploads downloaded binaries and metadata into SDDC Manager.  Before uploading, you must transfer the downloaded binaries and metadata to the SDDC Manager appliance.  The upload command must be run from within the SDDC Manager appliance. |
| list | Provides a comprehensive view of all available binaries. The command supports filtering to narrow down the selection. At least one filter is required.  The list command displays detailed information for each binary, including the component name, version number, release date, size, and type. This makes it easier to identify which binaries are relevant to your requirements before downloading. |
| cleanup | Use the cleanup command to manage disk space by removing unwanted or obsolete binaries, while retaining the ones you still need.  Run the cleanup command on a system where you have already downloaded binaries. |
| create-download-spec | Generates a download specification file based on the planned upgrades for a specific domain within the environment. The specification file is used to identify which binaries are required for the planned upgrades.  After you create the specification file, you can use it as an input parameter for the download command, ensuring that only the relevant binaries for the planned upgrade are downloaded.  The create-download-spec command must be run from within the SDDC Manager appliance. |

## Binaries Download Options

If the computer with internet access can only access the internet using a proxy server, use the following options when downloading binaries:

Proxy Server Options



| Option | Description |
| --- | --- |
| --proxy-https | Add this option if the proxy server uses HTTPs. |
| --proxy-user-password-file proxyServerPasswordFile | For a proxy server that requires authentication, replace proxyServerPasswordFile with the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password.  For example, --proxyPasswordFile ../../password.txt.  The supported proxy authentication methods are Basic and NTLMv1. |
| -r proxyServerUserName or  --proxy-user proxyServerUserName | For a proxy server that requires authentication, replace proxyServerUserName with the user name. |
| -s proxyServerHostName or  --proxy-server proxyServerHostName | Replace proxyServerHostName with the proxy server FQDN and port. For example: --proxy-server proxy.example.com:3128. |

Depot Options



| Option | Description |
| --- | --- |
| -d depotStore or  --depot-store depotStore | Directory where all binaries and metadata downloaded by the VCF Download Tool will be stored. Replace depotStore with the directory path.  This directory serves as the local repository for all downloaded artifacts, maintaining the necessary structure for easy access and management. |
| --depot-download-token-file depotDownloadTokenFile | Replace depotDownloadTokenFile with the path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |

Filter Options



| Option | Description |
| --- | --- |
| --automated-install | Downloads the binaries needed by the VCF Installer. |
| --component component | Downloads the binaries for a specified component. Replace component with one of the following values:  - VCENTER - SDDC\_MANAGER\_VCF - NSX\_T\_MANAGER - ESX\_HOST - VRSLCM - VRA - VROPS - VRLI - VRNI - VSAN\_OSA\_WITNESS - VSAN\_ESA\_WITNESS - VSAN\_FILE\_SERVICES - VMTOOLS - VCFDT - VCF\_OPS\_CLOUD\_PROXY - VIDB - HCX - VLR - DLVM - VMRC - VRO |
| --lifecycle-managed-by lcm | Downloads binaries whose lifecycle is managed by the specified component. Replace lcm with one of the following values:  - SDDC\_MANAGER\_VCF - VRSLCM - SELF |
| --sku sku | Downloads binaries for VMware Cloud Foundation or VMware vSphere Foundation. Replace sku with one of the following values:  - VCF - VVF |
| -t type or  --type type | Downloads binaries of the specified type. Replace type with one of the following values:  - INSTALL - UPGRADE |
| --vcf-version version[..[end version]] | Downloads binaries for a specific version versionof VMware Cloud Foundation, or for a range of versions start\_version..end\_version.  You can enter the version string in the following formats:  - a.b: For example, if you enter 9.0, the tool downloads the binaries for 9.0.0.0 and any 9.0.x binaries. - a.b.c: For example, if you enter 9.0.1, the tool downloads all 9.0.1.x binaries. - a.b.c.d: For example, if you enter 9.0.1.0, the tool only downloads 9.0.1.0 binaries.  When you specify a version range, the tool downloads all binaries from the start version to the end version and includes the binaries for both the start and end versions. |
| --id bundleIds | Downloads specific binaries using the bundle ID(s). Replace bundleIds with a single bundle ID or a comma-separated list of multiple bundle IDs. |
| --download-spec-file downloadSpecFile | Downloads only the binaries required for a specific planned upgrade.  Replace downloadSpecFile with the path to the download specification file generated by the create-download-spec command. This file contains the details of the binaries required for the planned upgrade. |

Binaries Download Examples



| Example Command | Description |
| --- | --- |
| ``` ./vcf-download-tool binaries download --depot-store binaries_dir --depot-download-token-file  token_file_path --vcf-version=9.0.0.0 --sku VCF --automated-install --type INSTALL ``` | Downloads the install binaries needed by VCF Installer for deploying a VMware Cloud Foundation 9.0. |
| ``` ./vcf-download-tool binaries download --depot-store binaries_dir --depot-download-token-file token_file_path --download-spec-file download_spec_file_path --proxy-server FQDN:Port --proxy-https --proxy-user username --proxy-user-password-file password_file_path ``` | Download binaries based on a download specification file using an authenticated proxy server. |

## Binaries Upload Options

| Option | Description |
| --- | --- |
| --depot-store depotStore or  -d depotStore | The directory on the SDDC Manager appliance where you copied all the binaries and metadata downloaded by the VCF Download Tool. |
| -f sddcManagerFqdn or  --sddc-manager-fqdn sddcManagerFqdn | Replace sddcManagerFqdn with the Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to the SDDC Manager instance. |
| -u sddcManagerUsername or  --sddc-manager-user sddcManagerUsername | Replace sddcManagerUsername with the user name for connecting to the SDDC Manager. |
| --sddc-manager-user-password-file sddcManagerPasswordFile | Replace sddcManagerPasswordFile with the path to a text file containing the password for the provided --sddc-manager-user. The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |

For example:

```
./vcf-download-tool binaries upload --depot-store= binaries_dir --sddc-manager-fqdn FQDN --sddc-manager-user username --sddc-manager-user-password-file password_file_path
```

## Binaries List Options

If the computer with internet access can only access the internet using a proxy server, use the following options when listing binaries:

Proxy Server Options



| Option | Description |
| --- | --- |
| --proxy-https | Add this option if the proxy server uses HTTPs. |
| --proxy-user-password-file proxyServerPasswordFile | For a proxy server that requires authentication, replace proxyServerPasswordFile with the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password.  For example, --proxyPasswordFile ../../password.txt.  The supported proxy authentication methods are Basic and NTLMv1. |
| -r proxyServerUserName or  --proxy-user proxyServerUserName | For a proxy server that requires authentication, replace proxyServerUserName with the user name. |
| -s proxyServerHostName or  --proxy-server proxyServerHostName | Replace proxyServerHostName with the proxy server FQDN and port. For example: --proxy-server proxy.example.com:3128. |

Depot Options



| Option | Description |
| --- | --- |
| --depot-download-token-file depotDownloadTokenFile | Replace depotDownloadTokenFile with the path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |

Filter Options



|  |  |
| --- | --- |
| --automated-install | Lists the binaries needed by the VCF Installer. |
| --component component | Lists the binaries for a specified component. Replace component with one of the following values:  - VCENTER - SDDC\_MANAGER\_VCF - NSX\_T\_MANAGER - ESX\_HOST - VRSLCM - VRA - VROPS - VRLI - VRNI - VSAN\_OSA\_WITNESS - VSAN\_ESA\_WITNESS - VSAN\_FILE\_SERVICES - VMTOOLS - VCFDT - VCF\_OPS\_CLOUD\_PROXY - VIDB - HCX - VLR - DLVM - VMRC - VRO |
| --lifecycle-managed-by lcm | Lists binaries whose lifecycle is managed by the specified component. Replace lcm with one of the following values:  - SDDC\_MANAGER\_VCF - VRSLCM - SELF |
| --patches-only | Lists the binaries for patch versions of components. |
| --sku sku | Lists binaries for VMware Cloud Foundation or VMware vSphere Foundation. Replace sku with one of the following values:  - VCF - VVF |
| -t type or  --type type | Lists binaries of the specified type. Replace type with one of the following values:  - INSTALL - UPGRADE |
| --vcf-version version[..[end version]] | Lists binaries for a specific version versionof VMware Cloud Foundation, or for a range of versions start\_version..end\_version.  You can enter the version string in the following formats:  - a.b: For example, if you enter 9.0, the tool lists the binaries for 9.0.0.0 and any 9.0.x binaries. - a.b.c: For example, if you enter 9.0.1, the tool lists all 9.0.1.x binaries. - a.b.c.d: For example, if you enter 9.0.1.0, the tool only lists 9.0.1.0 binaries.  When you specify a version range, the tool lists all binaries from the start version to the end version and includes the binaries for both the start and end versions. |
| --id bundleIds | Lists specific binaries using the bundle ID(s). Replace bundleIds with a single bundle ID or a comma-separated list of multiple bundle IDs. |
| --download-spec-file downloadSpecFile | Lists only the binaries required for a specific planned upgrade.  Replace downloadSpecFile with the path to the download specification file generated by the create-download-spec command. This file contains the details of the binaries required for the planned upgrade. |

Example:

|  |
| --- |
| ``` ./vcf-download-tool binaries list --depot-download-token-file token_file_path --vcf-version 9.0.0.0 --sku VCF --automated-install --type INSTALL ``` |

## Binaries Cleanup Options

Depot Options



| Option | Description |
| --- | --- |
| -d depotStore or  --depot-store depotStore | Directory where all binaries and metadata downloaded by the VCF Download Tool are stored. Replace depotStore with the directory path.  This directory serves as the local repository for all downloaded artifacts, maintaining the necessary structure for easy access and management. |

Filter Options



| Option | Description |
| --- | --- |
| --automated-install | Cleans up the binaries needed by the VCF Installer. |
| --component component | Cleans up the binaries for a specified component. Replace component with one of the following values:  - VCENTER - SDDC\_MANAGER\_VCF - NSX\_T\_MANAGER - ESX\_HOST - VRSLCM - VRA - VROPS - VRLI - VRNI - VSAN\_OSA\_WITNESS - VSAN\_ESA\_WITNESS - VSAN\_FILE\_SERVICES - VMTOOLS - VCFDT - VCF\_OPS\_CLOUD\_PROXY - VIDB - HCX - VLR - DLVM - VMRC - VRO |
| --lifecycle-managed-by lcm | Cleans up binaries whose lifecycle is managed by the specified component. Replace lcm with one of the following values:  - SDDC\_MANAGER\_VCF - VRSLCM - SELF |
| --patches-only | Cleans up the binaries for patch versions of components. |
| --sku sku | Cleans up binaries for VMware Cloud Foundation or VMware vSphere Foundation. Replace sku with one of the following values:  - VCF - VVF |
| -t type or  --type type | Cleans up binaries of the specified type. Replace type with one of the following values:  - INSTALL - UPGRADE |
| --vcf-version version[..[end version]] | Cleans up binaries for a specific version versionof VMware Cloud Foundation, or for a range of versions start\_version..end\_version.  You can enter the version string in the following formats:  - a.b: For example, if you enter 9.0, the tool cleans up the binaries for 9.0.0.0 and any 9.0.x binaries. - a.b.c: For example, if you enter 9.0.1, the tool cleans up all 9.0.1.x binaries. - a.b.c.d: For example, if you enter 9.0.1.0, the tool only cleans up 9.0.1.0 binaries.  When you specify a version range, the tool cleans up all binaries from the start version to the end version and includes the binaries for both the start and end versions. |
| --id bundleIds | Cleans up specific binaries using the bundle ID(s). Replace bundleIds with a single bundle ID or a comma-separated list of multiple bundle IDs. |
| --download-spec-file downloadSpecFile | Cleans up only the binaries required for a specific planned upgrade.  Replace downloadSpecFile with the path to the download specification file generated by the create-download-spec command. This file contains the details of the binaries required for the planned upgrade. |

For example:

```
./vcf-download-tool binaries cleanup --depot-store binaries_dir --vcf-version VCF_version --lifecycle-managed-by SDDC_MANAGER_VCF --type UPGRADE
```

## Binaries Create Download Spec Options

| Option | Description |
| --- | --- |
| --domain-name domainNames | Replace domainNames with a single workload domain or multiple comma-sepated workload domain names. |
| --download-spec-dir downloadSpecFile | Replace downloadSpecFile with the path to the directory where the file generated by the create download spec command will be stored. |
| -f sddcManagerFqdn or  --sddc-manager-fqdn sddcManagerFqdn | Replace sddcManagerFqdn with the Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to the SDDC Manager instance. |
| -u sddcManagerUsername or  --sddc-manager-user sddcManagerUsername | Replace sddcManagerUsername with the user name for connecting to the SDDC Manager. |
| --sddc-manager-user-password-file sddcManagerPasswordFile | Replace sddcManagerPasswordFile with the path to a text file containing the password for the provided --sddc-manager-user. The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |

Example:

```
./vcf-download-tool binaries create-download-spec --domain-name domain_name --download-spec-dir spec_output_dir --sddc-manager-fqdn FQDN --sddc-manager-user username --sddc-manager-user-password-file password_file_path
```