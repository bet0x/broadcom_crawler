---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-nsx-edge-nodes/edge-mpa-connectivity-down.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge MPA Connectivity Down
---

# NSX Edge MPA Connectivity Down

The NSX Edge MPA connectivity Down due to infrastructure service crash.

NSX Edge node disks being full or memory leak can cause certain processes to crash and lead to this failure. Admin cli get managers may return active manager node (if crash occurred post successful manager registration) and admin cli get controller will give error Failed to get controller list.

1. Run admin cli get diagnosis config or GET API /api/v1/transport-nodes/{transport-node-id}/node/diagnosis to diagnose failures related to health of NSX Edge nodes that are caused when services go down.
2. Run admin cli get cores-dumps to see if any cores got generated (in /var/core or /image/core) due to service crash. If core dump is seen, run cmd top -o %MEM as root to see which nsx process is consuming too much memory and admin cli get filesystem-stats to verify if partitions used by nsx is not full or close to full.
3. Run root cli /etc/init.d/nsx-proxy | nsx-nestdb status to get status of infrastructure services running on the NSX Edge node.
4. Clean up the disk space, then start any stopped infrastructure services on the host by issuing command /etc/init.d/<service-name> start (as a temporary workaround). Open support case with VMware if any cores are seen.