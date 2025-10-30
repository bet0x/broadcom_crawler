---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore/create-a-snapshot.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Create a Snapshot Before You Upgrade VCF Operations
---

# Create a Snapshot Before You Upgrade VCF Operations

Create a snapshot of each node in a cluster before you update a VCF Operations cluster. After the update completes, you must delete the snapshot to avoid performance degradation.

For more information about snapshots, see the vSphere Virtual Machine Administration documentation.

1. Log in to the VCF Operations Administrator interface at https://<primary-node-FQDN-or-IP-address>/admin.
2. Click Take Offline under the cluster status.
3. When all nodes are offline, open the vSphere client.
4. Right-click a VCF Operations virtual machine.
5. Click Snapshot and then click Take Snapshot. 
   1. Name the snapshot. Use a meaningful name such as "Pre-Update."
   2. Deselect the Snapshot the Virtual Machine Memory check box.
   3. Deselect the Ensure Quiesce Guest File System (Needs VMware Tools installed) check box.
   4. Click OK.
6. Repeat these steps for each node in the cluster.

Start the update process as described in [Install a Software Update](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-backup-and-restore/install-a-software-update.html#GUID-1ce55bb8-a253-43a1-8305-43468d0e9fdc-en).