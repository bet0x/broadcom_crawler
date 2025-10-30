---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/commission-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Commission ESX Hosts
---

# Commission ESX Hosts

Adding ESX hosts to the global inventory is called commissioning. You must commission ESX hosts before you can use them to create a new workload domain or add them to an existing VCF domain.

Prepare your hosts. See [Preparing ESX Hosts for VMware Cloud Foundation or vSphere Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation.html).

Ensure that each ESX host you commission meets the following criteria:

- Hosts for vSAN-based workload domains are vSAN-compliant and certified on the VMware Hardware Compatibility Guide.
- Hosts for NFS-based workload domains are certified on the VMware Hardware Compatibility Guide.
- Hosts for VMFS on FC-based workload domains are certified on the VMware Compatibility Guide. In addition, the hosts must have supported FC cards (Host Bus Adapters) and drivers installed and configured. For compatible FC cards, see the VMware Compatibility Guide.

  The VMFS datastore must be mounted on all the hosts before commissioning.
- Hosts for vVols-based workload domains are certified on the VMware Hardware Compatibility Guide.

  - For vVols on FC-based workload domains, ensure that all ESX hosts have access to the FC array before launching the workflow.
  - For vVols on NFS-based workload domains, ensure that all ESX hosts must be able to reach the NFS server from the NFS network assigned in the IP pool.
  - For vVols on iSCSI-based workload domains, ensure that the iSCSI software initiator must be enabled on each ESXi host and the VASA provider URL must be listed as the dynamic target.

  Starting with VMware Cloud Foundation 9.0 and vSphere Foundation 9.0, the vSphere Virtual Volumes capability, also known as vVols, is deprecated and will be removed in a future release of VMware Cloud Foundation and vSphere Foundation. Support for vSphere Virtual Volumes will continue for critical bug fixes only for versions of vSphere 8.x, VMware Cloud Foundation and vSphere Foundation 5.x, and other supported versions until end-of-support for the respective release.
