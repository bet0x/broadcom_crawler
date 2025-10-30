---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/external-connections/add-a-centralized-connection.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Centralized Connection
---

# Add a Centralized Connection

In a Centralized connection, the Transit Gateway that is attached to it inherits high availability mode and Edge nodes placement of the specified Tier-0 gateway.

Centralized Connection

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e2fa355b-d41d-4ba6-bb43-21a12ccfc668.cq5dam.web.1280.1280.jpeg)

1. From your browser, log in to the NSX Manager.
2. Navigate to Networking External Connection .
3. Click Add External Connection .
4. Enter the following fields:

   Field Name | Description || Name | Enter a name for the external connection. |
   | Type | Click to select the type of connection you want to create. The centralized connection is selected by default. |
   | Tier-0 Gateway | Select the Tier-0 or Tier-0 VRF gateway through which you want to route the traffic to external networks. |
   | Advertise Out Route Filter | Select an advertise out route filter of the Tier-0 you selected.  Configure this advanced filtering only if you want to filter specific external IP addresses for advertisement.  The system only advertises in-use external IP addresses and CIDR to a Tier-0 gateway. No filter is required to block advertisement of private blocks. |
   | Route Aggregation | Enter a route aggregation CIDR. A route aggregation CIDR uses a single and larger CIDR block to represent a group of smaller IP address ranges that allows a router to advertise a single route to the network instead of multiple individual routes. |
   | Description | Enter a description for this connection. |
   | Tags | Enter a tag and scope for this connection. |
5. Click Save.