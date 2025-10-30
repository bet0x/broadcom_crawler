---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/expand-a-workload-domain/add-a-host-to-a-vsphere-cluster-using-the-sddc-manager-ui.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Add an ESX Host to an SDDC Cluster in a VCF Domain
---

# Add an ESX Host to an SDDC Cluster in a VCF Domain

You can add an ESX host to an SDDC cluster using the vSphere Client. Adding an ESX host to an SDDC cluster in a VCF domain increases the available resources. You can add multiple hosts at the same time.

- Verify that one or more unassigned hosts are available in the Hosts inventory. See [View ESX Host Inventory](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/view-host-inventory.html).
- For information on commissioning hosts, see [Commission ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html).
- Verify that the ESX hosts you want to add is in an active state.
- Verify that the ESX host to be added matches the configuration of the ESX hosts already in the SDDC cluster. This allows the SDDC cluster configuration to remain balanced. If the host to be added does not match the pre-existing hosts in the SDDC cluster, the cluster will be unbalanced and a warning is displayed. The warning does not prevent the expansion and can be dismissed if needed.
- Verify that the ESX host you are adding has the same type of principal storage as the existing ESX hosts in the SDDC cluster. A host using NFS for principal storage will automatically use the same NFS configuration as the other hosts in the SDDC cluster. For a host using VMFS on FC, you must configure zoning, mount the associated volumes, and create the datastore on the host before adding the host to a SDDC cluster. A host using vVols for principal storage will automatically use the same vVols configuration as the other hosts in the SDDC cluster.
- If the SDDC cluster to which you are adding hosts uses a static IP pool for the NSX Host Overlay Network TEPs, that pool must include enough IP addresses for the hosts you are adding.
- Different NIC enumeration is allowed.
- To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

When you use the vSphere Client to add an ESX host to an SDDC cluster, it uses the cluster's existing vDS for management, vMotion, vSAN, and host overlay traffic.

You can add hosts to or remove hosts from multiple different SDDC clusters in parallel. For example, you add three hosts to Cluster A, and while that task is running, you can start a separate task to add (or remove) four hosts to Cluster B. See [VMware Configuration Maximums](https://configmax.esp.vmware.com/home) for information about the maximum number of add/remove hosts tasks that you can run in parallel.

1. In the vSphere Client, browse to the SDDC cluster in the inventory.
2. Select the SDDC cluster and click ActionsAdd HostsAdd Unassigned Hosts.
3. Select the host you want to add to the SDDC cluster and click Next.
4. On the vSphere Distributed Switch page, you can view the existing networking configuration on the cluster. It shows both vDS and NSX networking. Each vDS has two uplinks in it, and you can assign any free vmnics on the host to the existing uplinks on the vDS.
5. Click Next.
6. Review the host, switch configuration, and license details and click Finish. 

   A message indicating that the host is being added will appear.