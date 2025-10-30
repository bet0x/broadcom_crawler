---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/device-management-in-a-vsan-cluster/working-with-individual-devices-in-vsan-cluster/using-led-indicators-in-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >  Using Locator LEDs in vSAN
---

# Using Locator LEDs in vSAN

You can use
locator LEDs to identify the location of storage devices.

vSAN can light
the locator LED on a failed device so that you can easily identify the device.
This is particularly useful when you are working with multiple hot plug and
host swap scenarios.

Consider using I/O storage
controllers with pass-through mode, because controllers with RAID 0 mode
require additional steps to enable the controllers to recognize locator LEDs.

For information about
configuring storage controllers with RAID 0 mode, see your vendor
documentation.