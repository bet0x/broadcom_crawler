---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/obtain-the-certificate-thumbprint-from-a-vidm-host.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Obtain the Certificate Thumbprint from an VMware Workspace ONE Access Host
---

# Obtain the Certificate Thumbprint from an VMware Workspace ONE Access Host

Before you configure the integration of VMware Workspace ONE Access with NSX, you must get the certificate thumbprint from the Workspace ONE Access host.

You must use OpenSSL version 1.x or higher for the thumbprint. On an Workspace ONE Access host of version 3.3.2 or earlier, the command openssl might be running an older version of OpenSSL. In that case, you must use the command openssl1. This command is only available on an Workspace ONE Access host.

You can check your version of OpenSSL with the following command:

```
openssl version
```

On a server that is not the Workspace ONE Access host, you can use the openssl command that is running OpenSSL version 1.x or later.

1. Log in at the Workspace ONE Access host's console, or SSH to the Workspace ONE Access host as the user sshuser, or log in to any server that can ping the Workspace ONE Access host.
2. Run one of the following commands to get the thumbprint of the Workspace ONE Access host.
   - If you are logged in to a server that can ping the Workspace ONE Access host, run the openssl command to get the thumbprint:

     ```
     openssl s_client -connect <FQDN of vIDM host>:443 < /dev/null 2> /dev/null | openssl x509 -sha256 -fingerprint -noout -in /dev/stdin
     ```
   - If you are logged in to the Workspace ONE Access host, do one of the following:

     - If the OpenSSL version is 0.9.x or earlier, run the following command:

       ```
       openssl s_client -connect <FQDN of vIDM host>:443 < /dev/null 2> /dev/null | openssl x509 -sha256 -fingerprint -noout -in /dev/stdin
       ```

       If you get an error running the command, you might need to run openssl1 with the sudo command, that is, sudo openssl1 ....
     - If the OpenSSL version is 1.x or later, run the following command:

       ```
       openssl s_client -connect <FQDN of vIDM host>:443 < /dev/null 2> /dev/null | openssl x509 -sha256 -fingerprint -noout -in /dev/stdin
       ```

       If you get an error running the command, you might need to run openssl with the sudo command, that is, sudo openssl ....