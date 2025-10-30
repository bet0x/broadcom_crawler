---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/vcf-shutdown-and-startup/sddc-startup/start-the-management-domain/start-the-esx-hosts-and-vcenter-server-in-management-domain/start-esx-hosts-without-vsan-storage-in-the-management-domain.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Start ESX Hosts with NFS or Fibre Channel Storage in the Management Domain
---

# Start ESX Hosts with NFS or Fibre Channel Storage in the Management Domain

You start the ESX hosts using an out-of-band management interface, such as, ILO or iDRAC to connect to the hosts and power them on. Then, restart the cluster from vCenter.

External storage is running and accessible.

You perform this operation on all non-vSAN clusters in the management domain. You must start with the cluster that hosts the management vCenter.

1. Power on the first ESX host in the management domain.
   1. Log in to the first ESX host in the domain by using the out-of-band management interface.
   2. Power on the ESX host according to the hardware vendor guide.
2. Repeat the previous step to start all the remaining ESX hosts in the management domain.

   This operation takes several minutes to complete.
3. Log in into the ESX host that hosts vCenter and any infrastructure components.

   You must first start infrastructure components that runs in the management cluster before you start the vCenter.

   1. Log in into ESX host at https://<esx\_fqdn> as a user with the Administrator role.
   2. Locate the management vCenter appliance.
   3. Right-click the appliance and select PowerPower on.
4. Log in to vCenter for the management domain at https://<vcenter\_fqdn>/ui as a user with the Administrator role.
5. Verify that all hosts in the cluster are connected to the management vCenter.
6. Exit maintenance mode for all hosts in the cluster.

   This operations takes several minutes to complete.
7. Repeat Step 5 and Step 6 for all clusters with non-vSAN storage in the domain.