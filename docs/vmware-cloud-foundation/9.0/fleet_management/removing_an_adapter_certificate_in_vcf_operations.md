---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates/removing-adapter-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Removing an Adapter Certificate in VCF Operations
---

# Removing an Adapter Certificate in VCF Operations

You can delete an old or expired certificate associated with an adapter.

1. In a Web browser, navigate to the VCF Operations administration interface at https://node-FQDN-or-ip-address/ui.
2. Log in with the administrator user name and password.
3. In the menu, click AdministrationControl Panel, and then click the Trusted Certificates tile.
4. In the certificate window, select the certificate that has to be removed.
5. Click Delete to remove the certificate.

   You must own the credential used to configure the adapter to be able to delete the certificate. For more information, see [Configuring Credentials in Integrations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/configuring-credentials-in-integrations.html).
6. If the certificate is being used by the adapter, then the following message comes up: 

   ![The screenshot displays the confirmation dialog box. You can click yes to confirm the deletion or no to cancel.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/56e57e56-a80c-4a38-a8a2-1d18a9ccd313.original.png)

   A certificate can be configured for one or more adapters if it is the same destination system.
7. If you delete a certificate which is already being used by another adapter, the adapter fails to connect or start. As a workaround, perform the following steps: 
   1. On the left pane, click AdministrationIntegrations. 

      The Accounts tab appears.
   2. Select the particular integration and click the vertical ellipsis and then click  Edit.

      The Account Information page opens.
   3. Click Validate Connection.

      If the adapter instance is saved using a credential that is owned by another user, you must apply your own credentials to validate the connection. For more information, see [Manage Credentials](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/integrations-in-vmware-aria-operations/configuring-credentials-in-integrations/credentials-manage-credentials.html).
   4. A prompt comes up asking the user to import the associated certificate. Click OK.
   5. Restart the adapter from the Accounts tab