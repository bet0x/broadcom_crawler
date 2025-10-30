---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter/add-a-virtual-private-cloud-in-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a Virtual Private Cloud in vCenter
---

# Create a Virtual Private Cloud in vCenter

Learn how to create a VPC in vCenter.

A VPC connects to a Transit Gateway (recommended) and can have the following types of subnets:

- **Private - VPC**: A subnet scoped to the VPC and routed with other subnets inside the same VPC, but not to the outside network. NAT is needed if outside communication is required.
- **Private - Transit Gateway**: Subnets allowing inter-VPC connectivity below the Transit Gateway without NAT. It requires IP translation if workloads need to be reachable to an outside network.
- **Public**: A subnet that is accessible from outside the environment, from other VPCs but also from customers and workload above the Transit Gateway.

In case you have to grant access to specific workloads on private networks from the outside environment, you can use External IPs.

**External IPs:** IPs that allow outside connectivity for a VM on a private network by performing IP translation. It is implemented with 1:1 NAT on the workload picking an IP from External IP block and assigning it to the VM.

In addition to External IPs, it is also possible to configure Static Routes and Groups in a VPC.

Regardless of External Connection type (Centralized or Distributed), it is possible to configure Static Routes, Groups and DHCP Server in a VPC.

1. From your browser, log in to the vSphere Client.
2. In the vSphere Client, navigate to Virtual Private Clouds in the vCenter inventory. From the **Actions** drop-down menu, select New VPC.
3. On the Basic Info page, enter the following information.

   | **Option** | **Description** |
   | --- | --- |
   | Name | Enter a name for the VPC. |
   | Description | Enter a description for the VPC. |
   | Private- VPC IP CIDRs | Enter a block of IP CIDRs that can be assigned to private subnets of this VPC. These CIDRs are local to VPCs and can overlap between the VPCs. |
   | Connectivity & Services | You can modify these settings from the NSX UI.  - **External IP Blocks**: External IPs for the VMs attached to subnets. You will need to select the VM, the NIC, and whether to auto assign the IPs or provide IPs from an IP block. - **Private -Transit IP Blocks:** Enter private IP blocks to create private subnets in the VPC. The entered IP blocks are available for inter-VPC communication. Networks created from the Private - Transit Gateway IP blocks are not advertised. - **Transit Gateway Connectivity**: You can select the default connectivity profile and continue the VPC configuration based on the simplified VPC model. For more information about the VPC Connectivity Profile, see [Add a VPC Connectivity Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-vpc-connectivity-profile.html)[.](https://docs.google.com/document/d/19wm0y2Nn8vmAgfN344wbp53gCNf5AQBjcVScWCcO46Y/edit?tab=t.0#heading=h.7jfczbgvs8y) - **N-S Services**: Turn on the toggle to enable service gateway for the connected subnets and to support centralized services such as N-S firewall, NAT, or gateway QoS profile in the VPC. - **Default Outbound NAT**: Turn on the toggle if the traffic from workloads on private subnets can be routed outside the NSX VPC. This toggle is available only if **N-S Services** the toggle is turned on.  - **DHCP:** One of the following options is present:    - **None**: DHCP will not be enabled in the subnet and all IP addresses will be set statically.   - **DHCP Server**: The DHCP server specified in the service profile will automatically assign IP addresses and network settings to VMs connected to the subnet. You will also need to set **Generic DHCP Options**, and **Static Bindings** if you select this option. If the **Auto allocate Subnet CIDR from IP Block** toggle is off, then you need to provide IP CIDRs for allocation in the **Reserved IP Ranges** field. For more information, see [DHCP Configuration Settings: Reference](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html).  - **DHCP Relay**: The DHCP relay specified in the service profile will forward DHCP messages from VMs connected to the subnet to an external DHCP. DHCP Relay is not supported for Distributed Transit Gateway. |
4. Click Save.

   A new VPC is created in vCenter.