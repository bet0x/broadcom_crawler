---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-address-translation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Network Address Translation (NAT)
---

# Network Address Translation (NAT)

Network address translation (NAT) maps one IP address space to another. You can configure NAT on tier-0 and tier-1 gateways.

- Source NAT (SNAT) - translates a source IP address of outbound packets so that packets appear as originating from a different network. Supported on tier-0/tier-1 gateways running in active-standby mode. For one-to-one SNAT, the SNAT translated IP address is not programmed on the loopback port, and there is no forwarding entry with an SNAT translated IP as the prefix. For n-to-one SNAT, the SNAT translated IP address is programmed on the loopback port, and users will see a forwarding entry with an SNAT-translated IP address prefix. NSX SNAT is designed to be applied to traffic that egresses the NSX environment.
- Destination NAT (DNAT) - translates the destination IP address of inbound packets so that packets are delivered to a target address into another network. Supported on tier-0/tier-1 gateways running in active-standby mode. NSX DNAT is designed to be applied to traffic that ingresses the NSX environment.
- Reflexive NAT - (sometimes called stateless NAT) translates addresses passing through a routing device. Inbound packets undergo destination address rewriting, and outbound packets undergo source address rewriting. It is not keeping a session as it is stateless. Supported on tier-0 gateways running in active-active or active-standby mode, and on tier-1 gateways.
- Stateful NAT services are supported when using Stateful Active-Active HA mode on the T0 or T1 Gateway.

You can also disable SNAT or DNAT for an IP address or a range of addresses (No-SNAT/No-DNAT). If an address has multiple NAT rules, the rule with the highest priority is applied.

If there is a service configured in a DNAT rule, translated\_port will be realized on NSX Manager as destination\_port. This means that the service will be the translated port while the translated port is used to match the traffic as destination port. If there is no service configured, the port will be ignored.

If you are creating a NAT rule from a Global Manager in an NSX Federation environment, you can select site-specific IP addresses for NAT. Note the following:

- Do not click Set under Apply To if you want the default option of applying the NAT rule to all locations.
- Under Apply To, click Set and select the locations whose entities you want to apply the rule to and then select Apply NAT rule to all entities.
- Under Apply To, click Set, select a location and then select Interfaces from the Categories drop-down menu. You can select specific interfaces to which you want to apply the NAT rule.
- SNAT configured on a tier-0 gateway's external interface processes traffic from a tier-1 gateway, and from another external interface on the tier-0 gateway.
- NAT is configured on the uplinks of the tier-0/tier-1 gateways and processes traffic going through this interface. This means that tier-0 gateway NAT rules will not apply between two tier-1 gateways connected to the tier-0.

## NAT Support Matrices

Configuration Fields

| **Rule Type** | **Match** | | | **Translated IP | Port** | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Source IP** | **Destination IP** | **Port** | **Translated IP** | **Service protocol** | **Service source port** | **Service destination port** |
| **SNAT** | Optional | Optional | Optional (is used to match destination port) | Required | Optional | Optional (match as source port) | Optional (setting is ignored) |
| **DNAT** | Optional | Required | Optional (is used to match destination port) | Required | Optional | Optional (match as source port) | Optional (use as translated port) |
| **NO\_SNAT** | Required | Optional | Optional (is used to match destination port) | N/A | Optional | Optional (match as source port) | Optional (setting is ignored) |
| **NO\_DNAT** | Optional | Required | Optional (is used to match destination port) | N/A | Optional | Optional (match as source port) | Optional (setting is ignored) |
| **REFLEXIVE** | Required | N/A | N/A | Required | N/A | N/A | N/A |
| **NAT64** | Optional (IPv6) | Required (IPv6) | Optional (is used to match destination port) | Required (IPv6) | Required | Optional (match as source port) | Optional (setting is ignored) |

Configuration Use Cases

| **Types** | **1:1** | **n:n** | **n:m** | **n:1** | **1:m** |
| --- | --- | --- | --- | --- | --- |
| **SNAT** | Yes | Yes | Yes | Yes | No |
| **DNAT** | Yes | Yes | N/A | Yes | N/A |
| **NO\_SNAT** | - | - | - | - | - |
| **NO\_DNAT** | - | - | - | - | - |
| **REFLEXIVE** | Yes | Yes | N/A | No | No |
| **NAT64** | Yes | Yes | No | Yes | No |

NAT Traffic Flow Support on Interfaces

The following support matrix refers to rules applied to any object type.

| **Traffic Flow Support on Interfaces** | **DNAT** | **SNAT** | **NO\_DNAT** | **NO\_SNAT** | **REFLEXIVE** | **NAT64** |
| --- | --- | --- | --- | --- | --- | --- |
| **Inter-VRF → Uplink** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Inter-VRF → Downlink** | Yes | No | Yes | No | Yes | Yes |
| **Downlink → Inter-VRF** | No | Yes | No | Yes | Yes | No |
| **Uplink → Inter-VRF** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Uplink/External → Uplink/External** | Yes | Yes | Yes | Yes | Yes | Yes |
| **External (Uplink) → Connected Segment (Downlink)** | Yes | No | Yes | No | Yes | Yes |
| **Uplink → Service Interface** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Backplane → Backplane** | No | No | No | No | No | No |
| **Downlink → Uplink** | No | Yes | No | Yes | Yes | No |
| **Downlink → Service Interface** | No | Yes | No | Yes | Yes | No |
| **Service Interface → Service Interface** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Service Interface → Uplink** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Service Interface → Downlink** | Yes | No | Yes | No | Yes | Yes |