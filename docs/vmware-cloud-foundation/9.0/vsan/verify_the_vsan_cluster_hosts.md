---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/query-unicast-with-esxcli/verify-the-vsan-cluster-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Verify the vSAN Cluster Hosts
---

# Verify the vSAN Cluster Hosts

Use the esxcli vSAN cluster unicastagent list command to list the unicast communications details

1. Run the esxcli vsan cluster unicastagent list command.

```
NodeUuid                              IsWitness  Supports Unicast  IP Address     Port  Iface Name  Cert Thumbprint                                                                                  SubClusterUuid                        Traffic Type
------------------------------------  ---------  ----------------  ------------  -----  ----------  -----------------------------------------------------------------------------------------------  ------------------------------------  ------------
6813878b-f828-8805-6e39-0050569c8100          0              true  10.12.13.108  12321              D8:14:DA:80:2F:0C:0E:0C:BD:40:89:24:70:3D:33:EE:62:0B:6E:7C:4F:8D:D3:06:88:46:39:DD:E7:15:9D:0F  52fafd2f-885a-912b-123d-29320735129c  vsan
681512d1-f5d1-c10e-8b0c-0050569cf5e5          1              true  10.21.10.218  12321              A7:02:80:3B:64:8F:9A:AB:29:6B:54:3E:C1:76:01:3E:00:A2:DE:80:F4:78:7B:6C:E8:B9:3A:4A:77:4B:0F:38  52fafd2f-885a-912b-123d-29320735129c
6813878c-aab3-3810-65dc-0050569c55f1          0              true  10.12.13.107  12321              45:2E:E7:40:9E:0B:5D:87:18:2E:8E:C6:86:86:97:B1:B5:6E:79:57:C2:9E:21:3C:5F:4B:76:D3:3B:72:64:1B  52fafd2f-885a-912b-123d-29320735129c  vsan
68138797-2924-1613-be3b-0050569cfe64          0              true  10.12.13.104  12321              ED:97:72:FA:A0:52:6E:17:61:97:8C:3D:6F:CC:CB:49:98:56:97:AA:8B:9B:BE:47:D0:4A:35:A2:0E:95:FA:6C  52fafd2f-885a-912b-123d-29320735129c  vsan
68138793-f8bc-f72f-1e0d-0050569ce100          0              true  10.12.13.106  12321              86:99:32:7A:20:4A:D2:B3:B3:A9:6D:BE:60:A3:26:5B:83:EB:49:34:76:FB:7A:5B:EE:0E:54:FB:DC:AC:BE:74  52fafd2f-885a-912b-123d-29320735129c  vsan
68138791-58f8-8831-8403-0050569c8cfb          0              true  10.12.13.103  12321              B2:4F:11:0E:98:07:80:45:F2:F2:06:C9:D9:89:57:FA:8D:3C:2B:E3:A5:25:5C:2B:A5:D8:5A:17:6F:87:0D:7C  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878b-d309-023b-2c66-0050569ccf58          0              true  10.11.13.106  12321              E2:D6:36:BE:C8:D5:A2:F0:42:41:EF:9F:4C:D2:AD:67:6C:54:4E:3A:50:B3:B3:7C:35:54:A2:B7:3F:C9:5B:11  52fafd2f-885a-912b-123d-29320735129c  vsan
68138791-7d9b-c043-b0e7-0050569c74f8          0              true  10.11.13.104  12321              21:FC:6F:56:C9:26:33:6E:8E:1E:58:7D:A2:3F:3E:38:09:96:99:61:F2:7F:AB:F1:25:C9:6C:CC:0D:6D:BB:06  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878b-ae9c-6346-d735-0050569c73af          0              true  10.12.13.102  12321              A5:47:6C:FE:2A:9A:A9:8C:08:03:34:AD:D1:E0:A9:FA:9E:17:4F:62:1F:15:D1:ED:8B:01:D8:CE:D4:D7:01:D8  52fafd2f-885a-912b-123d-29320735129c  vsan
68138782-b02a-785a-4b5e-0050569ce4b4          0              true  10.12.13.105  12321              3C:92:51:62:F5:59:A0:73:39:E5:DE:B1:A9:1F:72:1E:F7:5D:4C:48:12:76:A5:BE:9B:16:FE:05:94:2A:EA:37  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878c-9879-9875-2cf0-0050569c5f2f          0              true  10.11.13.107  12321              77:8E:F9:D1:21:6B:CD:3C:66:A2:4A:55:BE:78:30:00:E9:BD:96:6B:F8:6F:FB:1C:1F:5E:33:6C:DE:D3:4D:7E  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878c-1ae0-1798-21ba-0050569c8c1a          0              true  10.11.13.103  12321              77:24:E0:DF:64:FD:D2:B1:FD:FA:D7:5B:1B:2C:FF:12:15:99:11:CE:FB:41:84:8D:3F:57:C0:67:A1:6F:12:B3  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878c-8bcb-20c9-0429-0050569c2f06          0              true  10.12.13.101  12321              43:E4:88:EB:55:04:FF:BA:8F:BE:12:C5:52:AB:21:05:9B:2C:04:11:68:34:4B:E7:AC:BE:F7:07:A9:B3:B1:C9  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878b-5ec9-b6d7-70ce-0050569c37d1          0              true  10.11.13.105  12321              A3:FC:61:0B:C3:37:43:47:54:EA:B2:A1:9F:B4:B2:D6:A0:C0:92:F9:79:6F:FF:B8:CD:3F:48:B0:28:FC:CA:AD  52fafd2f-885a-912b-123d-29320735129c  vsan
68138792-d6cb-49f1-24d4-0050569c8d7d          0              true  10.11.13.102  12321              C1:3C:C4:B1:C1:94:A6:5B:C1:17:F5:15:39:BB:C2:2D:41:2A:1E:71:B8:0F:8D:FB:DD:96:12:70:F6:82:D4:DA  52fafd2f-885a-912b-123d-29320735129c  vsan
6813878b-d7b2-c9f1-ce14-0050569ce307          0              true  10.11.13.108  12321              20:92:8B:1B:CE:D6:7B:5D:98:89:67:CD:D8:4B:E5:43:A5:56:F3:1A:D1:51:16:02:90:E4:50:76:02:A5:29:93  52fafd2f-885a-912b-123d-29320735129c  vsan
```

The output includes the vSAN node UUID, whether the node is a data host (0) or a witness host (1), IPv4 address/IPv6 address, UDP port, certificate thumbprint, and vSAN subcluster ID and traffic type. If troubleshooting, you can use this output to identify the vSAN cluster nodes match to ensure what vCenter maintains.