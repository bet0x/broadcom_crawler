---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host/configure-ntp-on-the-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Configure NTP on the Witness Host
---

# Configure NTP on the Witness Host

To prevent time synchronization issues, configure the NTP service on the vSAN witness host.

1. In the inventory panel of the vSphere Client, select vCenterDatacenter.
2. Select the vSAN witness host and click the Configure tab.
3. Configure the NTP client on the vSAN witness host.
   1. In the System section, click Time configuration and click the Edit button.
   2. Select Use Network Time Protocol (enable NTP client).
   3. Configure the following settings and click OK.

      | Setting | Value |
      | --- | --- |
      | NTP Servers | NTP server address |
      | Start NTP Service | Selected |
      | NTP Service Startup Policy | Start and stop with host |