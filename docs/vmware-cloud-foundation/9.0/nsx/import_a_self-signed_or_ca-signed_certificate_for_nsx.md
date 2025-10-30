---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-certificate.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Import a Self-signed or CA-signed Certificate for NSX
---

# Import a Self-signed or CA-signed Certificate for NSX

You can import a certificate with a private key to replace the default self-signed certificate, after activation.

- Verify that a certificate is available.
- The server certificate must contain the Basic Constraints extension basicConstraints = cA:FALSE.
- Ensure that the certificate is signed with a supported algorithm.

You can import self-signed or CA-signed certificates for platform or services using this procedure with the following exceptions:

- A CSR generated on NSX Manager which is self-signed cannot be used as a service certificate, such as the Load Balancer service. If you want to import a CA certificate for the Load Balancer service, see [Import a CA Certificate for NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/importing-certificates/import-a-ca-certificate.html#GUID-4da8a492-310f-4459-8245-ea63125c6105-en).
- On a stand-by Global Manager, the UI import operation is deactivated. Use the following REST API command to complete the import of a platform certificate on the standby GM. The display name is optional, but if not used, ensure the last attribute does not contain a trailing comma. Be sure to replace any end of line character with \n. The entire certificate should be provided in a single line. In order to replace newline characters with \n, you can use this command on UNIX based systems to convert each .pem (certificate and key) file to a value that can be passed in a JSON string to the NSX API: awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' certificate-name.pem. The new format places all the certificate information on a single line with embedded newline characters.

  For example:

  ```
  POST https://<nsx-mgr>/api/v1/trust-management/certificates?action=import
  {
      "display_name": "cert_sample",
      "pem_encoded": "-----BEGIN CERTIFICATE-----\nMIIC1CCDAbygAwIBAgIUMd1fGNGnvYKtilon2UMBP4rqRAowDQYJKoZIhvcNAQEL\nBQAwDzENMAsGA1UEAwwETVlDQTAeFw0yMzA5MjYxODMxMzVaFw0zMzA5MjMxODMx\nMzVaMBYxFDASBgNVBAMMC2NlcnRfc2FtcGxlMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAzMDsp1EGFPjus/xnHmacPJYVP0N8iQMb3W8TFFQC5jxdjNzi\ncMIb1YgpI+s3LJoyYCdZKeMcCWDwtgQXMTy9FYJCHKyt86CF0br9U9q9iC+NX93X\n+/wrWtXY89ESt0NOgj22sKI49EQT9bd0dNWupxapCb98Dyztk0cetIHa7ia1q7un\nXMZ7dofwuWUEUlT8qpyXF84N6bhWQSrXRyeQ+oZrsq3sAyfnKzbfcs0T3sztWn9M\nR7h8iPkjpJjVV5z1ghAgIDKFXG8RVU8fLgX5srtYV2Ij1II0qYwe/yGBfj7xsemB\n2lGGPotlbwUE5oPFISJvG9qLOoNKVLvBrxuNnQIDAQABoyEwHzAdBgNVHSUEFjAU\nBggrBgEFBQcDAQYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAAqPfZWNzG/b\nBhtN2gDjr0LplfC0yi8K6Ep3exECE5UOUJvHubko4Z6eCZFT8XSrAa6eZQEVe3O3\nwFvpdedCiEpI/IaFhpRUQDubJMPao7t4Uohz3k3ONMGbIci8dVUcQRQlmxFmx3wf\n0/33fy3b1zIOXqooQF3qUlpjms/RQOdD80dSlMze8WI7yz9LZt9Zc+sr8ePRi4Xy\ntudO6EYTiWm3CC5BxDDjKpkFCACFRT4zr5HsomHsFeo4hGIHl2zN0+JoGrdrWcta\nxdl5aQYy79vIMgvz696EKUGePEpJjpyP/wlwzmIY3RvXRKThuVXvg20gi365x8+J\niKbzpCGe0P0=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIC/zCCAeegAwIBAgIUUlHXcczsdMpei1ThgeQYpvgzaxMwDQYJKoZIhvcNAQEL\nBQAwDzENMAsGA1UEAwwETVlDQTAeFw0yMzA5MjYxODI2NDZaFw0zMzA5MjMxODI2\nNDZaMA8xDTALBgNVBAMMBE1ZQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQDbr78t32TUl1qTcDGvVQhiUkktntPO/5/FRDSIjy9qyNGDrcICDAYzOe79\nceXpOzfUStacEeTXse89q1MJz4ykaU2g6EUN2E4sfoP4KznBlObLHnnlxD482DL4\nbuMA8qCe0soUsGE6uoeFHnSW3M+NRI3GtJe1MM134JQ/TSNZTv+d93nB4bS2nSK7\nA1fFDRSuj8Ey7a1im8JgykL9ahJ6yxrpk8juEJwII04nHfAG102/8/YKEZyPWcPX\nYvLZEt/lBVxRPplWfbNIo3zfA09fzb4RMaOSsyBbqTBseL/4fxlnkeu1Rii3ZwcQ\nL4Wr6mKR1YCievsuXdLK5pWUH+BtAgMBAAGjUzBRMB0GA1UdDgQWBBTnYafa1EXn\nNPIqTkIO82kdamjDgTAfBgNVHSMEGDAWgBTnYafa1EXnNPIqTkIO82kdamjDgTAP\nBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQC2Ef+CPICTdWEKW3e6\nwaObe4Y85CS2wfSBRFvt0yCAUF8yysr3kQx85wdhfDfvidQdrgQIkDKe83J61r5l\n238wFo9O10RpFWl1csY4hZ19geeTW3L8tABp+f1or1vsAogfVtcaZwmqz/LEaZ0r\n4JdONE9gq40RgX5R9GPD04k3hKr6HoNHHnBssmNHgo8pLKRv04mx0yQyn45lKvet\ngcInI9j8YLsXGHdeiZ/zXKUgKQdicBw79K/mQCpgkpaEi3K9mFUFCUU9CiWxiy62\nSN2/SEuOWlb7Kq8VwJUfUn3lKoY9sofr9zsSsh5lhQOKb1uguo8xUF8v6iLuDAjr\n9bcn\n-----END CERTIFICATE-----\n",
      "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAzNDsp1EGFPjus/xnHmacPJYVP0N8iQMb3W8TFFQC5jxdjNzi\ncMIb1YgpI+s3LJoyYCdZKeMcCWDwtgQXMTy9FYJCHKyt86CF0br9U9q9iC+NX93X\n+/wrWtXY89ESt0NOgj22sKI49EQT9bd0dNWupxapCb98Dyztk0cetIHa7ia1q7un\nXMZ7dofwuWUEUlT8qpyXF84N6bhWQSrXRyeQ+oZrsq3sAyfnKzbfcs0T3sztWn9M\nR7h8iPkjpJjVV5z1ghAgIDKFXG8RVU8fLgX5srtYV2Ij1II0qYwe/yGBfj7xsemB\n2lGGPotlbwUE5oPFISJvG9qLOoNKVLvBrxuNnQIDAQABAoIBAQCE8JH2xIWVYlbh\np3RwaaDxOWTMMY4PC2SxLegOX8mOIQ2AYv3mxjD6QDCt8I9fNzKT+ZhLuPhAIp/H\nHfrM7im6aFtycK90qfmYxbarFi/O10kMQGZ2ZjDkBkqZa1qigGHd8CHIp1shRX5M\nIHPNU9vVAsJ34Mq0s7AA2sFV46X4zyEqHKLi1qVcsj68XJCrKJPTzOXiZWOHL8e0\nx4B8mGKbnWNmrq6styyYi9rzUnucoKL459YkaF/MEBpou3wvhprkR5Ufr4eNo0YV\nr0KfcEjxZqVT2o6r59+gSZQiCHael2MgslvMUTJOPgZ8tO78RQIHpH8GnNo+QkzB\nvXDfH2zhAoGBAPbeM7OveieHL37Iu/xY2wtDagSBD5K0VJhP8OOF5G1t1nHNcyWa\nYa49hTmGJ7bQsw5oGccvvsXCgGzaNbbAQtKlcz9kiXKOpTWV3t+RXtp0IXp8MIG6\nvWYd7yey7FHumHS/wC0h/REwx10153UpYaFJe2QJHw4yG9BJgN7o4duVAoGBANRT\n6BMPqV/6P9kJtduU8sZOVv3BbyUIkoBZlw2O7LB1IjIZcEm4By9DEAqCkFMp4gST\nW6o2eyXKp0oZ1UwqKdESG2LrGePNrmbQp7LvMngyk7CDqczA5gmnlndCy27k/d1Y\nQuWz+WDrqc8EAD7wRBmrwR0p3zCntPFRJPVu+yfpAoGACkDcYOAu8KlavadUt3xx\nTJx2MM2zeeJniRP461pKTIk9WOixmaQ53mTLvcHmsF8msLh+KZnAELKtZtgBVx/R\nJrKcgMuKMenezsT0xtBg4i3knhO+aAT7jNw9bKavzg9c4ax9LOK2ghpGjYaJoIIh\nffNxXoxKb+qA4TvMUHXXu6kCgYAhGeefORzVqqTTiDECx4jFo6bqLoLOSjTUr6Ld\n6T87DzfCiba4t2jfVFwm1036uRfUUMjEk3PFY3+LDNX05snYHzOHy1Eg84rR2oua\nWLIMjQ37QbtyAUybirXpZ89hPW/aVw0u1Ez3cCXr8Rq8tSZYvi8ABewWoL6TtGvH\nm4KqKQKBgCfZrv6wpCrS5Ep/AKQGdPOXCOM8O2+b4e/NJpSIH9Zk5Elg6WAunlCp\ntHyx1pZFq5RboxFw7DsM9eUTakHvGtTJ+EFHbyc5tKqWKnVbGmDYR6pNRULPEXU9\nhBQ1pzzmwGnO6AyxTxgoY5CosK2Ga1KjsWUXqay2QwIln+E+xxsm\n-----END RSA PRIVATE KEY-----\n"
  }
  ```

  In some cases, issues have been reported with certificates that contain \r\n in the PEM format. According to the X509 certificate standard, it is acceptable and NSX Manager allows these certificates to be used and in many cases there are no error results.

1. From your browser, log in with
   admin privileges to an NSX Manager
   at https://<nsx-manager-ip-address>.
2. With admin privileges, log in
   to NSX Manager.
3. Select SystemCertificates.
4. Select ImportImport Certificate and enter the certificate details. 

   Option | Description || Name | Assign a name to the certificate. |
   | Service Certificate | Set to Yes to use this certificate for services such as a load balancer and VPN. Set to No if this certificate is for the NSX Manager nodes. |
   | Certificate Contents | Browse to the certificate file on your computer and add the file. The certificate must not be encrypted. If it is a CA-signed certificate, be sure to include the whole chain in this order: certificate - intermediate - root. Everything must be provided in a single line. |
   | Private Key | Browse to the private key file on your computer and add the file. Private key is an optional field if imported certificate is based on NSX Manager generated CSR, as a private key exists on the NSX Manager appliance. |
   | Passphrase | In this release, this field is not used. |
   | Description | Enter a description of what is included in this certificate. |
5. Click Import.