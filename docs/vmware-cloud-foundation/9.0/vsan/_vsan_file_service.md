---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN File Service
---

# vSAN File Service

Use the vSAN file service to create file shares in the vSAN datastore that client workstations or virtual machines can access.

The data stored in a file share can be accessed from any device that has access rights. vSAN file service is a layer that sits on top of vSAN to provide file shares. It currently supports SMB, NFSv3, and NFSv4.1 file shares. vSAN file service comprises of vSAN Distributed File System (vDFS) which provides the underlying scalable filesystem by aggregating vSAN objects, a Storage Services Platform which provides resilient file server end points and a control plane for deployment, management, and monitoring. File shares are integrated into the existing vSAN Storage Policy Based Management, and on a per-share basis. vSAN file service brings in capability to host the file shares directly on the vSAN cluster.

![
          vSAN File service architecture.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/616c80b5-70db-4e1a-bc7d-a15e6b13f845.original.png)

When you configure vSAN file service, vSAN creates a single VDFS distributed file system for the cluster which will be used internally for management purposes. A file service VM (FSVM) is placed on each host. The FSVMs manage file shares in the vSAN datastore. Each FSVM contains a file server that provides both NFS and SMB service.

A static IP address pool should be provided as an input while enabling file service workflow. One of the IP addresses is designated as the primary IP address. The primary IP address can be used for accessing all the shares in the file services cluster with the help of SMB and NFSv4.1 referrals. A file server is started for every IP address provided in the IP pool. A file share is exported by only one file server. However, the file shares are evenly distributed across all the file servers. To provide computing resources that help manage access requests, the number of IP addresses must be equal to the number of hosts in the vSAN cluster.

vSAN file service supports vSAN stretched clusters and two-node vSAN clusters. A two-node vSAN cluster should have two data node servers in the same location or office, and the witness in a remote or shared location.

For more information about Cloud Native Storage (CNS) file volumes, see the VMware vSphere Kubernetes Service Components documentation.