---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/fips-compliance-for-vcf-components.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > FIPS Configuration for VCF Components
---

# FIPS Configuration for VCF Components

VMware Cloud Foundation supports the Federal Information Processing Standards (FIPS) 140-2, which specify security requirements for cryptographic modules.

Many VCF components support the FIPS standard inherently, and cannot be configured in ways that do not meet the standard. For example, ESX and VMware NSX. Other components may require enablement for FIPS compliance or have varying behavior depending on how they were deployed.

The following components have FIPS enabled by default:

- ESX
- vCenter
- NSX
- VCF Operations HCX
- VMware Live Recovery
- Data Services Manager

The table below summarizes FIPS enablement for components where FIPS is either not enabled by default or can be disabled in certain circumstances.

| Component | FIPS Configuration |
| --- | --- |
| SDDC Manager | In new VCF 9.0 deployments, FIPS compliance in SDDC Manager is on by default and cannot be turned off.  For deployments upgraded from VCF 5.x, the FIPS setting remains the same as it was in the original deployment. This setting cannot be altered after upgrade. |
| VCF Operations | FIPS compliance is off by default.  You can activate FIPS compliance during deployment by selecting the Activate FIPS Mode option during deployment. |
| VCF Operations for logs | FIPS compliance is off enabled by default.  You can enable FIPS compliance during deployment by selecting the the On option for FIPS Compliance. See [Deploying the VCF Operations for Logs Appliance](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/manual-deployment-of-components-to-complete-your-vcf-platform/installing-vcf-logs.html). |
| VCF Operations for networks | VCF Operations for networks uses FIPS compliant cryptographic algorithms for internal connections. FIPS compliance for external connections is off by default.  You can enable FIPS compliance for external connections by navigating to SettingsSystem ConfigurationFIPS Mode for External Connections and toggling the setting to On. |
| Cloud Proxy for VCF Operations | FIPS compliance is not enabled by default. You can enable FIPS compliance for cloud proxies after first enabling FIPS compliance for VCF Operations. For instructions on enabling FIPS compliance, see [Using the Cloud Proxy Command-Line Interface](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies/upgrading-cloud-proxy/using-the-cloud-proxy-command-line-interface-on-cloud.html). |
| VCF Automation | In new VCF 9.0 deployments, FIPS compliance in VCF Automation is enabled by default and cannot be turned off.  For deployments upgraded from VMware Aria Operations 18.x, the FIPS setting remains the same as it was in the original deployment. This setting cannot be altered after upgrade. |
| VMware vSphere Kubernetes Service | VKS 3.3 and later provide the ability to enable OS FIPS mode by configuring the osConfiguration cluster class variable. See [osConfiguration](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/using-tkg-service-with-vsphere-supervisor/provisioning-tkg-service-clusters/using-the-builtin-generic-v3-2-0-clusterclass/clusterclass-variables-for-customizing-a-cluster/osconfiguration.html) for more details. |
| VMware Virtual Disk Developer Kit (VDDK) | By default, VDDK does not enable FIPS. You can configure it by setting the option  vixDiskLib.ssl.enableSslFIPS=1 in the VDDK configuration file. See the instructions provided with the development kit at <https://developer.broadcom.com/sdks/vmware-virtual-disk-development-kit-vddk/latest> for more information. |