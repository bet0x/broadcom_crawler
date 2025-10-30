---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/network-address-translation-in-an-nsx-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Network Address Translation in an NSX VPC
---

# Network Address Translation in an NSX VPC

You
can add NAT rules with SNAT, DNAT, or Reflexive action in an NSX VPC.

The following functionality is currently not
supported for configuring NAT rules in an NSX VPC:

- Destination ports
- Translated ports
- Services
- No SNAT action
- No DNAT action

## Workflow for Adding NAT Rules in an NSX VPC

1. Select a project from the
   Project drop-down menu.
2. Click the
   VPCs tab, and then click
   VPC.
3. Expand the VPC details, and under
   the Network Services section, click the count next to
   NAT.
4. Click Add NAT
   Rule.
5. Enter a name for the NAT rule.
6. Select any one of these rule
   actions:
   - DNAT
   - SNAT
   - Reflexive
7. Depending on the action selected in
   the previous step, specify the IP address in the required fields.

   | Action | Required Fields | Notes |
   | --- | --- | --- |
   | DNAT | Destination IP and Translated IP | For destination IP address, only a single IPv4 address is currently supported. A CIDR block or a comma-separated IPv4 address list is not supported.  The destination IPv4 address must belong to the external IPv4 block of the NSX VPC and it must be available for allocation. |
   | SNAT | Translated IP | For translated IP address, only a single IPv4 address is currently supported. A CIDR block or a comma-separated IPv4 address list is not supported.  The translated IPv4 address must belong to the external IPv4 block of the NSX VPC and it must be available for allocation. |
   | Reflexive | Source IP and Translated IP | For translated IP address, only a single IPv4 address is currently supported. A CIDR block is not supported. |
8. By default, rule logging is
   deactivated. If you require rule logs for troubleshooting purposes, turn on the
   Logging option.
9. Specify a priority value. A lower
   value means a higher priority. The default is 0.
10. From the
    Firewall drop-down menu, select any one of these
    options:
    - Match Internal
      Address: This option is the default selection. It means
      that the N-S firewall rules in the NSX VPC will be applied to the internal address of a NAT
      rule.
      - For SNAT, the
        internal address is the original source address before NAT is
        done.
      - For DNAT, the
        internal address is the translated destination address after NAT
        is done.
      - For Reflexive, for
        egress traffic, the firewall is applied to the original source
        address before NAT is done. For ingress traffic, the firewall is
        applied to the translated destination address after NAT is
        done.
    - Match External
      Address: It means that the N-S firewall rules in the
      NSX VPC will be applied
      to the external address of a NAT rule.
      - For SNAT, the
        external address is the translated source address after NAT is
        done.
      - For DNAT, the
        external address is the original destination address before NAT
        is done.
      - For Reflexive, for
        egress traffic, the firewall is applied to the translated source
        address after NAT is done. For ingress traffic, the firewall is
        applied to the original destination address before NAT is
        done.
    - Bypass: It means that the packet bypasses
      the N-S firewall rules in the NSX VPC.
11. Click
    Save.