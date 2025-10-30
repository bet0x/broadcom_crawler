---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/deploying-a-witness-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Deploying a vSAN Witness Appliance
---

# Deploying a vSAN Witness Appliance

Specific vSAN configurations, such as a stretched cluster, require a witness host. Instead of using a dedicated physical ESX host as a witness host, you can deploy the vSAN witness appliance. The appliance is a preconfigured virtual machine that runs ESX and is distributed as an OVA file.

You can cross-host the witness for multiple stretched clusters only if the clusters run in four geographical locations. vSAN does not support cross-hosting with clusters available only in two locations.

Unlike a general purpose ESX host, the witness appliance does not run virtual machines. Its only purpose is to serve as a vSAN witness, and it can contain only witness components.

The workflow to deploy and configure the vSAN witness appliance includes this process.

When you deploy the vSAN witness appliance, you must configure the size of the witness supported by the vSAN stretched cluster. Choose one of the following options:

- Tiny supports up to 750 components (10 virtual machines or fewer).

  vSAN ESA does not support tiny witness appliance.
- Medium supports up to 21,833 components (500 virtual machines). As a shared witness, the Medium witness appliance supports up to 21,000 components and up to 21 two-node vSAN clusters.
- Large supports up to 45,000 components (more than 500 virtual machines). As a shared witness, the Large witness appliance supports up to 24,000 components and up to 24 two-node vSAN clusters.
- Extra Large supports up to 64,000 components (more than 500 virtual machines). As a shared witness, the Extra Large witness appliance supports up to 64,000 components and up to 64 two-node vSAN clusters.

These estimates are based on standard VM configurations. The number of components that make up a VM can vary, depending on the number of virtual disks, policy settings, snapshot requirements, and so on. For more information about witness appliance sizing for two-node vSAN clusters, see the [vSAN 2 Node Guide](https://www.vmware.com/docs/vmw-vsan-2-node-cluster-guide).

You also must select a datastore for the vSAN witness appliance. You must deploy the witness appliance on a third site independent of the two sites where it is intended to be stretched. The witness appliance must not share any physical resources with either data sites.

1. Download the appliance from the Broadcom Support Portal. Ensure that you download the correct witness appliance for vSAN ESA clusters and vSAN OSA clusters.
2. Deploy the appliance to a vSAN host or cluster. For more information, see [Deploy and Export OVF and OVA Templates](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_027&appid=vsphere-9-0&language=&format=rendered) in the vSphere Virtual Machine Administration guide.
3. Specify a unique VM name and select a datacenter and folder to deploy the VM and click Next.
4. Select a cluster or ESX host that acts as a compute resource to deploy the VM and click Next.
5. Review the details and click Next.
6. Read and accept the license agreement and click Next
7. Select medium, large, or extra large as the size of the vSAN witness appliance and click Next. When you deploy the vSAN witness appliance, you must configure the size of the witness.
8. Select the virtual disk format and the VM storage policy.
9. Select the datastore of the vSAN witness appliance and click Next. You can batch configure or configure per disk group, as required.
10. Browse and select the port group for the witness appliance management interface and a secondary port group for the secondary network for vSAN VMKernel port. Click Next. Broadcom recommends setting the management network for vSAN traffic.

    If you select the management network for vSAN traffic, you do not require to configure the secondary network. The secondary network port group can have the same name as the management network port group. If you are using the secondary network for vSAN traffic, select an appropriate port group.
11. Perform the following to customize the vSAN witness appliance and click Next:
    1. Set a root password for the vSAN witness appliance.
    2. Select the adapter to tag vSAN traffic type. You can select the management network or the secondary network. Broadcom recommends setting the management network for vSAN traffic. If you select the management network for vSAN traffic, you do not require to configure the secondary network and network settings can remain blank.
    3. Customize the network settings for the management network (vmk0). You can select DHCP or set a static IP address. If you select DHCP, you can leave the management network settings blank.
    4. Customise the network settings for the secondary network (vmk1), if required. You can use DHCP or set a static IP address. If you select DHCP, you can leave the secondary network settings blank.

       If you select the management network for vSAN traffic, you do not require to configure the secondary network and the network settings can remain unset.
12. Review the details and click Finish. After deployment of the vSAN witness appliance, power on the witness VM.

    You can use the management IP from the vSAN witness VM and add it as a standalone host in the vSAN streteched cluster.