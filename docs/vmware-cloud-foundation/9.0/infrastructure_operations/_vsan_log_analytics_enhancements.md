---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsan-overview/vsan-log-analytics-enhancements.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   vSAN Log Analytics Enhancements
---

# vSAN Log Analytics Enhancements

When VCF Operations is integrated with VCF Operations for logs, you can view and troubleshoot VCF Operations for logs object issues within VCF Operations. Earlier you could troubleshoot issues related only to vCenter objects, but now you can troubleshoot issues related to vSAN also.

The enhancements to vSAN log analytics include use of specific queries to retrieve log information for the following vSAN objects:

- vSAN Cluster
- Witness Host
- Disk Group
- Cache Disk
- Capacity Disk

## Where You Find vSAN Object Logs

Navigate to the vSAN Object Details page, and click the Logs tab.

If you are not logged in to VCF Operations for logs, then VCF Operations prompts you to log in to VCF Operations for logs with your login credentials.

VCF Operations uses special queries for each object type. Using the special queries for vSAN objects, you can perform the following actions:

- View interactive analytics for the selected vSAN object.
- Retrieve log details for the vSAN object.
- Analyze and troubleshoot issues related to the vSAN object.