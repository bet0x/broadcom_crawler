---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/checklist-summary-for-vsan-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Checklist Summary for vSAN Network
---

# Checklist Summary for vSAN Network

Use the checklist summary to verify your vSAN network requirements.

- Check if you use shared 10 GbE NIC or dedicated 1GbE NIC. All-flash clusters require 10 GbE NICs.
- Verify that redundant NIC teaming connections are configured.
- Verify that flow control is enabled on the ESX host NICs.
- Verify that VMkernel port for vSAN network traffic is configured on each host.
- Verify that you have identical VLAN, MTU and subnet across all interfaces.
- Verify that you can run vmkping successfully between all hosts. Use the health service to verify.
- If you use jumbo frames, verify that you can run vmkping successfully with 9000 packet size between all hosts. Use the health service to verify.
- Ensure that the physical switch can meet vSAN requirements (flow control and feature interoperability).
- Verify that the network does not have performance issues, such as excessive dropped packets or pause frames.
- Verify that network limits are within acceptable margins.
- Test vSAN network performance with iperf, and verify that it meets expectations.