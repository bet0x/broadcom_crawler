---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/deploying-a-witness-appliance/configure-management-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure Management Network on the Witness Appliance
---

# Configure Management Network on the Witness Appliance

Configure the
witness appliance, so that it is reachable on the network.

By default, the appliance can
automatically obtain networking parameters if your network includes a DHCP
server. If not, you must configure appropriate settings.

1. Power on your
   witness appliance and open its console.

   Because
   your appliance is an
   ESX host, you
   see the Direct Console User Interface (DCUI).
2. Press F2 and navigate to
   the Network Adapters page.
3. On the Network Adapters
   page, verify that at least one vmnic is selected for transport.
4. Configure the IPv4
   parameters for the management network.
   1. Navigate to the IPv4
      Configuration section and change the default DHCP setting to static.
   2. Enter the following
      settings:

      - IP address
      - Subnet mask
      - Default
        gateway
5. Configure DNS
   parameters.
   - Primary DNS
     server
   - Alternate DNS
     server
   - Hostname