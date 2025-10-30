---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/troubleshooting-syslog-issues.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Troubleshooting Syslog Issues
---

# Troubleshooting Syslog Issues

If logs are not received by the
remote log server, perform the following steps.

- Verify the remote log
  server's IP address.
- Verify that the
  level parameter is
  configured correctly.
- Verify that the
  facility parameter is
  configured correctly.
- If the protocol is TLS, set
  the protocol to UDP to see if there is a certificate mismatch.
- If the protocol is TLS,
  verify that port 6514 is open on both ends.
- Remove the message ID filter
  and see if logs are received by the server.
- Restart the
  rsyslog service with the command restart service syslog.

To learn more about how to configure
NSX appliances and
hypervisors to send log messages to a remote logging server, see [Configure Remote
Logging](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/configure-remote-logging.html#GUID-644083a6-84fd-426b-9580-5434e0b06ebe-en_GUID-0CEA7FB9-14C9-4214-A109-83F25C26DFDF).