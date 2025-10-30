---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-an-nsx-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an NSX VPC
---

# Add an NSX VPC

NSX VPC provides an isolated space for application owners to host applications and consume networking and security objects by using a self-service consumption model.

You must be assigned any one of these roles:

- Project Admin
- Enterprise Admin

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Expand the Project drop-down menu, and then select the project where you want to add an NSX VPC.
3. Click the VPCs tab, and then click Add VPC.
4. Enter a name for the NSX VPC.
5. Select a tier-0 or a tier-0 VRF gateway that the workloads in the NSX VPC can use for north-south connectivity outside this VPC.

   This drop-down menu displays only those tier-0 or tier-0 VRF gateways that were assigned to the project when the project was created.

   If no gateway is selected, the workloads in the NSX VPC will not have north-south connectivity.
6. Configure the IP Assignment settings. 
   1. In the External IPv4 Blocks field, select the IPv4 blocks that the system can use for public subnets in the NSX VPC.

      The external IP blocks that are assigned to the project are available for selection in the NSX VPC. These IPv4 blocks must be routable from outside the NSX VPC. You can assign a maximum of five external IPv4 blocks to each NSX VPC in a project.

      The selected external IPv4 blocks are used for public subnets only when the IP Assignment option is set to Automatic during the subnet creation.
   2. In the Private IPv4 Blocks field, select the IPv4 blocks that the system can use for private subnets in this NSX VPC.

      The IPv4 blocks that are added in the project with visibility set to Private are available for selection in the NSX VPC.

      If no IPv4 blocks are available for selection, click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png), and then click Create New to add a private IPv4 block.

      The selected private IPv4 blocks are used for private subnets only when the IP Assignment option is set to Automatic during the subnet creation.

      You must select either external IPv4 blocks or private IPv4 blocks, or both. If neither of them are selected, an error message is displayed when you save the NSX VPC.
   3. Under DHCP, select any one of these options.

      | Option | Description |
      | --- | --- |
      | Managed by NSX Policy Management | Default option. The system configures a Segment DHCP server for each subnet in the NSX VPC. The DHCP server dynamically assigns IP addresses to the workload VMs that are connected to the subnets in the NSX VPC. |
      | External | The system uses external or remote DHCP servers to dynamically assign IP addresses to the workload VMs that are connected to the subnets in the NSX VPC. You can specify the IP address of external DHCP servers in the DHCP relay profile that you select for the NSX VPC.  Workloads on only public VPC subnets can receive IP addresses from the external DHCP server. Currently, workloads on private VPC subnets cannot receive IP addresses from the external DHCP server unless the DHCP server itself is connected to the private or public VPC subnet.  In the DHCP Relay Profile drop-down menu, select an existing relay profile. If no DHCP relay profile is available, click Actions menu. to create a new DHCP relay profile.  For more information about adding a DHCP relay profile, see [Add an NSX DHCP Relay Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-an-nsx-dhcp-profile/add-an-nsx-dhcp-relay-profile.html#GUID-8acd5bf1-2b75-4464-af97-a1c9db0a2ca9-en).  The configuration of the external DHCP servers is not managed by NSX. |
      | None | System does not configure DHCP for the subnets in the NSX VPC  In this case, you must manually assign IP addresses to the workload VMs that are connected to the subnets in the NSX VPC. |
7. If DHCP configuration is managed by NSX, you can optionally enter the IP address of the DNS servers.

   When not specified, no DNS is assigned to the workloads (DHCP clients) that are attached to the subnets in the NSX VPC.
8. Configure the Services Settings.
   1. By default, the N-S Services option is turned on. If required, you can turn it off.

      When this option is turned on, it means that a service router is created for the connected subnets to support centralized services such as N-S firewall, NAT, or gateway QoS profile.

      When this option is turned off, only distributed router is created.

      After an NSX VPC is realized in the system, preferably avoid turning off the N-S Services option. The reason is that the centralized services will not be enforced on the subnets of the NSX VPC. For example, services such as N-S firewall, NAT, and so on, will not be enforced even if they are configured in the NSX VPC.
   2. From the Edge Cluster drop-down menu, select an edge cluster to associate with the NSX VPC.

      If the project does not have edge clusters assigned to it, this drop-down menu will be empty. Ensure that you have allocated at least one edge cluster to the project for it to be available for selection when adding an NSX VPC.

      The selected edge cluster is consumed for running centralized services in the NSX VPC such as NAT, DHCP, and N-S firewall. These services require an edge cluster to be associated with the NSX VPC.

      If DHCP is set to None and N-S Services option is turned off, then edge cluster is optional.
   3. By default, the Default Outbound NAT option is turned on. If required, you can turn it off.

      This option is available only when the N-S Services option is turned on for the NSX VPC.

      When Default Outbound NAT is turned on, it means that traffic from the workloads on the private subnets can be routed outside the NSX VPC. System automatically creates one default SNAT rule for the NSX VPC. The translated IP for the SNAT rule is taken from the external IPv4 block of the NSX VPC.

      After an NSX VPC is realized in the system, preferably avoid turning off the Default Outbound NAT option. The reason is that the workloads on the private subnets will no longer be able to communicate outside the NSX VPC.
   4. Use the Activate Default E-W Firewall Rules toggle to specify whether you want to turn on or off the default east-west firewall rules for this NSX VPC.

      The default east-west firewall rules allow all outgoing traffic from the workloads that are connected to the subnets in the NSX VPC and drops all incoming traffic to the VPC.

      This toggle is editable only when you apply an appropriate security license in your NSX deployment that entitles the system to distributed firewall security feature. This setting only turns on/off the default E-W firewall rules for the NSX VPC. It does not turn off the E-W firewall in the NSX VPC.

      For instance, if distributed firewall service is activated in your NSX platform, you can still deactivate the default E-W firewall rules of the NSX VPC. In this case, the system-wide default distributed firewall rules that are configured in the default space and the default distributed firewall rules that are configured in the project will be applied to the NSX VPC.

      The following table explains the default state of the Activate Default E-W Firewall Rules toggle in the NSX VPC under various scenarios. The term "base license" refers to the VMware Cloud Foundation (VCF) license.

      | Sr. No. | Scenario | Default State of the Toggle | Notes |
      | --- | --- | --- | --- |
      | 1 | You are a new NSX customer and have applied a base license that entitles the system to only the NSX networking features. | Off | This toggle is not editable because the current applied license does not support configuration of east-west (distributed) firewall security rules.  You need to apply the appropriate security license in the system, and then turn on this toggle to activate the default E-W firewall rules in the NSX VPC. |
      | 2 | You are a new NSX customer. On day 0, you have applied a base license that entitles the system to NSX networking features. You have also applied an appropriate security license that entitles the system to distributed firewall security. | On | The default E-W firewall rules are activated for the NSX VPC.  You can turn it off, if required. |
      | 3 | You are a new NSX customer. On day 0, you applied only the base license that entitles the system to only the NSX networking features. You have added some NSX VPCs in the system, let us say, VPCs A and B  Later, during day 2 operations, you applied an appropriate security license that entitles the system to distributed firewall security.  Now, you added user-defined E-W firewall rules in the existing VPCs A and B, and also created new VPCs in the project, let us say, VPCs C and D. | Off: for pre-existing VPCs in the project  On: for new VPCs in the project | In this scenario, the term "pre-existing VPCs" refers to NSX VPCs that existed in the project before the security license was applied on day 2. In this scenario, they refer to VPCs A and B. The term "new VPCs" refers to NSX VPCs that are added in the project after the security license was applied on day 2. In this scenario, they refer to VPCs C and D.  For pre-existing VPCs A and B, the system behavior is as follows:  This toggle will be in the Off state, by default. The user-defined E-W rules are effective in VPCs A and B. If you want to activate the default E-W rules in these VPCs, open these VPCs in the edit mode, and turn on this toggle manually. However, when turned on, it might impact the behavior of east-west traffic in VPCs A and B.  For new VPCs C and D, the system behavior is as follows:  This toggle will be in the On state by default. That is, for VPCs C and D, the default E-W rules are activated, by default. If required, you can turn it off so that only the user-defined E-W rules are effective in these VPCs. |
      | 4 | You are an existing NSX customer with a supported legacy NSX license that entitles your system to full DFW access.  After the supported legacy license expires, you apply a base license that entitles your system to NSX networking features, and also apply a security license that entitles your system to distributed firewall security. | On | The default E-W firewall rules and user-defined E-W firewall rules continue to run in existing VPCs that you created before changing to the new license. There is no change in the system behavior.  For all new VPCs that you add after changing the license, this toggle is turned on, by default. You can turn it off, if required. |
      | 5 | You are an existing NSX customer with a supported legacy NSX license that entitles your system to full DFW access. You have added two NSX VPCs in the system, let us say, VPCs A and B.  After the supported legacy license expires, you apply the base license that entitles your system to only the NSX networking features. A new security license is not applied.  Now, you have created two new NSX VPCs in the system, let us say, VPCs C and D. | On: for pre-existing VPCs in the project  Off: for new VPCs in the project | In this scenario, the term "pre-existing VPCs" refers to NSX VPCs that were added in the system when the legacy NSX license was valid. In this scenario, they refer to VPCs A and B. The term "new VPCs" refers to NSX VPCs that are added in the system after the base license was applied. In this scenario, they refer to VPCs C and D.  For pre-existing VPCs A and B, the system behavior is as follows:  This toggle is in the On state, by default. You can turn it off, if needed. But, this action is not reversible. That is, you cannot activate the default E-W firewall rules again in VPCs A and B.  The default E-W firewall rules and user-defined E-W firewall rules continue to run in VPCs A and B. But, you cannot edit these rules. Neither, you can add new E-W firewall rules. But, you can delete the existing user-defined firewall rules.  To have a full access to the distributed firewall rules, you need to apply an appropriate security license.  For new VPCs C and D, the system behavior is as follows:  This toggle is in the Off state, by default. You cannot turn it on because the current applied license does not entitle the system to the distributed firewall feature. |
      | 6 | You are a new NSX customer and your system has entered an Evaluation mode, which is valid for 60 days. | Off | During the evaluation period of a new NSX deployment, the system is entitled to only the networking features. The security features are not entitled. |
   5. If you want the NSX VPC to be discovered by the Avi Load Balancer Controller, turn on the Enable for Avi Load Balancer option.

      By default, this option is turned off. When it is turned on, it provides the ability to extend NSX multi-tenancy to Avi Load Balancer Controller and hence enables load balancer configuration in this context.

      You can turn on this option only when the following conditions are met:
      - At least one private IP address block is assigned to the NSX VPC.
      - At least one edge cluster is assigned to the NSX VPC.

      NSX VPC requires a private IP block because the load balancer virtual service IP (VIP) needs to be on a private subnet. An edge cluster is required so that the Avi Load Balancer Service Engines can receive IP addresses dynamically from the DHCP server.

      To learn more about Avi Load Balancer, see the [VMware Avi Load Balancer Documentation](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer.html).
9. Optionally, attach the following profiles that will be used by the subnets in the NSX VPC:

   - N-S Egress Quality of Service (QoS) profile
   - N-S Ingress QoS profile
   - IP Discovery profile
   - SpoofGuard profile
   - Mac Discovery profile
   - Segment Security profile
   - QoS

   To learn about the purpose of these profiles, see [Segment Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles.html#GUID-10670c86-8c61-4422-b18a-6014002b2cc1-en).
10. In the Short log identifier text box, enter a string that the system can use to identify the logs that are generated in the context of the NSX VPC.

    This identifier must be unique across all NSX VPCs. The identifier must not exceed eight alphanumeric characters.

    If the identifier is not specified, the system autogenerates it when you save the NSX VPC. After the identifier is set, you cannot modify it.
11. Optionally, enter a description for the NSX VPC.
12. Click Save.

When an NSX VPC is created successfully, the system implicitly creates a
gateway. However, this implicit gateway is exposed to the Project Admin in a
read-only mode and is not visible to the NSX VPC users.

To view the realized implicit gateway, a Project Admin can do the following steps:

1. Navigate to NetworkingTier-1 Gateways.
2. Click the VPC Objects check box at the bottom of the Tier-1 Gateways page.
3. Expand the gateway to view the configuration in a read-only mode.

   The following naming convention is used for the implicit gateway:

   \_TIER1-VPC\_Name

The lifecycle of this implicit gateway is
managed by the system. When an NSX VPC
is deleted, the implicit gateway is deleted automatically.

If you have enabled the Default Outbound NAT option, you can view the system-created default SNAT rule in the NSX VPC. Do these steps:

1. Expand the Network Services section of the NSX VPC.
2. Click the count next to NAT.
3. Observe the default NAT rule with SNAT action for the private IPv4 block in the NSX VPC. This NAT rule is not editable. If the NSX VPC is assigned multiple private IPv4 blocks, one default NAT rule with SNAT action is created for each private IPv4 block.

   For example:

   ![This screen capture is described in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d75e8cc2-45a4-4d0c-bf6b-19576552fccd.original.png)

   The source IP in the SNAT rule is the private IPv4 block of the NSX VPC. In this example, it is 193.0.1.0/24. The translated IP for this SNAT rule is assigned from the external IPv4 block of the NSX VPC. In this example, it is 192.168.1.0.