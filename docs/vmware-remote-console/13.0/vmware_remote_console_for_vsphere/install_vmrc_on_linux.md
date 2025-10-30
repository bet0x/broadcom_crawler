---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/installing-vmrc/install-vmrc-on-linux.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Install VMRC on Linux
---

# Install VMRC on Linux

Download the Linux installation package, extract, and run VMRC on your local machine.

First verify that your local machine is running a supported version of Linux, as described in the release notes for the version you downloaded.

The Linux installation package includes a GUI installer and command-line installer. To force the installer to use command-line mode, add the --console parameter when running the installation package.

Follow these steps:

1. Navigate to the product download area for [VMware Cloud Foundation](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Cloud%20Foundation&displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN) on the Broadcom support site. Sign-in might be required.
2. If this is your first download, you must visit one or both Terms and Conditions, then click the "I agree" checkbox to activate the cloud download button.
3. Click View Group on the right to expand. Click the cloud icon to download.
4. Switch to the root user with the su or sudo command.
5. If necessary, grant execute permissions to the installation package.

   ```
   chmod +x VMware-Remote-Console-version-build.x86_64.bundle
   ```
6. Run the installation package.

   ```
   ./VMware-Remote-Console-version-build.x86_64.bundle
   ```
7. To install in GUI mode, perform the following steps.

   1. Read and accept the terms of the license agreement. Click Next.
   2. Select whether to join Customer Experience Improvement Program (CEIP) and click Next.
   3. Click Install.
8. To install in command-line mode, perform the following steps.

   1. Press Enter and read the license agreement. You can type q to move to the end of the license agreement.
   2. When you reach the end of the license agreement, type yes to accept the license agreement.
   3. If you want to join the Customer Experience Improvement Program (CEIP) type yes.
   4. Wait for the installation to complete.

Now VMware Remote Console should be installed on your local machine and configured to open URLs that use the vmrc scheme.