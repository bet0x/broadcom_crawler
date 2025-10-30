---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/troubleshooting-vmware-cloud-foundation-or-vmware-vsphere-foundation-deployments.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Troubleshooting VMware Cloud Foundation or vSphere Foundation Deployments
---

# Troubleshooting VMware Cloud Foundation or vSphere Foundation Deployments

If you encounter errors during deployment, you can use log files and the Supportability and Serviceability (SoS) Utility to help with troubleshooting.

## Log Files and Locations

If you experience validation or deployment failures, check the log files for the domain manager service on the VCF Installer appliance.

```
/var/log/vmware/vcf/domainmanager/domainmanager.log
```

If you experience issues with VCF Operations or VCF Automation, check the log files on the VCF Operations fleet management appliance.

```
/var/log/vrlcm/vmware_vrlcm.log
```

## Local Account Options

If your local account is locked, you can log in the VM of the in VCF Installer appliance and restart the commonsvcs service. After the restart, allow approximately 5 minutes for the service to boot.

```
systemctl restart commonsvcs
```

## Supportability and Serviceability (SoS) Utility

You can run the SoS Utility on the VCF Installer appliance to perform health checks and collect logs, which you can use to help debug a deployment.

After a successful deployment, you should only run the SoS Utility on the SDDC Manager appliance.

The SoS Utility is not a debug tool, but it does provide health check operations that can facilitate debugging a failed deployment. To run the SoS Utility, SSH in to the VCF Installer appliance using the admin account and then enter su to switch to the root user. Navigate to the /opt/vmware/sddc-support directory and type ./sos followed by the options required for your desired operation.

```
./sos --option-1  --option-2...--option-n
```

## SoS Utility Help Options

Use the SoS Utility help to options to see information about the SoS tool itself.

| Option | Description |
| --- | --- |
| --help  -h | Provides a summary of the available SoS tool options |
| --version  -v | Provides the SoS tool's version number. |

## SoS Utility Generic Options

These are generic options for the SoS Utility.

| Option | Description |
| --- | --- |
| --debug-mode | Runs the SoS tool in debug mode. |
| --enable-stats | Enables collection of SoS execution stats. |
| --force | Allows SoS operations while workflows are running. In most cases, you should not use this option, although it is required to run health check options on the VCF Installer appliance. |
| --history | Displays the last twenty SoS operations performed. |
| --log-dir LOGDIR | Specifies the directory to store the logs. |
| --log-folder LOGFOLDER | Specifies the name of the log directory. |
| --setup-json SETUP\_JSON | Custom setup-json file for log collection.  SoS prepares the inventory automatically based on the environment where it is running. If you want to collect logs for a pre-defined set of components, you can create a setup.json file and pass the file as input to SoS. A sample JSON file is available on the VCF Installer appliance in the /opt/vmware/sddc-support/ directory. |
| --short | Displays health results only for failures and warnings. |
| --skip-known-host-check | Skips the specified check for SSL thumbprints for hosts in the known hosts file. |
| --zip | Creates a zipped tar file for the output. |

## SoS Utility Log File Options

| Option | Description |
| --- | --- |
| --api-logs | Collects output from APIs. |
| --vcf-installer-logs | Collects VCF Installer appliance support logs. |
| --esx-logs | Collects logs from the ESX hosts only.  Logs are collected from each ESX host available in the deployment. |
| --no-clean-old-logs | Use this option to prevent the tool from removing any output from a previous collection run.  By default, before writing the output to the directory, the tool deletes the prior run's output files that might be present. If you want to retain the older output files, specify this option. |
| --no-health-check | Skips the health check executed as part of log collection. |
| --nsx-logs | Collects logs from the NSX Manager instances only. |
| --sddc-manager-logs | Collects logs from the SDDC Manager only. |
| --vc-logs | Collects logs from the vCenter instances only.  Logs are collected from each vCenter server available in the deployment. |
| --vm-screenshots | Collects screen shots from all VMs. |
| --automation-logs | Collects VCF Automation support logs only. |
| --operations-logs | Collects VCF Operations support logs only. |
| --operations-fleet-logs | Collects VCF Operations fleet management support logs only. |
| --collect-all-logs | Collects logs for all components. |

## SoS Utility Health Check Options

The SoS Utility can be used to perform health checks on various components or services, including connectivity, compute, and storage.

The health check options are primarily designed to run on the SDDC Manager appliance. Running them on the VCF Installer appliance requires the --force parameter, which instructs the SoS Utility to identify the SDDC Manager appliance deployed by the VCF Installer, and then execute the health check remotely. For example:

```
./sos --health-check --force
```

| Option | Description |
| --- | --- |
| --certificate-health | Verifies that the component certificates are valid (within the expiry date). |
| --connectivity-health | Performs a connectivity health check to inspect whether the different components of the system such as the ESX hosts, vCenter servers, NSX Managers, and SDDC Manager VM can be pinged. |
| --compute-health | Performs a compute health check. |
| --general-health | Verifies ESX entries across all sources, checks the Postgres DB operational status for hosts, checks ESX for error dumps, and gets NSX Manager and cluster status. |
| --get-host-ips | Returns server information. |
| --health-check | Performs all available health checks. |
| --ntp-health | Verifies whether the time on the components is synchronized with the NTP server in the VCF Installer appliance. |
| --services-health | Performs a services health check to confirm whether services are running |