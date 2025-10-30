---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/restoring-nsx-t-manager-nodes-to-an-existing-cluster/add-a-new-nsx-t-manager-node-to-the-nsx-t-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Redeploy the Failed NSX Manager Node
---

# Redeploy the Failed NSX Manager Node

You deploy a new NSX Manager instance by using the configuration of the failed node.

Download the NSX Manager OVA file for the version of the failed NSX Manager instance. See [Retrieve the NSX Manager Version from SDDC Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/backup-and-restore-of-cloud-foundation/file-based-restore-for-sddc-manager-vcenter-server-and-nsx-t-data-center/restore-nsx-t-manager/prepare-for-restoring-nsx-t-manager/preparing-to-restore-nsx-t-manager-instance.html#GUID-eeca4c73-977d-4bb3-83e9-9e3d901b8d4e-en).

1. Log in to the vCenter interface at https://<vcenter\_fqdn>/ui with a user assigned the Administrator role.
2. Select MenuVMs and Templates.
3. In the inventory expand vCenterDatacenter.
4. Right-click the NSX folder and select Deploy OVF Template.
5. On the Select an OVF template page, select Local file, click Upload files, navigate to the location of the NSX Manager OVA file, click Open, and click Next.
6. On the Select a name and folder page, in the Virtual machine name text box, enter VM name of the failed node, and click Next.
7. On the Select a compute resource page, click Next.
8. On the Review details page, click Next.
9. On the Configuration page, select Medium, and click Next.
10. On the Select storage page, select the vSAN datastore, and click Next.
11. On the Select networks page, from the Destination network drop-down menu, select the management network distributed port group, and click Next.
12. On the Customize template page, enter these values and click Next.

    | Setting | Value |
    | --- | --- |
    | System root user password | nsx\_root\_password |
    | CLI admin user password | nsx\_admin\_password |
    | CLI audit password | nsx\_audit\_password |
    | Hostname | failed\_node\_FQDN |
    | Default IPv4 gateway | Enter the default gateway for the appliance. |
    | Management network IPv4 address | failed\_node\_IP\_address |
    | Management network netmask | Enter the subnet mask for the appliance. |
    | DNS server list | Enter the DNS servers for the appliance. |
    | NTP servers list | Enter the NTP services for the appliance. |
    | Enable SSH | Deselected |
    | Allow root SSH logins | Selected |
13. On the Ready to complete page, review the deployment details and click Finish.

    The NSX Manager virtual machine begins to deploy.