---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/download-the-remote-side-l2-vpn-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Download the Remote Side L2 VPN Configuration File
---

# Download the Remote Side L2 VPN Configuration File

To configure the
L2 VPN client session, you must obtain the peer code that was generated when
you configured the L2 VPN server session.

- You must have configured
  an L2 VPN server service and a session successfully before proceeding. See
  [Add an L2 VPN Server Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-server-service.html#GUID-7c30c658-2c66-44ae-93c7-81b508220a4f-en).

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to the
   tab.
3. In the table of L2 VPN
   sessions, expand the row for the L2 VPN server session you plan to use for the
   L2 VPN client session configuration.
4. Click
   Download
   Config and click
   Yes on the Warning
   dialog box.

   A text file with the name L2VPNSession\_<name-of-L2-VPN-server-session>\_config.txt is
   downloaded. It contains the peer code for the remote side L2 VPN configuration.

   Be careful when storing and sharing the peer code
   because it contains a PSK value, which is considered sensitive information.

   For example, L2VPNSession\_L2VPNServer\_config.txt contains the following
   configuration.

   ```
   [
     {
       "transport_tunnel_path": "/infra/tier-0s/ServerT0_AS/locale-services/1-policyconnectivity-693/ipsec-vpn-services/IpsecService1/sessions/Routebase1",
       "peer_code": 
   "MCw3ZjBjYzdjLHsic2l0ZU5hbWUiOiJSb3V0ZWJhc2UxIiwic3JjVGFwSXAiOiIxNjkuMjU0LjY0LjIiLCJkc3RUYXBJcCI6IjE2OS4yNTQuNjQuMSIsImlrZU9wdGl
   vbiI6ImlrZXYyIiwiZW5jYXBQcm90byI6ImdyZS9pcHNlYyIsImRoR3JvdXAiOiJkaDE0IiwiZW5jcnlwdEFuZERpZ2VzdCI6ImFlcy1nY20vc2hhLTI1NiIsInBzayI
   6IlZNd2FyZTEyMyIsInR1bm5lbHMiOlt7ImxvY2FsSWQiOiI2MC42MC42MC4xIiwicGVlcklkIjoiNTAuNTAuNTAuMSIsImxvY2FsVnRpSXAiOiIxNjkuMi4yLjMvMzEifV19"
     }
   ]
   ```
5. Copy the peer code, which you use to configure the L2 VPN client service and
   session. 

   Using the preceding configuration file example, the following peer code is
   what you copy to use with the L2 VPN client
   configuration.

   ```
   MCw3ZjBjYzdjLHsic2l0ZU5hbWUiOiJSb3V0ZWJhc2UxIiwic3JjVGFwSXAiOiIxNjkuMjU0LjY0LjIiLCJkc3RUYXBJcCI6IjE2OS4yNTQuNjQuMSIsImlrZU9wdGl
   vbiI6ImlrZXYyIiwiZW5jYXBQcm90byI6ImdyZS9pcHNlYyIsImRoR3JvdXAiOiJkaDE0IiwiZW5jcnlwdEFuZERpZ2VzdCI6ImFlcy1nY20vc2hhLTI1NiIsInBzayI
   6IlZNd2FyZTEyMyIsInR1bm5lbHMiOlt7ImxvY2FsSWQiOiI2MC42MC42MC4xIiwicGVlcklkIjoiNTAuNTAuNTAuMSIsImxvY2FsVnRpSXAiOiIxNjkuMi4yLjMvMzEifV19
   ```

Configure the L2 VPN Client
service and session. See
[Add an L2 VPN Client Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-client-service.html#GUID-5c3e0c6b-6835-4a9e-95b0-6f4b329fcd5e-en)
and
[Add an L2 VPN Client Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-client-session.html#GUID-db01896c-9282-4b8b-bdde-3881bc79ba62-en).