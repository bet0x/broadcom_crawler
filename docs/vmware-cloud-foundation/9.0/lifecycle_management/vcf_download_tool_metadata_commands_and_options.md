---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-metadata-commands.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > VCF Download Tool Metadata Commands and Options
---

# VCF Download Tool Metadata Commands and Options

Use the VCF Download Tool metadata commands to download and upload the metadata files (unified release manifest, product version catalog, vSAN HCL, and compatibility data) for VMware Cloud Foundation binaries.

## Metadata Commands

| Command | Description |
| --- | --- |
| download | Downloads all the metadata required by SDDC Manager in a single operation. It automatically retrieves all relevant metadata files, without requiring you to manually specify which files are needed.  The download command does not include UMDS metadata. |
| upload | Uploads all the downloaded metadata to SDDC Manager.  Before uploading, you must transfer the downloaded metadata to the SDDC Manager appliance.  The upload command must be run from within the SDDC Manager appliance. |

## Metadata Download Options

If the computer with internet access can only access the internet using a proxy server, use the following options when downloading metadata:

Proxy Server Options



| Option | Description |
| --- | --- |
| --proxy-https | Add this option if the proxy server uses HTTPs. |
| --proxy-user-password-file proxyServerPasswordFile | For a proxy server that requires authentication, replace proxyServerPasswordFile with the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password. For example, --proxyPasswordFile ../../password.txt. |
| -r proxyServerUserName or  --proxy-user proxyServerUserName | For a proxy server that requires authentication, replace proxyServerUserName with the user name. |
| -s proxyServerHostName or  --proxy-server proxyServerHostName | Replace proxyServerHostName with the proxy server FQDN and port. For example: --proxy-server proxy.example.com:3128. |

| Option | Description |
| --- | --- |
| -d depotStore or  --depot-store depotStore | Directory where all binaries and metadata downloaded by the VCF Download Tool will be stored. Replace depotStore with the directory path.  This directory serves as the local repository for all downloaded artifacts, maintaining the necessary structure for easy access and management. |
| --depot-download-token-file depotDownloadTokenFile | Replace depotDownloadTokenFile with the path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |

Example:

```
./vcf-download-tool metadata download --depot-store metadata_dir --depot-download-token-file token_file_path
```

## Metadata Upload Options

| Option | Description |
| --- | --- |
| --depot-store depotStore or  -d depotStore | The directory on the SDDC Manager appliance where you copied all the metadata downloaded by the VCF Download Tool. |
| -f sddcManagerFqdn or  --sddc-manager-fqdn sddcManagerFqdn | Replace sddcManagerFqdn with the Fully Qualified Domain Name (FQDN) of the SDDC Manager. This is the address that the VCF Download Tool will use to connect to the SDDC Manager instance. |
| -u sddcManagerUsername or  --sddc-manager-user sddcManagerUsername | Replace sddcManagerUsername with the user name for connecting to the SDDC Manager. |
| --sddc-manager-user-password-file sddcManagerPasswordFile | Replace sddcManagerPasswordFile with the path to a text file containing the password for the provided --sddc-manager-user. The password should be on a single line within the file. If this file is not provided, you are prompted to manually enter the password during execution. |

Example:

```
./vcf-download-tool metadata upload --depot-store metadata_dir --sddc-manager-fqdn FQDN> --sddc-manager-user username --sddc-manager-user-password-file password_file_path
```