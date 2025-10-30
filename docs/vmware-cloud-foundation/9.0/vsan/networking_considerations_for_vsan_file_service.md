---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/networking-considerations-for-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Networking Considerations for vSAN File Service
---

# Networking Considerations for vSAN File Service

vSAN File Service is a layer that sits on top of vSAN to provide file shares. It currently supports SMB, NFSv3, and NFSv4.1 file shares.

Following are the network considerations for vSAN File Service:

- You must allocate static IP addresses as file server IPs from vSAN File Service network, each IP is the access point to vSAN file shares.
  - For best performance, the number of IP addresses must be equal to the number of hosts in the vSAN cluster.
  - All the static IP addresses should be from the same subnet.
  - Every static IP address has a corresponding FQDN, which should be part of the Forward lookup and Reverse lookup zones in the DNS server.
- You must ensure to prepare the network as vSAN File Service network:
  - If using standard switch based network, the Promiscuous Mode and Forged Transmits are enabled as part of the vSAN File Services enablement process.
  - If using DVS based network, vSAN File Services are supported on DVS. Create a dedicated port group for vSAN File Services in the DVS. MacLearning and Forged Transmits are enabled as part of the vSAN File Services enablement process for a provided DVS port group.

    If using NSX-based network, ensure that MacLearning is enabled for the provided network entity from the NSX admin console, and all the hosts and File Services nodes are connected to the desired NSX-T network.
- For SMB share and NFS share with Kerberos security, you must provide information about your AD domain and organizational unit (optional). In addition, a user account with sufficient privileges to create and delete objects is required.
- Ensure that the file server can access AD server and DNS server. The file server must be able to access all the ports required by AD service.

  Following are the ports that vSAN File Service uses for network connectivity. Ensure that these ports are not blocked by the firewall.

  | Service | Port Number | Entity | Connectivity Requirements |
  | --- | --- | --- | --- |
  | Server Message Block (SMB) | TCP port 445 | File Servers | External network to file servers |
  | Quotas for a user of a local filesystem (RQUOTA) | TCP port 875 | File Servers | External network to file servers |
  | Network File System (NFS) | TCP and UDP port 2049 | File Servers | External network to file servers. NFSv3 can use both TCP and UDP ports but NFSv4.1 uses only TCP. |
  | NFS Mount | TCP and UDP port 20048 | File Servers | External network to file servers |
  | Network Status Monitor (NSM) server daemon | TCP and UDP port 27689 | File Servers | External network to file servers. Both inward and outward communication must be permitted. |
  | Network Lock Manager (NLM) | TCP and UDP port 32803 | File Servers | External network to file servers. Allows the connection initiated from File Server to client. Inbound and outbound connections must be allowed on firewall. The default port is UDP. |
  | Sun remote procedure call (sunrpc) | TCP and UDP port 111 | File Servers | External network to file servers |
  | LDAP | TCP port 389 | Active Directory (AD) servers (if AD domain is configured) | File servers to AD servers |
  | LDAP to Global Catalog | TCP port 3268 | AD servers (if AD domain is configured) | File servers to AD servers |
  | Kerberos | TCP port 88 | AD servers (if AD domain is configured) | File servers to AD servers |
  | Kerberos password change | TCP port 464 | AD servers (if AD domain is configured) | File servers to AD servers |
  | Domain Name Server (DNS) | TCP and UDP port 53 | DNS servers | File servers to DNS servers |
  | vSAN Distributed File System (VDFS) Server | TCP port 1564 | ESX hosts | Inside vSAN network |
  | Remote Procedure Call | TCP port 135 | AD servers (if AD domain is configured) | File servers to AD servers |
  | NetBIOS Session Service | TCP port 139 | AD servers (if AD domain is configured) | File servers to AD servers |
  | DNS | UDP port 53 | AD servers (if AD domain is configured) | File servers to AD servers |
  | LDAP, DC Locator, and Net Log on | UDP port 389 | AD servers (if AD domain is configured) | File servers to AD servers |
  | Randomly allocated high TCP ports | TCP 49152 - 65535 | AD servers (if AD domain is configured) | File servers to AD servers |