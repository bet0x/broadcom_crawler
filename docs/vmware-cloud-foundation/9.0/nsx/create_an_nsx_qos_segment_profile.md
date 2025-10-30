---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-qos-segment-profile/create-an-nsx-qos-segment-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Create an NSX QoS Segment Profile
---

# Create an NSX QoS Segment Profile

You can define the DSCP value and configure the ingress and egress settings to create a custom QoS switching profile.

- Familiarize yourself with the QoS switching profile concept. See [Understanding QoS Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-qos-segment-profile.html).
- Identify the network traffic you want to prioritize.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingSegmentsSegment
   Profiles.
3. Click Add Segment Profile to add a new profile.
4. Click ![Actions menu](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png) and click Edit.
5. Complete the QoS switching profile details.

   Option | Description || Name | Name of the profile. |
   | Mode | Select either a Trusted or Untrusted option from the Mode drop-down menu.  When you select the Trusted mode the inner header DSCP value is applied to the outer IP header for IP/IPv6 traffic. For non IP/IPv6 traffic, the outer IP header takes the default value. Trusted mode is supported on an overlay-based logical port. The default value is 0.  Untrusted mode is supported on overlay-based and VLAN-based logical port. For the overlay-based logical port, the DSCP value of the outbound IP header is set to the configured value irrespective to the inner packet type for the logical port. For the VLAN-based logical port, the DSCP value of IP/IPv6 packet will be set to the configured value. The DSCP values range for untrusted mode is between 0 to 63.  DSCP settings work only on tunneled traffic. These settings do not apply to traffic inside the same hypervisor. |
   | Priority | Set the DSCP priority value.  The priority values range from 0 to 63. |
   | Class of Service | Set the CoS value.  CoS is supported on VLAN-based logical port. CoS groups similar types of traffic in the network and each type of traffic is treated as a class with its own level of service priority. The lower priority traffic is slowed down or in some cases dropped to provide better throughput for higher priority traffic. CoS can also be configured for the VLAN ID with zero packet.  The CoS values range from 0 to 7, where 0 is the best effort service. |
   | Ingress | Set custom values for the outbound network traffic from the VM to the logical network.  You can use the average bandwidth to reduce network congestion. The peak bandwidth rate is used to support burst traffic and the burst size is based on the duration with peak bandwidth. You set burst duration in the burst size setting. You cannot guarantee the bandwidth. However, you can use the Average, Peak, and Burst Size settings to limit network bandwidth.  For example, if the average bandwidth is 30 Mbps, peak bandwidth is 60 Mbps, and the allowed duration is 0.1 second, then the burst size is 60 \* 1000000 \* 0.10/8 = 750000 Bytes.  The default value 0 disables rate limiting on the ingress traffic. |
   | Ingress Broadcast | Set custom values for the outbound network traffic from the VM to the logical network based on broadcast.  For example, when you set the average bandwidth for a logical switch to 3000 Kbps, peak bandwidth is 6000 Kbps, and the allowed duration is 0.1 second, then the burst size is 6000 \* 1000 \* 0.10/8 = 75000 Bytes.  The default value 0 disables rate limiting on the ingress broadcast traffic. |
   | Egress | Set custom values for the inbound network traffic from the logical network to the VM.  The default value 0 disables rate limiting on the egress traffic. |

   If the ingress, ingress broadcast, and egress options are not configured, the default values are used.
6. Click Save.