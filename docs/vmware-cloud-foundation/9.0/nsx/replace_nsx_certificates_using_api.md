---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Replace NSX Certificates Using API
---

# Replace NSX Certificates Using API

After you install NSX, the manager nodes and cluster have self-signed certificates. You can optionally replace the API and MGMT\_CLUSTER (aka VIP) self-signed certificates with common CA-signed certificate with a SAN (Subject Alternative Name) that matches the FQDNs and IPs of all the nodes and the VIP for the cluster. You can run only one certificate replacement operation at a time.

- Verify that a certificate is available in the NSX Manager. Note that on a standby Global Manager the UI import operation is deactivated. For details on the import REST API command for a standby Global Manager, refer to [Import a Self-signed or CA-signed Certificate for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-certificate.html#GUID-7c651d93-4af8-45f8-a5a4-0ce67739291c-en).
- The server certificate must contain the Basic Constraints extension basicConstraints = CA:FALSE.
- Verify that the certificate is valid by making the following API call:

  GET https://<nsx-mgr>/api/v1/trust-management/certificates/<cert-id>?action=validate
- Have your node ID string available, if needed. For help locating this information using the UI or the CLI, refer to [Finding NSX Node IDs for Certificate API Calls](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/finding-node-ids-for-certificate-api-calls.html).

Do not use automated scripts to replace multiple certificates at the same time. Errors might occur.

If you are using NSX Federation, you can replace the GM API certificates, GM MGMT\_CLUSTER (aka VIP) certificate, LM API certificates, and LM MGMT\_CLUSTER (aka VIP) certificates using the following APIs.

Starting with NSX Federation 4.1, you can replace a self-signed certificate that is used for the GM-LM communication.

When you replace the GLOBAL\_MANAGER or LOCAL\_MANAGER certificate, the site-manager sends these to all the other federated sites, so the communication remains intact.

The cipher suite TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 can now be used or replaced for communication between:

- NSX nodes within a cluster.
- Within the NSX Federation.
- NSX Manager to NSX Edge.
- NSX Manager to NSX agent.
- NSX Manager REST API communication (external).

You can also replace the GLOBAL\_MANAGER and LOCAL\_MANAGER certificates. See [Certificates for NSX and NSX Federation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html#GUID-c283012b-c8e5-4e1e-b479-40005684524c-en) for details on self-signed certificates auto-configured for NSX Federation.

Starting with NSX 4.2, the API service on each manager and VIP share the same certificate. You can also bulk replace the shared certificate by running the following 'batch replace' API .

```
POST https://{{ip}}/api/v1/trust-management/certificates/action/batch-replace
{
    "certificate_replacements": [
        {
         "old_certificate_id": "fe3d2623-df43-4757-8018-b1d8223a1475"
         "new_certificate_id": "66370296-cacf-45a7-9912-6e2718df87bb"
        }
    ]
}
```

Optionally, you can also replace each API service and the VIP service with their own unique certificates by running the 'apply certificate' API mentioned in the following procedure.

Both the batch replace and apply certificate APIs should be performed after the manager cluster has formed, because starting with NSX 4.2 the API certificates of the joining manager are replaced by the MGMT\_CLUSTER (aka VIP) certificates of the cluster being joined.

1. With admin privileges, log in
   to NSX Manager.
2. Select SystemCertificates.
3. In the ID column, select the ID of the certificate you want to use and copy the certificate ID from the pop-up window. 

   Make sure that when this certificate was imported, the option Service Certificate was set to No.

   Note: The certificate chain must be in the industry standard order of certificate - intermediate - root.
4. To replace the API certificate of a manager node, use the following API call. To find your Unified Appliance node ID, refer to [Finding NSX Node IDs for Certificate API Calls](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/finding-node-ids-for-certificate-api-calls.html).

   ```
   POST /api/v1/trust-management/certificates/<cert-id>?action=apply_certificate&service_type=API&node_id=<node-id>
   ```

   For example:

   POST https://<nsx-mgr>/api/v1/trust-management/certificates/77c5dc5c-6ba5-4e74-a801-c27dc09be76b?action=apply\_certificate&service\_type=API&node\_id=e61c7537-3090-4149-b2b6-19915c20504f
5. To replace the certificate of the manager cluster VIP, use the API call: 

   ```
   POST /api/v1/trust-management/certificates/<cert-id>?action=apply_certificate&service_type=MGMT_CLUSTER
   ```

   For example:

   POST https://<nsx-mgr>/api/v1/trust-management/certificates/d60c6a07-6e59-4873-8edb-339bf75711?action=apply\_certificate&service\_type=MGMT\_CLUSTER

   Ensure the thumbprint value gets updated for each location's Local Manager from within the Global Manager's Location Manager. Otherwise, communication between GM and LMs are disrupted. Tasks like selecting an NSX Edge cluster or requesting a tier-0 BGP summary from the Global Manager UI will not work if the thumbprint is not updated. For more information about the API, see the NSX API Guide. This step is not necessary if you did not configure the VIP.
6. To replace the LOCAL\_MANAGER and GLOBAL\_MANAGER certificates for NSX Federation use the following API call. The entire NSX Manager cluster (Local Manager and Global Manager) requires one LOCAL\_MANAGER certificate and one GLOBAL\_MANAGER certificate.

   ```
   POST https://<nsx-mgr>/api/v1/trust-management/certificates/<cert-id>?action=apply_certificate&service_type=<service-type>
   ```

   For example:

   ```
               POST https://<local-mgr>/api/v1/trust-management/certificates/77c5dc5c-6ba5-4e74-a801-c27dc09be76b?action=apply_certificate&service_type=LOCAL_MANAGER
   ```

   Or

   ```
   POST https://<global-mgr>/api/v1/trust-management/certificates/77c5dc5c-6ba5-4e74-a801-c27dc09be76b?action=apply_certificate&service_type=GLOBAL_MANAGER
   ```
7. To replace APH (aka APH\_AR) certificates use the following API call. To find your Unified Appliance node ID, refer to [Finding NSX Node IDs for Certificate API Calls](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/finding-node-ids-for-certificate-api-calls.html).

   ```
   POST https://<nsx-mgr>/api/v1/trust-management/certificates/<cert-id>?action=apply_certificate&service_type=APH&node_id=<node-id>
   ```

   For example:

   ```
   POST https://<nsx-mgr>/api/v1/trust-management/certificates/77c5dc5c-6ba5-4e74-a801-c27dc09be76b?action=apply_certificate&service_type=APH&node_id=93350f42-16b4-cb4e-99e0-fce2d17635a3
   ```
8. Starting with NSX 4.1, to replace the transport node (TN) or the Edge host certificates (called TN certificates) use the following API call. You must generate the private key outside of NSX Manager. If you generate the CSR in the NSX Manager, it is not possible to retrieve the private key, which is required in the API call. If it is a CA-signed certificate, include the whole chain in this order: certificate - intermediate - root. The entire certificate must be provided in a single line. Also replace any end of line character with \n. This is required in the pem\_encoded and private key values. To replace newline characters with \n you can use this command on UNIX based systems: awk '{gsub(/\\n/,"\n")}1' certificate.pem.

   ```
   POST https://<nsx-mgr>/api/v1/trust-management/certificates/action/replace-host-certificate/<transport-node-id>
   {
         "display_name": "cert_name",
         "pem_encoded": "---BEGIN CERTIFICATE---\n<certificate>\n---END CERTIFICATE-----\n",   
         "private_key": "---BEGIN RSA PRIVATE KEY---\n<private rsa key>\n---END RSA PRIVATE KEY---\n"
       }
   ```

   For example:

   ```
   POST https://<nsx-mgr>/api/v1/trust-management/certificates/aaction/replace-host-certificate/8e84d532-2cd8-46d8-90c7-04862980f69c
   {
       "display_name": "cert_sample",
       "pem_encoded": "-----BEGIN CERTIFICATE-----\nMIIC1DCCAbygAwIBAgIUMd1fGNGnvYKtilon2UMBP4rqRAowDQYJKoZIhvcNAQEL\nBQAwDzENMAsGA1UEAwwETVlDQTAeFw0yMzA5MjYxODMxMzVaFw0zMzA5MjMxODMx\nMzVaMBYxFDASBgNVBAMMC2NlcnRfc2FtcGxlMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAzMDsp1EGFPjus/xnHmacPJYVP0N8iQMb3W8TFFQC5jxdjNzi\ncMIb1YgpI+s3LJoyYCdZKeMcCWDwtgQXMTy9FYJCHKyt86CF0br9U9q9iC+NX93X\n+/wrWtXY89ESt0NOgj22sKI49EQT9bd0dNWupxapCb98Dyztk0cetIHa7ia1q7un\nXMZ7dofwuWUEUlT8qpyXF84N6bhWQSrXRyeQ+oZrsq3sAyfnKzbfcs0T3sztWn9M\nR7h8iPkjpJjVV5z1ghAgIDKFXG8RVU8fLgX5srtYV2Ij1II0qYwe/yGBfj7xsemB\n2lGGPotlbwUE5oPFISJvG9qLOoNKVLvBrxuNnQIDAQABoyEwHzAdBgNVHSUEFjAU\nBggrBgEFBQcDAQYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAAqPfZWNzG/b\nBhtN2gDjr0LplfC0yi8K6Ep3exECE5UOUJvHubko4Z6eCZFT8XSrAa6eZQEVe3O3\nwFvpdedCiEpI/IaFhpRUQDubJMPao7t4Uohz3k3ONMGbIci8dVUcQRQlmxFmx3wf\n0/33fy3b1zIOXqooQF3qUlpjms/RQOdD80dSlMze8WI7yz9LZt9Zc+sr8ePRi4Xy\ntudO6EYTiWm3CC5BxDDjKpkFCACFRT4zr5HsomHsFeo4hGIHl2zN0+JoGrdrWcta\nxdl5aQYy79vIMgvz696EKUGePEpJjpyP/wlwzmIY3RvXRKThuVXvg20gi365x8+J\niKbzpCGe0P0=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIC/zCCAeegAwIBAgIUUlHXcczsdMpei1ThgeQYpvgzaxMwDQYJKoZIhvcNAQEL\nBQAwDzENMAsGA1UEAwwETVlDQTAeFw0yMzA5MjYxODI2NDZaFw0zMzA5MjMxODI2\nNDZaMA8xDTALBgNVBAMMBE1ZQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQDbr78t32TUl1qTcDGvVQhiUkktntPO/5/FRDSIjy9qyNGDrcICDAYzOe79\nceXpOzfUStacEeTXse89q1MJz4ykaU2g6EUN2E4sfoP4KznBlObLHnnlxD482DL4\nbuMA8qCe0soUsGE6uoeFHnSW3M+NRI3GtJe1MM134JQ/TSNZTv+d93nB4bS2nSK7\nA1fFDRSuj8Ey7a1im8JgykL9ahJ6yxrpk8juEJwII04nHfAG102/8/YKEZyPWcPX\nYvLZEt/lBVxRPplWfbNIo3zfA09fzb4RMaOSsyBbqTBseL/4fxlnkeu1Rii3ZwcQ\nL4Wr6mKR1YCievsuXdLK5pWUH+BtAgMBAAGjUzBRMB0GA1UdDgQWBBTnYafa1EXn\nNPIqTkIO82kdamjDgTAfBgNVHSMEGDAWgBTnYafa1EXnNPIqTkIO82kdamjDgTAP\nBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQC2Ef+CPICTdWEKW3e6\nwaObe4Y85CS2wfSBRFvt0yCAUF8yysr3kQx85wdhfDfvidQdrgQIkDKe83J61r5l\n238wFo9O10RpFWl1csY4hZ19geeTW3L8tABp+f1or1vsAogfVtcaZwmqz/LEaZ0r\n4JdONE9gq40RgX5R9GPD04k3hKr6HoNHHnBssmNHgo8pLKRv04mx0yQyn45lKvet\ngcInI9j8YLsXGHdeiZ/zXKUgKQdicBw79K/mQCpgkpaEi3K9mFUFCUU9CiWxiy62\nSN2/SEuOWlb7Kq8VwJUfUn3lKoY9sofr9zsSsh5lhQOKb1uguo8xUF8v6iLuDAjr\n9bcn\n-----END CERTIFICATE-----\n",
       "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAzMDsp1EGFPjus/xnHmacPJYVP0N8iQMb3W8TFFQC5jxdjNzi\ncMIb1YgpI+s3LJoyYCdZKeMcCWDwtgQXMTy9FYJCHKyt86CF0br9U9q9iC+NX93X\n+/wrWtXY89ESt0NOgj22sKI49EQT9bd0dNWupxapCb98Dyztk0cetIHa7ia1q7un\nXMZ7dofwuWUEUlT8qpyXF84N6bhWQSrXRyeQ+oZrsq3sAyfnKzbfcs0T3sztWn9M\nR7h8iPkjpJjVV5z1ghAgIDKFXG8RVU8fLgX5srtYV2Ij1II0qYwe/yGBfj7xsemB\n2lGGPotlbwUE5oPFISJvG9qLOoNKVLvBrxuNnQIDAQABAoIBAQCE8JH2xIWVYlbh\np3RwaaDxOWTMMY4PC2SxLegOX8mOIQ2AYv3mxjD6QDCt8I9fNzKT+ZhLuPhAIp/H\nHfrM7im6aFtycK90qfmYxbarFi/O10kMQGZ2ZjDkBkqZa1qigGHd8CHIp1shRX5M\nIHPNU9vVAsJ34Mq0s7AA2sFV46X4zyEqHKLi1qVcsj68XJCrKJPTzOXiZWOHL8e0\nx4B8mGKbnWNmrq6styyYi9rzUnucoKL459YkaF/MEBpou3wvhprkR5Ufr4eNo0YV\nr0KfcEjxZqVT2o6r59+gSZQiCHael2MgslvMUTJOPgZ8tO78RQIHpH8GnNo+QkzB\nvXDfH2zhAoGBAPbeM7OveieHL37Iu/xY2wtDagSBD5K0VJhP8OOF5G1t1nHNcyWa\nYa49hTmGJ7bQsw5oGccvvsXCgGzaNbbAQtKlcz9kiXKOpTWV3t+RXtp0IXp8MIG6\nvWYd7yey7FHumHS/wC0h/REwx10153UpYaFJe2QJHw4yG9BJgN7o4duVAoGBANRT\n6BMPqV/6P9kJtduU8sZOVv3BbyUIkoBZlw2O7LB1IjIZcEm4By9DEAqCkFMp4gST\nW6o2eyXKp0oZ1UwqKdESG2LrGePNrmbQp7LvMngyk7CDqczA5gmnlndCy27k/d1Y\nQuWz+WDrqc8EAD7wRBmrwR0p3zCntPFRJPVu+yfpAoGACkDcYOAu8KlavadUt3xx\nTJx2MM2zeeJniRP461pKTIk9WOixmaQ53mTLvcHmsF8msLh+KZnAELKtZtgBVx/R\nJrKcgMuKMenezsT0xtBg4i3knhO+aAT7jNw9bKavzg9c4ax9LOK2ghpGjYaJoIIh\nffNxXoxKb+qA4TvMUHXXu6kCgYAhGeefORzVqqTTiDECx4jFo6bqLoLOSjTUr6Ld\n6T87DzfCiba4t2jfVFwm1036uRfUUMjEk3PFY3+LDNX05snYHzOHy1Eg84rR2oua\nWLIMjQ37QbtyAUybirXpZ89hPW/aVw0u1Ez3cCXr8Rq8tSZYvi8ABewWoL6TtGvH\nm4KqKQKBgCfZrv6wpCrS5Ep/AKQGdPOXCOM8O2+b4e/NJpSIH9Zk5Elg6WAunlCp\ntHyx1pZFq5RboxFw7DsM9eUTakHvGtTJ+EFHbyc5tKqWKnVbGmDYR6pNRULPEXU9\nhBQ1pzzmwGnO6AyxTxgoY5CosK2Ga1KjsWUXqay2QwIln+E+xxsm\n-----END RSA PRIVATE KEY-----\n"
   }
   ```

   Use the ID of the transport node for the node\_id, not the Unified Appliance (UA) ID. To find your node ID, refer to [Finding NSX Node IDs for Certificate API Calls](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/finding-node-ids-for-certificate-api-calls.html).

   For details on the default self-signed certificates configured by the system or for VMware Cloud Foundation certificate requirements, refer to [Types of Certificates in NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/types-of-certificates.html#GUID-c6e33279-700c-427e-8622-8ac8a88acee9-en).