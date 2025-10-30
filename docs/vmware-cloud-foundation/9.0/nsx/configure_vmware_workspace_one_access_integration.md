---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/configure-vmware-identity-manager-workspace-one-access-integration.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure VMware Workspace ONE Access Integration
---

# Configure VMware Workspace ONE Access Integration

You can integrate NSX with VMware Workspace ONE Access, which provides identity management services. The Workspace ONE Access deployment can be a standalone Workspace ONE Access host or an Workspace ONE Access cluster.

- Verify that you have the certificate thumbprint from the Workspace ONE Access host or the Workspace ONE Access load balancer, depending on the type of Workspace ONE Access deployment (a standalone Workspace ONE Access host or an Workspace ONE Access cluster). You can use the same command in both cases to obtain the thumbprint. See [Obtain the Certificate Thumbprint from an VMware Workspace ONE Access Host](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/obtain-the-certificate-thumbprint-from-a-vidm-host.html#GUID-b7149451-b1f1-4158-bc7e-ea8f4d577558-en).
- Verify that NSX Manager is registered as an OAuth client to Workspace ONE Access . During the registration process, note the client ID and the client secret. For more information, see the [Omnissa Access documentation](https://docs.omnissa.com/category/Workspace_ONE_Access). When you create the client, you only need to do the following:

  - Set Access Type to Service Client Token.
  - Specify a client ID.
  - Expand the Advanced field and click Generate Shared Secret.
  - Click Add.

Note: VMware Workspace ONE Access is the product formerly known as Workspace ONE Access or VMware Identity Manager (vIDM).

The Workspace ONE Access host or all the Workspace ONE Access cluster components should have a certificate signed by a certificate authority (CA). Otherwise, logging in to Workspace ONE Access from NSX Manager might not work with certain browsers, such as Microsoft Edge or Internet Explorer 11. For information about installing a CA-signed certificate on Workspace ONE Access, see the [Omnissa Access documentation](https://docs.omnissa.com/category/Workspace_ONE_Access).

When you register NSX Manager with Workspace ONE Access, you specify a redirect URI that points to NSX Manager. You can provide either the fully qualified domain name (FQDN) or the IP address. It is important to remember whether you use the FQDN or the IP address. When you try to log in to NSX Manager through Workspace ONE Access, you must specify the host name in the URL the same way, that is, if you use the FQDN when registering the manager with Workspace ONE Access, you must use the FQDN in the URL, and if you use the IP address when registering the manager with Workspace ONE Access, you must use the IP address in the URL. Otherwise, login will fail.

If NSX API access is needed, one of the following configurations must be true:

- Workspace ONE Access has a known CA-signed certificate.
- Workspace ONE Access has the connector CA certificate trusted on the Workspace ONE Access service side.
- Workspace ONE Access uses outbound connector mode.

NSX Managers and Workspace ONE Access must be in the same time zone. The recommended way is to use UTC.

You must configure your DNS servers to have PTR records if you are not using Virtual IP or an external load balancer (this means that the manager is configured using the physical IP or FQDN of the node).

If you configure Workspace ONE Access to be integrated with an external load balancer, you must enable session persistence on the load balancer to avoid issues such as pages not loading or a user being unexpectedly logged out.

If the Workspace ONE Access deployment is an Workspace ONE Access cluster, the Workspace ONE Access load balancer must be configured for SSL termination and re-encryption.

With Workspace ONE Access enabled, you can still log in to NSX Manager with a local user account if you use the URL https://<nsx-manager-ip-address>/login.jsp?local=true.

If you use the UserPrincipalName (UPN) to log in to Workspace ONE Access, authentication to NSX might fail. To avoid this issue, use a different type of credentials, for example, SAMAccountName.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemUser ManagementAuthentication ProvidersVMware Identity Manager
3. Click Edit.
4. To enable external load balancer integration, click the External Load Balancer Integration toggle. 

   If you have Virtual IP (VIP) set up (check SystemAppliancesVirtual IP), you cannot use the External Load Balancer Integration even if you enable it. This is because you can either have VIP or the External Load Balancer while configuring Workspace ONE Access but not both. Disable VIP if you want to use the External Load Balancer. See the topic Configure a Virtual IP Address for a Cluster in the section Advanced Network Management with NSX.
5. To enable VMware Workspace ONE Access integration, click the VMware Identity Manager Integration toggle.
6. Provide the following information. 

   Parameter | Description || VMware Identity Manager Appliance | The fully qualified domain name (FQDN) of the Workspace ONE Access host or the Workspace ONE Access load balancer, depending on the type of Workspace ONE Access deployment (a standalone Workspace ONE Access host or an Workspace ONE Access cluster). |
   | OAuth Client ID | The ID that is created when registering NSX Manager to Workspace ONE Access. |
   | OAuth Client Secret | The secret that is created when registering NSX Manager to Workspace ONE Access. |
   | SSL Thumbprint | The certificate thumbprint of the Workspace ONE Access host. It must be an SHA-256 thumbprint. |
   | NSX Appliance | The IP address or fully qualified domain name (FQDN) of NSX Manager. If you are using an NSX Manager cluster, use the load balancer FQDN or cluster VIP FQDN or IP address. If you specify a FQDN, you must access NSX Manager from a browser using the manager's FQDN in the URL, and if you specify an IP address, you must use the IP address in the URL. Alternatively, the Workspace ONE Access administrator can configure the NSX Manager client so that you can connect using either the FQDN or the IP address. |
7. Click Save.