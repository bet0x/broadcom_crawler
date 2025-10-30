---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/using-led-indicators-in-vsan/enable-and-disable-locator-leds.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Locator LEDs
---

# Locator LEDs

You can turn locator LEDs on vSAN storage devices on or off. When you turn on the locator LED, you can identify the location of a specific storage device.

- Verify that you have installed the supported drivers for storage I/O controllers that enable this feature. For information about the drivers that are certified by Broadcom, see the Brodcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.
- In some cases, you might need to use third-party utilities to configure the Locator LED feature on your storage I/O controllers. For example, when you are using HP you should verify that the HP SSA CLI is installed.

When you no longer need a visual alert on your vSAN devices, you can turn off locator LEDs on the selected devices.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Disk Management.
4. Select a host to view the list of devices.
5. At the bottom of the page, select one or more storage devices from the list, and perform the desired action for the locator LEDs. 

   Option | Action || Turn on LED | Turns on locator LED on the selected storage device. You also can use the Manage tab and click Storage > Storage Devices. |
   | Turn off LED | Turns off locator LED on the selected storage device. You also can use the Manage tab and click Storage > Storage Devices. |