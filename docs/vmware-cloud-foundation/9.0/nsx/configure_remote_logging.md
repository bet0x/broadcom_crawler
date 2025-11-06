---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes/configure-remote-logging.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure Remote Logging
---

# Configure Remote Logging

You can configure NSX appliances, NSX Edges, and hypervisors to send log messages to a remote log server.

- Familiarize yourself with the CLI command set logging-server. For more information, see the NSX Command-Line Interface Reference.
- If you specify the secure protocol TLS or LI-TLS, the server and client certificates must be stored in /image/vmware/nsx/file-store on each NSX appliance. Note that certificates in the file store are needed only if the exporter is configured using NSX CLI. If you use the API, then there is no need to use the file store. Once you complete the syslog exporter configuration, you must delete all certificates and keys from this location to avoid potential security vulnerabilities.

  Note that a TLS logging server does not support replacing of certificates. When a TLS logging server certificate is about to expire or gets expired, you must perform the follwoing steps:

  - Delete the existing TLS logging server by using an API or CLI.
  - Put the new certificate under /image/vmware/nsx/file-store and create a new TLS logging server with new certificate again.
- To configure a secure connection to a log server, verify that the server is configured with a CA-signed certificates. For example, if you have a VCF Operations for logs server vrli.prome.local as the log server, you can run the following command from a client to see the certificate chain on the server:

  ```
  echo -n | openssl s_client -connect vrli.prome.local:443  | sed -ne '/^Certificate chain/,/^---/p'
  ```

  For example:

  ```
  root@caserver:~# echo -n | openssl s_client -connect vrli.prome.local:443  | sed -ne '/^Certificate chain/,/^---/p'
  depth=2 C = US, L = California, O = GS, CN = Orange Root Certification Authority
  verify error:num=19:self signed certificate in certificate chain
  Certificate chain
  0 s:/C=US/ST=California/L=HTG/O=GSS/CN=vrli.prome.local
    i:/C=US/L=California/O=GS/CN=Green Intermediate Certification Authority
  1 s:/C=US/L=California/O=GS/CN=Green Intermediate Certification Authority
    i:/C=US/L=California/O=GS/CN=Orange Root Certification Authority
  2 s:/C=US/L=California/O=GS/CN=Orange Root Certification Authority
    i:/C=US/L=California/O=GS/CN=Orange Root Certification Authority
  ---
  DONE
  ```

Remote logging is supported on NSX Manager, NSX Edge, and hypervisors. You must configure remote logging on each node individually.

If host clusters are activated for Distributed Malware Prevention for vDefend service, you can log in to the Malware Prevention for vDefend service virtual machine (SVM) on each host and configure remote logging on the SVM. This functionality is supported starting in NSX 4.1.2. For more information, see Configure Remote Logging on an NSX Malware Prevention Service Virtual Machine.

For the protocol parameter, the options are UDP, TCP, LI, and the secure protocols TLS and LI-TLS. Note that LI and LI-TLS are VCF Operations for logs protocols. An VCF Operations for logs log server supports all the protocols. The protocols LI and LI-TLS can only be used if the log server is VCF Operations for logs. The benefit of using LI or LI-TLS is that they optimize network usage. If the log server is VCF Operations for logs, using LI or LI-TLS is recommended. If LI cannot be used, TCP has the advantage of being more reliable, whereas UDP has the advantage of requiring less system and network overhead.

