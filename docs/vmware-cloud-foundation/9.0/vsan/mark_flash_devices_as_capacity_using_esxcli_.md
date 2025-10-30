---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/preparing-a-new-or-existing-cluster-for-virtual-san/preparing-storage-devices/mark-flash-devices-as-capacity-using-esxcli.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Mark Flash Devices as Capacity Using ESXCLI 
---

# Mark Flash Devices as Capacity Using ESXCLI

You can manually mark the flash devices on each host as capacity devices using esxcli.

Verify that you are using vSAN 9.0 or later.

1. To learn the name of the flash device that you want to mark as capacity, run the following command on each host. 
   1. In the ESX Shell, run the esxcli storage core device list command.
   2. Locate the device name at the top of the command output and write the name down.

   The command takes the following options:

   Command Options



   | Options | Description |
   | --- | --- |
   | -d|--disk=str | The name of the device that you want to tag as a capacity device. For example, mpx.vmhba1:C0:T4:L0 |
   | -t|--tag=str | Specify the tag that you want to add or remove. For example, the capacityFlash tag is used for marking a flash device for capacity. |

   The command lists all device information identified by ESX.
2. In the output, verify that the Is SSD attribute for the device is true.
3. To tag a flash device as capacity, run the esxcli vsan storage tag add -d <device name> -t capacityFlash command. 

   For example, the esxcli vsan storage tag add -t capacityFlash -d mpx.vmhba1:C0:T4:L0 command, where mpx.vmhba1:C0:T4:L0 is the device name.
4. Verify whether the flash device is marked as capacity. 
   1. In the output, identify whether the IsCapacityFlash attribute for the device is set to 1.

Command Output

You can run the vdq -q -d <device name> command to verify the IsCapacityFlash attribute. For example, running the vdq -q -d mpx.vmhba1:C0:T4:L0 command, returns the following output.

```
\{
"Name"     : "mpx.vmhba1:C0:T4:L0",
"VSANUUID" : "",
"State"    : "Eligible for use by VSAN",
"ChecksumSupport": "0",
"Reason"   : "None",
"IsSSD"    : "1",
"IsCapacityFlash": "1",
"IsPDL"    : "0",
    \},
```