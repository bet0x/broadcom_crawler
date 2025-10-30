---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/distributed-load-balancer/supported-features.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Supported Features
---

# Supported Features

Supported features by Distributed Load Balancer (DLB).

## IDPS and Anti-malware Prevention

On the SecurityIDS/IPS & Anti-malware page, create a distributed firewall rule where destination is DLB pool server members and apply an IDPS security profile in the Detect Only or Detect and Prevent mode. Any traffic destined to the selected DLB pool server group is first processed by IDPS. If IDPS does not detect any malware it redirects traffic to the DLB pool servers.