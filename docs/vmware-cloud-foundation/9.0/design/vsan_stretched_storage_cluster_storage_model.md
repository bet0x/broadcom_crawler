---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-storage-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > vSAN Stretched Storage Cluster Storage Model
---

# vSAN Stretched Storage Cluster Storage Model

This is a topology choice for a vSAN Storage Cluster. This topology is identical from a deployment perspective to a vSAN Stretched Cluster deployment. This allows for a vSAN Compute Cluster to mount a vSAN Stretched Storage Cluster to avail of higher availability. A vSAN Compute Cluster can also be stretched

vSAN Stretched Storage Cluster Storage Model

This figure illustrates a vSAN Stretched storage cluster with vSAN compute clusters consuming storage capacity.

A vSAN compute cluster can be stretched or non-stretched. A non-stretched vSAN Compute cluster can be deployed on either availability zone (VCF api only).

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/8929a97f-9880-4ff1-a84e-0fc49d5a9b9c.original.svg)

vSAN Stretched Storage Clusters are essentially vSAN Stretched clusters and should inherit the same attributes.

vSAN Stretched Cluster Storage Model Attributes



| Attribute | Detail |
| --- | --- |
| Fault domain / availability zone | - vSAN Stretched Clusters comprise of three (3) Fault domains. A fault domain comprises of one or more vSAN nodes. - A fault domain or availability zone can represent a physical location. Fault domains / availability zones can either be two distinct data centers in a metro distance, or two safety or fire sectors (data halls) in the same large-scale datacenter. |
| vSAN traffic type | - vSAN Stretch Clusters utilize vSAN Traffic type for data traffic. - vSAN Stretch Clusters utilize vSAN Witness Traffic type for vSAN meta-data traffic.   vSAN Stretch Storage Clusters (ESA) can be configured to use vSAN Storage Cluster Client traffic for vSAN compute client clusters. See [vSAN Stretched Storage Cluster Storage Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/storage-models(1)/standard-vsan-storage-model/stretched-cluster-storage-models/vsan-stretched-storage-cluster.html). |
| vSAN witness appliance | A witness node is a pre-configured appliance that runs ESX and is distributed as an OVA file. |

vSAN Stretched Storage Cluster Model Options



| Design Area | Options |
| --- | --- |
| Witness traffic separation | - Witness traffic separation allows you to use a VMkernel adapter for vSAN witness traffic that is different from the adapter for vSAN data traffic. - There are two choices when stretching a vSAN clusters.    - When enabled, the ESX management network is used to communicate with the vSAN witness node.   - When disabled, The vSAN data traffic network is used to communicate with the vSAN witness traffic. |
| vSAN storage cluster client traffic | - **Dis-aggregated vSAN Storage traffic**  vSAN Storage traffic and vSAN VM IO traffic will be separated. If selected a new traffic type called **vSAN Storage Cluster Client traffic** can be selected. This will require an additional VMkernel interface and a separate network pool with an allocated IPv4 Segment. - **Converged vSAN Storage Traffic**  If selected vSAN traffic and vSAN VM IO traffic share the same physical resources. |
| Distributed switch models | - [Single Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/simple-network-model.html) - [Workload Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/workload-separation-network-model.html) - [Storage and Workload Separation Distributed Switch Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-and-workload-separation-network-model.html) - [vSAN Storage Cluster Separation Distributed Switch Model](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/network-designs/vsphere-cluster-network-models/storage-cluster-client-traffic-separation.html) |
| MTU | 1500 - 9000 |

