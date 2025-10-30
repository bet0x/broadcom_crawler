---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/managing-nsx-on-a-vsphere-distributed-switch/configuring-a-vsphere-distributed-switch.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configuring a vSphere Distributed Switch
---

# Configuring a vSphere Distributed Switch

When a transport node is configured on a VDS host switch, some network parameters can only be configured in vCenter.

The following requirements must be met to install NSX on a VDS host switch:

- vCenter 7.0 or a later version
- ESX 7.0 or a later version

The created VDS switch can be configured to centrally manage networking for NSX hosts.

Configuring a VDS switch for NSX networking requires objects to be configured on NSX and in vCenter.

- In vSphere:
- Create a VDS switch.

  - Set MTU to at least 1600. However, a minimum MTU of 1700 bytes is recommended.
  - Add ESX hosts to the switch. These hosts are later prepared as NSX transport nodes.
  - Assign uplinks to physical NICs.

  If after creating the VDS switch you change the MTU value in vSphere, you must then access the NSX UI and complete a transport node resync for all hosts using this VDS. This can be done at the cluster level by reapplying the same Transport Node Profile (TNP), or at the host level by issuing a transport node resync.
- In NSX:
  - When configuring a transport node, map uplinks created in NSX uplink profile with uplinks in VDS.

The following parameters can only be configured in a vCenter on a VDS backed host switch:

| Configuration | VDS | NSX | Description |
| --- | --- | --- | --- |
| MTU | In vCenter, set an MTU value on the switch.  A VDS switch must have an MTU of 1600 or higher. Minimum MTU of 1700 bytes is recommended.  In vCenter, select VDS, click ActionsSettingsEdit Settings. | Any MTU value set in an NSX uplink profile is overriden. | As a host transport node that is prepared using VDS as the host switch, the MTU value needs to be set on the VDS switch in vCenter. |
| Uplinks/LAGs | In vCenter, configure Uplinks/LAGs on a VDS switch.    In vCenter, select VDS, click ActionsSettingsEdit Settings. | When a transport node is prepared, the teaming policy on NSX is mapped to uplinks/LAGs configured on a VDS switch. | As a host transport node that is prepared using VDS as the host switch, the uplink or LAG are configured on the VDS switch. During configuration, NSX requires teaming policy be configured for the transport node. This teaming policy is mapped to the uplinks/LAGs configured on the VDS switch. |
| NIOC | Configure in vCenter. In vCenter, select VDS, click ActionsSettingsEdit Settings. | NIOC configuration is not available when a host transport node is prepared using a VDS switch. | As a host transport node that is prepared using VDS as the host switch, the NIOC profile can only be configured in vCenter. |
| Link Layer Discovery Protocol (LLDP) | Configure in vCenter. In vCenter, select VDS, click ActionsSettingsEdit Settings. | LLDP configuration is not available when a host transport node is prepared using a VDS switch. | As a host transport node that is prepared using VDS as the host switch, the LLDP profile can only be configured in vCenter. |
| Add or Manage Hosts | Manage in vCenter. In vCenter, go to NetworkingVDS SwitchAdd and Manage Host. | Prepared as transport nodes in NSX. | Before preparing a transport node using a VDS switch, that node must be added to the VDS switch in vCenter. |

NIOC profiles, Link Layer Discovery Protocol (LLDP) profile, and Link Aggregation Group (LAG) for these virtual machines are managed by VDS switches and not by NSX. As a vSphere administrator, configure these parameters from vCenter UI or by calling VDS API commands.

After preparing a host transport node with VDS as a host switch, the host switch type displays VDS as the host switch. It displays the configured uplink profile in NSX and the associated transport zones.

![Selecting the transport node displays the VDS switch details along with its associated uplink profile and transport zones.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/20be9951-a629-458a-84d8-f3837416edc5.original.png)

In vCenter, the VDS switch used to prepare NSX hosts is created as an NSX Switch.![vCenter displays the VDS switch used to prepare a NSX transport node as a NSX switch.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/c14e1a30-391a-471d-823d-fb3b2d219b5f.original.png)