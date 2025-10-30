---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-metadata-proxy-server.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX Metadata Proxy Server
---

# Create an NSX Metadata Proxy Server

A metadata proxy server enables VMs to retrieve metadata from an OpenStack Nova API
server.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsProfilesMetadata Proxies.
3. Click Add Metadata
   Proxy.
4. Enter a name for the metadata
   proxy server.
5. In the Server
   Address field, enter the URL and port for the Nova server.

   The valid port range is 3000 - 9000.
6. Select an Edge cluster.
7. Select Edge nodes.

   If you select any Edge node, you cannot enable Standby
   Relocation in the next step.
8. Enable Standby
   Relocation.

   Standby relocation means that if the Edge node running the metadata proxy
   fails, the metadata proxy will run on a standby Edge node. You can only enable
   standby relocation if you do not select any Edge node.
9. In the Shared
   Signature Secret field, enter the secret that the metadata proxy
   will use to access the Nova server.
10. Select a certificate for
    encrypted communication with the Nova server.
11. Select a cryptographic
    protocol.

    The options are TLSv1, TLSv1.1, and TLSv1.2. TLSv1.1 and TLSv1.2 are supported
    by default.