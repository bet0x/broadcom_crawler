---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overview-of-federation/features-supported-in-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Features and Configurations Supported in NSX Federation
---

# Features and Configurations Supported in NSX Federation

This page describes the features and configurations supported in NSX Federation.

## Configuration Maximums

An NSX Federation environment has the following configuration maximums:

- For most configurations, the Local Manager cluster has the same configuration maximums as an NSX Manager cluster. Go to [VMware Configuration Maximums tool](https://configmax.vmware.com/home) and select NSX.

  Select the NSX Federation category for NSX in the [VMware Configuration Maximums tool](https://configmax.vmware.com/home) for exceptions and other NSX Federation-specific values.
- For a given location, the following configurations contribute to the configuration maximum:
  - Objects that were created on the Local Manager.
  - Objects that were created on the Global Manager and include the location in its span.

  You can view the capacity and usage on each Local Manager. See View the Usage and Capacity of Categories of Objects in the NSX Administration Guide.

  You can view the capacity and usage on each Local Manager. See View the Usage and Capacity of Categories of Objects in the NSX Administration Guide.

## Feature Support

Note that in NSX Federation, Service insertion (Network Introspection) support only occurs when an NSX Federation environment has a Global Manager (GM) deployed under the following conditions:

- All service-insertion related configuration such as partner service registration, deployment and consumption, is done from a Local Manager (LM).
- Only objects configured on the LM are used with service insertion. This includes groups, segments, and any other constructs. Service insertion cannot be applied to workloads connected to a stretched/global segment defined from the GM, or any segment connected to a logical router created from the GM. Groups created from the Global Manager should not be used within service insertion redirection polices.

- NSX Federation locations must run on environments where administrators have full control of the underlay fabric.
- NSX Federation does not currently support Global Manager and Local Manager hosted on VMware Cloud on AWS, VMware Cloud on Dell, Azure VMware Solution, Google Cloud VMware Engine, Oracle Cloud VMware Solution, or Alibaba VMware Cloud Service.

After Local Manager is registered to Global Manager:

- You can continue to configure on Local Manager. For more details, refer to [Understanding NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overview-of-federation/understanding-federation.html).
- Some objects configured from Local Manager can have options/settings that are Global Manager objects. For example, you can plug in an LM\_created-t1 to a GM\_created-t0.
- Some objects configured from Local Manager cannot be configured with options/settings that are Global Manager objects. For example, you cannot plug in an LM\_created-segment to a GM\_created-t0. Note that you can only edit those LM-objects from Local Manager; Global Manager does not see those object. For more information, refer to "Logical Configuration Ownership" in the NSX-T Multi-Location Design Guide for your release.

The Features Supported in NSX Federation table describe the features available in Global Manager.

Features Supported in NSX Federation



| Feature | Details | Related Links |
| --- | --- | --- |
| Tier-0 Gateway | - Active-active and active-standby. - Active-active only | [Add a Tier-0 Gateway from Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/add-a-tier-0-gw-from-gm.html#GUID-a5ac6be0-6092-4d6e-83fb-043ce1b18bf1-en) |
| Tier-1 Gateway |  | [Add a Tier-1 Gateway from Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/create-tier-1-from-gm.html#GUID-9fa61957-df5f-456c-a456-f2c7ae1b54bf-en) |
| Segments | You can include Layer 2 bridge configuration from Global Manager. | [Add a Segment from Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/add-a-segment-from-global-manager.html#GUID-00ba31b0-9deb-4f86-ac3f-21268c4ac55f-en) and [Configure Bridging on Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/networking-topologies-in-nsx-federation/configure-bridging-on-global-manager.html) |
| Groups | Some limitations. See [Security in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/security-in-nsx-federation.html#GUID-cb5d2ea0-af69-4780-882b-2f990ac1a737-en). | See the section on creating groups from Global Manager in the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). |
| Distributed Firewall | Drafts of the security policies are now available on Global Manager. This includes support for auto and manual drafts. | See the section on creating drafts in Global Manager in the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). |
| Firewall Exclusion List | Available. | See the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). |
| Time Based Firewall Rules | Available. | See the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). |
| Gateway Firewall | Only Layer 3 and 4 rules are supported. | See the section on creating gateway policies and rules from Global Manager in the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). |
| Network Address Translation (NAT) | 1. Tier-0 Gateway:    - Active-active: You can configure stateless NAT only, that is, with action type Reflexive.    - Active-standby: You can create stateful or stateless NAT rules. 2. Tier-1 Gateway:    - You can create stateful or stateless NAT rules.    - Stateless NAT rules are pushed to all locations in the gateway's span unless scoped to one or more locations specifically.    - Stateful NAT rules are also pushed to all locations in the gateway's span or to the specific location selected. However, stateful NAT rules are realized and enforced only on the primary location. | [Configure an NSX NAT/DNAT/No SNAT/No DNAT/Reflexive NAT](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-address-translation/configure-an-nsx-nat.html#GUID-ee9c98e4-8201-4717-b77d-29106f0d464a-en) |
| DNS |  | See [Add an NSX DNS Forwarder Service](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/ip-address-management-ipam/add-an-nsx-dns-forwarder-service.html#GUID-9caf74cd-1134-4cc4-b904-af01050a680f-en) |
| DHCP and SLAAC | - DHCP Relay is supported on segments and gateways. - DHCPv4 server is supported on gateways with DHCP static bindings configured on segments. - You can assign IPv6 addresses using SLAAC with DNS Through RA (DAD detects duplicates within a location only). | - DHCP Relay: [Add an NSX DHCP Relay Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-relay-profile.html#GUID-8acd5bf1-2b75-4464-af97-a1c9db0a2ca9-en) - DHCP Server (supported on gateway only):   - [Add an NSX DHCP Server Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-server-profile.html#GUID-603e15a2-fd38-4d70-b646-c8c7534fccc2-en)   - [Attach an NSX DHCP Profile to a Tier-0 or Tier-1 Gateway](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/attach-an-nsx-dhcp-profile-to-a-tier-0-or-tier-1-gateway.html#GUID-462ad8dc-8a84-40a4-9186-ba183bc07a32-en)   - [NSX DHCP Configuration Settings: Reference](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html) - IPv6 address assignment: [Create NSX SLAAC and DAD Profiles for IPv6 Address Assignment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-slaac-and-dad-profiles-for-ipv6-address-assignment.html#GUID-630f2f84-3827-4936-aea4-2722b1046614-en) |
| Distributed Malware Detection and Prevention | Starting with NSX 4.1.2:  - Deploy NSX Application Platform (NAPP) on each federated Local Manager. - Deploy and manage Malware Prevention from the Local Manager UI. - You can use stretched and non-stretched segments for the virtual machine endpoints. | See the section on Malware Prevention for vDefend in the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). |
| Network Detection and Response | Starting with NSX 4.1.2:  - Deploy NAPP on each federated Local Manager. - Deploy and manage vDefend Network Detection and Response (NDR) from the Local Manager UI. - You can use stretched and non-stretched segments to collect NDR events. | For more details about Network Detection and Response, see the [VMware vDefend ATP](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-atp/9-0.html) documentation. |
| Using objects created on Global Manager in a Local Manager configuration | 1. Most configurations are supported. For example:    - Connecting a Local Manager tier-1 gateway to a Global Manager tier-0 gateway.    - You can use a Global Manager group in a Local Manager distributed firewall rule. 2. These configurations are not supported:    - Connecting a Local Manager segment to a Global Manager tier-0 or tier-1 gateway.    - Connecting a load balancer to a Global Manager tier-1 gateway. |  |
| Network Monitoring | - Expanded communication monitoring between Local Manager and Global Manager. - Traceflow across NSX instances in the same Federation. |  |
| Certificates | Starting with NSX 4.1, Local Manager self-signed certificates generate only when the Local Manager is in the NSX Federation environment. That same certificate gets deleted if Local Manager moves out of the NSX Federation environment. | [Certificates for NSX and NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html) |
| LDAP | Authenticate Global Manager users using a directory service such as Active Directory over LDAP or OpenLDAP. | [Integration with LDAP](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-ldap.html) |
| Backup and Restore | Backup with FQDN or IP is supported. | [Backup and Restore in NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/backup-and-restore-in-nsx-federation.html#GUID-65489aec-72d1-43f5-b419-3073bba66a2c-en) |
| Users | Starting with NSX 4.1, you can add new local users and remove audit and guest users. | [Manage Local User Accounts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/managing-local-user-accounts/manage-local-user-account.html) |
| vMotion between locations | Tag replication across locations is supported. |  |