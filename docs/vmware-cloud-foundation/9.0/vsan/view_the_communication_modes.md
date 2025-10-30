---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/query-unicast-with-esxcli/view-the-communication-modes.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View the Communication Modes
---

# View the Communication Modes

Using esxcli vsan cluster get command, you can view the CMMDS mode of the vSAN cluster node.

1. Run the esxcli vsan cluster get command.

```
Cluster Information
   Enabled: true
   Current Local Time: 2025-05-08T09:08:05Z
   Local Node UUID: 6813878b-163d-3a33-cc63-0050569c4bac
   Local Node Type: NORMAL
   Local Node State: MASTER
   Local Node Health State: HEALTHY
   Sub-Cluster Master UUID: 6813878b-163d-3a33-cc63-0050569c4bac
   Sub-Cluster Backup UUID: 6813878b-f828-8805-6e39-0050569c8100
   Sub-Cluster UUID: 52fafd2f-885a-912b-123d-29320735129c
   Sub-Cluster Membership Entry Revision: 17
   Sub-Cluster Member Count: 16
   Sub-Cluster Member UUIDs: 6813878b-163d-3a33-cc63-0050569c4bac, 68138792-d6cb-49f1-24d4-0050569c8d7d, 6813878c-1ae0-1798-21ba-0050569c8c1a, 68138791-7d9b-c043-b0e7-0050569c74f8, 6813878b-5ec9-b6d7-70ce-0050569c37d1, 6813878b-d309-023b-2c66-0050569ccf58, 6813878c-9879-9875-2cf0-0050569c5f2f, 6813878b-d7b2-c9f1-ce14-0050569ce307, 6813878b-f828-8805-6e39-0050569c8100, 6813878c-aab3-3810-65dc-0050569c55f1, 68138797-2924-1613-be3b-0050569cfe64, 68138793-f8bc-f72f-1e0d-0050569ce100, 68138791-58f8-8831-8403-0050569c8cfb, 6813878b-ae9c-6346-d735-0050569c73af, 68138782-b02a-785a-4b5e-0050569ce4b4, 681512d1-f5d1-c10e-8b0c-0050569cf5e5
   Sub-Cluster Member HostNames: sfo01-m01-r01-esx01.sfo.rainpole.io, sfo01-m01-r01-esx02.sfo.rainpole.io, sfo01-m01-r01-esx03.sfo.rainpole.io, sfo01-m01-r01-esx04.sfo.rainpole.io, sfo01-m01-r01-esx05.sfo.rainpole.io, sfo01-m01-r01-esx06.sfo.rainpole.io, sfo01-m01-r01-esx07.sfo.rainpole.io, sfo01-m01-r01-esx08.sfo.rainpole.io, sfo02-m01-r01-esx08.sfo.rainpole.io, sfo02-m01-r01-esx07.sfo.rainpole.io, sfo02-m01-r01-esx04.sfo.rainpole.io, sfo02-m01-r01-esx06.sfo.rainpole.io, sfo02-m01-r01-esx03.sfo.rainpole.io, sfo02-m01-r01-esx02.sfo.rainpole.io, sfo02-m01-r01-esx05.sfo.rainpole.io, sfo-m01-cl01-vsw01.sfo.rainpole.io
   Sub-Cluster Membership UUID: f89b1468-4c6d-7ebf-2a19-0050569c929a
   Unicast Mode Enabled: true
   Maintenance Mode State: OFF
   Config Generation: a90bad14-6d09-4a42-b001-5137386ff625 9 2025-05-08T03:05:15.343
   Mode: REGULAR
   vSAN ESA Enabled: true
   vSAN Max Client Network Enabled: false
```