---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/preparing-storage-devices/untag-flash-devices-used-as-capacity-using-esxcli.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Untag Flash Devices Used as Capacity Using ESXCLI
---

# Untag Flash Devices Used as Capacity Using ESXCLI

You can untag
flash devices that are used as capacity devices, so that they are available for
caching.

1. To untag a flash
   device marked as capacity, run the
   esxcli vsan
   storage tag remove -d <device name> -t capacityFlash command.
   For example, the
   esxcli vsan
   storage tag remove -t capacityFlash -d mpx.vmhba1:C0:T4:L0 command,
   where
   mpx.vmhba1:C0:T4:L0 is
   the device name.
2. Verify whether the
   flash device is untagged.
   1. In the output,
      identify whether the
      IsCapacityFlash
      attribute for the device is set to
      0.

Command
Output

You can run the
vdq -q -d
<device name> command to verify the
IsCapacityFlash
attribute. For example, running the
vdq -q -d
mpx.vmhba1:C0:T4:L0 command, returns the following output.

```
[
    \{
"Name"     : "mpx.vmhba1:C0:T4:L0",
"VSANUUID" : "",
"State"    : "Eligible for use by VSAN",
"ChecksumSupport": "0",
"Reason"   : "None",
"IsSSD"    : "1",
"IsCapacityFlash": "0",
"IsPDL"    : "0",
    \},
```