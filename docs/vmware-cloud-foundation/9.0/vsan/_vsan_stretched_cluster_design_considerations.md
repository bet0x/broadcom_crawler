---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/introduction-to-stretched-clusters/vsan-stretched-cluster-design-considerations.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Stretched Cluster Design Considerations
---

# vSAN Stretched Cluster Design Considerations

Consider these guidelines when working with a vSAN stretched cluster.

- Configure DRS settings for the vSAN stretched cluster.
  - DRS must be enabled on the cluster. If you place DRS in partially automated mode, you can control which virtual machines to migrate to each site. vSAN enables you to operate DRS in automatic mode, and recover gracefully from network partitions.
  - Create two host groups, one for the preferred site and one for the secondary site. Associate the hosts in the vSAN preferred fault domain to the preferred site host group, and associate the hosts in the vSAN secondary fault domain to the secondary site host group.
  - Create two VM groups, one to hold the virtual machines on the preferred site and one to hold the virtual machines on the secondary site.
  - Create two VM-Host affinity rules that map VMs-to-host groups, and specify which virtual machines and hosts reside in the preferred site and which virtual machines and hosts reside in the secondary site.
  - Configure VM-Host affinity rules to perform the initial placement of virtual machines in the cluster.
- Configure HA settings for the vSAN stretched cluster.
  - HA rule settings should respect VM-Host affinity rules during failover.
  - Disable HA datastore heartbeats.
  - Use HA with Host Failure Monitoring, Admission Control, and set FTT to the number of hosts in each site.
- Configure a vSAN storage policy that has a stretched cluster site failure tolerance rule. With vSAN ESA and auto-policy management enabled, Broadcom recommends storage policies to optimize capacity utilization based on the cluster size and topology.
- vSAN stretched clusters support enabling Symmetric Multiprocessing Fault Tolerance (SMP-FT) virtual machines only when Site Disaster Tolerance is set to None  with either Preferred or Secondary. vSAN does not support SMP-FT virtual machines on a vSAN stretched cluster with Site Disaster Tolerance set to 1 or more. vSAN two-host clusters support enabling SMP-FT with FTT set to 1 only when both data nodes are in the same site.
- When a host is disconnected or not responding, you cannot add or remove the witness host. This limitation ensures that vSAN collects enough information from all hosts before initiating reconfiguration operations.
- Using esxcli to add or remove hosts is not supported for vSAN stretched clusters.
- Do not create snapshots of the witness host or backup the witness host. If the witness host fails, see [Replace the Witness Host](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/removing-a-witness-host.html#GUID-861ebfe8-2696-4bfc-a61b-9daadcd853c5-en).

To learn how the stretched cluster storage policy rules impact the vSAN capacity requirements, see [vSAN Stretched Cluster Guide](https://www.vmware.com/docs/vsan-stretched-cluster-guide).