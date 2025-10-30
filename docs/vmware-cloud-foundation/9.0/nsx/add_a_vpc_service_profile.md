---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-cloud-in-nsx/add-a-vpc-service-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a VPC Service Profile
---

# Add a VPC Service Profile

A VPC service profile is a collection of services (DHCP and subnet profiles). It simplifies configuration of common services on multiple VPCs. When a project is created, a default service profile is also created for it.

1. From your browser, log in to an NSX Manager.
2. Click the Project drop-down menu, aand select the project for which you want to add a service profile. By default, the Default project is selected.
3. Go to VPCs Profiles  VPC Service Profile .
4. Click Add VPC Service Profile.
5. Enter the following fields.

   | Field Name | Description |
   | --- | --- |
   | Name | Enter a name for the VPC service profile. |
   | VPC | Shows where the service profile is used. |
   | Status | Shows if the service profile is successfully created. |
   | DHCP Configuration - Configure the following settings. | |
   | Enable DHCP Server Config | Turn on the toggle to enable the DHCP server. If you create a subnet and select the DHCP server option for the subnet, the settings configured here are applied to the subnets.  A DHCP server can either be a Centralized or a Distributed. By default, the DHCP server mode is Distributed. In case the VPC has a Distributed connectivity, the DHCP server mode can only be Distributed DHCP. If the VPC has a Centralized connectivity, the DHCP server mode can either be a Centralized DHCP server or a Distributed server with the default mode being a Distributed server.  You can use the NSX API to change the DHCP server mode. For more information about the API, see the NSX API Guide. |
   | DNS Server IPs | Enter the IPs of DNS servers provided to clients by the DHCP server. Note that if you require to configure DNS servers, the Enable DHCP Server Config toggle must be on. |
   | Lease Time (Seconds) | Enter the time for which clients can lease IP addresses from the DHCP server. |
   | NTP Server IPs | Enter the IPs of NTP servers provided to clients by the DHCP server. |
   | Enable DHCP Relay Config | Turn on the toggle to enable the relay-type DHCP configuration for relaying the DHCP client requests to external DHCP servers.  If you create a subnet and select the DHCP relay option for the subnet, the settings configured here are applied to the subnet’s DHCP relay. |
   | External DHCP Server Addresses | Enter addresses of external DHCP servers. Note that if you require to configure external DHCP servers, the **Enable DHCP Relay Config** toggle must be on. |
   | Subnet Profiles - Attach the following profiles to the VPC. For more information about these profiles, see [Segment Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles.html) | |
   | IP Discovery | Select an IP discovery profile or create a new profile to use. For more information, see [Create an IP Discovery Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-ip-discovery-segment-profile/create-an-nsx-ip-discovery-segment-profile.html). |
   | Spoofguard | Select a spoofguard profile or create a new profile to use. For more information, see [Create an Spoof Guard Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-spoofguard-segment-profile/create-an-nsx-spoofguard-segment-profile.html). |
   | MAC Discovery | Select a MAC discovery profile or create a new profile to use. For more information, see [Create an MAC Discovery Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-mac-discovery-segment-profile/create-an-nsx-mac-discovery-segment-profile.html). |
   | Segment Security | Select a segment security profile or create a new profile to use. For more information, see [Create a Segment Security Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-segment-security-segment-profile/create-an-nsx-segment-security-segment-profile.html). |
   | QoS | Select a QoS profile or create a new profile to use. For more information, see [Create an QoS Segment Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/segment-profiles/understanding-qos-segment-profile/create-an-nsx-qos-segment-profile.html). |
   | Description | Enter a description for the service profile. |
   | Tags | Enter tags and scope for this connectivity profile. |
6. Click Save.