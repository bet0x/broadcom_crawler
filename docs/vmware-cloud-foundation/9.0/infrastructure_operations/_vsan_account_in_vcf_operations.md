---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsan-overview.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   vSAN Account in VCF Operations
---

# vSAN Account in VCF Operations

You can make vSAN operational in a production environment by using dashboards to evaluate, manage, and optimize the performance of vSAN objects and vSAN-activated objects in your vCenter system.

vSAN extends the following features:

- Discovers vSAN disk groups in a vSAN datastore.
- Identifies the vSAN-activated cluster compute resource, host system, and datastore objects in a vCenter system.
- Automatically adds related vCenter components that are in the monitoring state.
- Support for vSAN datastores in workload optimization with cross-cluster rebalance actions.

  - You can move VMs from one vSAN datastore to another vSAN datastore.
  - You can optimize the container if all the vSAN clusters are not in resync state.
  - VMs with different storage policies for each disk or VMs with different types of storage for each disk will not be moved.
  - You can generate a re-balance plan only if sufficient disk space is available at the destination vSAN datastore (The vSAN datastore slack space will also be considered).
  - The storage policy assigned to the VM will be considered during the workload optimization (Compatibility check is performed against the storage policy).
  - VM migration from vSAN datastore to vSAN stretched clusters is not supported.