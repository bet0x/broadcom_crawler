---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/what-is-the-vcf-download-tool-/vcf-download-tool-general-options.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > VCF Download Tool General Options
---

# VCF Download Tool General Options

You can use the VCF Download Tool general options to view help, check the utility version, and choose whether or not to share data with the Customer Experience Improvement Program (CEIP).

## Help Options

| Option | Description |
| --- | --- |
| -h, --help | Provides information about the VCF Download Tool options and commands. |
| binaries -h, binaries --help | Provides information about the options for managing binaries. |
| metadata -h, metadata --help | Provides information about the options for managing metadata. |
| releases -h, releases --help | Provides information about the options for VMware Cloud Foundation releases. |
| umds -h, umds --help | Provides information about the options for the Update Manager Download Service (UMDS). |

Example:

```
./vcf-download-tool binaries -h
```

## Version Option

| Option | Description |
| --- | --- |
| -v, --version | Displays the version of the VCF Download Tool. |

## Customer Experience Improvement Program (CEIP) Option

The VCF Download Tool participates in the VMware Customer Experience Improvement Program (CEIP). Under CEIP, VMware collects information about participating customers’ use of on-premise products. You can enable or deactivate CEIP for the VCF Download Tool.

For additional information regarding the CEIP, see <https://www.broadcom.com/company/legal/privacy/data-usage-programs/ceip>.

| Option | Description |
| --- | --- |
| --ceip ENABLE or --ceip DISABLE | The first time you use the VCF Download Tool, you are prompted to make a choice about whether to participate in CEIP. This selection is maintained and used as the default, unless you specify the option again with a different value. |