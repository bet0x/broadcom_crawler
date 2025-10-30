---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/lifecycle-management-of-vcf-core-components/configure-an-online-depot-for-a-vcf-instance/configure-a-proxy-server-for-a-vcf-instance.html
product: vmware-cloud-foundation
version: 9.0
section: Lifecycle Management
breadcrumb: Lifecycle Management > Configure a Proxy Server for SDDC Manager
---

# Configure a Proxy Server for SDDC Manager

If SDDC Manager does not have direct internet access, you can configure a proxy server to access binaries. SDDC Manager supports proxy servers with authentication.

1. In VCF Operations, click Fleet ManagementLifecycle.
2. Click VCF Instances and click on the name of a VCF Instance.
3. Click Proxy Settings.
4. Click Set Up Proxy.
5. Toggle the Proxy Enabled setting to the on position.
6. Select HTTP or HTTPS.
7. Enter the proxy server IP address and port number.
8. If your proxy server requires authentication, toggle the Authentication setting to the on position and enter the user name and password.

   VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.
9. Click Save.