- Each host must have the correct number of physical NICs for the desired network configuration for the host. Hosts can have a single physical NIC or multiple physical NICs. For hosts with multiple physical NICs, only one can be connected to a standard switch, and the NIC must support all management traffic.
- All physical NICs must have a minimum speed of 10 Gbps.
- Management IP address is configured on a VMkernel interface connected to the Management Network on the standard switch.
- Host has the drivers and firmware versions specified in the VMware Hardware Compatibility Guide.
- A supported version of ESX is installed on the host. See the VMware Cloud Foundation Release Notes for information about supported versions.
- Has both forward and reverse lookup entries (FQDN) configured on the DNS server.
- Host name must be same as the FQDN.
- Self-signed certificate regenerated based on FQDN of host. See [Regenerate the Self-Signed Certificate on ESX Hosts](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/regenerate-the-self-signed-certificate-on-esx-hosts.html).
- Hardware health status is healthy without any errors.
- All disk partitions on HDD and SSD are deleted.
- A network pool must be created and available before host commissioning.
- The network pool must support the storage type you select for a host (vSAN, vSAN ESA, vSAN Storage Client, NFS, VMFS on FC, vVols). See [Network Pool Management](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/host-management/about-network-pools.html#GUID-ca2e8815-58db-40b8-9ad2-91a5e1fa0daf-en).
- Host is configured with an appropriate gateway. The gateway must be part of the management subnet.

To perform this task in the vSphere Client, you must have access to the management domain vCenter, or your VCF Instance must be configured with VCF SSO and vCenter linking. See [Configuring VCF Single Sign-On](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is.html) and [Linking vCenter instances in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/linking-vcenter-systems-in-vmware-cloud-foundation-operations.html). As an alternative, you can perform this task using the SDDC Manager UI (https://<sddc-manager-fqdn>).

You can add ESX hosts individually or use a JSON template to commission multiple hosts at once. You can also run multiple commission hosts tasks at the same time.

After you specify host details and select the network pool to associate the hosts with, the platform validates and commissions each host. Each host is added to the free pool and is available for VCF domains and vSphere clusters.

- Hosts that use vSAN storage can only be used with vSAN-based clusters.
  - Hosts that are commissioned for vSAN HCI with ESA enabled can only be used for vSAN ESA clusters.
  - Hosts that are commissioned for vSAN HCI without ESA enabled can only be used for vSAN OSA clusters.
  - Hosts that are commissioned for vSAN Storage (formerly vSAN Max) can only be used for vSAN storage clusters.
  - Hosts that are commissioned for vSAN Compute Cluster can only be used for vSAN compute clusters.
- Hosts that use NFS storage can only be used with NFS-based clusters.
- Hosts that use VMFS on FC storage can only be used with VMFS on FC-based clusters.
- Hosts that use vVols storage can only be used with vVols-based clusters.

See [VMware Configuration Maximums](https://configmax.broadcom.com/home) for information about the maximum number of hosts you can commission at one time and the maximum number of commission hosts tasks that you can run in parallel.

If you used ESX hosts with certificates generated by an external CA for deployment, hosts used for expanding VCF domains or for creating workload domains must also use certificates generated by an external CA. See [Configure ESX Hosts with Signed Certificates](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/configure-esxi-hosts-with-signed-certificates.html).

When you add a host during host commissioning, the platform temporarily activates SSH on the host in order to retrieve the host key. After it retrieves the host key, the platform deactivates SSH on the host.

With VMware Cloud Foundation 9.0.1 and later, you can use non-certified ESA disks during vSAN ESA cluster configuration for proof-of-concept purposes only. For more information, see kB [408300](http://knowledge.broadcom.com/external/article/408300).

1. In the vSphere Client, click Global Inventory ListsHostsUnassigned Hosts.
2. Click Commission Hosts.
3. On the Checklist page, review the prerequisites and confirm by clicking Select All.
4. Click Proceed.
5. Select whether you want to add hosts one at a time or import multiple hosts at once from a JSON file. 

   Option | Description || Add new | Enter the following information for the host you want to add: - Host FQDN The host FQDN must match the host name (including capitalization) provided during DNS configuration. - Storage Type (vSAN, NFS, VMFS on FC, or vVol) for principal storage   - If you select vSAN as the storage type:     - Select the vSAN Type (vSAN HCI, vSAN Storage, or vSAN Compute Cluster).     - For vSAN HCI choose whether or not to use the vSAN Express Storage Architecture (ESA).   - If you select vVols as the storage type, specify the vVols storage protocol type (FC, iSCSI, or NFS). - Network Pool Name (select a network pool from the drop-down menu) - User Name and Password (root credentials for the ESX host) Click Add. You can now add more ESX hosts or proceed to the next step. |
   | Import | 1. To download the JSON template, click the link. 2. Open the JSON template file and enter information about the hosts to add.    - Host FQDN    - Username and password (ESX root credentials)    - Storage type (VSAN, VSAN\_REMOTE, VSAN\_ESA, VSAN\_MAX, NFS, VMFS\_FC, VVOL) for principal storage Use VSAN\_REMOTE for a vSAN compute cluster. Use VSAN\_MAX for a vSAN storage cluster.    - Network pool name  You only need to provide the vVols storage protocol type (FC, ISCSI, or NFS) when you are using VVOLS as the storage type 3. To locate and select the JSON file containing host information, click Browse. 4. Click Upload. |

   The ESX host or hosts appear in the Hosts Added section.
6. Verify that the server fingerprint is correct for each host and then activate the Confirm All Finger Prints toggle.
7. Click Validate All. 

   The platform validates the host information you provided. Each host is marked as Valid or Invalid.

   For invalid hosts, you can correct the problem and validate again, or select the host and click Remove to proceed with commissioning the valid hosts.
8. Click Next.
9. Activate or deactivate Skip failed hosts during commissioning.

   This setting is enabled by default. When enabled, hosts that fail are skipped and commissioning continues on the remaining hosts.
10. Click Commission.

    The Hosts page appears, and the status of the commission task is displayed in the Tasks window.

    Multiple VMkernels are created to test the vMotion network. If MAC address filtering is enabled on your physical infrastructure, this may cause issues such as vMotion network connectivity validation failure.

The commissioned hosts are added to the Unassigned Hosts table.