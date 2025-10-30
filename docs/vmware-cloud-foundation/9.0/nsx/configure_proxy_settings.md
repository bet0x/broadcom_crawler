---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configure-proxy-settings.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Proxy Settings
---

# Configure Proxy Settings

To route and monitor all internet-bound HTTP/HTTPS traffic through a reliable
HTTP/HTTPS Proxy, you can configure proxy settings for your NSX Manager environment.

For HTTPS proxy, you must
have a proxy server self-signed certificate available in NSX Manager. See [Creating Self-signed Certificates for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/creating-self-signed-certificates.html) to create or import an existing
self-signed certificate.

Do not set up proxy configuration
on an NSX Edge, since transport nodes
require direct Internet connectivity for FQDN analysis and for URL
filtering.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemGeneral Settings.
3. To create an optional proxy
   configuration the first time, click the highlighted button on the Internet Proxy
   Server page or continue to the next step.
4. To turn on proxy server
   configuration, toggle the Proxy Enabled to Yes.
5. In the Scheme column, select HTTP
   or HTTPS.
6. In the
   Host field, enter an IP address or FQDN.
7. In the
   Port field, enter a port number.

   In general, the default port is 3128, but you can configure a different
   port if needed. This number should be unique and not already in use by other
   services on the network. This port must allow incoming traffic from the
   NSX components that need to
   use the proxy server.
8. In the
   Username field, enter a user name.
9. In the
   Password field, enter a password.
10. In the Test Connection URL, enter any web URL for
    confirmation of configuration success.

    For example: https://www.broadcom.com
11. If you selected HTTPS, in the
    Certificate  drop-down, select a proxy certificate
    trusted by NSX.
12. Click
    Save.