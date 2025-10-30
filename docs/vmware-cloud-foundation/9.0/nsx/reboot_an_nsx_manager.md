---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/reboot-nsx-manager-cluster-members.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Reboot an NSX Manager
---

# Reboot an NSX Manager

You can reboot an
NSX Manager
with a CLI command to recover from critical errors.

If you need to reboot multiple
NSX Managers,
you must reboot them one at a time. Wait for the rebooted
NSX Manager to
be online before rebooting another.

1. Log in to the CLI
   of the
   NSX Manager.
2. Run the following
   command.

   ```
   nsx-manager> reboot
   Are you sure you want to reboot (yes/no): y
   ```