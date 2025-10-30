---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/distributed-port-groups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Distributed Port Groups
---

# Distributed Port Groups

A distributed port group specifies port configuration options for each member port on
a vSphere distributed switch. Distributed
port groups define how a connection is made to a network.

## Distributed Port Group Creation in NSX

When you install Distributed Security to
a vSphere Distributed Switch
(VDS), the Distributed Virtual port groups (DVPG) and DVports of the VDS are
discovered and objects are automatically created to represent them in NSX.

For details, see [Activate NSX on Distributed Virtual Port Groups (DVPGs)](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security/activate-distributed-security-for-vds.html#GUID-bfdb4909-b7a5-471b-b047-6f6e63d6932e-en).

The objects created in NSX Manager for the DVPGs are called
distributed port
groups. They are not called segments in the
UI.

The objects created in NSX Manager for the DVports are called
distributed
ports. They are not called segment ports in the
UI.

Also, the following events occur during
the Distributed Security installation:

- The VLAN tags for the DVPG are
  automatically discovered and shown in NSX Manager. The VLAN tags can only be edited in vCenter.
- The default segment profiles are
  applied to the distributed port groups. You can later switch them to custom
  profiles.
- Only connected DVports from
  vCenter are
  discovered by NSX. Free
  DVports are not discovered.

After the Distributed Security
installation, you can view these objects by navigating to NetworkingSegments, and then selecting the Distributed Port
Groups tab.

The distributed port group and
distributed port objects are kept in sync between vCenter and NSX. This means that if DVPGs or DVports
are created or removed in vCenter, then those changes are automatically made to the
respective distributed port groups or distributed ports in NSX Manager. If changes are made in
vCenter while
connectivity is lost between vCenter and NSX,
those changes are automatically processed and reflected in NSX Manager when connectivity is
restored.

## Available Actions for Distributed Port Groups and Distributed Ports

You can perform the following actions for
distributed port groups and distributed ports in NSX Manager:

| Object | Available Actions |
| --- | --- |
| Distributed port groups | - Apply   SpoofGuard. - Apply IP   Discovery. - Apply switch   security profile. - Add and remove   tags which allows the distributed port group to be added to   dynamic NSGroups. - Add and remove   the distributed port group from static NSGroups. |
| Distributed ports | - Add and remove   tags which allows distributed ports to be added to dynamic   NSGroups. - Add and remove   distributed ports from static NSGroups. - Manage address   bindings. |