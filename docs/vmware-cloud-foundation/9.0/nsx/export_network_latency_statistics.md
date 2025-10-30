---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/network-latency-statistics/export-network-latency-statistics.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Export Network Latency Statistics
---

# Export Network Latency Statistics

You can export network latency statistics to external collectors and run analytics on the data. The netopa agent that is running in the ESX hosts can export the network latency statistics only to VCF Operations for networks. Other collector tools are not supported currently.

- In the VCF Operations for networks UI, complete the following tasks in the given order:
  1. Add vCenter as the data source. If you have multiple vCenters added as Compute Managers in your NSX environment, you can add all vCenters as the data source.
  2. Add NSX Manager as the data source.

  For detailed information about adding data sources in VCF Operations for networks, see the VCF Operations for networks documentation.
- Ensure that port 1991 is open on the collector to receive network latency data from the ESX hosts.

You can collect network latency statistics from only vCenter-managed ESX hosts. Collecting latency statistics from standalone ESX hosts is not supported.

You can export network latency statistics by using any one of the following methods:

- Method 1: Use the management plane APIs in NSX.
- Method 2: Enable an optional setting in the VCF Operations for networks UI to collect latency statistics.

1. Method 1: Use the NSX REST APIs.
   1. Ensure that you have configured the ESX hosts to measure network latency statistics.

      For detailed steps, see [Measure Network Latency Statistics](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/network-latency-statistics/measure-network-latency-statistics.html#GUID-a5021489-9900-4034-93e1-3c165820c2f3-en).
   2. Export the network latency statistics to the collector with the following PUT API:

      PUT https://<manager-ip>/api/v1/global-configs/OperationCollectorGlobalConfig -d '<content>'

      In the request body of this API, configure the following information:
      - Details of external collectors, such as collector IP address, collector port.
      - Report interval that controls the frequency at which the netopa agent sends statistics to the collector.
2. Method 2: Enable an optional setting in the VCF Operations for networks UI to collect latency statistics.

   When you add NSX Manager as the data source in VCF Operations for networks, select the Enable latency metric collection check box. This option enables VCF Operations for networks to collect latency statistics from the ESX hosts.

   For detailed information about adding NSX Manager as the data source in VCF Operations for networks, see the VCF Operations for networks documentation.

vNIC-to-vNIC latency statistics are exported to the external collector in the following format:

VIF1, VIF2, Max, Min, Avg

Where:

- VIF1, VIF2 represent the virtual interfaces or the vNICs.
- Max, Min, and Avg represent the maximum, minimum, and average time between the two vNICs in microseconds.

pNIC-to-vNIC and vNIC-to-pNIC latency statistics are exported to the external collector in the following format:

Endpoint1, Endpoint2, Max, Min, Avg

Where:

- Endpoint1, Endpoint2 can either be the virtual interface ID (VIF ID) or the name of the physical adapter on an ESX host (vmnic).
- Max, Min, and Avg represent the maximum, minimum, and average time between the two endpoints in microseconds.