---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configuring-industrial-vswitch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an Industrial vSwitch
---

# Configure an Industrial vSwitch

The Industrial Virtual Switch (IvS) is an NSX virtual switch configuration designed to support real-time PROFINET communication over industrial Ethernet networks, ensuring low latency and bounded jitter.

1. On the ESX hosts to be configured with Industrial vSwitch, configure the hosts in High Performance mode with no Power Saving methods. The examples below show the BIOS settings from a sample server.

   | **Setting Name** | **Configuration** |
   | --- | --- |
   | Enhanced Processor Performance | Enabled |
   | Enhanced Processor Performance Profile | Aggressive |
   | Power Regulator | Static High Performance Mode |
   | Minimum Processor Idle Power Core C-State | No C-States |
   | Minimum Processor Idle Power Package C-State | No Package State |
   | Energy/Performance Bias | Maximum Performance |
   | Collaborative Power Control | Disabled |
   | Intel Turbo Boost Technology | Disabled |
   | Workload Profile | Custom |
   | Time Format | Local Time |
   | Intel Hyper-Threading | Enabled |
2. Verify that the NICs used for Industrial vSwitch uplinks support EDP Dedicated/Poll mode. Check the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/search?program=io&persona=live&column=brandName&order=asc) for the list of supported NICs.
3. Disable Default Queue Receive Side Scaling (DRSS) on the hosts. The IvS prioritizes latency, and aims for minimal and deterministic jitter. To help achieve this, disabling DRSS on the physical NICs in each host is required. Refer to [Configure NetQ Receive Side Scaling](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-data-path-optional-configurations/configure-netq-receive-side-scaling.html) for procedures to disable DRSS.

IvS enables the forwarding of PROFINET traffic between virtual Programmable Logic Controllers (vPLCs) running on ESX hosts and I/O devices located outside the vSphere cluster. IvS also supports the Parallel Redundancy Protocol (PRP), providing seamless network redundancy and high availability for traffic across two distinct LANs. Additionally, IvS is natively optimized and tuned for PROFINET performance.

IvS is not compatible with the vDefend suite. If the ports connected to an IvS are configured with DFW, the latency will not meet 500 microseconds and 10% jitter that might be required by PROFINET-RT applications.

The following considerations apply to IvS configuration and use:

- A maximum of two Industrial vSwitches are supported per Transport Node Profile and per vSphere host, and they can only be configured on VLAN transport zones.
- PRP can only be configured and enabled on one IvS per host.
- Deterministic latency for packets forwarded in Industrial vSwitch is not guaranteed to be bounded during vMotion, software upgrade, or configuration changes.
- For virtual machines connected to the IvS to leverage the supported features, only vmxnet3 interfaces using the latest driver version 1.9 or later are supported. Latency Sensitivity High is also required for the VM settings.

Use the following procedure to configure IvS.

1. From the vCenter create a host switch with with the “Industrial vSwitch” option.

   ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e3ab22ac-b11d-4cb9-8372-09c879310ec2.original.png)
2. To leverage Parallel Redundancy Protocol (PRP) in IvS, go to the vSwitch configurations under ConfigureSettingsPRP Settings and map the LAN-A and LAN-B networks to the appropriate uplinks connected to those LAN networks. The IvS supports a maximum of 2 uplinks per PRP LAN network.
3. Log in to the NSX Manager or access the NSX interface from vCenter and add the IvS hosts.
4. Navigate to SystemFabricProfilesUplink ProfilesAdd Uplink Profile.
5. Create an Uplink Profile for the IvS created in vCenter by entering relevant industrial virtual switch.
6. Next to Teaming in the display, click Set to enter the Teaming configuration.
7. Click Add and then Apply.
8. Click Save.
9. Navigate to SystemFabricTransport ZonesAdd Transport Zone.
10. Enter the Transport Zone name and traffic type VLAN.
11. Click Save.
12. Navigate to SystemHostsTransport Node Profiles.
13. Click Add a Transport Node Profile (TNP) and enter the profile name.
14. Under Host Switch, click Set.
15. Click Add Host Switch and complete the configuration:
    1. Enter the vCenter Name.
    2. For Select VDS, select the Industrial vSwitch.
    3. Select the Transport Zone that you created in a previous step.
    4. Select the Uplink Profiles that you created in a previous step.

       The system automatically populates and displays the Teaming Policy Uplink Mapping.
16. Expand Advanced Configuration.

    The system displays prepopulated values for latency and redundancy.
17. For CPU Config, click Set.

    The CPU Config screen appears.
18. Set the number of CPUs and number of cores to use for the Enhanced Data Path Dedicated mode. Five CPU cores is the maximum supported.
19. Click Add and then Save.
20. (Optional) Review and modify any of the Advanced Configuration settings.
21. Click Add and then Save.
22. Install the Transport Node on the host by applying TNP on the cluster.
    1. Navigate to SystemFabricHostsClusters.
    2. Select the cluster and click Configure NSX.
    3. Select the Transport Node Profile created for the IvS, and click Save.

       The system applies the Transport Node Profile to the cluster.
23. Navigate to NetworkingSegmentsProfilesSegment Profiles.
24. Click Add Segment Profile, and select Industrial vSwitch and enter Segment Profile name.

    For more information, see [Understanding Industrial vSwitch Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-industrial-vswitch-segment-profile.html).
25. Using the toggles, enable the full Network Path Latency and enter the Sampling Rate.
26. Click Save.
27. Create a segment for Real-Time networks:
    1. Navigate to NetworkingSegmentsNSX.
    2. Click Add Segment and enter the segment name.
    3. Select the transport zone, and enter the appropriate VLAN number.
    4. Click Save.
    5. Expand Segment Profiles.
    6. Expand Industrial Switch and select the IvS segment profile.
28. Click Save.

This completes the procedure.

Configure the the vNICs on the vPLC VM and connect them to the respective IvS segment.