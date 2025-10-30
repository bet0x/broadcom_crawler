---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-nat-rule-for-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a NAT Rule for VPC
---

# Add a NAT Rule for VPC

You can add a NAT rule for a VPC for external IP binding for mapping between internal and external networks or for accessing the internet.

For creating a NAT rule for CTGW, consider the following conditions.

- DNAT rule should be configured at the nearest point to the translated IP, that is, the VPC.
- SNAT rule should be configured at the furthest point till the Match IP is visible - VPC for Private IP and CTGW for Project IP.

Perform the following steps to add a NAT rule for VPC.

1. On the Additional Configurations page, click Set in the NAT field.
2. Click Add NAT Rule.
3. Enter the following information.

   Field Name | Description || Name | Enter a NAT name. |
   | Action | Select an action. The following actions are available:  - SNAT - DNAT - Reflexive - NO SNAT - NO DNAT |
   | Source IP | Port | Enter the source network address and source port.  Specify an IP address, or an IP address range in CIDR format. For SNAT, NO\_SNAT and Reflexive rules, this is a required field and represents the source network of the packets leaving the network.  For DNAT and NO\_DNAT rules, optionally it can contain a source network of incoming packets.  For a NULL value, this field represents any network. |
   | Destination IP | Port | Enter a destination IP address or an IP address range in CIDR format and destination port.  For DNAT and NO\_DNAT rules, this is a required field and represents the source network of the packets leaving the network. This field is not applicable for Reflexive. |
   | Select Protocol | Select the required protocol. |
   | Translated IP | Port | Enter a value for translated IP. Specify an IPv4 address, or an IP address range in CIDR format. If translated IP is less than the match IP for SNAT it will work as PAT. |
   | Enabled | Turn on the toggle to enable the rule. |
   | Logging | Turn on the toggle to enable logging. |
   | Priority | A lower value means a higher priority. The default is 0. A No SNAT or No DNAT rule should have a higher priority than other rules. |
   | Firewall | The available settings are:  - Match External Address - The firewall will be applied to the external address of a NAT rule.    - For SNAT, the external address is the translated source address after NAT is done.   - For DNAT, the external address is the original destination address before NAT is done.   - For REFLEXIVE, to egress traffic, the firewall is applied to the translated source address after NAT is done. For ingress traffic, the firewall is applied to the original destination address before NAT is done. - Match Internal Address - Indicates the firewall will be applied to the internal address of a NAT rule.    - For SNAT, the internal address is the original source address before NAT is done.   - For DNAT, the internal address is the translated destination address after NAT is done.   - For REFLEXIVE, for egress traffic, the firewall is applied to the original source address before NAT is done. For ingress traffic, the firewall is applied to the translated destination address after NAT is done. - Bypass - The packet bypasses firewall rules. |
   | Description | Enter a description for NAT. |
   | Tag | Enter tag and scope for NAT. |
4. Click Save.