---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/log-files.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Accessing the VMware Cloud Foundation Upgrade Log Files
---

# Accessing the VMware Cloud Foundation Upgrade Log Files

You can check the log files for failed upgrades to help troubleshoot and resolve issues.

1. SSH in to the SDDC Manager appliance with the vcf user name and enter the password.
2. To access upgrade logs, navigate to the /var/log/vmware/vcf/lcm directory.
   - lcm-debug log file contains debug level logging information.
   - lcm.log contains information level logging.

     Once SDDC Manager is upgraded to 9.0, all logging information will be sent to the lcm-debug log file and lcm.log will no longer be updated.