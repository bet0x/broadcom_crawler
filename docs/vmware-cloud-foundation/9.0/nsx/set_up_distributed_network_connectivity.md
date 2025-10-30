---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/setting-up-network-connectivity/set-up-distributed-network-connectivity.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Set up Distributed Network Connectivity
---

# Set up Distributed Network Connectivity

Starting with VCF 9.0, a simplified workflow is introduced to set up network configuration. The workflow is available in both NSX and vCenter. This section describes how to use the workflow from NSX to configure a distributed connectivity.

To use the workflow you must have a role of NSX administrator. Also, before you start using the workflow ensure that the following requirements are met.

- Dedicated VLANs and subnets must be available for Distributed Transit Gateway connection to Top of Rack (ToR). The same VLAN must be configured on all the ToR switches where the ESX host are connected which offers VPCs. All the hosts running VPC workloads must have access to these VLANs.
- Disable 'ICMP redirect' on external gateway for these VLAN(s). External Gateway should allow packets received from ESX over these VLANs forwarded back to the same or different ESX.
- Reserve external IP blocks for VPC connectivity. External IP blocks must be same as or a subset of dedicated VLAN subnets.

To set up a distributed gateway connectivity on Day 0 when no other connectivity is set up, perform the following steps:

1. From your browser, log in to the NSX Manager.
2. Go to System Quick StartSetup Network Connectivity.
3. Click Configure NSX Networking.
4. Select the Distributed Gateway  option on the Gateway Type page and click **Next**.
5. On the Networking Prerequisites dialog box, click Select all and click Continue.
6. On the Edge Cluster page, enter the following details.

   | Field Name | Description |
   | --- | --- |
   | VLAN ID | Enter the VLAN ID. |
   | Gateway CIDR IPv4 Address | Enter the gateway IP address that is configured on the ToR switches. |
   | VPC Configuration | |
   | VPC External IP Blocks | Enter IP blocks for VPC. |
7. Click Next.