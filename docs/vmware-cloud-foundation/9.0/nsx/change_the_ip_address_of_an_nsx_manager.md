---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/change-the-ip-address-of-an-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Change the IP Address of an NSX Manager
---

# Change the IP Address of an NSX Manager

You can change the
IP address of an
NSX Manager in
an
NSX Manager
cluster. This section describes several approaches.

Familiarize yourself with how to deploy an NSX Manager into a cluster. For more information, see the NSX Installation Guide.

For example, if you have a
cluster consisting of Manager A, Manager B, and Manager C, you can change the
IP address of one or more of the managers in the following ways:

- Scenario A:
  - Manager A has IP
    address 172.16.1.11.
  - Manager B has IP
    address 172.16.1.12.
  - Manager C has IP
    address 172.16.1.13.
  - Add Manager D with a
    new IP address, for example, 192.168.55.11.
  - Remove Manager A.
  - Add Manager E with a
    new IP address, for example, 192.168.55.12.
  - Remove Manager B.
  - Add Manager F with a
    new IP address, for example, 192.168.55.13.
  - Remove Manager C.
- Scenario B:
  - Manager A has IP
    address 172.16.1.11.
  - Manager B has IP
    address 172.16.1.12.
  - Manager C has IP
    address 172.16.1.13.
  - Add Manager D with a
    new IP address, for example, 192.168.55.11.
  - Add Manager E with a
    new IP address, for example, 192.168.55.12.
  - Add Manager F with a
    new IP address, for example, 192.168.55.13.
  - Remove Manager A,
    Manager B, and Manager C.
- Scenario C:
  - Manager A has IP
    address 172.16.1.11.
  - Manager B has IP
    address 172.16.1.12.
  - Manager C has IP
    address 172.16.1.13.
  - Remove Manager A.
  - Add Manager D with a
    new IP address, for example, 192.168.55.11.
  - Remove Manager B.
  - Add Manager E with a
    new IP address, for example, 192.168.55.12.
  - Remove Manager C.
  - Add Manager F with a
    new IP address, for example, 192.168.55.13.

The first two scenarios require additional virtual RAM,
CPU, and disk for the additional NSX Managers
during this IP address change.

Scenario C is not recommended because it temporarily
reduces the number of NSX Managers and
a loss of one of the two active managers during the IP address change will have an
impact on the operations of NSX. This
scenario is for a situation where additional virtual RAM, CPU and disk are not
available and an IP address change is required.

If you are using the cluster VIP feature, you
must either use the same subnet for the new IP addresses or deactivate the cluster
VIP during the IP address changes because the cluster VIP requires all NSX Managers to be in the same subnet.

1. If the
   NSX Manager you
   want to remove was deployed manually, perform the following steps.
   1. Run the following
      CLI command to detach the
      NSX Manager
      from the cluster.

      detach
      node <node-id>
   2. Delete the NSX Manager VM.
2. If the
   NSX Manager you
   want to delete was deployed automatically through the
   NSX Manager UI,
   perform the following steps.
   1. From your browser,
      log in with administrator privileges to an
      NSX Manager at
      https://nsx-manager-ip-address.

      This
      NSX Manager
      must not be the one that you want to delete.
   2. From the Systems
      tab, click NSX Management Nodes. 

      The status of the
      NSX Manager cluster is displayed.
   3. For the
      NSX Manager
      that you want to delete, click the gear icon and select
      Delete.
3. Deploy a new
   NSX Manager.