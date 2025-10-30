---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/transport-node-installation-failure-due-to-pending-reboot.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node Installation Failure Due To Pending Reboot 
---

# Transport Node Installation Failure Due To Pending Reboot

Transport Node install task fails
due to pending reboot.

This issue occurs if host is pending
reboot from previous installation or upgrade of vibs on the host.

1. Run
   following CLI on the host as root to verify.

   vim-cmd hostsvc/hostsummary|grep -i reboot requireSecureBoot =
   <unset>, rebootRequired = true 

   If
   rebootRequired is set to true,
   reboot the host and then try installation of NSX modules again on the
   host.