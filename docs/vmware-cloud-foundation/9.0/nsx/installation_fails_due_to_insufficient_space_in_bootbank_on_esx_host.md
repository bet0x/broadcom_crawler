---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/installation-fails-due-to-insufficient-space-in-bootbank-on-esxi-host.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Installation Fails Due to Insufficient Space in Bootbank on ESX Host
---

# Installation Fails Due to Insufficient Space in Bootbank on ESX Host

NSX installation might fail if there is insufficient space in the bootbank or in the alt-bootbank on an ESX host.

On the ESX host, you might see a similar log (esxupdate.log) message:

```
20**-**-**T13:37:50Z esxupdate: 5557508: BootBankInstaller.pyc:
ERROR: The pending transaction requires 245 MB free space,
however the maximum supported size is 239 MB.^@
```

Unused VIBs on the ESX host can be relatively large in size. These unused VIBs can result in insufficient space in the bootbank or in the alt-bootbank when installing the required VIBs.

- Uninstall the VIBs that are no longer required and free up additional disk space.

For more information on deleting the unused VIBs, see Knowledge Base article 324231: [NSX VIBs fail to install/upgrade, due to insufficient space in bootbank on ESX host](https://knowledge.broadcom.com/external/article?articleNumber=324231).