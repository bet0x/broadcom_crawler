---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ip-address-management-ipam/add-an-nsx-dns-forwarder-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX DNS Forwarder Service
---

# Add an NSX DNS Forwarder Service

You can configure a DNS forwarder to
forward DNS queries to external DNS servers.

Before you configure a DNS
forwarder, you must configure a default DNS zone. Optionally, you can configure one or
more FQDN DNS zones. Each DNS zone is associated with up to 3 DNS servers. When you
configure a FQDN DNS zone, you specify one or more domain names. A DNS forwarder is
associated with a default DNS zone and up to 5 FQDN DNS zones. When a DNS query is
received, the DNS forwarder compares the domain name in the query with the domain names
in the FQDN DNS zones. If a match is found, the query is forwarded to the DNS servers
specified in the FQDN DNS zone. If a match is not found, the query is forwarded to the
DNS servers specified in the default DNS zone.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingIP
   ManagementDNS.
3. Click DNS Services.
4. Click Add DNS Service.
5. Enter a name.
6. Select a tier-0 or tier-1
   gateway.
7. Enter the IP address of the DNS
   service.

   Clients send DNS queries to this IP address, which is also known as the DNS
   forwarder's listener IP.
8. Select a default DNS zone.
9. Select up to five FQDN zones.
10. Select a log level.
11. Enter a description.
12. Click the Admin
    Status toggle to enable or disable the DNS service.
13. Change the cache size.
14. Click
    Save.