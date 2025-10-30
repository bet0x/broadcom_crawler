---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/edge-bare-metal-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge Bare Metal Requirements
---

# NSX Edge Bare Metal Requirements

Before you configure the NSX Edge bare metal, make sure that your environment meets the supported requirements.

## NSX Edge Bare Metal Memory, CPU, and Disk Requirements

Minimum Requirements

| Memory | CPU Cores | Disk Space |
| --- | --- | --- |
| 32 GB | 8 | 200 GB |

Recommended Requirements

| Memory | CPU Cores | Disk Space |
| --- | --- | --- |
| 256 GB | 24 | 200 GB |

## NSX Edge Bare Metal DPDK CPU Requirements

For the DPDK support, the underlaying platform needs to meet the following requirements:

- CPU must have AES-NI capability.
- CPU must have 1 GB Huge Page support.
- NSX Edge Bare Metal supports up to 80 cores for the entire system. This means that on a server with a single socket, its CPU can have up to 80 cores. On a server with 2 sockets, each socket cannot have more than 40 cores.

| Hardware | Type |
| --- | --- |
| CPU | - Intel Xeon Platinum 9xxx, 8xxx - Intel Xeon Gold 6xxx, 5xxx - Intel Xeon Silver 4xxx - Intel Xeon Bronze 3xxx - Intel Xeon E56xx, L56xx, X56xx (Westmere-EP) - Intel Xeon E7-xxxx (Westmere-EX and later CPU generation) - Intel Xeon E5-xxxx (Sandy Bridge and later CPU generation) |
| - AMD EPYC Series processors |

## NSX Edge Bare Metal Hardware Requirements

Verify that the bare metal NSX Edge hardware is listed in this URL <https://ubuntu.com/certified?category=Server&release=22.04%20LTS&category=Server>. If the hardware is not listed, the storage, video adapter, or motherboard components might not work on the NSX Edge appliance. Bare Metal supports both UEFI and legacy BIOS modes.

## NSX Edge Bare Metal NIC Requirements

