---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/external-connections/add-a-distributed-connection.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Distributed Connection
---

# Add a Distributed Connection

Distributed Connection

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6a54cb60-eb91-4b3e-9231-ff6834463edf.cq5dam.web.1280.1280.jpeg)

1. From your browser, log in to the NSX Manager.
2. Navigate to Networking  External Connection.
3. Click Distributed Connection.
4. Enter the following fields:

   Field Name | Description || Name | Enter a name for the external connection. |
   | Type | Click the Distributed Connection option. |
   | Gateway CIDR IP Address | Enter the gateway address and netmask through which the traffic should be routed to the external network. |
   | VLAN ID | Enter the VLAN ID to which the traffic is to be routed. This VLAN must be dedicated for external connectivity of workloads deployment in VPCs and must be stretched across all clusters where VPCs are deployed.  Also, note that the External IP block must be a subset of VLAN CIDRs and any in-use IP address on the physical network must be pre-allocated on NSX to avoid duplicate IP assignment. |
   | Description | Enter a description for this connection. |
   | Tags | Enter a tag and scope for this connection. |
5. Click Save.