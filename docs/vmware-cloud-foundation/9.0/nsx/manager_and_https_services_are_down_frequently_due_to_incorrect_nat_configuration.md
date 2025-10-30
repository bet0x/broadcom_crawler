---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-nsx-manager-cluster/manager-and-https-services-down-due-to-incorrect-nat-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Manager and HTTPS Services Are Down Frequently Due to Incorrect NAT Configuration
---

# Manager and HTTPS Services Are Down Frequently Due to Incorrect NAT Configuration

If
you incorrectly configured NAT, the Manager and HTTPS service might go down
frequently.

1. Do not use 0.0.0.0/0, x.0.0.0/8, x.x.0.0/16 subnet ranges in the NAT rules for
   SNAT Translated IP section (SNAT rule) and for Destination Network section (DNAT
   rule).
2. Fix the incorrect NAT configuration.
3. Configure NAT rule where IP address range and count does not exceed 256 for
   SNAT Translated IP section (SNAT rule) and for Destination Network section (DNAT
   rule).