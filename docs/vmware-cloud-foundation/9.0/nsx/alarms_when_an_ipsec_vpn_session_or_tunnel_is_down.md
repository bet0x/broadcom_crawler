---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/troubleshooting-vpn-issues-in-nsx-t-data-center/alarms-when-an-ipsec-vpn-session-is-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Alarms When an IPsec VPN Session or Tunnel Is Down
---

# Alarms When an IPsec VPN Session or Tunnel Is Down

When an IPsec VPN session or tunnel is down, an alarm is raised and the reason for
the Down alarm is displayed on the Alarms dashboard or the VPN page on the
NSX Manager user
interface.

Use the following tables to locate the
Reason message that you see on the NSX Manager user interface and review the
possible cause for the Down alarm. To resolve the alarm, perform the
necessary actions listed for the specific Reason message and possible
cause for the Down alarm.

Causes and Solutions for
an IPsec VPN Session Is Down Alarm



| Reason for the IPsec VPN Session Down Alarm | Possible Cause | Necessary Actions to Resolve the Alarm Message |
| --- | --- | --- |
| Authentication failed | The IKE SA establishment between the VPN gateways failed due to a failure in authentication. Authentication of the IKE SA depends on the pre-shared key, Local ID, and Remote ID values. | - Verify the   Local ID and Remote   ID values. The Local ID value must be set   as the Remote ID value in the peer VPN gateway. - Verify the   Pre-shared Key value. It must match   exactly in both the VPN gateways. |
| No proposal chosen | The IKE transform configuration in both the local and peer configuration file are inconsistent. | Ensure that the following properties are configured the same for both gateways.  - DH   groups - Digest and encryption   algorithms |
| Peer sent delete | The peer gateway initiated a delete case. A DELETE payload is received for IKE SA. | To determine why the peer gateway sent a DELETE payload, examine the syslogs on the NSX Edge and on the peer gateway side. |
| Peer not responding | The IKE SA negotiation timed out. | - Verify that   the remote gateway is up. - Verify the   connectivity to the remote gateway. |
| Invalid syntax | - IKE   proposals or transforms are not formed correctly. - There are   malformed IKE payloads. | To debug the invalid syntax, analyze the edge syslogs. |
| Invalid spi | An invalid SPI value was received in the IKE payload. | To debug the invalid SPI value, analyze the edge syslogs. |
| Configuration failed | The session configuration realization failed in NSX Edge due to some constraints or certain criteria. The reason is listed in the session dump under Session\_Config\_Fail\_Reason. | Resolve the error using the reason displayed in the session dump under Session\_Config\_Fail\_Reason. |
| Negotiation not started | The IKE SA negotiation has not started. | - Verify that   the Connection Initiation Mode property   in the session configuration is set to Respond   Only. - Verify the   VPN configuration of both gateways. At least one of the   gateways must be set to Initiator. |
| IPsec service not enabled | Status of the VPN service used for the session is not active. | Verify if the Admin Status in the IPsec VPN service configuration is not enabled. |
| Session not enabled | Admin has not enabled the session. | Enable the session to resolve this error. |
| SR state is not Active | SR is in a standby state. | Verify VPN session status on the NSX Edge node where HA peer SR is in the Active state. |

Causes and Solutions for
an IPsec VPN Tunnel Is Down Alarm



| Reason for the IPsec VPN Tunnel Down Alarm | Possible Cause | Necessary Actions to Resolve the Alarm Message |
| --- | --- | --- |
| Peer sent delete | The peer gateway sent a DELETE payload for the IPSEC SA. | To understand why the peer gateway sent a DELETE payload, you must check the syslogs on the NSX Edge and on the peer gateway side. |
| No proposal chosen | The ESP transform configuration is not consistent in the configurations for both the local and peer gateways. | Ensure that the following properties are configured the same for both gateways.  - DH   groups - Digest and encryption   algorithms - The   PFS is activated or not. |
| TS unacceptable | The IPsec SA setup has failed due to a mismatch in the policy rule definition between the gateways for the tunnel configuration. | Check the local and remote network configuration on both gateways. |
| IKE SA down | The IKE SA session is down. | First, check the session down reason in the edge syslogs. Refer to the Necessary Actions column in the previous table to resolve the session down errors, and then check whether the tunnel down reason still persists. |
| Invalid syntax | - The   proposals or transforms are not formed correctly. - There are   malformed payloads. | To debug the invalid syntax, analyze the edge syslogs. |
| Invalid spi | An invalid SPI value was received in the ESP payload. | To debug the invalid SPI value, analyze the edge syslogs. |
| No IKE peers | All IKE peers are dead. There are no peer gateways left with whom to try to establish a connection. | - Check if   the remote gateway is up. - Check the   connectivity to the configured peer gateways. |
| IPsec negotiation not started | The IPsec SA negotiation has not started. | The IKE SA is not up yet. Check the session down reason in the edge syslogs and resolve the errors. |