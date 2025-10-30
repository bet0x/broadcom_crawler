---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-ipsec-vpn-sessions/download-the-remote-side-ipsec-vpn-configuration-file.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Download the Remote Side IPSec VPN Configuration File
---

# Download the Remote Side IPSec VPN Configuration File

To
set up IPSec between two sites you must configure the two VPN endpoints with matching
attributes. This topic helps you to understand the requirements to ensure that your IPSec
VPN device vendor attributes match the VPN-related attributes of your local IPSec VPN
session.

Each IPSec VPN vendor has their own
format of accepting the configurations. In certain cases there are default values
used for a few parameters. You can use the Download Config
feature in the NSX IPSec VPN Sessions
UI which provides all the VPN-related configurations that an administrator can use
to configure a peer VPN vendor device. It is based on the IPSec VPN session
configured at NSX. The feature
presents all hidden/default attributes for the IPSec VPN session to allow the
administrator to configure the peer VPN device, which may have different default
values. Any configuration mismatch can lead to the IPsec VPN tunnel not coming up
properly.

Clicking DOWNLOAD
CONFIG, as shown in the IPSec VPN Sessions Download Config Button
image, downloads a text file that contains relevant attributes that might be
required to configure the IPSec VPN session counterpart at the peer VPN device.

IPSec VPN Sessions
Download Config Button

![Download Config button located in far left IPSec VPN Sessions
                            page](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/835beed9-96a2-4c5d-a262-a3689ccc8b0b.original.png)

Procedure

1. Ensure you have configured an
   IPSec VPN service and a session successfully before proceeding.
2. Go to the NetworkingVPN  IPSec Sessions tab to access the Download Config
   button.
3. In the table of IPSec VPN
   Sessions, expand the row for the session you plan to use for the IPSec VPN
   session configuration. For example, the Sample\_Policy\_Based row is expanded in the IPSec VPN Sessions
   Download Config Button image.
4. Click Download
   Config and click Yes on the
   Warning dialog box to download a text file.
5. Use the downloaded config file to configure the policy or route-based IPSec
   VPN session attributes at the peer VPN endpoint to ensure it contains the
   required matching values.

The following sample text file is similar
to the file that gets downloaded. The file name, Sample\_Policy\_Based.txt is
a policy-based IPSec VPN session configured in NSX. The name of the file downloaded is based on the name of the
session. For example <session-name>.txt.

```
 # Suggestive peer configuration for Policy IPSec Vpn Session
#
# IPSec VPN session path          : /infra/tier-0s/ServerT0_AS/ipsec-vpn-services/IpsecOnServerT0/sessions/SAMPLE_POLICY_BASED
# IPSec VPN session name          : SAMPLE_POLICY_BASED
# IPSec VPN session description   : 
# Tier 0 path                     : /infra/tier-0s/ServerT0_AS
#
# Enforcement point path    : /infra/sites/default/enforcement-points/default
# Enforcement point type    : NSX
#
# Suggestive peer configuration for IPSec VPN Connection
#
# IPSecVPNSession Id         : e7f34d43-c894-4dbb-b7d2-c899f81b1812
# IPSecVPNSession name       : SAMPLE_POLICY_BASED
# IPSecVPNSession description: 
# IPSecVPNSession enabled    : true
# IPSecVPNSession type       : Policy based VPN
# Logical router Id          : 258b91be-b4cb-448a-856e-501d03128877
# Generated Time             : Mon Apr 29 07:07:43 GMT 2024
#
# Internet Key Exchange Configuration [Phase 1]
# Configure the IKE SA as outlined below
IKE version                  : IKE_V2
Connection initiation mode   : INITIATOR
Authentication method        : PSK
Pre shared key               : nsxtVPN!234
Authentication algorithm     : [SHA2_256]
Encryption algorithm         : [AES_128]
SA life time                 : 86400
Negotiation mode             : Not applicable for ikev2
DH group                     : [GROUP14]
Prf Algorithm                : [SHA2_256]
#
# IPsec_configuration [Phase 2]
# Configure the IPsec SA as outlined below
Transform Protocol              : ESP
Authentication algorithm        : 
Sa life time                    : 3600
Encryption algorithm            : [AES_GCM_128]
Encapsulation mode              : TUNNEL_MODE
Enable perfect forward secrecy  : true
Perfect forward secrecy DH group: [GROUP14]
#
# IPsec Dead Peer Detection (DPD) settings
DPD enabled         : true
DPD probe interval  : 60
#
# IPSec VPN Session Configuration
Peer address    : 1.1.1.10 # Peer gateway public IP.
Peer id         : 1.1.1.10
#
Local address   : 200.200.200.1 # Local gateway public IP.
Local id        : 200.200.200.1
#
# Policy Rules
#Rule1
Sources: [192.168.19.0/24]
Destinations: [172.16.18.0/24]
```

