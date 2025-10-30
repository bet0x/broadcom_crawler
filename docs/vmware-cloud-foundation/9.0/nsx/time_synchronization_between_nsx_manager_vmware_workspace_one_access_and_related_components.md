---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/time-synchronization-between-nsx-manager-vidm-and-related-components.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Time Synchronization between NSX Manager, VMware Workspace ONE Access, and Related Components
---

# Time Synchronization between NSX Manager, VMware Workspace ONE Access, and Related Components

For authentication to work correctly, NSX Manager, VMware Workspace ONE Access, and other service providers such as Active Directory must all be time synchronized. This section describes how to time synchronize these components.

## VMware Infrastructure

Follow the instructions in the following Knowledge Base articles to synchronize ESX hosts.

- [318888: Verifying time synchronization across an ESX/ESX host environment](https://knowledge.broadcom.com/external/article?articleNumber=318888)
- [317537: Configure Network Time Protocol (NTP)](https://knowledge.broadcom.com/external/article?articleNumber=317537)

## Third-Party Infrastructure

Follow the vendor's documentation on how synchronize VMs and hosts.

## Configuring NTP on the VMware Workspace ONE Access Server (Not Recommended)

If you are not able to synchronize time across the hosts, you can disable synchronizing to host and configure NTP on the Workspace ONE Access server. This method is not recommended because it requires the opening of UDP port 123 on the Workspace ONE Access server.

- Check the clock on the Workspace ONE Access server and make sure it is correct.

  ```
      # hwclock
      Tue May  9 12:08:43 2017  -0.739213 seconds
  ```
- Edit /etc/ntp.conf and add the following entries if they don't exist.

  ```
      server time.nist.gov
      server pool.ntp.org
      server time.is dynamic
      restrict 192.168.100.0 netmask 255.255.255.0 nomodify notrap
  ```
- Open UDP port 123.

  ```
      # iptables -A INPUT -p udp --dport 123 -j ACCEPT
  ```

  Run the following command to check that the port is open.

  ```
      # iptables -L –n
  ```
- Start the NTP service.

  ```
      /etc/init.d/ntp start
  ```
- Make NTP run automatically after a reboot.

  ```
      # chkconfig --add ntp
      # chkconfig ntp on
  ```
- Check that the NTP server can be reached.

  ```
      # ntpq -p
  ```

  The reach column should not show 0. The st column should show some number other than 16..