---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-virtual-infrastructure-workload-domain/start-vcenter-server-in-the-virtual-infrastructure-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start the vCenter Appliance for a Workload Domain
---

# Start the vCenter Appliance for a Workload Domain

Use the vSphere Client to power on the vCenter appliance for the workload domain. If the workload domain contains a vSAN cluster, check its health status too.

vCenter startup is done:

- If vCenter is running on a vSAN cluster, automatically from the orchestration host .
- If vCenter is running on a non-vSAN storage, manually following the steps below.

If the vCenter appliance is running on the infrastructure, you must start the ESX hosts first.

1. Log in into the resource that hosts the vCenter appliance.
   1. For an ESX host, log in to the ESX host at https://<esx\_fqdn> as a user with the Administrator role.
   2. For the management vCenter, log in to vCenter at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
2. Start vCenter Server.
   1. Locate the vCenter Server virtual machine for the workload domain.
   2. Right-click the virtual machine and select PowerPower on.

   The startup of the virtual machine and the vSphere services takes some time to complete.