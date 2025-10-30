---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-vmrc/configure-proxy.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Configure Proxy Settings
---

# Configure Proxy Settings

You can configure a proxy server through which VMRC can connect to your virtual machines.

HTTP(S) is the only supported protocol for proxy connections.

In previous releases, the VMWARE\_HTTPSPROXY environment variable was used to set a proxy server. Proxy settings configured in this procedure take precedence over the value VMWARE\_HTTPSPROXY. However, if you do not configure proxy settings, VMWARE\_HTTPSPROXY continues to take effect.

To use a proxy server that requires authentication, you must configure proxy settings using this procedure rather than accept the VMWARE\_HTTPSPROXY setting.

1. In a web browser, go to vmrc://settings and click Open Link. The Connection Proxy dialog appears. If VMRC was already opened:

   1. On Windows, select VMRC > Preferences.
   2. On MacOS, select VMware Remote Console > Settings.
   3. On Linux, select File > Remote Console Preferences.
2. In the Connection Proxy dialog, follow these steps:

   1. Click Enable proxy for remote virtual machine. On Windows and Linux, also click Connection Proxy Settings.
   2. Enter the IP address (or hostname) and port of your proxy server. You can enter either IPv4 or IPv6 address.
   3. Enter the user name and password to authenticate with your proxy server. On MacOS, first click Using Credentials.
   4. Click OK or Save. On MacOS, restart VMRC for the configured settings to take effect.

After you have configured proxy settings, VMRC will send all subsequent virtual machine connections through the specified proxy server.

If VMRC displays connection-related errors, ensure that your proxy settings are correct. On MacOS, be sure you restarted VMRC.