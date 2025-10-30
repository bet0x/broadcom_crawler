---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/configuring-vsan-stretched-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Manually Configure vSAN Stretched Cluster
---

# Manually Configure vSAN Stretched Cluster

Configure a vSAN cluster that stretches across two geographic locations or sites.

- Verify that you have a minimum of three hosts: one for the preferred site, one for the secondary site, and one host to act as a witness.
- Verify that you have configured one host to serve as the witness host for the vSAN stretched cluster. Verify that the witness host is not part of the vSAN cluster, and that it has only one VMkernel adapter configured for vSAN data traffic.
- Verify that the witness host is empty and does not contain any components. To configure an existing vSAN host as a witness host, first remove the witness from an existing two-node cluster or vSAN stretched cluster and remove any vSAN disk groups or storage pools on the witness host.

1. Navigate to the vSAN cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains.
4. Click Configure Stretched Cluster to open the vSAN stretched cluster configuration wizard.
5. Select the hosts that you want to assign to the secondary fault domain and click  >>.

   The hosts that are listed under the Preferred fault domain are in the preferred site.
6. Click Next.
7. Select a witness host that is not a member of the vSAN stretched cluster and click Next.
8. Claim storage devices on the witness host and click Next. 

   For vSAN OSA, select devices for cache and for capacity.

   For vSAN ESA, select compatible flash devices or enable I want vSAN to manage the disks.
9. On the Ready to complete page, review the configuration and click Finish.