---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter/view-the-summary-of-virtual-private-cloud-in-vcenter.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > View the Summary of Virtual Private Cloud in vCenter
---

# View the Summary of Virtual Private Cloud in vCenter

Learn how to view the summary of VPCs in vCenter. You can view the information summary for all the VPCs or a specific VPC.

1. To view the summary of a single VPC,
   1. From your browser, log in to the vSphere Client.
   2. In the vSphere Client, navigate to the VPC under Virtual Private Clouds.
   3. Click Summary.

      | **Option** | **Description** |
      | --- | --- |
      | **VPC Details** | |
      | Status | Displays the status of the VPC. |
      | VPC Subnets | Displays the number of subnets of this VPC. |
      | External IPs | Displays the number of external IPs assigned to the VM across all datacenters and vCenter servers. |
      | VMs | Displays the total number of VMs connected to this VPC across all datacenters and vCenter servers. |
      | Private - VPC IP CIDRs | Block of IP CIDRs that are assigned to private subnets of this VPC. These CIDRs are local to VPCs and can overlap between the VPCs. |
      | **Connectivity and Services** | |
      | External IP Blocks | External IPs for the VMs attached to subnets.  Indicates if IP blocks are set. |
      | Private - Transit Gateway IP Blocks | Indicates if transit gateway IP blocks is set.  Private IP blocks to create private subnets in the VPC. |
      | Transit Gateway Connectivity | Default connectivity profile.  Indicates if transit gateway connectivity is configured. |
      | N-S Services | Displays the status of N-S services.  Service gateway for the connected subnets and to support centralized services such as N-S firewall, NAT, or gateway QoS profile in the VPC. |
      | Default Outbound NAT | Indicates if the traffic from workloads on private subnets are routed outside the NSX VPC. |
      | **Subnets and Workloads** | |
      | By Status | Shows the status of this VPC. |
      | By Access Mode | Indicates the access mode for the subnet.  - Private VPC - Private Transit Gateway - Public |
      | **Statistics** | |
      | North-South Traffic | Displays the statistics for all traffic in the north-south service. |
      | Rx Dropped Packets | Total number of packets that were dropped by the receiving network. |
      | Transmitted (Tx) | Total number of packets that were transmitted successfully. |
      | Tx Dropped | Total number of packets that were dropped before transmission. |
      | East-West Traffic | Displays the statistics for all traffic in the east-west service. |
      | Rx Dropped Packets | Total number of packets that were dropped by the receiving network. |
      | Transmitted (Tx) | Total number of packets that were transmitted successfully. |
      | Tx Dropped | Total number of packets that were dropped before transmission. |
2. To view the aggregated summary of all the VPCs,
   1. From your browser, log in to the vSphere Client.
   2. In the vSphere Client, navigate to Virtual Private Clouds in the vCenter inventory.
   3. Click Summary.

      | **Option** | **Description** |
      | --- | --- |
      | **Overview** | |
      | VPCs | Displays the number of VPCs |
      | VPC Subnets | Displays the number of subnets of this VPC. |
      | VMs | Displays the total number of VMs connected to the VPC across all datacenters and vCenter Servers. |
      | **VPCs** | |
      | Top VPCs by number of subnets | Shows the number of subnets of this VPC. |