---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/tier-0-vrf-gateways/inter-vrf-routing/configure-inter-vrf-route-advertisement.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an NSX Inter-VRF Route Advertisement
---

# Configure an NSX Inter-VRF Route Advertisement

With Inter-VRF Route Advertisement, you can configure advertisement rules to advertise routes and prefixes on connected gateway to create inter-VRF routing between two VRFs.

Ensure that the IP prefix list is created, see [Create an IP Prefix List](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/create-an-nsx-ip-prefix-list.html#GUID-7e7229d2-780a-4c00-8c40-a9f929cbcefd-en_GUID-F32EB987-1AF3-45AD-865E-505E81857165).

Inter-VRF forwarding is enabled when Inter-VRF routing is configured on either end between two Tier-0 VRFs or between a Tier-0 VRF gateway and its Tier-0 gateway.

![Inter-VRF Routing Topology](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0b5dc783-3912-4da5-bc57-5a0a2873b75d.original.png)

Configuration workflow:

![Configuration workflow for the sample topology](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e4f95a19-6c37-47bf-a396-5b6014b324f0.original.png)

You can enable Inter-VRF Route Advertisement by configuring:

- Connect Gateway - To attach the Target VRF to source.
- Set Advertisement Out Rules - To advertise the connected subnets of the source to the target VRF. You can allow or deny the subnets that you want to advertise to the target VRF i.e., you want the target VRF to learn.
- Set In Filter Prefix Lists - To select prefixes that you want to accept or deny from the target VRF.

NSX assigns an IPv4 and IPv6 address to each Tier-0 VRF gateway and Tier-0 gateway. IPv4 subnet is configured in the Inter VRF Transit Subnet field of the default Tier-0. For assigning IPv6 addresses to Inter-VRF interfaces, NSX allocates one IPv6 subnet. A /64 IPv6 subnet is allocated from the Tier-1-Tier-0 transit subnets configured on the default Tier-0.

1. With admin privileges, log in to NSX Manager.
2. Connect Gateway:
   1. Select Networking.
   2. Select either the default/parent Tier-0 gateway or the Tier-0 VRF gateway, which you would like to configure.
   3. Click on the ellipsis button (three dots) and select Edit.
   4. Click Routing.
   5. Click Set next to Inter VRF Routing.
   6. Click Add Inter VRF Routing.
   7. In Connected Gateway, select the target VRF from the drop-down menu.
   8. Click Save.

      Wait for the Status to change to ‘Success’.
3. Set Advertisement Out Rules:
   1. Click on the ellipsis button (three dots) and select Edit.
   2. Click Set below Advertisement Out Rules.
   3. Click Add Advertisement Out Rules.

      - Enter Name - Requires validation for Name.
      - Enter Subnets - Specify subnets that are used to assign addresses to logical links connecting parent Tier-0 and child Tier-0 VRF.

        Leave the Subnet field blank to set it as 'any'. If subnet is 'any', Route Advertisement Type filters must be applied.
      - Apply filter – Click on the (i) icon for more information about it. Toggle to 'Yes' if you would like to apply the filters.

        Disable the filters to advertise the configured aggregate prefix subnets.
      - Advertisement Action - Action to advertise filtered routes to the connected Tier0 gateway.
        - Allow: Enables the advertisement
        - Deny: Disables the advertisement
      - Prefix Operator - Prefix operator to filter subnets.
        - GE prefix operator: Filters all the routes with prefix length greater than or equal to the subnets configured.
        - EQ prefix operator: Filters all the routes with prefix length equal to the subnets configured.

        Prefix operation is ignored if no route advertisement type is specified.
      - Select route advertisement types to be filtered.
   4. Click Save.

      Wait for the Status to change to ‘Success.’
4. Set In Filter Prefix Lists:
   1. Click on the ellipsis button (three dots) and select Edit.
   2. Click Set below In Filter Prefix Lists
   3. Click  Add In Filter Prefix Lists.
   4. Select the Prefix List that you had created in IP Prefix Lists window.
   5. Click Add.
   6. Click Save.

      Wait for the Status to change to ‘Success’.

   You may also download the advertised routes, by selecting Download Advertised Network from the ellipsis menu (three dots) next to the configured target VRF.