---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/add-a-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Service
---

# Add a Service

You can configure a service, and
specify parameters for matching network traffic such as a port and protocol pairing.

You can also use a service to allow or block certain
types of traffic in firewall rules. You cannot change the type after you create a
service. Some services are predefined and cannot be modified or deleted.

1. With admin privileges, log in
   to NSX Manager.
2. Select InventoryServices.
3. Click Add Service.
4. Enter a name.
5. Click Set.
6. Select a type.

   The choices are Layer 2 and Layer 3 and
   above.
7. Under the
   Port-Protocol tab, click Add Service
   Entry to add one or more service entries. 

   For layer 2, the only available service type is Ether.

   For layer 3 and above, the
   available service types are IP,
   IGMP, ICMPv4,
   ICMPv6,ALG,
   TCP, and UDP.

   The following built-in ALGs for DFW are
   supported: FTP, TFTP, MS\_RPC\_TCP, MS\_RPC\_UDP, ORACLE\_TNS, SUN\_RPC\_TCP
   and SUN\_RPC\_UDP.

   The following built-in ALGs for Gateway
   Firewall are supported: FTP and TFTP.
8. Click the
   Services tab to add one or more services.

   Any service that you add is considered a nested service because it is included in the
   service that you are creating. The recommended maximum level of nesting is 3. An
   example of three levels of nesting: service A includes service B, service B
   includes service C, and service C includes service D. In addition, cyclic
   nesting is not allowed. In the previous example, service C cannot include
   service A or B.
9. Click Apply.
10. Add one or more tags.
11. Enter a description.
12. Click
    Save.