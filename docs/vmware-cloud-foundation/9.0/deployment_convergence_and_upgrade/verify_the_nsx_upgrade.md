---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/verify-the-upgrade-nsxt.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Verify the NSX Upgrade
---

# Verify the NSX Upgrade

After you upgrade NSX, you can verify whether the versions of the upgraded components have been updated. For more information on the NSX Manager, see "Overview of the NSX Manager" in the NSX Administration Guide.

Perform a successful upgrade.

1. From your browser, log in as a local admin user to an NSX Manager at https://nsx-manager-ip-address/login.jsp?local=true.
2. Select SystemUpgrade.
3. Verify that the overall upgrade version, component version, and initial and target product version are accurate. 
   1. Verify that the Dashboard, fabric hosts, edge cluster, transport nodes, and all logical entities status indicators are green, normal, deployed, and do not show any warnings.
   2. Verify the status of several components. 

      - Fabric nodes installation
      - Transport node Local Control Plane (LCP) and Management plane agent connectivity
      - Routers connectivity
      - NAT rules
      - DFW rules
      - DHCP lease
      - BGP details
      - Flows in the IPFIX collector
      - TOR connectivity to enable the network traffic

   The status of the upgrade appears as Successful.

   If you upgraded from NSX 4.1.x or earlier, you will see new [system-generated transport zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html) in addition to the transport zones originally configured in your source deployment.

   - For clusters prepared for networking and security, you will see new security transport zones. The system generates these security transport zones by default.
   - For clusters prepared for NSX on DVPGs, you will see new VLAN transport zones. The system generates these VLAN transport zones by default.
4. Modify the default admin password expiration.

   If the password expires, you will be unable to log in and manage components. Additionally, any task or API call that requires the administrative password to execute will fail. By default, passwords expire after 90 days. For more information, see Knowledge Base article 338942: [NSX admin password expired](https://knowledge.broadcom.com/external/article?articleNumber=338942).

   1. Reset the expiration period.

      You can set the expiration period for between 1 and 9999 days.

      ```
      nsxcli set user admin password-expiration <1 - 9999>
      ```
   2. You can disable password expiry so the password never expires.

      ```
      nsxcli clear user audit password-expiration
      ```
5. If you have VIDM enabled, access your the local account at https://nsx-manager-ip-address/login.jsp?local=true.
6. Verify CPU and Memory values for edge VMs.

   After upgrading, log in to the vSphere Client to verify if your existing edge VMs are configured with the following CPU and Memory values. If they are not, edit the VM settings to match these values.

   | NSX Edge Form Factor | Memory | vCPU |
   | --- | --- | --- |
   | NSX Edge Small VM | 4 GB | 2 |
   | NSX Edge Medium VM | 8 GB | 4 |
   | NSX Edge Large VM | 32 GB | 8 |
7. (For upgrades from NSX 4.1.x or earlier) Create a new certificate for the NSX cluster VIP, either self-signed or signed by a third-party Certificate Authority, that includes the Subject Alternative Name and Subject Alternative IP for all NSX Manager nodes in the cluster.

   This step ensures a successful repository sync for any NSX Manager node that is redeployed in the future. For more information, see KB article 395087: [After redeploying NSX Manager, repo sync is in failed status](https://knowledge.broadcom.com/external/article?articleNumber=395087).
8. [Download the Consistency Check Report](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/download-consistency-check-report.html) and remediate any failures detected during the upgrade.