---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/checking-cpu-usage-and-network-latency.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Checking CPU Usage and Network Latency
---

# Checking CPU Usage and Network Latency

Use APIs to monitor CPU usage and network latency.

## Checking CPU Usage

These APIs work similar to the
top command:

- Run the following API to check
  process status for all appliances:

  ```
  GET /api/v1/systemhealth/appliances/process/status
  ```
- Run the following API to check the
  process status of a specific appliance.

  ```
  GET https://<nsx-manager-ip>/api/vi/systemhealth/appliances/<appliance-id>/process/status
  ```

## Checking Network Latency

- Run the following API to check
  for network latency values for all
  appliances:

  ```
  GET /api/v1/systemhealth/appliances/latency/status
  ```
- Run the following API to check
  for network latency values for a specific appliance:

  ```
  GET https://<nsx-manager-ip>/api/v1/systemhealth/appliances/<appliance-id>/latency/status
  ```

See the latest version of the NSX API Guide at <https://code.vmware.com/> for API
details.