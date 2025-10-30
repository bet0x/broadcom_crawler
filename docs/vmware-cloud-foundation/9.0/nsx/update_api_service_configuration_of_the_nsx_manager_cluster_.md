---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/update-api-service-configuration-of-the-nsx-manager-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Update API Service Configuration of the NSX Manager Cluster 
---

# Update API Service Configuration of the NSX Manager Cluster

You can modify the API service properties of the NSX Manager cluster, such as TLS protocol version, cipher suites, and so
on.

Starting in 4.2, TLS 1.1 ciphers are
deactivated by default, but can be activated by the user using the following
procedure. The supported ciphers for TLS 1.1 are:

- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA

The supported ciphers for TLS 1.2 are:

- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

The supported ciphers for TLS 1.3 are:

- TLS\_AES\_128\_GCM\_SHA256
- TLS\_AES\_256\_GCM\_SHA384
- TLS\_CHACHA20\_POLY1305\_SHA256
- Starting in NSX 4.2,
  TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

The following procedure explains the workflow of running the NSX API service calls to
activate the TLS 1.1 protocol, and to activate or deactivate the cipher suites in
the API service configuration. TLS 1.1 is deactivated by default. You can use this
same procedure to deactivate other TLS versions as
needed. Note that NSX supports a minimum and maximum
version, so support of TLS 1.1 and TLS 1.3, but not TLS 1.2 is not supported. For
example, TLS 1.1 and TLS 1.2 or TLS 1.2 and TLS 1.3 can be supported.

For a detailed information about the API schema, example request, example response,
and error messages of the NSX API service, read the NSX API Guide.

1. Run the following GET API to
   read the configuration of the NSX API service:

   GET
   https://<NSX-Manager-IP>/api/v1/cluster/api-service

   The API response contains the list of cipher suites and TLS protocols.
   Note that the TLS 1.0 support is not
   listed.

   ```
   curl -u admin:${PASSWORD} -i -k https://$IP/api/v1/cluster/api-service  "protocol_versions" : [ {
       "name" : "TLSv1.1",
       "enabled" : false
     }, {
       "name" : "TLSv1.2",
       "enabled" : true
     }, {
       "name" : "TLSv1.3",
       "enabled" : true
     } ],
   ```
2. ```
   curl -u admin:${PASSWORD} -i -k https://$IP/api/v1/cluster/api-service
   {
     "global_api_concurrency_limit": 199,
     "client_api_rate_limit": 100,
     "client_api_concurrency_limit": 40,
     "connection_timeout": 30,
     "redirect_host": "",
     "cipher_suites": [
       {"enabled": true, "name": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"},
       {"enabled": true, "name": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"},
       {"enabled": true, "name": "TLS_RSA_WITH_AES_256_GCM_SHA384"},
       {"enabled": true, "name": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"},
       {"enabled": true, "name": "TLS_RSA_WITH_AES_128_GCM_SHA256"}
       {"enabled": true, "name": "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384}",
       {"enabled": true, "name": "TLS_RSA_WITH_AES_256_CBC_SHA256"},
       {"enabled": true, "name": "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"},
       {"enabled": true, "name": "TLS_RSA_WITH_AES_256_CBC_SHA"},
       {"enabled": true, "name": "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"},
       {"enabled": true, "name": "TLS_RSA_WITH_AES_128_CBC_SHA256"},
       {"enabled": false, "name": "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"},
       {"enabled": false, "name": "TLS_RSA_WITH_AES_128_CBC_SHA"}
       {"enabled": false, "name": "TLS_RSA_WITH_AES_128_CBC_SHA"}         
     ],
     "protocol_versions": [
       {"enabled": false, "name": "TLSv1.1"},
       {"enabled": true, "name": "TLSv1.2"}
       {"enabled": true, "name": "TLSv1.3"}]
   }
   ```
3. Activate or deactivate the TLS
   1.1 protocol.
   1. To activate a TLS
      version, set TLSv1.1 to enabled =
      true, for example. To deactivate a TLS version, set your
      TLS version to enabled = false.
   2. Run the following PUT
      API to send the changes to the NSX API server:

      PUT
      https://<NSX-Manager-IP>/api/v1/cluster/api-service
4. Activate or deactivate the
   cipher suites.
   1. Set one or more cipher
      names to enabled = true or enabled =
      false depending on your requirements.
   2. Run the following PUT
      API to send the changes to the NSX API server:

      PUT
      https://<NSX-Manager-IP>/api/v1/cluster/api-service
5. Verify the activation is complete.

The API service on each NSX Manager node restarts after it is updated using the API. There
might be a delay of up to a minute between the time the API call completes and when
the new configuration comes into effect. The changes in the API service
configuration are applied to all the nodes in the NSX Manager cluster.