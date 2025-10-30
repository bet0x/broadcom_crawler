---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/nsx-edge-installation-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Edge Installation Requirements
---

# NSX Edge Installation Requirements

The NSX Edge provides routing services and connectivity to networks that are external to the NSX deployment. NSX Edge nodes provide a pool of capacity for running centralized services and is required if you want to deploy a tier-0 router or a tier-1 router with stateful services such as network address translation (NAT), VPN, and so on.

There can be only one tier-0 router per NSX Edge node. However, multiple tier-1 logical routers can be hosted on one NSX Edge node. NSX Edge VMs of different sizes can be combined in the same cluster; however, it is not recommended.

NSX Edge Deployment, Platforms, and Installation Requirements



| Requirements | Description |
| --- | --- |
| Supported deployment methods | - OVA/OVF - ISO with PXE - ISO without PXE |
| Supported platforms | NSX Edge is supported as VM (only on ESX) or as physical server (bare metal). Both leverage the data plane development kit (DPDK) for faster packet processing and high performance. |
| PXE installation | The Password string must be encrypted with sha-512 algorithm for the root and admin user password. |
| NSX appliance password | - At least 12 characters - At least one lower-case letter - At least one upper-case letter - At least one digit - At least one special character - At least five different characters - No dictionary words - No palindromes - More than four monotonic character sequence is not allowed |
| Hostname | When installing NSX Edge, specify a hostname that does not contain invalid characters such as an underscore. If the hostname contains any invalid character, after deployment the hostname will be set to localhost. For more information about hostname restrictions, see https://datatracker.ietf.org/doc/html/rfc952 and https://datatracker.ietf.org/doc/html/rfc1123. |
| VMware Tools | The NSX Edge VM running on ESX has VMTools installed. Do not remove or upgrade VMTools. |
| System | Verify that the system requirements are met. |
| Ports | Verify that the required ports are open. See <https://ports.broadcom.com/>. |
| IP Addresses | Plan your NSX Edge IPv4 and IPv6 IP addressing scheme. However, a NSX Edge configured for IPv4 and IPv6 stack is not supported on an ESX node that is configured only for IPv6 addressing scheme. Also, NSX Edge tunnel endpoints on a dual IPv4 and IPv6 scheme cannot communicate with an ESX node using only IPv6 addressing scheme. |
| OVF Template | - Verify that you have adequate privileges to deploy an OVF template on the ESX host. - Verify that hostnames do not include underscores. Otherwise, the hostname is set to localhost.   - A management tool that can deploy OVF templates, such as vCenter or the vSphere Client.  The OVF deployment tool must support configuration options to allow for a manual configuration. - The Client Integration Plug-in must be installed. |
| NTP Server | The same NTP server must be configured on all NSX Edge VMs or Bare Metal Edges in an Edge cluster. |

## Intel-based Chipsets

NSX Edge nodes are supported on ESX-based hosts with Intel chipsets. If an unsupported chipset type is used, vSphere EVC mode may prevent Edge nodes from starting, showing an error message in the console.

## AMD EPYC

NSX Edge nodes are also supported on AMD-based chipsets. NSX Edge nodes can now be deployed on AMD EPYC series chipsets.

## NSX Edge Support of vSphere Business Continuity Features

Starting in NSX 2.5.1, vMotion, DRS, and vSphere HA are supported for NSX Edge nodes. Use vMotion and DRS with caution to avoid traffic disruption, especially, when the BFD timers are set to less than one second.

## NSX Edge Installation Scenarios

When you install NSX Edge from an OVA or OVF file, either from vSphere Web Client or the command line, OVA/OVF property values such as user names, passwords, or IP addresses are not validated before the VM is powered on.

- If you specify a user name for any of the local users, the name must be unique. If you specify the same name, it is ignored and the default names (for example, admin or audit) are used.
- If the password for the root or admin user does not meet the complexity requirements, you must log in to NSX Edge through SSH or at the console as root with password vmware and admin with password default. You are prompted to change the password.
- If the password for other local users (for example, audit) does not meet the complexity requirements, the user account is disabled. To enable the account, log in to NSX Edge through SSH or at the console as the admin user and run the command set user local\_user\_name to set the local user's password (the current password is an empty string). You can also reset passwords in the UI using System > User Management > Local Users.

Changes made to the NSX while logged in with the root user credentials might cause system failure and potentially impact your network. You can only make changes using the root user credentials with the guidance of VMware Support team.

The core services on the appliance do not start until a password with sufficient complexity has been set.

After you deploy NSX Edge from an OVA file, you cannot change the VM's IP settings by powering off the VM and modifying the OVA settings from vCenter.