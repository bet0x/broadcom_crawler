---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-management-domain/shut-down-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down VCF Operations
---

# Shut Down VCF Operations

You shut down VCF Operations by first taking the cluster offline and then shutting down the appliances of the VCF Operations cluster.

1. Log in to the VCF Operations administration interface at https://<vcf\_operations\_fqdn>/admin as a user with the Administrator role.
2. Take the VCF Operations cluster offline.
   1. On the System status page, click Take cluster offline.
   2. In the Take cluster offline dialog box, provide the reason for the shutdown and click OK.

      This operation might take about an hour to complete.
3. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
4. Shut down VCF Operations.
   1. In the VMs and Templates inventory, locate a VCF Operations appliance.
   2. Right-click the appliance and select PowerShut down Guest OS.
   3. In the confirmation dialog box, click Yes.

      This operation takes several minutes to complete.
   4. Repeat the steps for the remaining VCF Operations appliances.