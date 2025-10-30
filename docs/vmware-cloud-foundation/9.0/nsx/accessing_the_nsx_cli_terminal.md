---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/accessing-the-nsx-cli-terminal.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Accessing the NSX CLI Terminal
---

# Accessing the NSX CLI Terminal

After logging into the root shell of an ESX host, you can do one of the following:

- Use a singleton NSX CLI directly from the root shell by
  running the nsxcli –c <cmd-to-run> command.
- Go into interactive mode by running
  the nsxcli command.

  The NSX Syslog directory on the
  ESX host is
  /var/log/nsx-syslog.