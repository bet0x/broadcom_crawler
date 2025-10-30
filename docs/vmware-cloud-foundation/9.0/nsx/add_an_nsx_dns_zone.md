---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ip-address-management-ipam/add-an-nsx-dns-zone.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX DNS Zone
---

# Add an NSX DNS Zone

You can configure
DNS zones for your DNS service. A DNS zone is a distinct portion of the domain
name space in DNS.

When you configure a DNS zone, you can specify a source IP
for a DNS forwarder to use when forwarding DNS queries to an upstream DNS server. If you
do not specify a source IP, the DNS query packet's source IP will be the DNS forwarder's
listener IP. Specifying a source IP is needed if the listener IP is an internal address
that is not reachable from the external upstream DNS server. To ensure that the DNS
response packets are routed back to the forwarder, a dedicated source IP is needed.
Alternatively, you can configure SNAT on the logical router to translate the listener IP
to a public IP. In this case, you do not need to specify a source IP.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingIP
   ManagementDNS.
3. Click the
   DNS
   Zones tab.
4. To edit a default zone, click
   ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) next to the object you want to edit and click
   Edit.
   1. Enter a name and
      optionally a description.
   2. Enter the IP address of
      up to three DNS servers.
   3. Enter an IP address in
      the Source IP field.
5. To edit an FQDN zone, click
   ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) next to the object you want to edit and click
   Edit. 
   1. Enter a name and
      optionally a description.
   2. Enter a FQDN for the
      domain.
   3. Enter the IP address of
      up to three DNS servers.
   4. Enter an IP address in
      the Source IP field.
6. Click
   Save.