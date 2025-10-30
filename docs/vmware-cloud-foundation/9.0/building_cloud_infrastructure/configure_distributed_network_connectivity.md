---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-network-connectivity-in-vcenter/managing-distributed-network-connectivity.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Configure Distributed Network Connectivity
---

# Configure Distributed Network Connectivity

Distributed connection allows a lightweight distributed connection to the data-center fabric without the need to deploy Edge nodes or configure dynamic routing. In addition to on-demand networking and distributed routing, other services available when using distributed connections are External IPs (1:1 NAT) and distributed DHCP.

- Dedicated VLAN(s) and subnets must be available for the Distributed Transit Gateway connection to the ToR. The same VLAN must be configured on all the ToR switches where the ESX host are connected which offers VPCs. All the hosts running VPC workloads must have access to these VLAN(s).
- Reserve external IP blocks for VPC connectivity. External IP blocks must be the same as or a subset of dedicated VLAN subnets. For more information, see [Create a Virtual Private Cloud in vCenter](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/managing-virtual-private-clouds-in-vcenter/add-a-virtual-private-cloud-in-vcenter.html).

A distributed connection is the one where a Transit Gateway connects to a VLAN provisioned in the fabric. This happens directly on the host which implies the VLAN needs to be available on the ESX hosts (on physical uplinks used by the NSX vmkernel). The workflow is available in both NSX and vCenter. This section describes how to use the workflow from vCenter to configure a distributed connectivity. To set up a distributed gateway connectivity for the first time from vCenter, perform the following steps:

1. From your browser, log in to the vSphere Client with administrator credentials.
2. In the vSphere Client, navigate to the vCenter for the Workload Domain and select Networks > Network Connectivity.
3. Click Configure Network Connectivity.
4. In the Transit Gateway page, select Distributed Connectivity.

   Select gateway connectivity for the created VPCs that align with the infrastructure requirements and networking preferences.
5. Complete the Networking prerequisites. Click Continue.
6. Enter the information on External Network Connectivity Details page.

   | **Field Name** | **Description** |
   | --- | --- |
   | VLAN ID | Enter the VLAN ID to which the traffic is to be routed. This VLAN must be dedicated for external connectivity of workloads deployment in VPCs and must be stretched across all clusters where VPCs are deployed. |
   | Gateway CIDR IPv4 Address | Enter the gateway address through which the traffic should be routed to the external network. |
   | **VPC Configuration** | |
   | VPC External IPv4 Blocks | Enter IP blocks for VPC. |
   | Private - TGW IPV4 Blocks | Enter IP blocks for Private - TGW IPV4. |
7. On the Validations page, review the details and click Done.