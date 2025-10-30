---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-dns-server-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update the DNS Server Configuration for VCF Core Components 
---

# Update the DNS Server Configuration for VCF Core Components

SDDC Manager uses DNS servers to provide name resolution for the VCF core components. You can update the DNS server information that you provided during VMware Cloud Foundation deployment.

- Verify that both forward and reverse DNS resolution are functional for each component using the updated DNS server information.
- Verify that the new DNS server is reachable from each of the VMware Cloud Foundation components.
- Verify that SDDC Manager can reach all VMware Cloud Foundation components over SSH.
- Verify that all VMware Cloud Foundation components are in an active state.

When you update the DNS server configuration, SDDC Manager performs DNS configuration updates for the following components:

- SDDC Manager
- vCenter instances
- ESX hosts
- NSX Managers
- NSX Edge nodes

If the update fails, SDDC Manager rolls back the DNS settings for the failed component. Fix the underlying issue and retry the update starting with the failed component.

Updating the DNS server configuration can take some time to complete, depending on the size of your environment. Schedule DNS updates at a time that minimizes the impact to the system users.

To update the DNS configuration for VCF management components, see [Update the DNS Configuration for VCF Management Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-dns-configuration.html).

1. In the VCF Operations console, click AdministrationSDDC ManagerNetwork SettingsDNS Servers.
2. Click Edit.
3. Review the overview information and click Next.
4. Review the prerequisites and click Next.
5. Enter a primary DNS server IP address and click Save.

   Optionally, enter an alternative DNS server IP address.