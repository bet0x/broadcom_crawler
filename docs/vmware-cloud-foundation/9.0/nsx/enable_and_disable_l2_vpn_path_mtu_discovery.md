---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-nsx-l2-vpn/enable-and-disable-l2-vpn-path-mtu-discovery.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enable and Disable L2 VPN Path MTU Discovery
---

# Enable and Disable L2 VPN Path MTU Discovery

You can enable or disable the L2 VPN path MTU (PMTU) discovery feature using CLI
commands. By default L2 VPN PMTU discovery is enabled.

You must have the user name and password for the admin account to log in to the
NSX Edge node.

1. Log in with admin privileges to
   the CLI of the NSX Edge node
   .
2. To check the status of the L2
   VPN PMTU discovery feature, use the following command.

   ```
   Nsxedge> get dataplane l2vpn-pmtu config
   ```

   If the feature is enabled, you
   see the following output: l2vpn\_pmtu\_enabled :
   True.

   If the feature is disabled, you see the following output:
   l2vpn\_pmtu\_enabled : False.
3. To disable the L2 VPN PMTU
   discovery feature, use the following command.

   ```
   nsxedge> set dataplane l2vpn-pmtu disabled
   ```