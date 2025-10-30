---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/password-management/resetting-passwords-on-an-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Resetting the Passwords of an Appliance
---

# Resetting the Passwords of an Appliance

The following procedure applies to
NSX Manager, NSX Edge, and Cloud Service Manager
appliances.

If you have an NSX Manager cluster, resetting the password for any of the local users on one automatically resets the password for the other NSX Managers in the cluster. The synchronization of the password can take a few minutes.

If you have renamed the local user, use the new name in the following procedures.

When you reboot an appliance, the GRUB boot menu does
not appear by default. Before you perform this procedure, you must configure
GRUB so that the GRUB boot menu displays. For more information about configuring
GRUB and changing the GRUB root password, see "Configure an
Appliance to Display the GRUB Menu at Boot Time" in the NSX Installation Guide.

If you know the password for root but have forgotten the password for your local users, you can reset it using the following procedure:

1. Log in to the appliance as
   root.
2. To stop the server:
   1. For NSX Edge, run the
      command /etc/init.d/nsx-edge-api-server stop.
   2. Otherwise, run the command
      /etc/init.d/nsx-mp-api-server stop.
3. (Optional) To reset the password for
   admin, run the command passwd
   admin.
4. (Optional) To reset the password for
   audit, run the command passwd
   audit.
5. (Optional) To reset a guest user password, run the
   command passwd guestusername.
6. Run the command touch
   /var/vmware/nsx/reset\_cluster\_credentials.
7. To restart the server:
   1. For NSX Edge, run the
      command /etc/init.d/nsx-edge-api-server start.
   2. Otherwise, run the command
      /etc/init.d/nsx-mp-api-server start.

If you have forgotten the root user's password, you can reset it using the following procedure. You can then use the above procedure to reset the password for all local users.

1. Connect to the console of the appliance.
2. Reboot the system.
3. When the GRUB boot menu appears, press the left SHIFT or ESC key quickly. If you wait too long and the boot sequence does not pause, you must reboot the system again.
4. Press e to edit the menu.

   Choose the top Ubuntu line then enter the user name root and the GRUB password for root (not the same as the appliance's user root). The default password is NSX@VM!WaR10.
5. Press e to edit the selected option.
6. Search for the line starting with linux and add systemd.wants=PasswordRecovery.service to the end of the line.
7. Press Ctrl-X to boot.
8. When the log messages stop, enter the new password for root.
9. Enter the password again.

   The boot process continues.
10. After the reboot, you can verify the password change by logging in as root with the new password.