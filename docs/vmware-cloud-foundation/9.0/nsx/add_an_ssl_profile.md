---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/load-balancer/setting-up-load-balancer-components/setting-up-virtual-server-components/add-an-ssl-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add an SSL Profile
---

# Add an SSL Profile

SSL profiles configure application-independent SSL properties such as, cipher lists and reuse these lists across multiple applications. SSL properties are different when the load balancer is acting as a client and as a server, as a result separate SSL profiles for client-side and server-side are supported.

SSL profile is not supported in the NSX limited export release.

Client-side SSL profile refers to the load balancer acting as an SSL server and stopping the client SSL connection. Server-side SSL profile refers to the load balancer acting as a client and establishing a connection to the server.

You can specify a cipher list on both the client-side and server-side SSL profiles. NSX Managers come with the following default SSL Profiles:

- default-balanced-client-ssl-profile
- default-balanced-server-ssl-profile
- default-high-compatibility-client-ssl-profile
- default-high-compatibility-server-ssl-profile
- default-high-security-client-ssl-profile,
- default-high-security-server-ssl-profile.

The "balanced" SSL Profile supports a mix of SSL protocols and ciphers to offer a perfect mix of performance and security to clients/servers. The "high-compatibility" SSL Profile supports a large range of SSL protocols and ciphers to offer access to the widest range of clients/servers. The "high-security" SSL Profile supports the highest-secured SSL protocols and ciphers to offer the most secured access to clients/servers. Additionally, custom SSL profiles can be created.

The cipher TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 is also added to the balanced and high compatibility client/server profiles to support the communication between the NSX Manager and a load balancer virtual server for vIDM. With this new addition, you no longer need to create a custom profile and add the cipher TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 as a workaround for supporting the communication between the NSX Manager and a vIDM LB VIP.

SSL session caching allows the SSL client and server to reuse previously negotiated security parameters avoiding the expensive public key operation during the SSL handshake. SSL session caching is disabled by default on both the client-side and server-side.

SSL session tickets are an alternate mechanism that allows the SSL client and server to reuse previously negotiated session parameters. In SSL session tickets, the client and server negotiate whether they support SSL session tickets during the handshake exchange. If supported by both, server can send an SSL ticket, which includes encrypted SSL session parameters to the client. The client can use that ticket in subsequent connections to reuse the session. SSL session tickets are enabled on the client-side and disabled on the server-side.

SSL Offloading

![A diagram of SSL offloading.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a3c799b2-df79-4426-a341-e186f216332e.original.png)


End-to-End SSL

![A diagram of end-to-end SSL.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f77d8be3-c882-4a3b-b837-f4d786d0ff0a.original.png)

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingLoad BalancingProfilesSSL Profile.
3. Select a Client SSL Profile and enter the profile details. 

   Option | Description || Name and Description | Enter a name and a description for the Client SSL profile. |
   | SSL Suite | Select the SSL Cipher group from the drop-down menu and available SSL Ciphers and SSL protocols to be included in the Client SSL profile are populated. Balanced SSL Cipher group is the default. |
   | Session Caching | Toggle the button to allow the SSL client and server to reuse previously negotiated security parameters avoiding the expensive public key operation during an SSL handshake. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |
   | Supported SSL Ciphers | Depending on the SSL suite, you assigned the supported SSL Ciphers are populated here. Click View More to view the entire list. If you selected Custom, you must select the SSL Ciphers from the drop-down menu. |
   | Supported SSL Protocols | Depending on the SSL suite, you assigned the supported SSL protocols are populated here. Click View More to view the entire list. If you selected Custom, you must select the SSL Ciphers from the drop-down menu. |
   | Session Cache Entry Timeout | Enter the cache timeout in seconds to specify how long the SSL session parameters must be kept and can be reused. |
   | Prefer Server Cipher | Toggle the button so that the server can select the first supported cipher from the list it can support. During an SSL handshake, the client sends an ordered list of supported ciphers to the server. |
4. Select a Server SSL Profile and enter the profile details. 

   Option | Description || Name and Description | Enter a name and a description for the Server SSL profile. |
   | SSL Suite | Select the SSL Cipher group from the drop-down menu and available SSL Ciphers and SSL protocols to be included in the Server SSL profile are populated. Balanced SSL Cipher group is the default. |
   | Session Caching | Toggle the button to allow the SSL client and server to reuse previously negotiated security parameters avoiding the expensive public key operation during an SSL handshake. |
   | Tags | Enter tags to make searching easier. You can specify a tag to set a scope of the tag. |
   | Supported SSL Ciphers | Depending on the SSL suite, you assigned the supported SSL Ciphers are populated here. Click View More to view the entire list. If you selected Custom, you must select the SSL Ciphers from the drop-down menu. |
   | Supported SSL Protocols | Depending on the SSL suite, you assigned the supported SSL protocols are populated here. Click View More to view the entire list. If you selected Custom, you must select the SSL Ciphers from the drop-down menu. |
   | Session Cache Entry Timeout | Enter the cache timeout in seconds to specify how long the SSL session parameters must be kept and can be reused. |
   | Prefer Server Cipher | Toggle the button so that the server can select the first supported cipher from the list it can support. During an SSL handshake, the client sends an ordered list of supported ciphers to the server. |