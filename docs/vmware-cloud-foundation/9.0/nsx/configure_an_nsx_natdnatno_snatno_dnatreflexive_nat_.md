---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-address-translation/configure-an-nsx-nat.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX NAT/DNAT/No SNAT/No DNAT/Reflexive NAT 
---

# Configure an NSX NAT/DNAT/No SNAT/No DNAT/Reflexive NAT

You can configure different types of
NAT for IPv4 on a tier-0 or tier-1 gateway.

If there is a service configured in this
NAT rule, the translated\_port will be realized on NSX Manager as the
destination\_port. This means the service will be the translated port while the
translated port is used to match the traffic as destination port. If there is no
service configured, the port will be ignored.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingNAT.
3. From the
   View drop-down menu, select
   NAT.
4. Click Add NAT Rule.
5. Enter a Name.
6. Select an action. 

   Gateway | Available Actions || Tier-1 gateway | Available actions are SNAT, DNAT, Reflexive, NO SNAT, and NO DNAT. |
   | Tier-0 gateway in active-standby mode | Available actions are SNAT, DNAT, NO SNAT, and NO DNAT. |
   | Tier-0 gateway in active-active mode | The available action is Reflexive. |
7. In the Source
   IP field, enter the source network address. 

   Specify an IP address, or an IP address range in CIDR format. For
   SNAT, NO\_SNAT and
   Reflexive rules, this is a required field and
   represents the source network of the packets leaving the network.

   For DNAT and NO\_DNAT rules,
   optionally it can contain source network of incoming packets.

   For a NULL value, this field represents any network.
8. Enter a Destination. 

   Specify an IP address, or an IP address range in CIDR format. For
   DNAT and NO\_DNAT rules, this
   is a required field and represents the source network of the packets leaving the
   network. This field is not applicable for
   Reflexive.
9. Enter a value for Destination
   Port.
10. Enter a value for Translated IP. 

    Specify an IPv4 address, or an IP address range in CIDR format. If translated
    IP is less than the match IP for SNAT it will work as PAT.
11. From the
    Select
    Service drop-down menu, select a service, which has an
    associated port number.

    If there is a service interface configured in a NAT rule,
    translated\_port will be realized on NSX Manager as
    destination\_port. This means that the service will be
    the translated port while the translated port is used to match the traffic as
    destination port. If there is no service configured, the port will be
    ignored.
12. For Apply To, click
    Set and select objects that this rule applies to. 

    The available objects are
    Tier-0
    Gateways, Interfaces,
    Labels, Service Instance
    Endpoints, and Virtual
    Endpoints.

    If you are using
    NSX Federation and
    creating a NAT rule from a Global Manager appliance, you can select site-specific IP
    addresses for NAT. You can apply the NAT rule to any of the following
    location spans:
    - Do not click
      Set if you want to use the default option
      of applying the NAT rule to all locations.
    - Click
      Set. In the Applied To | New
      Rule dialog box, select the locations whose entities
      you want to apply the rule to and then click
      Apply.
    - Click
      Set. In the Applied To | New
      Rule dialog box, select a location and then select
      Interfaces from the
      Categories drop-down menu. You can select
      specific interfaces to which you want to apply the NAT rule.
    - Click
      Set. In the Applied To | New
      Rule dialog box, select a location and then select
      VTI from the
      Categories drop-down menu. You can select
      specific VTIs to which you want to apply the NAT rule.
13. Toggle the
    Enabled field to Yes.
14. Select a firewall setting. 

    The available settings are:
    - Match External
      Address - The firewall will be applied to external
      address of a NAT rule.
      - For SNAT, the
        external address is the translated source address after NAT is
        done.
      - For DNAT, the
        external address is the original destination address before NAT
        is done.
      - For REFLEXIVE, to
        egress traffic, the firewall is applied to the translated source
        address after NAT is done. For ingress traffic, the firewall is
        applied to the original destination address before NAT is
        done.
    - Match Internal
      Address - Indicates the firewall will be applied to
      internal address of a NAT rule.
      - For SNAT, the
        internal address is the original source address before NAT is
        done.
      - For DNAT, the
        internal address is the translated destination address after NAT
        is done.
      - For REFLEXIVE, for
        egress traffic, the firewall is applied to the original source
        address before NAT is done. For ingress traffic, the firewall is
        applied to the translated destination address after NAT is
        done.
    - Bypass
       - The packet bypasses firewall rules.
15. Toggle the
    Logging button to enable logging.
16. Specify a priority value. 

    A lower value means a higher priority. The
    default is 0. A No SNAT or No DNAT
    rule should have a higher priority than other rules.
17. Apply to Policy Based
    VPN: Applies only for the DNAT or
    No DNAT rule category. The rule is applied based on
    the priority value. Despite the Bypass or
    Match settings, the settings applied for the
    Apply To parameter of a NAT policy are still
    honored.
    - Bypass: NAT Rule is not applied to the traffic
      decrypted from a policy-based IPSec VPN tunnel. This is the default setting.
    - Match: If the traffic is decrypted from a
      policy-based IPSec VPN tunnel, the NAT policy is evaluated and matched. NAT
      policy is NOT evaluated on the traffic that is not decrypted from a
      policy-based IPSec VPN tunnel.

    For a NAT policy to hit the decrypted traffic, the policy must be set to
    Match and the interface where encrypted traffic is
    sent/received must be set in the Apply To parameter of
    the NAT policy. For more information on the Apply To
    parameter, see [Network Address Translation (NAT)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-address-translation.html#GUID-b25a100b-666f-4dd5-a0b9-fe7babb97f35-en).
18. Click Save.