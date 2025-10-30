---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start VCF Operations
---

# Start VCF Operations

You start VCF Operations by first starting the appliances of the VCF Operations cluster, then taking the cluster online.

1. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
2. Start VCF Operations.
   1. Locate a VCF Operations appliance.
   2. Right-click the VCF Operations appliance and select PowerPower On.
   3. In the confirmation dialog box, click Yes.

      This operation takes several minutes to complete.
   4. Repeat the steps for the remaining VCF Operations appliances.
3. Log in to the VCF Operations administration interface at https://<vcf\_operations\_fqdn>/admin as a user with the Administrator role.
4. Take the VCF Operations cluster online.
   1. Log in to the VCF Operations administration interface at https://<vcf\_operations\_fqdn>/admin as a user with the Administrator role.
   2. On the System status page, click Bring Cluster Online.

      This operation might take about an hour to complete.