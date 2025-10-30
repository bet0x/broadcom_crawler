---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/vsan-network-characteristics/using-unicast-in-vsan-network/query-unicast-with-esxcli/view-the-vsan-network-information.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > View the vSAN Network Information
---

# View the vSAN Network Information

Use the esxcli vsan network list command to view the vSAN network information such as the VMkernel interface that vSAN uses for communication, the unicast port (12321), and the traffic type (vSAN or witness) associated with the vSAN interface.

1. Run the esxcli vsan network list command.

```
Interface
  VmkNic Name: vmk1
  IP Protocol: IP
  Interface UUID: e290be58-15fe-61e5-1043-246e962c24d0
  Agent Group Multicast Address: 224.2.3.4
  Agent Group IPv6 Multicast Address: ff19::2:3:4
  Agent Group Multicast Port: 23451
  Master Group Multicast Address: 224.1.2.3
  Master Group IPv6 Multicast Address: ff19::1:2:3
  Master Group Multicast Port: 12345
  Host Unicast Channel Bound Port: 12321
  Multicast TTL: 5 
  Traffic Type: vsan
```

This output also displays the vmkernal interface used for vSAN, and vSAN traffic type. While the output displays muticast, it is no longer used for vSAN communication and can be ignored.