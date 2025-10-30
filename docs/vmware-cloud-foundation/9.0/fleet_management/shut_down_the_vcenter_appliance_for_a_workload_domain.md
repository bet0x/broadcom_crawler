---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/vcf-shutdown/shut-down-the-virtual-infrastructure-workload-domain/shut-down-the-vcenter-server-instance-in-the-virtual-infrastructure-workload-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Shut Down the vCenter Appliance for a Workload Domain
---

# Shut Down the vCenter Appliance for a Workload Domain

If the vCenter appliance is running on a different infrastructure than the one it manages, to shut down the vCenter appliance for a workload domain in VCF, you use the vSphere Client.

Verify that all ESX hosts in all clusters are stopped and are disconnected.

If the vCenter appliance is running on the infrastructure that it manages, you stop it as part of the shutdown operation for ESX hosts.

1. Identify the vCenter instance that runs the vCenter appliance for this workload domain.
2. Log in to vCenter for the management or workload domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
3. Shut down vCenter Server.
   1. Locate the vCenter Server virtual machine for the workload domain.
   2. Right-click the virtual machine and select PowerShut down Guest OS.
   3. In the confirmation dialog box, click Yes.

   This operation takes several minutes to complete.