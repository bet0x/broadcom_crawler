---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/configuring-ping-adapter-instances.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Ping Account in VCF Operations
---

# Ping Account in VCF Operations

In VCF Operations, you can configure the ping functionality to verify the availability of end points that exist in your VMware Cloud Foundation platform. The ping functionality is configured at the adapter instance for IP addresses, group of IP addresses, and FQDN's.

Activate the Ping adapter before you configure it.

- If you have multiple adapter instances running on different collectors and both are pinging the same address, you can still get statistics from both the adapter instances for the same IP.
- The FQDN names are checked for validity, the FQDN validation relies on RFC1034 and RFC1123, and only top level domains of the internet are validated. The .local domain is not supported as it does not fall into the list of top-level domains in the Domain Name System (DNS) of the Internet.

1. From the left menu, click AdministrationIntegrations.
2. In the Accounts tab, click Add.
3. Click Ping.
4. If the management pack has not been installed previously, Click Yes in the dialog box to install the management pack.
5. Configure the Ping adapter instance.

   Option | Description || Name | Enter a name for the adapter instance. |
   | Description | Enter the description of the adapter instance. |
   | Unique Name | Specify the name for the adapter instance. You can use the name to view the metrics published for the adapter instance. |
   | Address List | Specify the IP address, IP address range, and the FQDN which must be pinged. |
   | Configuration Filename | Specify the name of the configuration file. The configuration file contains the IP addresses, CIDR information, and FQDN details as a comma-separated file. |
   | Collector / Group | Select the collector from which this adapter instance must run. |
   | Validate Connection | Click to check whether the connection is successful or not. |
   | Advanced Settings | To configure the advanced settings, click the drop-down menu. |
   | Wait Interval Time (second) | Specify the time interval in seconds to wait before running the next batch. Range: 0-300 seconds. |
   | Batch Size | Specify the number of request packets to send to each target. Range: 20-100. |
   | Interval (millisecond) | Specify the time the fping waits between successive packets to an individual targets. Greater or equal to 2000 milli seconds. |
   | DNS Name Resolve Interval (minute) | Specify the time at which you must resolve the DNS name for the next cycle. Minimum value is 15 minutes. |
   | Packet Size (byte) | Specify the byte size of the packet when you ping. Range: 56-65536 bytes. |
   | Don't Fragment | Select False to fragment the packet and True to not fragment the packet. |
   | Generate FQDN Child IPs | Select True to create IP objects by resolved names and add as child of FQDN. |
6. Click Add.

   The adapter instance is added to the list. Newly created ping accounts do not start monitoring the data automatically and you must manually initiate the data collection.

After you configure the Ping adapter instance, you can view the adapter details from AdministrationIntegrationsRepository.