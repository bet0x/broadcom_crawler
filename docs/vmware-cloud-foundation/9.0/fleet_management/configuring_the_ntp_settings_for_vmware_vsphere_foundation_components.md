---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/admin-ui-global-ntp-settings-page.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configuring the NTP Settings for VMware vSphere Foundation Components
---

# Configuring the NTP Settings for VMware vSphere Foundation Components

To configure the NTP configuration for your VMware vSphere Foundation component, you can use the VCF Operations administration UI.

The Network Time Protocol (NTP) setting is used to synchronize the time of your VCF Operations cluster nodes. Configure the NTP setting in VCF Operations to ensure that all the cluster nodes follow the same time protocol. Following the same time protocol allows your cluster's services to run smoothly. The primary node serves as the NTP server by default and the time of all nodes are synchronized to the primary node. You can continue using the primary node as the NTP server and add another NTP server to serve as a failover if the primary node fails. In case you do not want to use the primary node, you can add the NTP server you wish to use.

1. Log in to the VCF Operations administration interface at https://primary-node-name-or-ip-address/admin.
2. Click the NTP Settings icon.

   The Global Network Time Protocol settings wizard opens. The primary node is listed as the existing NTP server.

   You must configure at least two NTP servers to have a back-up if one server fails.
3. Add a secondary NTP server. Enter the IP of FDQN of the NTP server you wish to use in NTP Server Address field.
4. Click Add.

   The new NTP server is displayed along with the primary node.
5. Ensure that the status of the NTP server is green which means its reachable and working.
6. To delete a NTP server, click Remove next to the NTP server status.