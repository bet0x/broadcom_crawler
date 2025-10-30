---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/attribute-types/fqdn.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > FQDNs
---

# FQDNs

A fully qualified domain name (FQDN) is the complete domain name for a specific host on the Internet. FQDNs are used in firewall rules to allow or reject traffic going to specific domains.

The FQDN attribute type is used in distributed firewall FQDN Filtering policies, as described in the [VMware vDefend documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html). NSX supports custom FQDNs that are defined by an administrator in addition to the pre-defined list of FQDNs. Custom FQDN supports the following:

- FQDN supports processing of DNS response record packets containing canonical names (CNAMEs).
- Full FQDN names such as maps.google.com or myapp.corp.com
- Partial REGEX with \* at the beginning only such as \*eng.northpole.com or \*yahoo.com
- FQDN name length up to 64 characters
- FQDN names must end with the registered top level domain (TLD) such as .com, .org, or .net

When creating a custom FQDN, using a wildcard domain is best practice. For example, using \*.example.com, would include sub domains such as americas.example.com and emea.example.com. Using example.com, would not include any sub domains.

Custom FQDNs do not support custom top level domain names, such as www.example.john.

1. From your browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address>.
2. Select InventoryProfiles.
3. Select Security  Profiles.
4. Select the Attribute Types tab, and FQDNs.

   A table of system-generated FQDNs appears.
5. Select ActionsAdd FQDN.
6. Enter the domain name in form \*[hostname].[domain]. For example, \*abracadabra.com

   Do not include http:// or any other header.
7. Click Save. 

   The user-defined FQDN is shown in the table of available FQDNs, with User in the Created By column.
8. To display a subset of FQDNs, click Filter by Name, Path and more and select Created by or Domain.

FQDNs can be used in context profiles for distributed firewall rules.