1. To configure remote logging on an NSX appliance or an NSX Edge:
   1. Run the following command to configure a log server and the types of messages to send to the log server. Multiple facilities or message IDs can be specified as a comma delimited list, without spaces. 

      ```
      set logging-server <hostname-or-ip-address[:port]> proto <proto> level <level> [facility <facility>] [messageid <messageid>] [serverca <filename>] [clientca <filename>] [certificate <filename>] [key <filename>] [structured-data <structured-data>]
      ```

      You can run the command multiple times to add multiple configurations. For example:

      ```
      set logging-server 192.168.110.60 proto udp level info facility local6 messageid SYSTEM,FABRIC
      ```

      ```
      set logging-server 192.168.110.60 proto udp level info facility auth,user
      ```

      To forward multi-tenancy logs to the remote logging server, specify the project and the VPC in the structured-data parameter. For example,

      ```
      set logging-server <server-ip>  proto udp level err structured-data proj=<project-shortId>
      set logging-server <server -ip  proto udp level err structured-data vpc=<vpc-shortId>
      ```

      To forward only audit logs to the remote server, specify audit="true" in the structured-data parameter. For example:

      ```
      set logging-server <server-ip> proto udp level info structured-data audit="true"
      ```

      All NSX logs use facility local6. You should use the messageid and structured-data filters only when the facility filter is not set or when local6 is included in the specified facilities.
   2. Configure secure remote logging:

      - To configure secure remote logging using the protocol LI-TLS, specify the parameter proto li-tls. For example:

        ```
        set logging-server vrli.prome.local proto li-tls level info messageid SWITCHING,ROUTING,FABRIC,SYSTEM,POLICY,HEALTHCHECK,SHA,MONITORING serverca intermed-ca-full-chain.crt
        ```

        If the configuration is successful, you will get a prompt without any text. To see the content of the server certificate chain (intermediate followed by root), log in as root and run the following command:

        ```
        keytool -printcert -file /image/vmware/nsx/file-store/intermed-ca-full-chain.crt
        ```

        For example,

        ```
        root@nsx1:~# keytool -printcert -file /image/vmware/nsx/file-store/intermed-ca-full-chain.crt
        Certificate[1]:
        Owner: CN=Green Intermediate Certification Authority, O=GS, L=California, C=US
        Issuer: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Serial number: 3e726e7fbb3b0a7a6b4edd767f867fd2
        Valid from: Sun Mar 15 00:00:00 UTC 2020 until: Mon Mar 17 00:00:00 UTC 2025
        Certificate fingerprints:
         MD5:  94:C8:9F:92:56:60:EB:DB:ED:4B:11:17:33:27:C0:C9
         SHA1: 42:9C:3C:51:E8:8E:AC:2E:5E:62:95:82:D7:22:E0:FB:08:B8:64:29
         SHA256: 58:B8:63:3D:0C:34:35:39:FC:3D:1E:BA:AA:E3:CE:A9:C0:F3:58:53:1F:AD:89:A5:01:0D:D3:89:9E:7B:C5:69
        Signature algorithm name: SHA256WITHRSA
        Subject Public Key Algorithm: 4096-bit RSA key
        Version: 3
        Certificate[2]:
        Owner: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Issuer: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Serial number: 3e726e7fbb3b0a7a6b4edd767f867fd1
        Valid from: Mon Mar 16 07:16:07 UTC 2020 until: Fri Mar 10 07:16:07 UTC 2045
        Certificate fingerprints:
         MD5:  ED:AC:F1:7F:88:05:83:2A:83:C0:09:03:D5:00:CA:7B
         SHA1: DC:B5:3F:37:DF:BD:E0:5C:A4:B7:F4:4C:96:12:75:7A:16:C7:61:37
         SHA256: F2:5B:DE:8A:F2:31:9D:E6:EF:35:F1:30:6F:DA:05:FF:92:B4:15:96:AA:82:67:E3:3C:C1:69:A3:E5:27:B9:A5
        Signature algorithm name: SHA256WITHRSA
        Subject Public Key Algorithm: 4096-bit RSA key
        Version: 3
        ```

        The logs for both successful and failure conditions are in /var/log/loginsight-agent/liagent\_2020-MM-DD-<file-num>.log. If the configuration is successful, you can view the VCF Operations for logs configuration with the following command:

        ```
        cat /var/lib/loginsight-agent/liagent-effective.ini
        ```

        For example,

        ```
        root@nsx1:/image/vmware/nsx/file-store# cat /var/lib/loginsight-agent/liagent-effective.ini
        ; Dynamic file representing the effective configuration of VMware Log Insight Agent (merged server-side and client-side configuration)
        ;     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
        ; Creation time: 2020-03-22T19:41:21.648800

        [server]
        hostname=vrli.prome.local
        proto=cfapi
        ssl=yes
        ssl_ca_path=/config/vmware/nsx-node-api/syslog/bb466082-996f-4d77-b6e3-1fa93f4a20d4_ca.pem
        ssl_accept_any_trusted=yes
        port=9543
        filter={filelog; nsx-syslog; pri_severity <= 6 and ( msgid == "SWITCHING" or msgid == "ROUTING" or msgid == "FABRIC" or msgid == "SYSTEM" or msgid == "POLICY" or msgid == "HEALTHCHECK" or msgid == "SHA" or msgid == "MONITORING" )}

        [filelog|nsx-syslog]
        directory=/var/log
        include=syslog;syslog.*
        parser=nsx-syslog_parser

        [parser|nsx-syslog_parser]
        base_parser=syslog
        extract_sd=yes

        [update]
        auto_update=no
        ```
      - To configure secure remote logging using the protocol TLS, specify the parameter proto tls. For example:

        ```
        set logging-server vrli.prome.local proto tls level info serverca Orange-CA.crt.pem clientca Orange-CA.crt.pem certificate gc-nsxt-mgr-full.crt.pem key gc-nsxt-mgr.key.pem
        ```

        Note the following:
        - For the serverCA parameter, only the root certificate is required, not the full chain.
        - If clientCA is different from serverCA, only the root certificate is required.
        - The certificate should hold the full chain of the NSX Manager (they should be NDcPP compliant - EKU, BASIC and CDP (CDP - this check can be ignored)).

        You can inspect the content of each certificate with the keytool command. For example,

        ```
        keytool -printcert -file /image/vmware/nsx/file-store/Orange-CA.crt.pem
        ```

        ```
        keytool -printcert -file gc-nsxt-mgr-full.crt.pem
        ```

        Example output:

        ```
        root@gc3:~# keytool -printcert -file /image/vmware/nsx/file-store/Orange-CA.crt.pem
        Owner: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Issuer: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Serial number: 3e726e7fbb3b0a7a6b4edd767f867fd1
        Valid from: Mon Mar 16 07:16:07 UTC 2020 until: Fri Mar 10 07:16:07 UTC 2045
        Certificate fingerprints:
         MD5:  ED:AC:F1:7F:88:05:83:2A:83:C0:09:03:D5:00:CA:7B
         SHA1: DC:B5:3F:37:DF:BD:E0:5C:A4:B7:F4:4C:96:12:75:7A:16:C7:61:37
         SHA256: F2:5B:DE:8A:F2:31:9D:E6:EF:35:F1:30:6F:DA:05:FF:92:B4:15:96:AA:82:67:E3:3C:C1:69:A3:E5:27:B9:A5
        Signature algorithm name: SHA256WITHRSA
        Subject Public Key Algorithm: 4096-bit RSA key
        Version: 3
        root@gc3:~#

        root@gc3:/image/vmware/nsx/file-store# keytool -printcert -file gc-nsxt-mgr-full.crt.pem
        Certificate[1]:
        Owner: CN=gc.prome.local, O=GS, L=HTG, ST=California, C=US
        Issuer: CN=Green Intermediate Certification Authority, O=GS, L=California, C=US
        Serial number: bdf43ab31340b87f323b438a2895a075
        Valid from: Mon Mar 16 07:26:51 UTC 2020 until: Wed Mar 16 07:26:51 UTC 2022
        Certificate fingerprints:
               MD5:  36:3C:1F:57:96:07:84:C0:6D:B7:33:9A:8D:25:4D:27
               SHA1: D1:4E:F9:45:2D:0D:34:79:D2:B4:FA:65:28:E0:5C:DC:74:50:CA:3B
               SHA256: 3C:FF:A9:5D:AA:68:44:44:DD:07:2F:DD:E2:BE:9C:32:19:7A:03:D5:26:8D:5F:AD:56:CA:D2:6C:91:96:27:6F
        Signature algorithm name: SHA256WITHRSA
        Subject Public Key Algorithm: 4096-bit RSA key
        Version: 3
        Certificate[2]:
        Owner: CN=Green Intermediate Certification Authority, O=GS, L=California, C=US
        Issuer: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Serial number: 3e726e7fbb3b0a7a6b4edd767f867fd2
        Valid from: Sun Mar 15 00:00:00 UTC 2020 until: Mon Mar 17 00:00:00 UTC 2025
        Certificate fingerprints:
               MD5:  94:C8:9F:92:56:60:EB:DB:ED:4B:11:17:33:27:C0:C9
               SHA1: 42:9C:3C:51:E8:8E:AC:2E:5E:62:95:82:D7:22:E0:FB:08:B8:64:29
               SHA256: 58:B8:63:3D:0C:34:35:39:FC:3D:1E:BA:AA:E3:CE:A9:C0:F3:58:53:1F:AD:89:A5:01:0D:D3:89:9E:7B:C5:69
        Signature algorithm name: SHA256WITHRSA
        Subject Public Key Algorithm: 4096-bit RSA key
        Version: 3
        Certificate[3]:
        Owner: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Issuer: CN=Orange Root Certification Authority, O=GS, L=California, C=US
        Serial number: 3e726e7fbb3b0a7a6b4edd767f867fd1
        Valid from: Mon Mar 16 07:16:07 UTC 2020 until: Fri Mar 10 07:16:07 UTC 2045
        Certificate fingerprints:
               MD5:  ED:AC:F1:7F:88:05:83:2A:83:C0:09:03:D5:00:CA:7B
               SHA1: DC:B5:3F:37:DF:BD:E0:5C:A4:B7:F4:4C:96:12:75:7A:16:C7:61:37
               SHA256: F2:5B:DE:8A:F2:31:9D:E6:EF:35:F1:30:6F:DA:05:FF:92:B4:15:96:AA:82:67:E3:3C:C1:69:A3:E5:27:B9:A5
        Signature algorithm name: SHA256WITHRSA
        Subject Public Key Algorithm: 4096-bit RSA key
        Version: 3
        ```

        Examples of successful logging in /var/log/syslog:

        ```
        <182>1 2020-03-22T21:54:34.501Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully created CA PEM file /config/vmwarensx-node-api/syslog/92a78d8a-acfd-4515-b05a-2927b70ae920_ca.pem for logging server vrli.prome.local:6514
        <182>1 2020-03-22T21:54:36.269Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully created client CA PEM file /config/vmwarensx-node-api/syslog/92a78d8a-acfd-4515-b05a-2927b70ae920_client_ca.pem for logging server vrli.prome.local:6514
        <182>1 2020-03-22T21:54:36.495Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="INFO"] cert issuer = /C=US/L=California/O=GS/CN=Green IntermediateCertification Authority
        <182>1 2020-03-22T21:54:36.514Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="INFO"] cert subject = /C=US/ST=California/L=HTG/O=GS/CN=gc.promelocal
        <182>1 2020-03-22T21:54:36.539Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="INFO"] certificate trust check succeeded. status: 200, result:{'status': 'OK'}
        <182>1 2020-03-22T21:54:36.612Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="INFO"] Certificate already exists, skip import
        <182>1 2020-03-22T21:54:37.322Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully created certificate PEM file /config/vmwarensx-node-api/syslog/92a78d8a-acfd-4515-b05a-2927b70ae920_cert.pem for logging server vrli.prome.local:6514
        <182>1 2020-03-22T21:54:38.020Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully created key PEM file /config/vmwarensx-node-api/syslog/92a78d8a-acfd-4515-b05a-2927b70ae920_key.pem for logging server vrli.prome.local:6514
        ```

        Examples of logging failure in /var/log/syslog:

        ```
        <182>1 2020-03-22T21:33:30.424Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully created client CA PEM file /config/vmwarensx-node-api/syslog/76332782-1ec6-483a-95d4-2adeaf2ef112_client_ca.pem for logging server vrli.prome.local:6514
        <182>1 2020-03-22T21:33:30.779Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="INFO"] cert issuer = /C=US/L=California/O=GS/CN=Green IntermediateCertification Authority
        <182>1 2020-03-22T21:33:30.803Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="INFO"] cert subject = /C=US/ST=California/L=HTG/O=GS/CN=gc.promelocal
        <179>1 2020-03-22T21:33:30.823Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="root" level="ERROR" errorCode="NODE10"] Certificate trust check failed. status:200, result: {'error_message': 'Certificate CN=gc.prome.local,O=GS,L=HTG,ST=California,C=US was not verifiably signed by CN=gc.prome.local,O=GS,L=HTG,ST=California,C=US: certificate does not verifywith supplied key', 'status': 'ERROR'}
        <179>1 2020-03-22T21:33:30.824Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="ERROR" errorCode="NODE10"] Failed to create certificate PEM file config/vmware/nsx-node-api/syslog/76332782-1ec6-483a-95d4-2adeaf2ef112_cert.pem for logging server vrli.prome.local:6514
        <182>1 2020-03-22T21:33:31.578Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully deleted CA PEM file /config/vmwarensx-node-api/syslog/76332782-1ec6-483a-95d4-2adeaf2ef112_ca.pem
        <182>1 2020-03-22T21:33:32.342Z gc3.prome.local NSX 5187 - [nsx@6876 comp="nsx-manager" subcomp="node-mgmt" username="admin" level="INFO"] Successfully deleted client CA PEM file /config/vmwarensx-node-api/syslog/76332782-1ec6-483a-95d4-2adeaf2ef112_ca.pem
        <182>1 2020-03-22T21:33:32.346Z gc3.prome.local NSX 16698 - [nsx@6876 comp="nsx-cli" subcomp="node-mgmt" username="admin" level="INFO" audit="true"] CMD: set logging-server vrli.prome.local prototls level info serverca Orange-CA.crt.pem clientca Orange-CA.crt.pem certifi
        cate gc-nsxt-mgr.crt.pem key gc-nsxt-mgr.key.pem (duration: 6.365s), Operation status: CMD_EXECUTED
        ```

        You can check if the certificate and private key match with the following command. For example:

        ```
        diff  <(openssl x509 -in certs/gc-nsxt-mgr.crt.pem -pubkey -noout) <(openssl rsa -in private/gc-nsxt-mgr.key.pem -pubout)
        ```

        If the certificate and private key match, the output will be writing RSA key. Any other output means they do not match. For example, if the certificate and private key match, you will see:

        ```
        root@caserver:~/server-certs# diff  <(openssl x509 -in certs/gc-nsxt-mgr.crt.pem -pubkey -noout) <(openssl rsa -in private/gc-nsxt-mgr.key.pem -pubout)
        writing RSA key
        ```

        Example of a corrupt private key:

        ```
        root@caserver:~/server-certs# diff  <(openssl x509 -in certs/gc-nsxt-mgr.crt.pem -pubkey -noout) <(openssl rsa -in private/gc-nsxt-mgr-corrupt.key.pem -pubout)
        unable to load Private Key
        140404188370584:error:0D07209B:asn1 encoding routines:ASN1_get_object:too long:asn1_lib.c:147:
        140404188370584:error:0D068066:asn1 encoding routines:ASN1_CHECK_TLEN:bad object header:tasn_dec.c:1205:
        140404188370584:error:0D07803A:asn1 encoding routines:ASN1_ITEM_EX_D2I:nested asn1 error:tasn_dec.c:386:Type=RSA
        140404188370584:error:04093004:rsa routines:OLD_RSA_PRIV_DECODE:RSA lib:rsa_ameth.c:119:
        140404188370584:error:0D07209B:asn1 encoding routines:ASN1_get_object:too long:asn1_lib.c:147:
        140404188370584:error:0D068066:asn1 encoding routines:ASN1_CHECK_TLEN:bad object header:tasn_dec.c:1205:
        140404188370584:error:0D07803A:asn1 encoding routines:ASN1_ITEM_EX_D2I:nested asn1 error:tasn_dec.c:386:Type=PKCS8_PRIV_KEY_INFO
        140404188370584:error:0907B00D:PEM routines:PEM_READ_BIO_PRIVATEKEY:ASN1 lib:pem_pkey.c:141:
        1,14d0
        < -----BEGIN PUBLIC KEY-----
        < MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAv3yH7pZidfkLrEP3zVa9
        < EcOKXlFFjkThZRZMfguenlm8s6QHYVvuUX8IRB48Li3/DUfOj0bzaPWktpv+Q2P0
        < N/j4LoX2RzjV/DPxYfLP6GMNMc21L3s9ruBeWUthtUP8khCWd2d2rZ09cUZVl0P9
        < kIYBb5RMFC7Z1OUtH3bKdepEf+sXz3DaKZ/WySzYq9x86QDaA3ABO3Q0i7txBscI
        < FvXuMDOMQaC3pPp9FWO6IPRAWB57wahLJv6K5qGIfwubSBFg53grT4snf1lDZAhZ
        < 9hz5JgGr80GVyWyb7rgigpl9iUWAZx8U9De9XoxmvBN5iEGTIuKGaEgICL176crb
        < RMkhjnCqNHI+z6sQvpYJ7U0zZc72eBIWoHUkcWWk3eU6Oy4OiyW6jYuXG7hZYlly
        < nSkme3mZUWJKvcoX05+3zeCP623/HzE7X2sNyWFjzeF3XEvauZrIbsJh/xp2ShDa
        < uKKEY0gUGhLtCa3TpV9l8d6tFWVy8XjVjdjoVt4s7MfUo/airVmRykfsWrKyNUOQ
        < qRZvSbqjt8pm+3bSvKdXX4ul7ptPG2GF20ETWHPwjk2JwQpGhR9zK8fsKzvm6hXi
        < kq76zI4FefuVps3e1r39+0F+p6d6i2oUoo24sC1iSePTDhU74efVp6iv8HmnDgYX
        < Ylm6Kusr0JT5TJFDfASmrj8CAwEAAQ==
        < -----END PUBLIC KEY-----
        ```

        Example of a valid private key and certificate but they are not made for each other:

        ```
         root@caserver:~/server-certs# diff  <(openssl x509 -in certs/gc-nsxt-mgr.crt.pem -pubkey -noout) <(openssl rsa -in private/vrli.key.pem -pubout)
         writing RSA key
         2,13c2,13
         < MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAv3yH7pZidfkLrEP3zVa9
         < EcOKXlFFjkThZRZMfguenlm8s6QHYVvuUX8IRB48Li3/DUfOj0bzaPWktpv+Q2P0
         < N/j4LoX2RzjV/DPxYfLP6GMNMc21L3s9ruBeWUthtUP8khCWd2d2rZ09cUZVl0P9
         < kIYBb5RMFC7Z1OUtH3bKdepEf+sXz3DaKZ/WySzYq9x86QDaA3ABO3Q0i7txBscI
         < FvXuMDOMQaC3pPp9FWO6IPRAWB57wahLJv6K5qGIfwubSBFg53grT4snf1lDZAhZ
         < 9hz5JgGr80GVyWyb7rgigpl9iUWAZx8U9De9XoxmvBN5iEGTIuKGaEgICL176crb
         < RMkhjnCqNHI+z6sQvpYJ7U0zZc72eBIWoHUkcWWk3eU6Oy4OiyW6jYuXG7hZYlly
         < nSkme3mZUWJKvcoX05+3zeCP623/HzE7X2sNyWFjzeF3XEvauZrIbsJh/xp2ShDa
         < uKKEY0gUGhLtCa3TpV9l8d6tFWVy8XjVjdjoVt4s7MfUo/airVmRykfsWrKyNUOQ
         < qRZvSbqjt8pm+3bSvKdXX4ul7ptPG2GF20ETWHPwjk2JwQpGhR9zK8fsKzvm6hXi
         < kq76zI4FefuVps3e1r39+0F+p6d6i2oUoo24sC1iSePTDhU74efVp6iv8HmnDgYX
         < Ylm6Kusr0JT5TJFDfASmrj8CAwEAAQ==
         ---
         > MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqvsjay7+o7gCW7szT3ho
         > bC34XX2l6u5Jl4/X/pUDI/YHmIf06bsZ1r/l4bTL4Q7BM6+9MI6UYEE7DxUoINGO
         > o4FEEQE32KWVFe3gw3homHU39q4pQjsJsxTcTE3oDMlIY0nWJ0PRUst3DffyUH1L
         > W0NUN9YdN+fAl2Uf021iuDqVy9V8AH3ON6fu+QCA8nt71ZkzeTxSA0ldpl2NA17F
         > rD8rm05wxnV7WtuV7V8PstISiClzhHgZRMl+B0r30OitnyAzEGLaRT3//PKfe0Oe
         > HCdxGMlrUtMqxIItJahEsqvMufyqNYecVscyXLHPelizKCsQfy8cO8LnznG8VAdc
         > YILSn3uYGZap6aF1SgVxsvZicwvlYnssmgE13Af0nScmfM96k9h5joHVEkWK6O8v
         > oT5DGG1kVL2Qly97x0b6EnzUorzivv5zJMKvFcOektR8HdMHQit5uvmMRY3S5zow
         > FtvfSDfWxxKyTy6GBrpP+8F+Jq91yGy/qa9lhKBzT2lg+rJp7T8k7/Nm9Tjyx7jL
         > EqgEKZEL4chxpo8ucF98hbvXWRuaFHC2iDzGuUmuS1FfjVvHTuIbEMQfjapLZrHx
         > 8jHfOP/PL+6kPbvNZZ2rTpczuEoGTQFFW9vX48GzIEyMeR6QWpPR0F7r4xak68P5
         > 2PJmMveinDhU35IqWEXHAwcCAwEAAQ==
        ```
   3. To view the logging configuration, run the following command:

      ```
      get logging-server
      ```

      For example,

      ```
      nsx> get logging-servers
      192.168.110.60 proto udp level info facility local6 messageid SYSTEM,FABRIC
      192.168.110.60 proto udp level info facility auth,user
      ```
   4. To clear the remote logging configuration, run the following command: 

      ```
      clear logging-servers
      ```
2. To configure remote logging on an ESX host: 
   1. Run the following commands to configure syslog and send a test message: 

      ```
      esxcli network firewall ruleset set -r syslog -e true
      ```

      ```
      esxcli system syslog config set --loghost=udp://<log server IP>:<port> --log-level=info
      ```

      ```
      esxcli system syslog reload
      ```

      ```
      esxcli system syslog mark -s "This is a test message"
      ```
   2. You can run the following command to display the configuration: 

      ```
      esxcli system syslog config get
      ```