| NIC Type | Description | Vendor ID | PCI Device ID | Firmware Version |
| --- | --- | --- | --- | --- |
| Mellanox ConnectX-4 Lx EN | PCI\_DEVICE\_ID\_MELLANOX\_CONNECTX4 | 15b3 | 0x1013 | 14.24.1000 and later versions |
| Mellanox ConnectX-4 Lx | PCI\_DEVICE\_ID\_MELLANOX\_CONNECTX4LX | 15b3 | 0x1015 | 14.31.22.50 and later versions |
| Mellanox ConnectX-5 | PCI\_DEVICE\_ID\_MELLANOX\_CONNECTX5 | 15b3 | 0x1017 | 16.21.1000 and later versions |
| Mellanox ConnectX-5 EX | PCI\_DEVICE\_ID\_MELLANOX\_CONNECTX5EX | 15b3 | 0x1019 | 16.21.1000 and later versions |
| Mellanox ConnectX-6 | PCI\_DEVICE\_ID\_MELLANOX\_CONNECTX6 | 15b3 | 0x101B | 20.27.0090 and later versions |
| Mellanox ConnectX-6 Dx | PCI\_DEVICE\_ID\_MELLANOX\_CONNECTX6DX | 15b3 | 0x101D | 22.27.6008 and later versions |
| Intel X520/Intel 82599 | IXGBE\_DEV\_ID\_82599\_KX4 | 8086 | 0x10F7 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_KX4\_MEZZ | 8086 | 0x1514 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_KR | 8086 | 0x1517 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_COMBO\_BACKPLANE | 8086 | 0x10F8 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_CX4 | 8086 | 0x10F9 | 19.5.12 and later versions |
|  |  |  |  |
| IXGBE\_DEV\_ID\_82599\_SFP | 8086 | 0x10FB | 19.5.12 and later versions |
| IXGBE\_SUBDEV\_ID\_82599\_SFP | 8086 | 0x11A9 | 19.5.12 and later versions |
| IXGBE\_SUBDEV\_ID\_82599\_RNDC | 8086 | 0x1F72 | 19.5.12 and later versions |
| IXGBE\_SUBDEV\_ID\_82599\_560FLR | 8086 | 0x17D0 | 19.5.12 and later versions |
| IXGBE\_SUBDEV\_ID\_82599\_ECNA\_DP | 8086 | 0x0470 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_SFP\_EM | 8086 | 0x1507 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_SFP\_SF2 | 8086 | 0x154D | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_SFP\_SF\_QP | 8086 | 0x154A | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_QSFP\_SF\_QP | 8086 | 0x1558 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599EN\_SFP | 8086 | 0x1557 | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_XAUI\_LOM | 8086 | 0x10FC | 19.5.12 and later versions |
| IXGBE\_DEV\_ID\_82599\_T3\_LOM | 8086 | 0x151C | 19.5.12 and later versions |
| Intel X540 | IXGBE\_DEV\_ID\_X540T | 8086 | 0x1528 | n/a |
| IXGBE\_DEV\_ID\_X540T1 | 8086 | 0x1560 | n/a |
| Intel X550 | IXGBE\_DEV\_ID\_X550T | 8086 | 0x1563 | 21.5.9 and later versions |
| IXGBE\_DEV\_ID\_X550T1 | 8086 | 0x15D1 | 21.5.9 and later versions |
| IXGBE\_DEV\_ID\_X550EM\_A\_10G\_T | 8086 | 0x15C8 | 21.5.9 and later versions |
| IXGBE\_DEV\_ID\_X550EM\_A\_QSFP | 8086 | 0x15CA | 21.5.9 and later versions |
| IXGBE\_DEV\_ID\_X550EM\_A\_QSFP\_N | 8086 | 0x15CC | 21.5.9 and later versions |
| IXGBE\_DEV\_ID\_X550EM\_X\_10G\_T | 8086 | 0x15AD | 21.5.9 and later versions |
| IXGBE\_DEV\_ID\_X550EM\_X\_XFI | 8086 | 0x15B0 | 21.5.9 and later versions |
| Intel X710 | I40E\_DEV\_ID\_SFP\_X710 | 8086 | 0x1572 | 8.30 and later versions |
| I40E\_DEV\_ID\_KX\_C | 8086 | 0x1581 | 8.30 and later versions |
| I40E\_DEV\_ID\_10G\_BASE\_T | 8086 | 0x1586 | 8.30 and later versions |
| I40E\_DEV\_ID\_10G\_BASE\_T4 | 8086 | 0x1589 | 8.30 and later versions |
| I40E\_DEV\_ID\_10G\_SFP | 8086 | 0x104E | n/a |
| I40E\_DEV\_ID\_10G\_B | 8086 | 0x104F | n/a |
| Intel XL710 | I40E\_DEV\_ID\_KX\_B | 8086 | 0x1580 | 9.0 and later versions |
| I40E\_DEV\_ID\_QSFP\_A | 8086 | 0x1583 | 9.0 and later versions |
| I40E\_DEV\_ID\_QSFP\_B | 8086 | 0x1584 | 9.0 and later versions |
| I40E\_DEV\_ID\_QSFP\_C | 8086 | 0x1585 | 9.0 and later versions |
| I40E\_DEV\_ID\_20G\_KR2 | 8086 | 0x1587 | 9.0 and later versions |
| I40E\_DEV\_ID\_20G\_KR2\_A | 8086 | 0x1588 | 9.0 and later versions |
| I40E\_DEV\_ID\_10G\_BASE\_T\_BC | 8086 | 0x15FF | 9.0 and later versions |
| Intel XXV710 | I40E\_DEV\_ID\_25G\_B | 8086 | 0x158A | 9.0 and later versions |
| I40E\_DEV\_ID\_25G\_SFP28 | 8086 | 0x158B | 9.0 and later versions |
| Intel E810-C (100G) | ICE\_DEV\_ID\_E810C\_QSFP | 8086 | 0x1592 | 4.0.0 and later versions |
| Intel E810-XXV (25G) | ICE\_DEV\_ID\_E810\_XXV\_SFP | 8086 | 0x159B | 4.0.0 and later versions |
|  | ICE\_DEV\_ID\_E810\_XXV\_BACKPLANE | 8086 | 0x1599 | 4.0.0 and later versions |
|  | ICE\_DEV\_ID\_E810\_XXV\_QSFP | 8086 | 0x159A | 4.0.0 and later versions |
| Intel E810-C | ICE\_DEV\_ID\_E810C\_BACKPLANE | 8086 | 0x1591 | 4.0.0 and later versions |
|  | ICE\_DEV\_ID\_E810C\_SFP | 8086 | 0x1593 | 4.0.0 and later versions |
| Intel E822-C | ICE\_DEV\_ID\_C822N\_BACKPLANE | 8086 | 0x1890 | 3.1 and later versions |
|  | ICE\_DEV\_ID\_C822N\_QSFP | 8086 | 0x1891 | 3.1 and later versions |
|  | ICE\_DEV\_ID\_C822N\_SFP | 8086 | 0x1892 | 3.1 and later versions |
| Cisco VIC 1300 series | Cisco UCS Virtual Interface Card 1300 | 1137 | 0x0043 | n/a |
| Cisco VIC 1400 series | Cisco UCS Virtual Interface Card 1400 | 1137 | 0x0043 | n/a |

For all the supported NICs listed above, verify that the media adapters and cables you use follow the vendor's supported media types. Any media adapter or cables not supported by the vendor can result in unpredictable behavior, including the inability to boot up due to an unrecognized media adapter. See the NIC vendor documentation for information about supported media adapters and cables.

Cisco VICs: To successfully claim Cisco VICs for the NSX Edge datapath, configure multiple RX and TX queues from the Cisco UCS Manager. The number of queues configured must be sufficient for datapath to have one queue per core. For configuration details, refer to the Cisco documentation.