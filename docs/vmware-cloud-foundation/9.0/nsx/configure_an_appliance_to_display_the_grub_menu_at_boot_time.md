---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/scale-up-nsx-manager/installing-nsx-manager-cluster-on-vsphere/install-nsx-manager-on-esxi-using-the-command-line-ovf-tool/configure-an-appliance-to-display-the-grub-menu-at-boot-time.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an Appliance to Display the GRUB Menu at Boot Time
---

# Configure an Appliance to Display the GRUB Menu at Boot Time

You must configure an NSX appliance to display the GRUB menu at boot time if you want to
reset the root password of the appliance.

If the configuration is not
performed after deploying the appliance and you forget the root password, resetting
it is not possible.

1. Log in to the VM as root.
2. In the /etc/default/grub file, set the GRUB\_TIMEOUT\_STYLE
   to menu or countdown.

   - If this option set to
     menu, then GRUB will display the menu and
     then wait for the timeout set by GRUB\_TIMEOUT to
     expire before booting the default entry. Pressing a key interrupts the
     timeout.
   - If this option is set to
     countdown, then before displaying the menu,
     GRUB will wait for the timeout set by GRUB\_TIMEOUT
     to expire. If ESC or F4 are pressed, or SHIFT is held down during that
     time, it will display the menu and wait for input. It will show a
     one-line indication of the remaining time.
3. In the /etc/default/grub
   file, change the value for the parameter GRUB\_TIMEOUT. 

   GRUB\_TIMEOUT=4
4. Generate a new password by
   running the following command:

   grub-mkpasswd-pbkdf2
5. In the
   /etc/grub.d/40\_custom file, replace the existing GRUB
   password. 

   The default password is NSX@VM!WaR10.
6. Update the GRUB configuration.

   update-grub