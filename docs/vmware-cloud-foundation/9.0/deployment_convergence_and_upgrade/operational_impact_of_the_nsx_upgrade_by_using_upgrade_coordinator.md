---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/operational-impact-of-nsx-t-upgrade.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Operational Impact of the NSX Upgrade by Using Upgrade Coordinator
---

# Operational Impact of the NSX Upgrade by Using Upgrade Coordinator

The duration of the NSX upgrade process depends on the number of components you have to upgrade in your infrastructure. It is important to understand the operational state of NSX components during an upgrade.

The upgrade of components occurs in the following order:

1. Management Plane
2. Edge nodes
3. vCenter
4. Hosts

## Management Plane Upgrade

| During Upgrade | After Upgrade |
| --- | --- |
| - Do not make any configuration changes during the Management plane upgrade. - User interface is unavailable for a short period. - When upgrading from NSX 4.x, API service is momentarily unavailable. When upgrading from VCF 9.x, API downtime is negligible. - When upgrading from NSX 4.x, you may experience longer than usual workload traffic downtime for VMs undergoing migration through vSphere vMotion. When upgrading from VCF 9.x, this possible downtime is further reduced. | - Configuration changes are allowed. - New features introduced in the upgrade are not configurable until all edge and host nodes are upgraded and the Finalize Upgrade step is complete. - From the Upgrade Coordinator, verify that the upgrade process has completed. Perform configuration tasks only after the upgrade process is complete. |

## NSX Edge Cluster Upgrade

| During Upgrade | After Upgrade |
| --- | --- |
| - During the edge upgrade, you might experience the following traffic interruptions:    - North-south datapath is affected if the edge is part of the datapath.   - East-west traffic between tier-1 routers using edge firewall, NAT, or load balancing.   - Temporary Layer 2 and Layer 3 interruption. - Configuration changes are not blocked on NSX Manager but might be delayed. - The hardware versions of edge node VMs change or remain the same as follows:   - For edge nodes auto-deployed through the NSX Manager UI or the API, the VM hardware is automatically updated to the maximum version supported by the underlying ESX host.   - For edge nodes manually deployed through vSphere Client, the VM hardware remains unchanged at the same version.For more details, see Broadcom KB [319091](https://knowledge.broadcom.com/external/article?articleNumber=319091). | - Configuration changes are allowed. - Upgraded edge cluster is compatible with the older versions of the hosts. - New features introduced in the upgrade are not configurable until all the edge and host nodes are upgraded and the Finalize Upgrade step is complete. - Run post checks to make sure that the upgraded edge cluster and NSX do not have any problems. |

## Hosts Upgrade

The following considerations apply only when using NSX Manager to upgrade the NSX VIBs on ESX 8.x hosts.

To upgrade ESX 7.x hosts, you must first upgrade to ESX 8.x.

| During Upgrade | After Upgrade |
| --- | --- |
| - For standalone ESX hosts or ESX hosts that are part of a disabled DRS cluster, place hosts in maintenance mode. - For ESX hosts that are part of a fully automated DRS cluster, if the host is not in maintenance mode, the upgrade coordinator requests the host to be put in maintenance mode. The vSphere DRS tool migrates the VMs to another host in the same cluster during the upgrade and places the host in maintenance mode. - For ESX host, for an in-place upgrade you do not need to power off the tenant VMs. - During an in-place upgrade:    - For VMs attached to an NSX logical switch or VMs connected to the distributed portgroup of a VDS prepared for NSX for vSphere, vmotion of VMs is not supported from and to the host on which an upgrade is in progress.   - Creating new VMs is also not supported on hosts on which an upgrade is in progress. NSX In-place Upgrade for vSphere Lifecycle Manager baseline clusters is supported with VMware Cloud Foundation 5.2.1 and later. For more information, refer to "Upgrade NSX for VMware Cloud Foundation 5.2.x" in the VMware Cloud Foundation Lifecycle Management guide. - Configuration changes are allowed on NSX Manager. - You may experience brief disruption in traffic during in-place upgrade of the hosts. For critical applications that cannot handle packet loss, maintenance mode upgrade is recommended. | - Power on or return the tenant VMs of standalone ESX hosts or ESX hosts that are part of a disabled DRS cluster that were powered off before the upgrade. - New features introduced in the upgrade are not configurable until all the edge and host transport nodes are upgraded and the Finalize Upgrade step is complete. - Run post checks to make sure that the upgraded hosts and NSX do not have any problems. |

## Limitations on In-Place Upgrade

The following considerations apply:

- For automated upgrades through SDDC Manager:

  - In-place upgrade is integrated with the live patch process in VMware Cloud Foundation lifecycle management.
  - When upgrading to an NSX hot patch or express patch, VMware Cloud Foundation will initiate a live patch when possible and trigger the in-place upgrade.
- For manual upgrades through NSX Manager:

  - In-place upgrade is supported only for ESX 8.x hosts in non-vLCM clusters.
  - When using in-place upgrade, serial upgrade within the cluster is required.
  - For vSAN clusters, NSX in-place upgrade does not check vSAN health. The absence of a check means that in the event of a failure, you may experience a breach of vSAN FTT and/or some data loss.

In-place upgrade is not supported in the following scenarios:

- More than 1000 vNICs are configured on the ESX host and the VM's vNICs connect to a single VDS. If the host has multiple VDS for NSX, this vNIC limit is per VDS.
- Layer 7 firewall rules or Identity Firewall rules are enabled.
- Service Insertion has been configured to redirect north-south traffic or east-west traffic. See Security in the NSX Administration Guide for information on uninstalling service insertion.
- A VProbe-based packet capture is in progress.
- The nsx-cfgagent service is not running on the host.
- IDS/IPS or distributed malware prevention is enabled for your NSX environment.