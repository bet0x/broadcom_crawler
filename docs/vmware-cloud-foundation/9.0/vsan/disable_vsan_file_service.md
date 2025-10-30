---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/disable-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Disable vSAN File Service
---

# Disable vSAN File Service

You can disable vSAN file service.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Services.
4. On the File Service row, click Edit > Disable.

   The Disable File Service wizard opens.
5. Click Disable.

   - If you disable file service with existing file shares, the file service domain will not be deleted. File shares remain stored in the vSAN datastore, and their configuration is preserved for future use.
   - If you disable file service without existing file shares, the empty file service domains without any active file shares gets automatically cleaned up. This ensures that your vSAN environment remains free of unused or orphaned domains, with optimized system performance and resource usage.