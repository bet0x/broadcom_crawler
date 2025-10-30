---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/configure-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure vSAN File Service
---

# Configure vSAN File Service

You can configure the file service, which enable you to create file shares on your vSAN datastore.

Ensure the following before configuring the vSAN file service:

- Enable vSAN file service.
- Allocate static IP addresses as file server IPs from vSAN file service network, each IP is the single point access to vSAN file shares.
  - For best performance, the number of IP addresses must be equal to the number of hosts in the vSAN cluster.
  - All the static IP addresses must be from the same subnet.
  - Every static IP address has a corresponding FQDN, which must be part of the Forward lookup and Reverse lookup zones in the DNS server.
- If you are planning to create a Kerberos based SMB file share or a Kerberos based NFS file share, you need the following:
  - Microsoft Active Directory (AD) domain to provide authentication to create an SMB file share or an NFS file share with the Kerberos security.
  - (Optional) Active Directory Organizational Unit to create all file server computer accounts.
  - A domain user in the directory service with the sufficient privileges to create and delete computer accounts.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Services.
4. On the File Service row, click Configure Domain.

   The File Service Domain wizard opens.
5. In the File Service Domain page, enter the unique namespace and click Next. The domain name must have minimum two characters. The first character must be an alphabet or a number. The remaining characters can include an alphabet, a number, an underscore ( \_ ), a period ( . ), a hyphen ( - ).
6. In the Networking page, enter the following information, and click Next:

   - Protocol: You can select IPv4 or IPv6. vSAN file service only supports IPv4 or IPv6 stack. The reconfiguration between IPv4 and IPv6 is not supported.
   - DNS servers: Enter a valid DNS server to ensure the proper configuration of file service.
   - DNS suffixes: Provide the DNS suffix that is used with the file service. All other DNS suffixes from where the clients can access these file servers must also be included. File service does not support DNS domain with single label, such as "app", "wiz", "com" and so on. A domain name given to file service must be of the format thisdomain.registerdrootdnsname. DNS name and suffix must adhere to the best practices detailed in <https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain>.
   - Subnet mask: Enter a valid subnet mask. This text box appears when you select IPv4.
   - Prefix length: Enter a number between 1 and 128. This text box appears when you select IPv6.
   - Gateway: Enter a valid gateway.
   - IP Pool: Enter IP addresses and the corresponding DNS names.

   vSAN ESA cluster supports 500 file shares. Out of those 500 file shares, maximum 100 file shares can be SMB. For example, if you create 100 SMB file shares then the cluster can only support additional 400 NFS file shares.

   Each file server on a vSAN ESA cluster can support a maximum of 50 file shares and requires at least 10 IPs to have the maximum of 500 shares. With the increase in the file servers or file shares per host, there might be an impact on the performance of vSAN file service. For best performance, the number of IP address must to be equal to the number of hosts in the vSAN cluster.

   Affinity site option is available if you are configuring vSAN file service on a vSAN stretched cluster. This option allows you to configure the placement of the file server on Preferred or Secondary site. This helps in reducing the cross-site traffic latency. The default value is Either, which indicates that no site affinity rule is applied to the file server.

   If your cluster is a ROBO cluster, ensure that the Affinity site value is set to Either.

   In a site failure event, the file server affiliated to that site fails over to the other site. The file server fails back to the affiliated site when it is recovered. Configure more file servers to one site if more workloads can be expected from a certain site.

   If the file server contains SMB file shares, then it does not failback automatically even if the site failure is recovered.

   Consider the following while configuring the IP addresses and DNS names:
   - To ensure proper configuration of file service, the IP addresses you enter in the Networking page must be static addresses and the DNS server must have records for those IP addresses. For best performance, the number of IP addresses must be equal to the number of hosts in the vSAN cluster.
   - You can have a maximum of 64 hosts in the cluster. If large scale cluster support is configured, you can enter up to 64 IP addresses.
   - You can use the following options to automatically fill the IP address and DNS server name text boxes:

     AUTO FILL: This option is displayed after you enter the first IP address in the IP address text box. Click the AUTO FILL option to automatically fill the remaining fields with sequential IP addresses, based on the subnet mask and gateway address of the IP address that you have provided in the first row. You can edit the auto filled IP addresses.

     LOOK UP DNS: This option is displayed after you enter the first IP address in the IP address text box. Click the LOOK UP DNS option to automatically retrieve the FQDN corresponding to the IP addresses in the IP address column.

     - All valid rules apply for the FQDNs. For more information, see [https://tools.ietf.org/html/rfc953](https://datatracker.ietf.org/doc/html/rfc953).
     - The first part of the FQDN, also known as NetBIOS Name, must not have more than 15 characters.

     The FQDNs are automatically retrieved only under the following conditions:

     - You must have entered a valid DNS server in the Domain page.
     - The IP addresses entered in the IP Pool page must be static addresses and the DNS server must have records for those IP addresses.
7. In the Directory service page, enter the following information and click Next.

   | Option | Description |
   | --- | --- |
   | Directory service | Configure an Active Directory domain to vSAN file service for authentication. If you are planning to create an SMB file share or an NFSv4.1 file share with Kerberos authentication, then you must configure an AD domain to vSAN file service. |
   | AD domain | Fully qualified domain name joined by the file server. |
   | Preferred AD Server | Enter the IP address of the preferred AD server. In case of multiple IP addresses, ensure that they are separated by comma. |
   | Organizational unit (Optional) | Contains the computer account that the vSAN file service creates. In an organization with complex hierarchies, create the computer account in a specified container by using a forward slash mark to denote hierarchies (for example, organizational\_unit/inner\_organizational\_unit).  By default, the vSAN file service creates the computer account in the Computers container. |
   | AD username | User name to be used for connecting and configuring the Active Directory service.  This user name authenticates the active directory on the domain. A domain user authenticates the domain controller and creates vSAN file service computer accounts, related SPN entries, and DNS entries (when using Microsoft DNS). As a best practice, create a dedicated service account for the file service.  A domain user in the directory service with the following sufficient privileges to create and delete computer account: - (Optional) Add/Update DNS entries |
   | Password | Password for the user name of the Active Directory on the domain. vSAN file service use the password to authenticate to AD and to create the vSAN file service computer account. |

   - vSAN file service does not support the following:
     - Read-Only Domain Controllers (RODC) for joining domains because the RODC cannot create computer accounts. As a security best practice, a dedicated org unit must be pre-created in the Active Directory and the user name mentioned here must be controlling this organization.
     - Disjoint namespace.
     - Multiple domains and Single Active Directory Forest environments.
   - Only English characters are supported for Active Directory user name.
   - Only single AD domain configuration is supported. However, the file servers can be put on a valid DNS subdomain. For example, an AD domain with the name example.com can have file server FQDN as name1.eng.example.com.
   - Pre-created computer accounts for file servers are not supported. Make sure that the user provided here have sufficient privilege over the organizational unit.
   - vSAN file service also has a Health Check to indicate if the forward and reverse lookups for file servers are working properly.
8. Review the settings and click Finish.

The file service domain is configured. File servers are started with the IP addresses that were assigned during the vSAN file service configuration process.

Run vSAN health check and verify the health findings.