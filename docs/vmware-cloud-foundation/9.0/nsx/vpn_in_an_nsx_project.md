---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/nsx-projects/vpn-in-an-nsx-project.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > VPN in an NSX Project
---

# VPN in an NSX Project

In
a multi-tenant NSX environment, a Project
Admin can configure L2 VPN and IPSec VPN service on the tier-1 gateways of a
project.

To configure VPN on the tier-1 gateway of a
project, an edge cluster must be assigned to the project.

The following functionality is supported for VPN service in
projects:

- On each tier-1 gateway of a
  project, you can configure only one IPSec service and one L2 VPN service.
- For configuring route-based IPSec
  VPN, static-routes are supported. Dynamic routing with virtual tunnel interface
  (VTI) using BGP is not supported on the tier-1 gateway of a project.
- The workflow for configuring IPSec
  VPN and L2 VPN service in a project is the same as it is for configuring these
  services in the default space. For more information, see [Adding NSX VPN Services](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-nsx-vpn-services.html).
- Both pre-shared key authentication
  and certificate-based authentication are supported for configuring IPSec VPN
  sessions.
  - An Enterprise Admin can
    share service certificates and certificate revocation lists (CRLs) with
    the projects, if required. The Project Admin can use the shared
    certificates to authenticate IPSec endpoints when certificate-based
    authentication is configured for IPSec VPN sessions.
  - Alternatively, a Project
    Admin can create, update, or manage the service certificates and CRLs in
    the project view, and use them to configure IPSec VPN sessions in the
    project.
- System-created VPN profiles are
  shared by default with all the projects in the system. A Project Admin can
  either use the following default VPN profiles or create new profiles to
  configure VPN services in the project.
  - IKE profile
  - IPSec tunnel profile
  - DPD profile
  - L2 VPN tunnel profile
  - Compliance suite related
    profiles

  To learn about adding IKE,
  IPSec, and DPD profiles, see [Adding Profiles](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/virtual-private-network-vpn/adding-profiles.html). If an
  Enterprise Admin has created VPN profiles in the default space, they can be
  shared with specific projects, if required. Shared profiles can be consumed
  in a read-only mode in the projects.
- An Enterprise Admin can restrict
  the number of VPN related objects that can be created under a project by
  defining quotas for various object types. For example, quotas can be defined on
  these VPN objects:
  - IPSec VPN sessions
  - L2 VPN sessions
  - Local endpoints
  - IPSec VPN services
  - L2 VPN services
  - VPN profiles

  This list is not exhaustive.
  For the full list of objects, go to Quotas tab on the
  NSX Manager
  UI.
- Monitoring status of VPN services,
  VPN sessions, and other VPN statistics is supported in the project view.
- Configuration
  of L2 VPN and IPSec VPN tunnels between tier-1 gateways of two different
  projects in the same NSX
  deployment is supported.
- Configuration of L2 VPN and IPSec
  VPN tunnels between tier-1 gateways of the same project is supported.

The following points must be kept in mind
when configuring VPN service on the tier-1 gateways of a project:

- IPSec local endpoints are realized
  as loopback IPs on the tier-1 gateway of the project. Local endpoint IP must be
  unique across the data center. The endpoint IPs are advertised to the tier-0
  gateway that is associated with the project, and then pushed to the upstream
  networks through BGP.
- To allow IPSec packets (IKE UDP
  port 500 and 4500, ESP) towards tier-1 gateway, the Enterprise Admin must define
  firewall rules on the tier-0 gateway that is associated with the project. The
  firewall rules on the tier-0 gateway are not automatically created by the
  system. However, firewall rules on the tier-1 gateway of the project are
  auto-created to allow IKE and ESP traffic between the endpoints in the IPSec VPN
  session.