---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-cloud-foundation.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   VMware Cloud Foundation Account in VCF Operations
---

# VMware Cloud Foundation Account in VCF Operations

In VMware Cloud Foundation a VCF domain is a policy-based resource construct with specific availability and performance attributes. It combines compute (vSphere), storage (vSAN), networking (NSX), and VCF Operations fleet management to form a single consumable entity that creates logical resource pools across compute, storage, and networking.

A VCF domain consists of one or more vSphere clusters, provisioned automatically by the VCF Operations fleet management (SDDC Manager). There are two types of VCF domains - the management domain and the workload domain.

The management domain contains the VMware Cloud Foundation management components which include an instance of vCenter and a single or three node NSX cluster for the management domain. It can use vSAN, VMFS on FC, or NFS storage.

The workload domain is created for user workloads. For each workload domain, you can choose the storage option (vSAN, NFS, FC, iSCSI). A workload domain can consist of one or more vSphere clusters. Each cluster must start with a minimum of three hosts and can scale up to a maximum of 64 hosts. The VCF Operations fleet management (SDDC Manager) automates the creation of the workload domain and the underlying vSphere cluster(s).

For the first workload domain in your environment, the SDDC Manager deploys a vCenter and a single or three node NSX cluster in the management domain. For each subsequent workload domain, the SDDC Manager deploys an additional vCenter. New workload domains can share the same NSX cluster with the existing workload domain, or deploy a new NSX cluster. However, workload domains cannot share the management domain's NSX cluster.

Configure the VCF account in VCF Operations to monitor these constructs of VCF.