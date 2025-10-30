---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/monitor-virtual-san-through-esxi-host-client.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Monitor vSAN from ESX Host Client
---

# Monitor vSAN from ESX Host Client

You can monitor vSAN health and basic configuration through the ESX host client.

The ESX host client is a browser-based interface for managing a single ESX host. It enables you to manage the host when vCenter is not available. The host client provides tabs for managing and monitoring vSAN at the host level.

- The vSAN tab displays basic vSAN configuration.
- The Hosts tab displays the ESX hosts participating in the vSAN cluster.
- The Health tab displays host-level health findings.

1. Open a browser and enter the IP address of the host. 

   The browser redirects to the login page for the host client.
2. Enter the username and password for the host, and click Login.
3. In the host client navigator, click Storage.
4. In the main page, click the vSAN datastore to display the Monitor link in the navigator.
5. Click the tabs to view vSAN information for the host. 
   1. Click the Events tab to display the ESX host events.
   2. Click the vSAN tab to display basic vSAN configuration.
   3. Click the Hosts tab to display the ESX hosts participating in the vSAN cluster.
   4. Click the Health tab to display host-level health findings.
6. (Optional) On the vSAN tab, click Edit Settings to correct configuration issues at the host level.

   Select the values that match the configuration of your vSAN cluster, and click Save.