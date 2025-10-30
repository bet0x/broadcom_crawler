---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/vmware-cloud-foundation-operations-vm-level-restore/verify-vcf-operations-integration-state.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Verify VCF Operations State
---

# Verify VCF Operations State

After a successful restore of VCF Operations, you verify the state of the analytics cluster and each integration adapter

The cluster should be online and all integration adapters should be in a collecting state.

1. Verify the VCF Operations cluster state.
   1. Log in to the VCF Operations admin console at https://vcf\_ops\_primary-node-fqdn/admin/ with the admin user.
   2. On the system status page, verify that all nodes are in a Running state and their status is Online.
   3. Navigate to Cloud Proxies and verify that the Health Status for each cloud proxy is Healthy.
2. Verify the VCF Operations integration adapters state.
   1. Log in to the VCF Operations interface at https://vcf\_ops\_primary-node-fqdn/ as a user assigned Administrator role.
   2. Navigate to AdministrationIntegrations.
   3. Expand each integration and ensure their status is OK.