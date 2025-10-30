---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/network-io-control-design.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Network I/O Control Detailed Design
---

# Network I/O Control Detailed Design

vSphere Network I/O Control version 3 is enabled by default on the vSphere Distributed Switches created in VMware Cloud Foundation and provides a mechanism to reserve bandwidth for system traffic based on the capacity of the physical adapters on an ESX host. This can be particularly useful when different traffic types share the same physical adapters on the hosts.

## vSphere Distributed Switch Network I/O Control Options

Network I/O Control supports different mechanisms for resource management of system traffic related to infrastructure services, such vSAN, vMotion, etc and VM traffic. For system traffic shares are used to ensure a dedicated percentage of the bandwidth at time when there is contention on the physical adapter. Network I/O Control provisions bandwidth to the network adapters of virtual machines by using constructs of shares, reservation and limit. In VMware Cloud Foundation the default shares are applied to the system traffic, the table below shows the default values.

| Traffic Type | Shares | Shares Value |
| --- | --- | --- |
| Management Traffic | Normal | 50 |
| Fault Tolerance (FT) Traffic | Low | 25 |
| vMotion Traffic | Low | 25 |
| VM Traffic | High | 100 |
| iSCSI Traffic | Low | 25 |
| NFS Traffic | Low\* | 25 |
| vSphere Replication (VR) Traffic | Low | 25 |
| vSAN Traffic | High | 100 |
| vSphere Data Protection Backup Traffic | Low | 25 |
| vSphere Backup NFC Traffic | Normal | 50 |
| NVMe over TCP | Normal | 50 |
| Provisioning Traffic | Normal | 50 |

Depending on the the distributed switch configuration and the type of system traffic on the distributed virtual switch these value can be modified post deployment to meet the requirements of the environment.

\* High if NFS storage is used as principal storage for the cluster

\*\* Low if vSAN is not used as principal storage for the cluster

In some cases vSphere Network I/O Control needs to be disabled, for vSphere cluster hosting edge clusters, it is recommend to disable the feature.