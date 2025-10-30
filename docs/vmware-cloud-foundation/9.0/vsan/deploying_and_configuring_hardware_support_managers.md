---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/managing-proactive-hardware/deploying-and-configuring-hardware-support-managers.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Deploying and Configuring Hardware Support Managers
---

# Deploying and Configuring Hardware Support Managers

Regardless of the hardware vendor, you must deploy the hardware support manager appliance on a host with sufficient memory, storage, and processing resources.

Typically, hardware support manager appliances are distributed as OVF or OVA templates. You can deploy them on any host in any vCenter instance.

After you deploy the appliance, you must power on the appliance virtual machine and register the appliance as a vCenter extension. You might need to log in to the appliance as an administrator. Each hardware support manager might register with only one or multiple vCenter systems.

For detailed information about deploying, configuring, and managing hardware support managers, refer to the respective OEM-provided documentation and see [Deploying Hardware Support Managers](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0/managing-host-and-cluster-lifecycle/using-images-to-install-and-update-esxi-hosts-and-clusters/firmware-updates.html#GUID-B001135C-59AF-4CFD-9B73-94648B41D1A0-en) in the Managing Host and Cluster Lifecycle guide.