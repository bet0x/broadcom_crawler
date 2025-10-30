---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   Add an NSX IPSec VPN Service
---

# Add an NSX IPSec VPN Service

NSX supports a site-to-site IPSec VPN service between a Tier-0 or Tier-1 gateway and remote sites. You can create a policy-based or a route-based IPSec VPN service. You must create the IPSec VPN service first before you can configure either a policy-based or a route-based IPSec VPN session.

- Familiarize yourself with the IPSec VPN. See [Understanding IPSec VPN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/understanding-ipsec-vpn.html#GUID-f0bb166f-53a6-4307-8fe1-7510b3e7b5cc-en).
- You must have at least one tier-0 or tier-1 gateway configured and available for use. See [Add an NSX Tier-0 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/add-an-nsx-tier-0-gateway.html#GUID-cf0263b7-a347-4d07-b72f-4de927e2a28e-en) or [Add an NSX Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-1-gateways/add-an-nsx-tier-1-gateway.html#GUID-2567f98d-7076-468c-8afc-285870869371-en) for more information.
- When configuring NSX with both NAT and IPSec, it is important to follow the correct sequence of steps to ensure proper functionality. Specifically, configure NAT before setting up the VPN connection. If you inadvertently configure the VPN before NAT, for instance, by adding a NAT rule after your VPN session is configured, the VPN tunnel status will remain down. You must reenable or restart the VPN configuration to reestablish the VPN tunnel. To avoid this issue, always configure NAT before setting up the VPN connection in NSX or perform the workaround to resolve the issue.

IPSec VPN is not supported in the NSX limited export release.

IPSec VPN is not supported when the local endpoint IP address goes through NAT in the same logical router that the IPSec VPN session is configured.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to NetworkingVPNVPN Services.
3. Select Add ServiceIP Sec.
4. Enter a name for the IPSec service. 

   This name is required.
5. From the Tier-0/Tier-1 Gateway drop-down menu, select the Tier-0 or Tier-1 gateway to associate with this IPSec VPN service.
6. Enable or disable Admin Status. 

   By default, the value is set to Enabled, which means the IPSec VPN service is enabled on the Tier-0 or Tier-1 gateway after the new IPSec VPN service is configured.
7. Set the value for IKE Log Level. 

   The default is set to the Info level.
8. Enter a value for Tags if you want to include this service in a tag group.
9. To enable or disable the stateful synchronization of VPN sessions, toggle Session sync.

   By default, the value is set to Enabled.
10. Click Global Bypass Rules if you want to allow data packets to be exchanged between the specified local and remote IP addresses without any IPSec protection. In the Local Networks and Remote Networks text boxes, enter the list of local and remote subnets between which the bypass rules are applied. 

    If you enable these rules, data packets are exchanged between the specified local and remote IP sites even if their IP addresses are specified in the IPSec session rules. The default is to use the IPSec protection when data is exchanged between local and remote sites. These rules apply for all IPSec VPN sessions created within this IPSec VPN service.
11. Click Global Bypass Rules if you want to allow data packets to be exchanged between the specified local and remote IP addresses without any IPSec protection. In the Local Networks and Remote Networks text boxes, enter the list of local and remote subnets between which the bypass rules are applied. 

    If you enable these rules, data packets are exchanged between the specified local and remote IP sites even if their IP addresses are specified in the IPSec session rules. The default is to use the IPSec protection when data is exchanged between local and remote sites. These rules apply for all IPSec VPN sessions created within this IPSec VPN service.
12. Click Save. 

    After the new IPSec VPN service is created successfully, you are asked whether you want to continue with the rest of the IPSec VPN configuration. If you click Yes, you are taken back to the Add IPSec VPN Service panel. The Sessions link is now enabled and you can click it to add an IPSec VPN session.

After one or more IPSec VPN sessions are added, the number of sessions for each VPN service will appear in the VPN Services tab. You can reconfigure or add sessions by clicking the number in the Sessions column. You do not need to edit the service. If the number is zero, it is not clickable and you must edit the service to add sessions.

Use information in [Adding IPSec VPN Sessions](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions.html#GUID-b6d2027d-0bfb-4f1c-8825-aa676c3b6def-en) to guide you in adding an IPSec VPN session. You also provide information for the profiles and local endpoint that are required to finish the IPSec VPN configuration.