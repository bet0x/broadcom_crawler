---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/configuring-and-managing-vmrc/set-vmrc-console-display-resolution.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Set VMRC Console Display Resolution
---

# Set VMRC Console Display Resolution

You can configure display resolution preferences that determine how a virtual machine is displayed after resizing the VMRC window.

You change display resolution by resizing the window. This action works only if VMware Tools is installed and up-to-date in the target virtual machine.

1. In a web browser, go to vmrc://settings and click Open Link. A dialog window appears. If VMRC was already opened:

   1. On Windows, select VMRC > Preferences.
   2. On MacOS, select VMware Remote Console > Settings.
   3. On Linux, select File > Remote Console Preferences.
2. Click Display.
3. Choose your preferred VM Window Resize setting.

| Option Name | Preference Type | Description |
| --- | --- | --- |
| Resize the virtual machine and the window. | Autofit Guest | The virtual machine display resolution will resize to fit the window. |
| Stretch the virtual machine in the window. | Stretch Mode | The virtual machine display will stretch to fill the window, but not change the resolution. |

These display resolution preferences apply to both normal window and full screen mode.