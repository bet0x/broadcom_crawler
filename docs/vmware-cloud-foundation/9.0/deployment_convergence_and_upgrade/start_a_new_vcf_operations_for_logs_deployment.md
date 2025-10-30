---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/vcf-operations-for-logs-for-vvf-clients/start-a-new-vcf-operations-for-logs-deployment.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Start a New VCF Operations for Logs Deployment
---

# Start a New VCF Operations for Logs Deployment

When you access the VCF Operations for logs web interface for the first time after the virtual appliance deployment or after removing a worker node from a cluster, you must finish the initial configuration steps.

- In the vSphere Client, note the IP address of the VCF Operations for logs virtual appliance.
- Verify that you are using a supported browser.

More recent browser versions also work, but have not been validated. Cookies must be activated in your browser. Supported browsers are:

- Mozilla Firefox 45.0 and above
- Google Chrome 51.0 and above
- Safari 9.1 and above
- Internet Explorer 11.0 and above
  - Internet Explorer Document mode must be set to **Standards Mode**. Other modes are not supported.
  - **Browser Mode:** Compatibility View is not supported.
  - To use Internet Explorer with the VCF Operations for logs web interface, Windows local storage integrity level must be configured as low.

All settings that you modify during the initial configuration are also available in the Configuration web user interface.

1. Use a supported browser to navigate to the web user interface of VCF Operations for logs. 

   The URL format is https://operations\_for\_logs-host/, where operations\_for\_logs-host is the IP address or host name of the VCF Operations for logs virtual appliance.

   The initial configuration wizard opens.
2. Click Start New Deployment.
3. Set the password for the administrator (user name admin) and click Save and Continue. Optionally, you can provide an email address for the administrator. 

   The administrator is a user linked to the Super Admin role.
4. Enter the license key, click Add License Key, and click Save and Continue.
5. On the General Configuration page, enter the email address to receive system notifications from VCF Operations for logs.
6. If you are using webhooks to send notifications to VCF Operations or a third-party application, enter a space-separated list of URLs in the Send HTTP Post System Notifications To text box.
7. To leave the CEIP, deselect the Join the VMware Customer Experience Program option. Click Save and Continue. 

   If you join the CEIP, VCF Operations for logs uses a third-party tool called Pendo to collect analytics cookies. Pendo collects data based on your interaction with the user interface by tracking where you click, to help VMware understand how VCF Operations for logs is used. This data is used to improve the VMware services and design them better.
8. On the Time Configuration page, set how time is synchronized on the VCF Operations for logs virtual appliance and click Test. 

   Option | Description || ESX host | By default, VCF Operations for logs is configured to synchronize time with the ESX host where you deployed the VCF Operations for logs virtual appliance. |
9. Click Save and Continue.
10. To enable outgoing alert and system notification emails, specify the properties of an SMTP server. 

    To verify that the SMTP configuration is correct, enter a valid email address and click Test. VCF Operations for logs sends a test email to the address that you provided.
11. To provide a custom SSL certificate, upload a certificate file to the cluster in a PEM format. You can also view the details of the existing certificate.

    The system adds the certificate to the truststores of all the nodes of the cluster and saves it for later use.
12. Click Save and Continue.

After the VCF Operations for logs process restarts, you are redirected to the Dashboards page of VCF Operations for logs.

- Log in to the VCF Operations UI. Navigate to AdministrationControl Panel and click the Operations-Logs Appliance Integration tile. Enter the address, username and password of the VCF Operations for logs deployment. This completes the VCF Operations integration with VCF Operations for logs.
- In the VCF Operations UI, navigate to Infrastructure OperationsConfigurationsLog Collections. Configure the vCenter instance. This configuration is to pull tasks, events, and alerts, and to configure ESX hosts to send syslog feeds to VCF Operations for logs.
- Install the VCF Operations for logs Linux Agent for monitoring journal service.