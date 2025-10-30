---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/remove-nsx-t-extension-from-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Remove NSX Extension from vCenter
---

# Remove NSX Extension from vCenter

When you add a compute manager, NSX Manager adds its identity as an extension in vCenter. If you remove the compute manager, the extension in vCenter will be removed automatically. If the extension is not removed for some reason, you can maually remove the extension with the following procedure.

1. Log in to the MOB at https://<vCenter hostname or IP address>/mob.
2. Click the content link, which is the value for the content property in the Properties table.
3. Click the ExtensionManager link, which is the value for extensionManager property in the Properties table.
4. Click the UnregisterExtension link in the Methods table.
5. Enter com.vmware.nsx.management.nsxt in the value text field.
6. Click the Invoke Method link on the right hand side of the page below the Parameters table. 

   The method result says void but the extension will be removed.
7. To make sure the extension is removed, click the FindExtension method on the previous page and invoke it by entering the same value for the extension. 

   The result should be void.