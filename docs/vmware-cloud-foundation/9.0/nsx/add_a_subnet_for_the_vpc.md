---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-subnet-for-the-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Subnet for the VPC
---

# Add a Subnet for the VPC

1. On the Additional Configurations page click Set in the Subnet field.
2. Enter the following fields.

   | Field Name | Description |
   | --- | --- |
   | Name | Enter the name of the subnet. |
   | Access Mode | Select an access mode for the subnet.  - Private VPC - Private Transit Gateway - Public |
   | Gateway Connectivity | Turn on this toggle to connect this subnet to the other subnets in the VPC. |
   | IP CIDR | Turn on the toggle Auto allocate Subnet CIDR from IP Blocks to auto allocate the IPs and select a subnet size. Based on the type of subnet you create, IPs are allocated from the private, public, or private TGW CIDRs you defined in the connectivity profile of the VPC.  If you choose to turn off the auto allocation of subnet CIDR, then enter the IP CIDR. |
   | Virtual Machine | Shows the virtual machines attached to this subnet. |
   | Subnet Ports | Shows the subnet ports. |
   | DHCP Configuration - Note that DHCP Configuration options are available only if the DHCP settings are configured in the Service Profile linked to the VPC. | |
   | DHCP Config | Select one of the following options:  - None : DHCP will not be enabled in the subnet and all IP addresses will be set statically. - DHCP Server: The DHCP server specified in the service profile will automatically assign IP addresses and network settings to VMs connected to the subnet. You can set Classless Static Routes  or Generic DHCP Options  if you want such DHCP options to be configured to the subnet VMs.  If you don't want the DHCP server to dynamically allocate the whole range of this subnet IP CIDR to the subnet VMs, you can specify the IP ranges that you want to exclude through the Reserved IP Ranges field. The Static Bindings  should be a part of the Reserved IP Ranges .  For more information, see [DHCP Configuration Settings: Reference](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-dhcp-policy-ui/configure-nsx-dhcp-service/nsx-dhcp-configuration-settings-reference.html).  - DHCP Relay : The DHCP relay specified in the service profile will forward DHCP messages from VMs connected to the subnet to an external DHCP. Note that DHCP Relay is not supported for Distributed Transit Gateway. |
   | Description | Enter a description for this subnet. |
   | Tags | Enter a tag and scope for this subnet. |
3. Click Save.