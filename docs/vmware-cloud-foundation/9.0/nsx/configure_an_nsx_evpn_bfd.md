---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ethernet-vpn-evpn/evpn-route-server-mode/evpn-route-server-mode-configuration-workflow/configure-an-nsx-evpn-bfd.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX EVPN BFD
---

# Configure an NSX EVPN BFD

In EVPN Server Route mode, BFD
(Bidirectional Flow Detection) between the ESX nodes and data center gateways can be "optionally" enabled
for TEP fast failure detection.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingGlobal Networking Config.
3. Click
   Edit.
4. For EVPN BFD Profile, select a BFD profile.

   If you need to create a new profile with required BFD timers, click the menu
   icon (three dots) and select Create New.
5. For Enable EVPN BFD, make sure that the toggle is
   on.
6. Click Save.