---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/removing-a-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Replace the Witness Host
---

# Replace the Witness Host

You can replace or change the witness host for a vSAN stretched cluster.

Verify that the witness host is not in use by another cluster, has a VMkernel configured for vSAN traffic, and has no vSAN partitions on its disks.

Change the ESX host used as a witness host for your vSAN stretched cluster.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains.
4. Click the Change button. The Change Witness Host wizard opens.
5. Select a new host to use as a witness host, and click Next.
6. Claim disks on the new witness host, and click Next.
7. On the Ready to complete page, review the configuration, and click Finish.