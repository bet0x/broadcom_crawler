---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-releases-commands.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > VCF Download Tool Releases Commands
---

# VCF Download Tool Releases Commands

Use the VCF Download Tool releases commands to download the unified release manifest and view a list of available VMware Cloud Foundation releases.

## Releases Commands

| Command | Description |
| --- | --- |
| list | Provides a comprehensive list of all available VMware Cloud Foundation releases. The list command supports filtering to narrow down the selection.  When executed without specifying a release, the list command displays all the releases currently available. If a specific release is provided as a parameter, the command shows detailed information about the products included within that release. |

## Releases Options

If the computer with internet access can only access the internet using a proxy server, use the following options when listing releases:

Proxy Server Options



| Option | Description |
| --- | --- |
| --proxy-https | Add this option if the proxy server uses HTTPs. |
| --proxy-user-password-file proxyServerPasswordFile | For a proxy server that requires authentication, replace proxyServerPasswordFile with the path to a file where the password for proxy authentication is stored. The file content is used as the proxy password.  For example, --proxyPasswordFile ../../password.txt.  The supported proxy authentication methods are Basic and NTLMv1. |
| -r proxyServerUserName or  --proxy-user proxyServerUserName | For a proxy server that requires authentication, replace proxyServerUserName with the user name. |
| -s proxyServerHostName or  --proxy-server proxyServerHostName | Replace proxyServerHostName with the proxy server FQDN and port.  For example: --proxy-server proxy.example.com:3128. |

Depot Options



| Option | Description |
| --- | --- |
| --depot-download-token-file depotDownloadTokenFile | Replace depotDownloadTokenFile with the path to a text file containing single line with your depot download token.  You can generate a download token in the Broadcom Support Portal. |

Filter Options



| Option | Description |
| --- | --- |
| --vcf-version version | Replace version with the VMware Cloud Foundation version for which to show detailed information about the products included within that release.  If you do not provide a version, the list command returns all available versions. |

Example:

```
./vcf-download-tool releases list --vcf-version 9.0.0.0 --depot-download-token-file token_file_path
```