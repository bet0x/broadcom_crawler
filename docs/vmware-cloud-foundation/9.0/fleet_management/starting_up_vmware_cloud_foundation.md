---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Starting Up VMware Cloud Foundation
---

# Starting Up VMware Cloud Foundation

To maintain the components integration and avoid operation faults, you follow a specified order to start up the management virtual machines in VMware Cloud Foundation.

- Verify that external services such as Storage, Active Directory, DNS, NTP, SMTP, and FTP or SFTP are available.
- If a vSphere Storage APIs for Data Protection (VADP) based backup solution is deployed on the default management cluster, verify that the solution is properly started and operational according to the vendor guidance.

You start the management components for the management domain first. Then, you start the management components for the workload domains and the customer workloads.

If the NSX Manager cluster and NSX Edge cluster are shared with other workload domains, start the other workload domains first. Start up NSX Manager and NSX Edge nodes as part of the startup of the last workload domain.