---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/connect-sddc-manager-to-a-software-depot-for-downloading-bundles/configure-a-proxy-server-to-download-bundles-from-sddc-manager.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Configure a Proxy Server for Accessing VMware Cloud Foundation Bundles
---

# Configure a Proxy Server for Accessing VMware Cloud Foundation Bundles

If SDDC Manager does not have direct internet access, you can configure a proxy server to access bundles. SDDC Manager supports proxy servers with authentication.

1. In the navigation pane, click AdministrationProxy Settings.
2. Click Set Up Proxy.
3. Toggle the Enable Proxy setting to the on position.
4. Select HTTP or HTTPS.
5. Enter the proxy server IP address and port number.
6. If your proxy server requires authentication, toggle the Authentication setting to the on position and enter the user name and password.

   VMware Cloud Foundation does not support proxy servers with NTLMv2 authentication.
7. Click Save.

You can now download bundles as described in [Download VMware Cloud Foundation 9.0 Upgrade Bundles Using an Online or Offline Depot](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/downloading-vmware-cloud-foundation-bundles/download-bundles-from-sddc-manager.html#GUID-0f25699f-4662-40de-b1e1-5db36396212f-en).