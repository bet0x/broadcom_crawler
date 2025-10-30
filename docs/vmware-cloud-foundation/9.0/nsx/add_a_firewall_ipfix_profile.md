---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/network-monitoring/add-a-firewall-ipfix-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Firewall IPFIX Profile
---

# Add a Firewall IPFIX Profile

You can configure IPFIX profiles for firewalls.

1. With admin privileges, log in
   to NSX Manager.
2. Select Plan &
   TroubleshootIPFIX.
3. Click the Firewall IPFIX Profiles tab.
4. Click Add Firewall IPFIX Profile.
5. Complete the following details. 

   | Setting | Description |
   | --- | --- |
   | Name and Description | Enter a name and optionally a description. If you want to create a global profile, name the profile global. A global profile cannot be edited or deleted from the UI, but you can do so using NSX APIs. |
   | Active Flow Export Timeout (Minutes) | The length of time after which a flow will time out, even if more packets associated with the flow are received. Default is 1. |
   | Observation Domain ID | This parameter identifies which observation domain the network flows originate from. The default is 0 and indicates no specific observation domain. |
   | Collector Configuration | Select a collector from the drop-down menu. |
   | Applied To | Click Set and select a group to apply the filter to, or create a new group. If another IPFIX profile exists and applies to the same group, this new profile will take precedence. The Applied To setting of the previous profile will be removed. |
   | Priority | This parameter resolves conflicts when multiple profiles apply. The IPFIX exporter will use the profile with the highest priority only. A lower value means a higher priority. |
6. Click Save and then Yes to continue configuring the profile.
7. Click Save.