---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   VMware Infrastructure Health Account in VCF Operations
---

# VMware Infrastructure Health Account in VCF Operations

The VMware Infrastructure Health monitors the VCF platform applications and provides metrics for their health and efficiency. With its dashboards, you can track monitor the overall health and configuration of the accounts, their applications, and services. Applications discovered by this management pack are listed in the applications section.

VMware Infrastructure Health is activated by default and a new VMware Infrastructure Health account is created for each new node and cloud proxy in . The VMware Infrastructure Health account monitors the health of the VCF platform accounts including VCF.

VMware Infrastructure Health in VCF Operations monitors the following accounts.

1. VCF
2. VCF Operations for logs (managed by VCF Operations fleet management)
3. VCF Operations for networks
4. vCenter
5. NSX
6. vSAN
7. VCF Automation Orchestrator
8. VCF Automation (version 8.x)
9. VCF Operations
10. VMware Live Site Recovery
11. VCF Operations fleet management

The VMware Infrastructure Health focuses mainly on the operations of the VCF platform and is integrated with it to provide an understanding of the availability, services, virtual machines, certificates, passwords, and active alerts through the VCF Operations page. You can view the account specific and domain specific data for VCF.

## Limitations

VMware Infrastructure Health monitors VCF Operations for networks and VCF Automation (version 8.x) accounts that are in warning state. VMware Infrastructure Health does not monitor any other accounts that are in the warning state.

Starting from VCF Operations 9.0, VMware Infrastructure Health monitors vCenter instances that are in the stopped state.