---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/update-licenses.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Updating Licenses and Viewing the License Usage File
---

# Updating Licenses and Viewing the License Usage File

You must update your licenses in VCF Operations to verify that a usage file has been submitted, or when you make a license-related change such as subscription capacity changes, renewals, or splitting licenses and changing their capacity. Unlike prior VCF versions, when you update licenses, you do not need to reassign licenses to the assets.

If you do not make any license-related changes in the VCF Business Services console, you must still update your licenses at least once every 6 months (180 days). If license usage data is not submitted within the required reporting time-frame, and you do not update your licenses, your licenses are treated as expired, your hosts are disconnected from the vCenter instance, and you cannot start any workload operations.

## **How to view the detailed contents of your usage file**

You can view your license usage in a ready-to-read usage file that is decompressed and decoded, or you can view the raw usage file that is created in your VCF Operations instance. The raw usage file is JSON Web Signed (JWS) file compressed with gZip.

If your VCF Operations instance is in connected mode, usage files are automatically generated and submitted daily. If your VCF Operations instance is in disconnected mode, you must manually download and submit usage files on regular intervals. The content of the usage files are identical in connected and disconnected mode.

If your VCF Operations is in connected mode, you can only view the ready-to-read usage file.

|  |  |
| --- | --- |
| View a ready-to-read usage file | 1. In the VCF Operations instance, navigate to License ManagementRegistration. 2. Under File History, download the usage file you want to view, and open it. |
| View the raw usage file in a human-readable format | 1. Download and install gZip decompression software. 2. In the VCF Operations instance, navigate to License ManagementRegistration, and click Generate Usage File. 3. Use the decompression software and decompress the content of the usage file. The result is a file with the same name but no file extension. 4. Use a text editor to open the decompressed file, and copy the content. 5. Paste the content of the usage file into a JWT Decoding tool.   After the content is decoded, you can view the collected license usage information. |

## License Usage File Content

| **Property** | **Description** |
| --- | --- |
| usage\_report\_generated\_time | The date and time when the usage report is generated. |
| usage\_report\_id | The unique ID of this usage report. |
| asset\_id | The unique ID of the VCF Operations instance where data is collected. |
| asset\_status | Active. |
| xr2 | A unique opaque fingerprint of the VCF Operations instance where data is collected; used in conjunction with the asset\_id to link the usage data to the registered VCF Operations instance. No identifiable environment details can be derived from the fingerprint. |
| product\_version | - 9.0 when the license is version 9+. - 1.0 when a pre-version 9 license key is used. |
| product\_name | Product display name. |
| Allocation\_id | License ID for the version 9+ license. |
| license\_key\_id | License key for a pre-version 9 license. |
| usage\_start\_time | Start time of the usage period. |
| usage\_end\_time | End time of the usage period. |
| granularity | Always hourly. |
| uom | TiB or core for version 9+ licenses. |
| quantity | License usage quantity for this usage period. |
| total\_quantity | License capacity (included for pre-version 9 licenses only). |
| unassigned\_licenses | List of version 9 licenses (allocation\_id) that are added to VCF Operations and are not used. |
| license\_usage\_anomaly\_details | Generally empty. Indicates cases where usage data was corrupted - possibly as a result of a corrupt database, corrupt software update, or related circumstances. |

The license usage file exclusively gathers this specific information and, for clarity, does not collect personal data or customer data.