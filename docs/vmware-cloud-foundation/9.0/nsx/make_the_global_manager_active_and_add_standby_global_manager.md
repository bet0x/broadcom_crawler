---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/make-gm-active.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Make the Global Manager Active and Add Standby Global Manager
---

# Make the Global Manager Active and Add Standby Global Manager

After you have deployed a Global Manager
appliance, you can make the Global Manager
active.

Adding a standby Global Manager
is optional but recommended for high availability of the Global Manager.

1. Log in to the appliance at
   https://global-manager-ip-or-fqdn/.
2. Select SystemLocation Manager. In the Global Manager tile, click
   Make Active. Provide a descriptive name for the
   active Global Manager and click
   Save.
3. Add a standby Global Manager
   cluster.
   1. Install a new Global Manager appliance in a secondary location and start
      it. Follow the same instructions as for installing the primary
      Global Manager, see
      [Install the Active and Standby Global Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/install-global-manager-appliances.html#GUID-58099280-5447-4d17-8fab-caf2d3ce134c).
   2. From the active
      Global Manager, add this
      newly installed Global Manager appliance as standby. 

      Navigate back to your active Global Manager and click Add Standby
      and provide the following information:

      | Option | Description |
      | --- | --- |
      | Global Manager Name | Provide a name for the standby Global Manager. |
      | FQDN/IP | Enter the FQDN or IP address of the Global Manager cluster VIP at the secondary location. Do not enter an individual Global Manager FQDN or IP. |
      | Username and Password | Provide the admin user's credentials for the Global Manager at the secondary location. |
      | SHA-256 Thumbprint | Log in to any Global Manager node at the secondary location and run this command: ``` get certificate cluster thumbprint ```  The result is the cluster VIP certificate:  bfae1a0a...  If the GM-Standby is a single Manager VM, use the same command. |
      | Check Compatibility | Click Check Compatibility to ensure that the Global Manager can be added as standby. This checks that the NSX version is compatible. |
   3. Click
      Save.
   4. Click Make
      Standby.