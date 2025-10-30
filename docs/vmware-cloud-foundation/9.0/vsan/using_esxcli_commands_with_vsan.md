---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/using-esxcli-commands-with-vsan.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Using Esxcli Commands with vSAN
---

# Using Esxcli Commands with vSAN

Use Esxcli commands to obtain
information about vSAN OSA or vSAN ESA and to
troubleshoot your vSAN environment.

The following commands are available:

| Command | Description |
| --- | --- |
| esxcli vsan network list | Verify which VMkernel adapters are used for vSAN communication. |
| esxcli vsan storage list | List storage disks claimed by vSAN. |
| esxcli vsan storagepool list | List storage pool claimed by vSAN ESA. This command is applicable only for vSAN ESA cluster. |
| esxcli vsan cluster get | Get vSAN cluster information. |
| esxcli vsan health | Get vSAN cluster health status. |
| esxcli vsan debug | Get vSAN cluster debug information. |

The
esxcli vsan
debug commands can help you debug and troubleshoot the
vSAN cluster,
especially when
vCenter
is not available.

Use:
esxcli vsan debug
{cmd} [cmd options]

Debug commands:

| Command | Description |
| --- | --- |
| esxcli vsan debug disk | Debug vSAN physical disks. |
| esxcli vsan debug object | Debug vSAN objects. |
| esxcli vsan debug resync | Debug vSAN resyncing objects. |
| esxcli vsan debug controller | Debug vSAN disk controllers. |
| esxcli vsan debug limit | Debug vSAN limits. |
| esxcli vsan debug vmdk | Debug vSAN VMDKs. |

Example
esxcli vsan
debug commands:

```
esxcli vsan debug disk summary get
   Overall Health: green
   Component Metadata Health: green
   Memory Pools (heaps): green
   Memory Pools (slabs): green
```

```
esxcli vsan debug disk list
UUID: 52e1d1fa-af0e-0c6c-f219-e5e1d224b469
   Name: mpx.vmhba1:C0:T1:L0
   SSD: False
   Overall Health: green
   Congestion Health:
         State: green
         Congestion Value: 0
         Congestion Area: none
   In Cmmds: true
   In Vsi: true
   Metadata Health: green
   Operational Health: green
   Space Health:
         State: green
         Capacity: 107365793792 bytes
         Used: 1434451968 bytes
         Reserved: 150994944 bytes
```

```
esxcli vsan debug object health summary get
    Health Status                                     Number Of Objects
    ------------------------------------------------  -----------------
    reduced-availability-with-no-rebuild-delay-timer                  0
    reduced-availability-with-active-rebuild                          0
    inaccessible                                                      0
    data-move                                                         0
    healthy                                                           1
    nonavailability-related-incompliance                              0
    nonavailability-related-reconfig                                  0
    reduced-availability-with-no-rebuild                              0
```

```
esxcli vsan debug object list
    Object UUID: 47cbdc58-e01c-9e33-dada-020010d5dfa3
       Version: 5
       Health: healthy
       Owner:
       Policy:
          stripeWidth: 1
          CSN: 1
          spbmProfileName: vSAN Default Storage Policy
          spbmProfileId: aa6d5a82-1c88-45da-85d3-3d74b91a5bad
          forceProvisioning: 0
          cacheReservation: 0
          proportionalCapacity: [0, 100]
          spbmProfileGenerationNumber: 0
          hostFailuresToTolerate: 1

       Configuration:
          RAID_1
             Component: 47cbdc58-6928-333f-0c51-020010d5dfa3
               Component State: ACTIVE,  Address Space(B): 273804165120 (255.00GB),  
               Disk UUID: 52e95956-42cf-4d30-9cbe-763c616614d5, Disk Name: mpx.vmhba1..
               Votes: 1,  Capacity Used(B): 373293056 (0.35GB), 
               Physical Capacity Used(B): 369098752 (0.34GB),  Host Name: sc-rdops...
             Component: 47cbdc58-eebf-363f-cf2b-020010d5dfa3
               Component State: ACTIVE,  Address Space(B): 273804165120 (255.00GB),  
               Disk UUID: 52d11301-1720-9901-eb0a-157d68b3e4fc,  Disk Name: mpx.vmh...
               Votes: 1,  Capacity Used(B): 373293056 (0.35GB),  
               Physical Capacity Used(B): 369098752 (0.34GB),  Host Name: sc-rdops-vm..
          Witness: 47cbdc58-21d2-383f-e45a-020010d5dfa3
            Component State: ACTIVE,  Address Space(B): 0 (0.00GB),  
            Disk UUID: 52bfd405-160b-96ba-cf42-09da8c2d7023,  Disk Name: mpx.vmh...
            Votes: 1,  Capacity Used(B): 12582912 (0.01GB),  
            Physical Capacity Used(B): 4194304 (0.00GB),  Host Name: sc-rdops-vm...
    
       Type: vmnamespace
       Path: /vmfs/volumes/vsan:52134fafd48ad6d6-bf03cb6af0f21b8d/New Virtual Machine
       Group UUID: 00000000-0000-0000-0000-000000000000
       Directory Name: New Virtual Machine
```

```
esxcli vsan debug controller list
    Device Name: vmhba1
       Device Display Name: LSI Logic/Symbios Logic 53c1030 PCI-X Fusion-MPT Dual Ult..
       Used By VSAN: true
       PCI ID: 1000/0030/15ad/1976
       Driver Name: mptspi
       Driver Version: 4.23.01.00-10vmw
       Max Supported Queue Depth: 127
```

```
esxcli vsan debug limit get
       Component Limit Health: green
       Max Components: 750
       Free Components: 748
       Disk Free Space Health: green
       Lowest Free Disk Space: 99 %
       Used Disk Space: 1807745024 bytes
       Used Disk Space (GB): 1.68 GB
       Total Disk Space: 107365793792 bytes
       Total Disk Space (GB): 99.99 GB
       Read Cache Free Reservation Health: green
       Reserved Read Cache Size: 0 bytes
       Reserved Read Cache Size (GB): 0.00 GB
       Total Read Cache Size: 0 bytes
       Total Read Cache Size (GB): 0.00 GB
```

```
esxcli vsan debug vmdk list
    Object: 50cbdc58-506f-c4c2-0bde-020010d5dfa3
       Health: healthy
       Type: vdisk
       Path: /vmfs/volumes/vsan:52134fafd48ad6d6-bf03cb6af0f21b8d/47cbdc58-e01c-9e33-
             dada-020010d5dfa3/New Virtual Machine.vmdk
       Directory Name: N/A
```

```
esxcli vsan debug resync list
   Object            Component              Bytes Left To Resync  GB Left To Resync
   ----------------  ---------------------  --------------------  -----------------
   31cfdc58-e68d...  Component:23d1dc58...             536870912  0.50
   31cfdc58-e68d...  Component:23d1dc58...            1073741824  1.00
   31cfdc58-e68d...  Component:23d1dc58...            1073741824  1.00
```