The IPSec VPN Sessions Configuration File
Attributes table contains the attributes in the Sample\_Policy\_Based.txt
VPN session config file to use when configuring IPSec VPN at the peer VPN device.

IPSec VPN Sessions
Configuration File Attributes



| Category | Attribute Name | Meaning and Value of Attribute to be Configured at the Peer VPN Device | Peer Device Configurability |
| --- | --- | --- | --- |
| ISAKMP Phase 1Parameters | IKE version | IKE protocol version | Mandatory |
|  | Connection initiation mode | Whether the device initiates IKE connection | Optional.  Mandatory if NSX IPSec is configured with Connection Initiation Mode = "Respond Only." |
|  | Authentication method | Authentication mode for IKE - Pre-Shared Key or Certificate | Mandatory |
|  | Pre shared key | Value of Shared Key if the Authentication Mode is PSK | Mandatory |
|  | Authentication algorithm | Authentication algorithm to be used for IKE | Mandatory |
|  | Encryption algorithm | Encryption algorithm to be used for IKE | Mandatory |
|  | SA life time | Lifetime of IKE Security Association (SA) in seconds | Optional |
|  | Negotiation mode | Mode of IKEv1 protocol - Only Main mode is supported. Not relevant for IKEv2 | Mandatory |
|  | DH group | Diffie Hellman Group to be used for IKE SA negotiation | Mandatory |
|  | Prf Algorithm | Pseudo Random function to be used for IKE SA negotiation | Mandatory |
|  | Peer address | IP address of the VPN endpoint at the NSX side | Mandatory |
|  | Peer id | Identity of the VPN endpoint at the NSX side | Mandatory |
|  | Local Address | Address of the VPN endpoint at the peer endpoint side (in configuration done in NSX side) | Mandatory |
|  | Local ID | Identity of the VPN endpoint to be configured at the peer endpoint side | Mandatory |
| ISAKMP Phase 2 Parameters | Transform Protocol | Transform Protocol | Transform Protocol |
|  | Authentication algorithm | Integrity protection algorithm for IPSec packets | Mandatory |
|  | SA Lifetime | Lifetime of IPSec SA, in seconds.  Keys are refreshed as the SA lifetime approaches. | Optional |
|  | Encryption algorithm | Encryption protection for IPSec packets | Mandatory |
|  | Encapsulation mode | Mode for IPSec Tunnel (Tunnel or Transport) | Mandatory. Only Tunnel Mode is supported. |
|  | Enable perfect forward secrecy | PFS (enabled or inactive) | Mandatory |
|  | Perfect forward secrecy DH group | DH group to be used for PFS | Mandatory |
|  | Sources | Applies to policy-based VPN. This is the subnet or subnets behind the peer VPN endpoint. | Mandatory for policy-based VPN |
|  | Destinations | Applies to policy-based VPN. This is the subnet or subnets behind the NSX VPN endpoint for which traffic needs to be tunneled over IPSec. | Mandatory for policy-based VPN |
| Other Parameters | DPD enabled | Whether Dead Peer Detection is enabled | Optional |
|  |  | Frequency at which DPD is performed (in seconds) | Optional |