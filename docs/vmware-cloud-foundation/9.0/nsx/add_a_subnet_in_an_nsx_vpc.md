---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds/add-a-subnet-in-an-nsx-vpc.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Subnet in an NSX VPC
---

# Add a Subnet in an NSX VPC

A subnet in an NSX VPC represents an
independent layer 2 broadcast domain. NSX VPC
subnets are realized as overlay segments in the default transport zone of the
project.

You must be assigned any one of these
roles in the NSX VPC:

- VPC Admin
- Network Admin

1. From your browser, log in to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Select the required project from
   the Project drop-down menu, if not already
   selected.
3. Click the
   VPCs tab and expand the details of the NSX VPC where you want to add a subnet.
4. Expand the
   Connectivity section and click
   Set. If subnets are existing in the NSX VPC, click the subnet count.

   The Set Subnets dialog box opens.
5. Click Add
   Subnet.
6. Configure the subnet properties.

   | Property | Description |
   | --- | --- |
   | Name | Enter a name for the subnet. |
   | Access Mode | Select any one of these access modes: Private, Public, Isolated.  To learn more these access modes, see the Access Modes for NSX VPC Subnets section in [NSX Virtual Private Clouds](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-virtual-private-clouds.html#GUID-b449af2a-c42d-4428-a0b1-57517d937d2b-en).  By default, private is selected. |
   | IP Assignment | By default, Automatic IP assignment is set for private and public subnets. It means that the system will assign an IPv4 CIDR for the subnet automatically. For a public subnet, the CIDR is assigned from the external IPv4 blocks of the NSX VPC. For a private subnet, the CIDR is assigned from the private IPv4 blocks of the NSX VPC.  For isolated subnets, only Manual IP assignment mode is supported.  In Manual IP assignment mode, you must enter a valid IPv4 CIDR for the subnet. |
   | Size | This property is applicable only when you select the Automatic IP assignment mode.  Select a size from the drop-down menu. System reserves four IP addresses for internal use, such as subnet network address, subnet gateway address, subnet broadcast address, DHCP server address.  For example, if you select size as 32, you can attach a maximum of 28 workloads to the subnet. |
   | IP CIDR | This property is applicable only when you select the Manual IP assignment mode.  Enter the IPv4 subnet address in a CIDR format. For example, 172.16.0.1/24  You can enter only one IPv4 CIDR. If the IPv4 CIDR that you entered is invalid or unavailable for assignment, the system throws an appropriate error message. You must enter a different IPv4 CIDR until the system accepts it. |
   | Description | Optionally, enter a description for the subnet. |
7. Click
   Save.

When a subnet is realized successfully in the NSX VPC, the Status column shows
Successful.

Subnets in an NSX VPC are realized as
overlay segments in the default transport zone of the project.

An Enterprise Admin or a Project Admin
can view these overlay segments by doing these steps:

1. Ensure that you are in the project view.
2. Navigate to NetworkingSegments.
3. Click the VPC realized objects check box at the bottom of
   the Segments page.

   For example:

   ![This screen capture is described in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/ca4d448d-4ffe-4511-833e-090070a00ed0.original.png)

   This screen capture shows two system-created segments
   orders\_vpc\_subnet and
   sales\_vpc\_subnet. These segments represent
   subnets in the sales\_vpc, and are displayed in
   a read-only mode on the Segments
   page.

You can now start attaching workload VMs to the subnet by using the vSphere Client.

The following subsections briefly
explains some tasks that you can do after a subnet is realized in an NSX VPC.

Set subnet ports
:   On the Set
    Subnets dialog box, under the Subnet
    Ports column, click Set, and then
    click Add Subnet Port.

    The workflow for adding ports
    on an NSX VPC subnet is the
    same as it is for adding ports on an NSX segment. To learn more, see the steps for adding
    segment ports in [Create an NSX Segment](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/add-an-nsx-segment.html).

View IPAM statistics of NSX VPC subnets
:   Expand the subnet details and
    click View IPAM Statistics. At the time of subnet
    creation, if DHCP in the NSX VPC is managed by NSX or by external DHCP servers, the IPAM
    Statistics page displays the DHCP IP pool range.

    The system automatically
    allocates 100% of available IP addresses in the subnet to the DHCP pool
    range. The system reserves four IP addresses from the subnet for its
    internal use. The DHCP static IP pool is empty and hence it is not
    displayed on IPAM Statistics page. You cannot edit
    the system-managed DHCP pool configuration of the VPC subnet.

    For example:

    ![This screen capture is described in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e7ec0f44-18b3-4693-aca4-990e1a4e0b75.original.png)

    In this screen capture, the
    sales\_vpc\_subnet is a private subnet
    with size 16. The DHCP configuration for this subnet is automatically
    managed by NSX. The system
    reserves four IP addresses from the subnet for its internal use, by
    default. So, the remaining 12 IP addresses are automatically allocated
    to the DHCP IP pool range (193.0.1.3-193.0.1.14). The IP addresses are
    dynamically assigned to the workload VMs on the subnet from this DHCP
    pool
    range.

    If you prefer to manually
    configure the DHCP pool ranges for dynamic and static IP assignments in
    the VPC subnet, you can add the subnet in the NSX VPC by running the following
    NSX API. Currently,
    the UI does not support manual DHCP configuration of NSX VPC subnets.

    ```
    PUT https://<nsx-mgr>/policy/api/v1/orgs/default/projects/<project-id>/vpcs/<vpc-id>/subnets/<subnet-id>/
    ```

    Example Request Body:

    ```
    {
        "ipv4_subnet_size": 16,
        "access_mode": "Public",
        "resource_type": "VpcSubnet",
        "dhcp_config": {
            "enable_dhcp": true,
            "static_pool_config": {
                "ipv4_pool_size": 8
            }
        }
    }
    ```

    This example payload shows
    that you have created a public NSX VPC subnet of size 16. You have specified the size of
    the static IP pool as eight. Therefore, out of the total 12 IP addresses
    that are available for allocation to the workloads in the NSX VPC subnet, the remaining four IP
    addresses are allocated to the DHCP IP pool for a dynamic IP
    assignment.

    When you view the
    IPAM Statistics page of this NSX VPC, the system displays the IP
    address utilization of both the DHCP IP pool and the static IP pool.

    At the time of subnet
    creation, if DHCP in the NSX VPC is none, the IPAM Statistics
    page of the subnet displays only the static IP pool information.

View traffic statistics of NSX VPC subnets
:   Expand the subnet details and
    click View Subnet Statistics.

    If you want to view the
    traffic statistics for the full NSX VPC, and not for a specific subnet in the VPC, expand
    the NSX VPC details, and
    then click View VPC Statistics.