vSAN Stretched Cluster Model Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-SC-REQD-CFG-001 | Two (2) availability zones and a third site for the witness appliance location. | Fault domains are mapped to availability zones to provide logical and physical ESX host separation and ensure a copy of vSAN data is always available even when an availability zone goes offline. | - This requires both availability zones to have an equal number of ESX hosts residing in each site, and are connected using a high bandwidth/low latency connection known as an inter-site link, or ISL. - The third site should host the witness appliance and must not have a logical or physical dependency on either availability zone. |
| VCF-VSAN-SC-REQD-CFG-002 | The minimum latency required between the data sites hosting virtual machine objects should not exceed 5 milliseconds (ms) in round trip time (RTT), or 2.5ms one way. | The latency minimums exist largely to ensure that applications can write data resiliently across two sites in a timely manner. | Stretched cluster network latency requirements will dictate the realistic geographic distance between sites. |
| VCF-VSAN-SC-REQD-CFG-003 | The minimum latency required between witness site and the data sites should not exceed 200ms RTT, or 100ms one way. | The witness site only stores small amounts of metadata, and is not a part of the vSAN data path. | None. |
| VCF-VSAN-SC-REQD-CFG-004 | vSAN Stretched Cluster Data Site to Data Site Bandwidth minimum is no less than 10GbE.  - The vSAN Stretched Cluster Bandwidth Sizing document can be used for general guidance in sizing for vSAN OSA and ESA architectures. | The network requirements for the data-site to data site in a stretch cluster remain the same for both vSAN ESA and OSA. | - VM workloads will ultimately determine the network bandwidth demand between data-sites.  - Please review <https://www.vmware.com/docs/vmw-vsan-stretched-cluster-bandwidth-sizing> |
| VCF-VSAN-SC-REQD-CFG-005 | vSAN Stretched Cluster Data Site to Witness Site Bandwidth is based on number of VMs that is protected by a stretch cluster storage policy. | - Network communication from the data sites to the witness host appliance is comprised entirely of metadata and this is wholly dependent on the number of VM and components protected by vSAN Stretch Cluster polices.   - There is no minimum bandwidth defined as estimating the bandwidth required for the witness site is based on the number of VM components. | For accurate sizing please review <https://www.vmware.com/docs/vmw-vsan-stretched-cluster-bandwidth-sizing> |
| VCF-VSAN-SC-REQD-CFG-006 | Management Domain initial cluster  Minimum of eight (8) nodes for vSAN stretched cluster for high availability (HA) install | Management domain initial clusters deployed in high availability (HA) mode have a requirement for 4 nodes in a non-stretched deployment. Stretching a cluster is a day two operation and will require 4 additional hosts on the second availability zone. | vSAN stretched cluster will operate optimally with a balanced ESX host configuration on each availability zone and be able to tolerate a local site failure |
| VCF-VSAN-SC-REQD-CFG-007 | Workload domain clusters (except for management Domain initial cluster)  Minimum of six (6) nodes for vSAN stretched clusters | This will provide minimum requirements for site availability and site local availability, tolerating a site failure and one failure on each availability zone.  This will give a balance between a host failure on a local availability zone and a full availability zone failure. | vSAN stretched cluster will operate optimally with a balanced ESX host configuration on each availability zone and be able to tolerate a local site failure with minimum three (3) nodes per site.  However with three nodes per site, vSAN will not automatically rebuild objects that are impacted by a local failure. |
| VCF-VSAN-SC-REQD-CFG-008 | For vSAN OSA architecture  Modify the default Storage Policy as follows   - **Site disaster tolerance:** Site mirroring - **Failure to tolerate :** One (1) failure RAID-1 (Mirroring) | Provides the minimum necessary protection for VMs in each availability zone, with the ability to recover from an availability zone outage.  - For vSAN ESA , Auto Policy configuration will automatically alter the default storage policy to reflect the number of hosts and underlying vSAN topology, when the cluster is converted to a stretch cluster. | - Additional Storage is necessary to satisfy the storage policy requirements in both availability zones. - Additional policies can be configured for specific workloads depending on their individual performance or availability requirements which may differ from what the default vSAN stretched cluster policy. |
| VCF-VSAN-SC-REQD-CFG-009 | Deploy a vSAN witness appliance in a location that is not co-located to the ESX hosts in any of the availability zones. | Ensures availability of vSAN witness appliance in the event of a failure of one of the availability zones. | You must provide a third availability zone that is logically and physically independent of the data sites  The third site must be able to provide a environment capable to host the witness appliance. |
| VCF-VSAN-SC-REQD-CFG-010 | Deploy a witness appliance that corresponds to vSAN Architecture, (ESA or OSA). | Ensures the witness appliance deployed is compatible to the correct vSAN Storage architecture | None. |
| VCF-VSAN-SC-REQD-CFG-011 | Connect the first VMkernel (vmk0) adapter of the vSAN witness appliance to the management network in the witness site. | The ESX host management networks in both availability zones must be routed to the vSAN witness host management network in the third witness site. | When using witness traffic separation, the second interface on vSAN witness host (vmk1) can be removed. |
| VCF-VSAN-SC-REQD-CFG-012 | Configure vSAN Witness host identity as per standard ESX host recommendations. | - Allows vSAN Witness host to be managed identically as a ESX host.  - Ensures host identity, DNS and NTP is consistently configured | Apply the requirements for [External Services Design](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-vcenter-server-networking.html#GUID-c17bff55-9bff-4181-be36-b0bc39c59133-en_GUID-FF48E31A-A83D-4EED-8FFC-9A2B4F0EB331) |
| VCF-VSAN-SC-REQD-CFG-013 | Enable vSphere Lifecycle Manager images on the vSAN witness host. | - VMware Cloud Foundation 9.0 requires vSphere Lifecycle Manager images for ESX hosts. - This will prevent warnings or vSAN health check alarms. | This requires either deploying or converting a vSAN witness host as a vSphere Lifecycle Manager image managed entity. |

vSAN Stretch Storage Cluster Model Additional Design Requirements



| Design Requirement ID | Design Requirement | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-SC-STG-CLU-REQD-CFG-001 | Use four (4) vSAN Nodes per availability zone (total of 8 vSAN data nodes). | This satisfy the requirement to have at least four nodes for a vSAN Storage cluster. Having four (4) vSAN nodes per availability zone will provide a balance of capacity and availability | This is an additional requirement for a standard vSAN stretch cluster and will require additional vSAN Nodes. |

vSAN Stretch Storage Cluster Model Additional Design Recommendations



| Design Recommendation ID | Design Recommendation | Justification | Implication |
| --- | --- | --- | --- |
| VCF-VSAN-SC-STG-CLU-RCMD-CFG-001 | A recommendation of seven (7) hosts in each availability zone (total of 14 vSAN Data nodes) | This will ensure a cluster could support a storage policy with a secondary level of resilience of FTT=2 using RAID-6 erasure coding, and allow vSAN to regain its prescribed level of resilience in the event of a sustained host outage. | An additional host beyond the minimum required allows vSAN to reconstruct the stripe and parity in the most efficient way, with the fewest performance implications. |
| VCF-VSAN-SC-STG-CLU-RCMD-CFG-002 | Use Witness Traffic Separation | Removes the requirement for the backend data node network to route with the vSAN Witness Host vmkernel interface  Removes the requirement of static routes between vSAN data node traffic | Simpler network design avoids complex routing between vSAN data nodes and vSAM Witness host |