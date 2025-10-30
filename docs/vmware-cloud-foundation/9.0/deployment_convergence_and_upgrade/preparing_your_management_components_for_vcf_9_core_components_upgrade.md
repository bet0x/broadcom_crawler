---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Preparing Your Management Components for VCF 9 Core Components Upgrade
---

# Preparing Your Management Components for VCF 9 Core Components Upgrade

Before you can proceed with the upgrade of core components, there are mandatory management components required on version 9 and optional upgrade tasks depending on your current infrastructure.

You must have the following components (either upgraded or deployed) on version 9:

- VCF Operations
- VCF Operations fleet management appliance
- VCF Operations collector (cloud proxy) appliance (for new deployments, deploy after the SDDC Manager upgrade)

Optional component upgrades:

- VMware Aria Automation / VCF Automation
- VMware Aria Automation Orchestrator / VCF Operations orchestrator
- VMware Aria Operations for Networks / VCF Operations for networks

Components that do not support upgrade to version 9 and must be re-deployed later:

- VMware Aria Operations for Logs / VCF Operations for logs