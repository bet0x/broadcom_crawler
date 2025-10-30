---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-vlcm-baseline-clusters-to-vlcm-image-clusters-using-powercli(1).html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Transitioning vSphere Lifecycle Manager Baseline Clusters to vSphere Lifecycle Manager Image Clusters Using PowerShell
---

# Transitioning vSphere Lifecycle Manager Baseline Clusters to vSphere Lifecycle Manager Image Clusters Using PowerShell

You can use the PowerShell script through a menu-driven interface or a command-line interface (CLI). The menu-driven interface provides a guided transition process and is best suited for smaller environments. The command-line interface is useful for larger environments and can be used to operate against a single cluster at a time or, at scale, using JSON files.

After you start a task with PowerShell, entering Ctrl-C or exiting PowerShell will not halt many tasks (for example, image import, compliance checks, or transition tasks). Those tasks will continue to run in the background in SDDC Manager or vCenter.

If the script execution does not trust the certificate of the SDDC Manager, run $Env:SkipCertificateCheck="enabled" prior to running the script.

## Logging

The script records all actions to time-stamped files in a logs  sub-directory created under the directory containing the script. This functionality facilitates troubleshooting.

If you run the script and this directory does not already exist, it is automated created.

```
PS C:\Users\Admin> .\VcfBaselineClusterTransition.ps1 -Connect

LogFolder not found, creating C:\Users\Admin\logs
```