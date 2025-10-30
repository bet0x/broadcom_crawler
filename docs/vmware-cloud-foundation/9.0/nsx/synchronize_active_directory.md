---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/synchronize-active-directory.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Synchronize Active Directory
---

# Synchronize Active Directory

Active Directory objects can be used to create security groups based on user identity, and identity-based firewall rules.

Do not enable Distributed Intrusion Detection Service (IDS) in an environment that is using Distributed Load Balancer. NSX does not support using IDS with a Distributed Load Balancer.

You can register an entire AD (Active Directory) domain to be used by IDFW (Identity Firewall), or you can synchronize a subset of a large domain. Once a domain is registered, NSX synchronizes all AD data required by IDFW. Selective sync is used for large active directory domains.

Selective sync allows you to selectively choose organizational units so that you do not have to sync the entire domain. Only the selected organization units which are created and changed since the last delta sync will be updated during a selective sync. Groups that are moved out of the selected organization units are not updated during a selective sync. Configuration maximums still apply selective sync. Deleted groups are removed in a full sync, when all groups are updated. To specify organization units for synchronization, see [Configuring Active Directory and Event Log Scraping](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configuring-active-directory-and-event-log-scraping.html#GUID-405fbbd6-44c1-41e4-bc9f-f0658d3145d0-en).

Use the API to connect an AD domain with more than 500 OUs. The UI does not support showing an AD Domain with more than 500 OUs.

If you use the API to manually end a full sync after it is has begun, the sync stats will not be updated correctly.

Scale limits for Active Directory and IDFW can be found on the [VMware Configuration Maximums](https://configmax.vmware.com/guest?vmwareproduct=NSX-T%20Data%20Center&release=NSX-T%20Data%20Center%203.1.3&categories=19-47) page.

IDFW relies on the security and integrity of the guest operating system. There are multiple methods for a malicious local administrator to spoof their identity to bypass firewall rules. User identity information is provided by the Guest Introspection Agent inside guest VMs. Security administrators must ensure that NSX Guest Introspection Agent is installed and running in each guest VM. Logged-in users should not have the privilege to remove or stop the agent.

1. With admin privileges, log in
   to NSX Manager.
2. Navigate to SystemIdentity Firewall AD.
3. Click the three button menu (![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)) next to the Active Directory that you want to synchronize, and select one of the following: 

   Option | Description || Sync All | Full sync of all data is performed from the Active Directory, regardless of the state of sync on NSX. |
   | Sync Delta | Perform a delta synchronization, where local AD objects that have changed since the last synchronization are updated. A full sync of all data is not performed. Deleted groups are removed during Sync All, when all groups are updated. |
4. Click Save.
5. Click View Sync Status to see the current state of the Active Directory, the previous synchronization state, the synchronization status, and the last synchronization time.