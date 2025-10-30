---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshooting-host-transport-nodes/transport-node-is-in-disconnected-state.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Transport Node status is Disconnected or Unknown
---

# Transport Node status is Disconnected or Unknown

ESX host prepared as a Transport Node status goes into
Unknown or
Disconnected
state due to lost connection to
NSX Manager.
NSX displays
the following error:
Heart beating between NSX management node and host
<uuid> is down.

Host infrastructure services being down
due to
ESX disks being full or
memory leak may result in this condition. If
ESX.

If
ESX disks are full or if there
is a memory leak, it can cause certain processes to crash and cause the transport node
to go into
Disconnected state. When you run admin cli
get managers, NSX might return active manager node if the crash
occurred post successful manager registration. When you run admin cli
get
controllers, NSX gives error
Failed to get controller
list.

1. Run admin cli
   get core-dumps to see if any cores got
   generated (in
   /var/core or /image/core) due to service
   crash.
2. If core-dump happens, run cmd
   esxtop to see which NSX process is consuming too much
   memory and
   df -h to verify disk partitions used by nsx is not
   full or close to full.
3. Run
   /etc/init.d/nsx-proxy | nsx-nestdb status to get status
   of infrastructure services on the host.
4. Clean up the disk space, then
   start any stopped infrastructure services on the host by issuing command
   /etc/init.d/<service-name> start (as a temporary
   workaround).
5. Open a support case with VMware if you see any cores.