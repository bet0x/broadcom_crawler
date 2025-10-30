---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host/deploy-the-vsan-witness-host-for-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Deploy vSAN Witness Host
---

# Deploy vSAN Witness Host

You deploy the vSAN witness host for a stretched cluster at a site which is isolated from the existing availability zones to prevent propagation of failure or outage in the data center.

Download the VMware vSAN Witness Appliance .ova file from the [Broadcom Support Portal](https://support.broadcom.com/).

- For stretching a vSAN OSA cluster, download the appliance for vSAN OSA.
- For stretching a vSAN ESA cluster, download the appliance for vSAN ESA.
- For stretching a vSAN storage cluster, download the appliance for vSAN ESA.
- For stretching a vSAN compute cluster or creating a vSAN compute stretch cluster, no vSAN witness appliance is required.

1. In a web browser, log in to vCenter at https://vcenter\_fqdn/ui.
2. Select MenuHosts and Clusters.
3. In the inventory panel, expand vCenter ServerDatacenter.
4. Right-click the cluster and select Deploy OVF template.
5. On the Select an OVF template page, select Local file, click Upload files, browse to the location of the vSAN witness host OVA file, and click Next.
6. On the Select a name and folder page, enter a name for the virtual machine and click Next.
7. On the Select a compute resource page, select a compute resource, and click Next.
8. On the Review details page, review the settings and click Next.
9. On the License agreements page, accept the license agreement and click Next.
10. On the Configuration page, select Medium and click Next.
11. On the Select storage page, select a datastore and click Next.
12. On the Select networks page, select a portgroup for the witness and management network, and click Next.
13. On the Customize template page, enter the root password for the witness, select a network for vSAN Traffic, enter the details for each source network, and click Next.

    If you do not specify management and secondary network details, DHCP is used.
14. On the Ready to complete page, click Finish and wait for the process to complete.
15. Power on the vSAN witness host.
    1. In the inventory panel, navigate to vCenter ServerDatacenterCluster.
    2. Right-click the vSAN witness VM and from the Actions menu, select PowerPower on.