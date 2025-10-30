---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configuring Cloud Proxies in VCF Operations
---

# Configuring Cloud Proxies in VCF Operations

You need cloud proxies to collect data from physical data centers. You can deploy classic or unified cloud proxies based on your requirements. For high availability or load balancing, you must deploy two or more cloud proxies in a collector group. A cloud proxy collects data from the end-point environment and uploads it to VCF Operations. Cloud proxies can support multiple vCenter accounts. For more information on cloud proxies, see [Cloud Proxy FAQ](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-faq.html).

- Verify that you have an IP address and a DNS configuration for the cloud proxy.
- Verify that you have proper permissions to deploy OVF templates in vSphere. For more information, see [Deploy and Export OVF and OVA Templates](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_027&appid=vsphere-9-0&language=&format=rendered).
- Allow outgoing HTTPS traffic for cloud proxy over port 443. For more information on firewall requirements, see KB article [93210](https://kb.vmware.com/s/article/93210).
- Allow incoming traffic to cloud proxy over ports 443, 8443, 4505, and 4506 for telegraf based application monitoring.
- Allow incoming traffic to cloud proxy over port 443 for push model adapters or Suite-API on cloud proxy.
- Verify that the user has the required Cloud Proxy roles to access configuration templates. For more information, see the [Access Control: Roles Tab](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/-configuring-administration-settings/managing-user-access-control/access-control-overview/access-control-roles-tab.html).
- Add a vCenter cloud account and provide an account with the following read and write privileges:

  - vCenter IP address or FQDN.
  - Permissions required to install a cloud proxy on the vCenter Server.

  For more information on privileges, see [Privileges Required for Configuring a Adapter Instance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations/privileges-required-for-configuring-a-vcenter-adapter-instance.html).
- Cloud proxies must have a proper DNS resolution to the VCF Operations nodes when using short/long FQDN names.

Using a firewall to restrict traffic by IP is not recommended since IPs can change without notice. Restricting traffic must be performed via FQDNs only.

Refer to the cloud proxy sizing requirements before configuring a cloud proxy. For more information, see [Collecting Data with Cloud Proxy in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud.html).

1. Log in to VCF Operations.
2. From the left menu, click AdministrationCloud Proxies, and then click Add.
3. Click Broadcom support portal to navigate to the Broadcom support portal, log in using your credentials. and download the cloud proxy OVA file.

   VCF Operations supports log collection and log assist. You can download and deploy an unified cloud proxy OVA to collect logs. If you do not want to use your cloud proxy for log collection or log assist, download and deploy a classic cloud proxy OVA. For more information on types of cloud proxy and sizing requirements, see [Collecting Data with Cloud Proxy in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud.html).
4. Navigate to your vCenter, select the name of your vSphere,cluster, and select Deploy OVF Template from the Actions menu.
5. Insert the OVA link and then click Next.
   - Paste the cloud proxy OVA link in the URL field.
   - Click the Local File option, browse, and select the downloaded OVA file.
6. Follow the prompts to install the OVA on your vCenter.

   For the most current information about sizing and scaling, see [Knowledge Base article 78491](https://kb.vmware.com/s/article/78491).
7. When prompted to enter the Unique Registration Key in the Customize template screen, return to the Install Cloud Proxy page in VCF Operations.
8. Activate Data Persistence to store data in the cloud proxy in case of connectivity issues. For more information, see [Activating Data Persistence in Cloud Proxy](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud/activating-data-persistence-in-cloud-proxy.html#GUID-b9ecdac5-f75f-428a-82e6-ac74ad72613e-en).
9. Click the Copy Key icon.

   The unique registration key expires 24 hours after generation. To avoid using an expired key, click Regenerate Key before proceeding. The unique registration key is used by the cloud proxy to authenticate to VCF Operations.

   Upon clicking Regenerate Key, the unique registration key is refreshed and a new key is generated if you reload the cloud proxy page. A new unique registration key is generated if you activate data persistence, or log forwarding, or both.
10. Return to vSphere and paste the key in the Unique Registration Key text box to install the VCF Operations Cloud Proxy.
11. Select Prefer IPv6 to use IPv6 for internal communications.
12. Set up a proxy server in the Customize template screen. 
    1. Enter details in the Network Proxy IP Address and Network Proxy Password properties. 

       If you use network proxy for log forwarding, port 9543 must be open.
    2. To activate SSL, select the Use SSL connection to proxy check box.
    3. If you are using SSL, you can verify the certificate of the proxy server. Public certificate authorities are used to verify the proxy server certificate. To activate this, select the Verify proxy's SSL cert check box in the Verify SSL cert property.
    4. You can specify the IP/FQDN URL that is used to access the system when a load balancer is used.
    5. If you have a custom certificate authority, paste the root certificate authority in the Custom CA property to verify the certificate of the proxy server. Include the following lines when you copy the root certificate authority:

       ```
       "-----BEGIN CERTIFICATE-----"
       ```

       ```
       "-----END CERTIFICATE-----"
       ```
13. Click Finish. 

    The deployment takes a few minutes to finish.
14. Locate the cloud proxy you just installed, select the VCF Operations Cloud Proxy, and click Power on.

    You must power on the VMware Aria Operations Cloud Appliance within 24 hours of registering it. After 24 hours, the Unique Registration Key expires, and you must delete the VMware Aria Operations Cloud Appliance and deploy another cloud proxy.
15. Return to the Cloud Proxy page in VCF Operations to view the status of the cloud proxy you just installed. For more information, see [Monitoring the Health of Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies.html#GUID-6887a5cc-2bce-41e9-b965-603887775adb-en).
16. To view the accounts that are using this connection, click the Cloud Proxy.
17. To delete a cloud proxy, click the vertical ellipsis and then click Delete. For more information, see [Deleting Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/deleting-cloud-proxies.html#GUID-c9122649-6bb4-4142-be04-9e9f7948adc6-en).