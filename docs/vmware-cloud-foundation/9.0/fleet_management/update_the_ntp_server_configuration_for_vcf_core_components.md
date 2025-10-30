---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-ntp-server-configuration.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update the NTP Server Configuration for VCF Core Components
---

# Update the NTP Server Configuration for VCF Core Components

SDDC Manager uses NTP servers to synchronize time between the VCF core components. You can update the NTP server information that you provided during VMware Cloud Foundation deployment.

- Verify the new NTP server is reachable from all components.
- Time skew between new NTP servers is less than 5 minutes.
- Verify that SDDC Manager can reach all VMware Cloud Foundation components over SSH.

You must have at least one NTP server. When you update the NTP server configuration, SDDC Manager performs NTP configuration updates for the following components:

- SDDC Manager
- vCenters
- ESX hosts
- NSX Managers
- NSX Edge nodes

If the update fails, SDDC Manager rolls back the NTP settings for the failed component. Fix the underlying issue and retry the update starting with the failed component.

Updating the NTP server configuration can take some time to complete, depending on the size of your environment. Schedule NTP updates at a time that minimizes the impact to the system users.

To update the NTP configuration for VCF management components, see [Update the NTP Configuration for VCF Management Components](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/update-ntp-configuration.html).

1. In the VCF Operations console, click AdministrationSDDC ManagerNetwork SettingsNTP Servers.
2. Click Edit.
3. Review the overview information and click Next.
4. Review the prerequisites and click Next.
5. Enter one or more NTP server IP addresses and click Save.