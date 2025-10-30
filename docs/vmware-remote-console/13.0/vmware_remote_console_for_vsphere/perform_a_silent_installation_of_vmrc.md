---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vmware-remote-console/13-0/vmware-remote-console-for-vsphere/introduction/installing-vmrc/install-vmrc-on-windows/perform-silent-installation.html
product: vmware-remote-console
version: 13.0
section: VMware Remote Console for vSphere
breadcrumb: VMware Remote Console for vSphere > Perform a Silent Installation of VMRC
---

# Perform a Silent Installation of VMRC

You can perform a silent installation of VMware Remote Console on Windows machines.

Silent installation, also known as unattended installation, allows system administrators to automate the installation process. During a silent installation, the end user is not required to perform any actions.

Prerequisites:

- Verify that the target machine is running a supported version of Windows. For a list of supported operating systems, see the release notes for your version of VMware Remote Console.
- Read the VMware Remote Console End-User License Agreement (EULA) and be sure you can accept its terms and conditions. The EULA is not displayed during a silent installation. If you want to read the EULA, perform a standard installation.

Follow these steps:

1. Follow the download steps above for VMRC on Windows.
2. Transfer the file to the target machine and decompress it to a temporary directory.
3. Run Command Prompt as an administrator.
4. Run the following command to perform a silent installation.

```
VMware-VMRC-version-build.exe /s /v "/qn EULAS_AGREED={0 | 1} INSTALLDIR="install-directory" DATACOLLECTION={0 | 1}" /l "log-file"
```

| Option | Description |
| --- | --- |
| EULAS\_AGREED | Enter 1 to indicate that you accept the terms and conditions of the EULA. Entering 0 stops installation. |
| INSTALLDIR | Enter the directory where you want to install VMRC. If the directory does not exist, it will be created. If you do not include this parameter, VMRC will be installed in folder:   ``` C:\Program Files (x86)\VMware\VMware Remote Console. ``` |
| AUTOSOFTWAREUPDATE | This option has no effect since checking for updates was discontinued. |
| DATACOLLECTION | Enter 1 to join the Customer Experience Improvement Program (CEIP) or 0 to decline. |
| /l | Enter the file path of the VMRC installation log file. If the file does not exist, it will be created, but you must specify an existing directory. If you do not include this parameter, installation log will be written to the %TEMP%\vminst.log file. |

VMware Remote Console should be installed on the target machines and configured to open URLs that use the vmrc scheme.