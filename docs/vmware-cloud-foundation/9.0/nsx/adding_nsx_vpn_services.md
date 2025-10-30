---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Adding NSX VPN Services
---

# Adding NSX VPN Services

You can add either an IPSec VPN
(policy-based or route-based) or an L2 VPN service using the NSX Manager user interface (UI).

The following sections provide information about the
workflows required to set up the VPN service that you need. The topics that follow these
sections provide details on how to add either an IPSec VPN or an L2 VPN service using
the NSX Manager UI.

## Policy-Based IPSec VPN Configuration Workflow

Configuring a policy-based IPSec VPN service workflow
requires the following high-level steps.

1. Create and enable an IPSec VPN
   service using an existing Tier-0 or Tier-1 gateway. Refer to [Add an NSX IPSec VPN Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html#GUID-fa3387e6-8188-4db8-913c-c1fa71b9db5a-en).
2. Create a DPD (dead peer detection)
   profile, if you prefer not to use the system default. Refer to [Add DPD Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-dpd-profiles.html#GUID-0847f7a4-8cd4-476b-b869-b92f80caf0a5-en).
3. To use a non-system default IKE
   profile, define an IKE (Internet Key Exchange) profile. Refer to [Add IKE Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ike-profiles.html#GUID-a2237c0f-5118-4758-87ae-af2e44c807e0-en).
4. Configure an IPSec profile using
   [Add IPSec Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ipsec-profiles.html#GUID-bac00336-8901-4f87-9f42-d63493d2aec7-en).
5. Use [Add Local Endpoints](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-local-endpoints.html#GUID-af6404f4-1d30-49a9-8752-0214143ca288-en) to create a
   VPN server hosted on the NSX Edge.
6. Configure a policy-based IPSec VPN
   session, apply the profiles, and attach the local endpoint to it. Refer to
   [Add a Policy-Based IPSec Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/add-a-policy-based-ipsec-session.html#GUID-b54c8bc3-155d-4776-ac8c-552fb895bf23-en).
   Specify the local and peer subnets to be used for the tunnel. Traffic from a
   local subnet destined to the peer subnet is protected using the tunnel
   defined in the session.
7. To get a representative
   configuration of VPN on the remote VPN endpoint, use the Download
   Configuration feature. This file contains parameters that
   come from the IPSec VPN session configured in step 6 and can be used to
   configure the remote endpoint of the VPN session. Refer to [Download the Remote Side IPSec VPN Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/download-the-remote-side-ipsec-vpn-configuration-file.html) for
   details.

## Route-Based IPSec VPN Configuration Workflow

A route-based IPSec VPN
configuration workflow requires the following high-level steps.

1. Configure and enable an IPSec VPN service using an
   existing Tier-0 or Tier-1 gateway. Refer to [Add an NSX IPSec VPN Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-an-ipsec-vpn-service.html#GUID-fa3387e6-8188-4db8-913c-c1fa71b9db5a-en).
2. Define an IKE profile if you prefer not to use the
   default IKE profile. Refer to [Add IKE Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ike-profiles.html#GUID-a2237c0f-5118-4758-87ae-af2e44c807e0-en).
3. If you decide not to use
   the system default IPSec profile, create one using
   [Add IPSec Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-ipsec-profiles.html#GUID-bac00336-8901-4f87-9f42-d63493d2aec7-en).
4. Create a DPD profile if you want to do not
   want to use the default DPD profile. Refer to [Add DPD Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles/add-dpd-profiles.html#GUID-0847f7a4-8cd4-476b-b869-b92f80caf0a5-en).
5. Add a local endpoint using
   [Add Local Endpoints](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/add-local-endpoints.html#GUID-af6404f4-1d30-49a9-8752-0214143ca288-en).
6. Configure a route-based IPSec VPN session, apply
   the profiles, and attach the local endpoint to the session. Provide a VTI IP
   in the configuration and use the same IP to configure routing. The routes
   can be static or dynamic (using BGP). Refer to [Add a Route-Based IPSec Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/add-a-route-based-ipsec-session.html#GUID-283768dd-af07-48cc-91fb-2fc169f4bf4f-en).
7. To get a representative configuration of VPN
   on the remote VPN endpoint, use the Download
   Configuration feature. This file contains parameters that
   come from the IPSec VPN session configured in step 6 and can be used to
   configure the remote endpoint of the VPN session. Refer to [Download the Remote Side IPSec VPN Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/download-the-remote-side-ipsec-vpn-configuration-file.html) for
   details.

## L2 VPN Configuration Workflow

Configuring an L2 VPN requires that you configure an L2
VPN service in Server mode and then another L2 VPN service in Client mode. You also
must configure the sessions for the L2 VPN server and L2 VPN client using the peer
code generated by the L2 VPN Server. Following is a high-level workflow for
configuring an L2 VPN service.

1. Create an L2 VPN Service in Server
   mode.
   1. Configure a route-based IPSec VPN tunnel with a
      Tier-0 or Tier-1 gateway and an L2 VPN Server service using that
      route-based IPSec tunnel. Refer to [Add an L2 VPN Server Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-server-service.html#GUID-7c30c658-2c66-44ae-93c7-81b508220a4f-en).
   2. Configure an L2 VPN server session, which binds
      the newly created route-based IPSec VPN service and the L2 VPN
      server service, and automatically allocates the GRE IP addresses.
      Refer to [Add an L2 VPN Server Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-server-session.html#GUID-0285324c-755a-4f29-9514-40678dd0f5d6-en).
   3. Add segments to the L2 VPN
      Server sessions. This step is also described in [Add an L2 VPN Server Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-server-session.html#GUID-0285324c-755a-4f29-9514-40678dd0f5d6-en).
   4. Use [Download the Remote Side L2 VPN Configuration File](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/download-the-remote-side-l2-vpn-configuration.html#GUID-9cea66af-4145-40af-ad6e-8c780d2b774b-en)
      to obtain the peer code for the L2 VPN Server service session, which
      must be applied on the remote site and used to configure the L2 VPN
      Client session automatically.
2. Create an L2 VPN Service in Client
   mode.
   1. Configure another route-based IPSec VPN service
      using a different Tier-0 or Tier-1 gateway and configure an L2 VPN
      Client service using that Tier-0 or Tier-1 gateway that you just
      configured. Refer to [Add an L2 VPN Client Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services/add-l2-vpn-service/add-an-l2-vpn-client-service.html#GUID-5c3e0c6b-6835-4a9e-95b0-6f4b329fcd5e-en)
      for information.
   2. Define the L2 VPN Client sessions by importing
      the peer code generated by the L2 VPN Server service. Refer to [Add an L2 VPN Client Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-client-session.html#GUID-db01896c-9282-4b8b-bdde-3881bc79ba62-en).
   3. Add segments to the L2 VPN
      Client sessions defined in the previous step. This step is described
      in [Add an L2 VPN Client Session](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-l2-vpn-sessions/add-an-l2-vpn-client-session.html#GUID-db01896c-9282-4b8b-bdde-3881bc79ba62-en).